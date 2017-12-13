#!/usr/bin/env python
"""
pdns.py: Manage PowerDNS Zones/Records
"""

import argparse
import csv
import json
import requests

__author__ = "Larry Smith Jr."
__email___ = "mrlesmithjr@gmail.com"
__maintainer__ = "Larry Smith Jr."
__status__ = "Development"
# http://everythingshouldbevirtual.com
# @mrlesmithjr

EXAMPLES = """
Create a new Master Zone with info below:
-----------------------------------------

Zone: dev.vagrant.local
ZoneType: MASTER
Master: 172.28.128.3
Nameservers:
172.28.128.3
172.28.128.4
172.28.128.5

./pdns.py add_zones --apihost 172.28.128.3 --zone dev.vagrant.local --zoneType MASTER --nameservers 172.28.128.3,172.28.128.4,172.28.128.5


Create the Slave Zones with the info below:
-------------------------------------------

Zone: dev.vagrant.local
ZoneType: SLAVE
Master: 172.28.128.3
Slaves:
172.28.128.4
172.28.128.5

./pdns.py add_zones --apihost 172.28.128.4 --zone dev.vagrant.local --zoneType SLAVE --masters 172.28.128.3


Create Master Zones using a CSV file:
-------------------------------------

Create a master_zones.csv similar to below:

zone,zoneType,masters,nameservers
128.28.172.in-addr.arpa,MASTER,,"172.28.128.3,172.28.128.4,172.28.128.5"
dev.vagrant.local,MASTER,,"172.28.128.3,172.28.128.4,172.28.128.5"
prod.vagrant.local,MASTER,,"172.28.128.3,172.28.128.4,172.28.128.5"
test.vagrant.local,MASTER,,"172.28.128.3,172.28.128.4,172.28.128.5"
vagrant.local,MASTER,,"172.28.128.3,172.28.128.4,172.28.128.5"

The first row is the header...

Now read the csv file using CLI argument:

./pdns.py add_zones --apihost 172.28.128.3 --readcsv master_zones.csv

Create records with info below:
-------------------------------

Zone: dev.vagrant.local
name: test01.dev.vagrant.local
recordType: A
content: 172.28.128.161
name: development.dev.vagrant.local
recordType: CNAME
content: test01.dev.vagrant.local

./pdns.py add_records --zone dev.vagrant.local --name test01 --content 172.28.128.161 --recordType A
./pdns.py add_records --zone dev.vagrant.local --name development --content test01.dev.vagrant.local --recordType CNAME


Create records using a csv file:
---------------------------------------

Create a add_records.csv file similar to below:

name,zone,record_type,content,disabled,ttl,set_ptr,priority
development,test.vagrant.local,A,172.28.128.3,FALSE,3600,TRUE,0
node0,test.vagrant.local,A,172.28.128.4,FALSE,3600,TRUE,0
node1,test.vagrant.local,A,172.28.128.5,FALSE,3600,TRUE,0
node100,test.vagrant.local,A,172.28.128.100,FALSE,3600,TRUE,0
node101,test.vagrant.local,A,172.28.128.101,FALSE,3600,TRUE,0
node102,test.vagrant.local,A,172.28.128.102,FALSE,3600,TRUE,0
node2,dev.vagrant.local,A,172.28.128.201,FALSE,3600,TRUE,0
node201,dev.vagrant.local,A,172.28.128.202,FALSE,3600,TRUE,0
node202,dev.vagrant.local,A,172.28.128.203,FALSE,3600,TRUE,0
node203,dev.vagrant.local,CNAME,node201.dev.vagrant.local,FALSE,3600,TRUE,0
smtp,vagrant.local,A,172.28.128.20,FALSE,3600,TRUE,0
mail,vagrant.local,CNAME,smtp.vagrant.local,FALSE,3600,TRUE,0

The first row is the header...

Now read the csv file using CLI argument:

./pdns.py add_records --apihost 172.28.128.3 --readcsv add_records.csv


Delete records with info below:
-------------------------------

Zone: vagrant.local
name: smtp.vagrant.local
recordType: A

./pdns.py delete_records --apihost 172.28.128.3 --name smtp --zone vagrant.local --recordType A


Delete records reading from a csv file:
---------------------------------------

Create a delete_records.csv similar to below:

name,zone,record_type
node100,test.vagrant.local,A
node101,test.vagrant.local,A
node202,dev.vagrant.local,A
node203,dev.vagrant.local,CNAME

The first row is the header...

Now read the csv file using CLI argument:

./pdns.py delete_records --apihost 172.28.128.3 --readcsv delete_records.csv

Query PDNS config
-----------------

./pdns.py query_config --apihost 172.28.128.3


Query zones
-----------

./pdns.py query_zones --apihost 172.28.128.3

Api version
-----------

./pdns.py query_config --apihost 172.28.128.3 --apiversion old
Default is PDNS v4.0.x version v1 api /api/v1
For PDNS v3.x use --apiversion old

"""


class PDNSControl(object):
    """
    Main execution
    """

    def __init__(self):
        self.read_cli_args()
        self.setup_api_call()
        self.decide_action()

    def add_records(self):
        """
        Add new DNS records

        Create new DNS records of different types
        """
        if self.args.readcsv is None:
            payload = {
                "rrsets": [
                    {
                        "name": self.args.name + '.' + self.args.zone,
                        "type": self.args.recordType,
                        "changetype": "REPLACE",
                        "records": [
                            {
                                "content": self.args.content,
                                "disabled": self.args.disabled,
                                "name": self.args.name + '.' + self.args.zone,
                                "ttl": self.args.ttl,
                                "set-ptr": self.args.setPTR,
                                "type": self.args.recordType,
                                "priority": self.args.priority
                            }
                        ]
                    }
                ]
            }
            zone_check = requests.get(self.uri, headers=self.headers)
            if zone_check.status_code == 200:
                dummy_r = requests.patch(
                    self.uri, data=json.dumps(payload), headers=self.headers)
                print("DNS Record '%s' Successfully Added/Updated"
                      % (self.args.name + '.' + self.args.zone))
            else:
                print "DNS Zone '%s' Does Not Exist..." % self.args.zone
        elif self.args.readcsv is not None:
            try:
                f = open(self.args.readcsv)
                csv_f = csv.reader(f)
                next(csv_f, None)  # skip headers
                for row in csv_f:
                    uri = ("http://%s:%s%s/servers/localhost/zones/%s"
                           % (self.args.apihost, self.args.apiport, self.args.apiversion, row[1]))
                    if row[4].lower() == "false":
                        disabled = False
                    elif row[4].lower() == "true":
                        disabled = True
                    if row[6].lower() == "false":
                        set_ptr = False
                    if row[6].lower() == "true":
                        set_ptr = True
                    payload = {
                        "rrsets": [
                            {
                                "name": row[0] + '.' + row[1],
                                "type": row[2],
                                "changetype": "REPLACE",
                                "records": [
                                    {
                                        "content": row[3],
                                        "disabled": disabled,
                                        "name": row[0] + '.' + row[1],
                                        "ttl": row[5],
                                        "set-ptr": set_ptr,
                                        "type": row[2],
                                        "priority": row[7]
                                    }
                                ]
                            }
                        ]
                    }
                    zone_check = requests.get(uri, headers=self.headers)
                    if zone_check.status_code == 200:
                        dummy_r = (requests.patch(uri, data=json.dumps(payload),
                                                  headers=self.headers))
                        print("DNS Record '%s' Successfully Added/Updated"
                              % (row[0] + '.' + row[1]))
                    else:
                        print "DNS Zone '%s' Does Not Exist...Skipping" % row[1]
            finally:
                f.close()

    def add_zones(self):
        """
        Add new DNS zones

        Create Master, Native or Slave zones
        """
        if self.args.readcsv is None:
            masters = []
            nameservers = []
            if self.args.masters:
                for master in self.args.masters.split(','):
                    masters.append(master)
            if self.args.nameservers:
                for nameserver in self.args.nameservers.split(','):
                    nameservers.append(nameserver)
            if self.args.zoneType == "MASTER":
                payload = {
                    "name": self.args.zone,
                    "kind": self.args.zoneType,
                    "masters": [],
                    "soa_edit_api": "INCEPTION-INCREMENT",
                    "nameservers": nameservers
                }
            elif self.args.zoneType == "NATIVE":
                payload = {
                    "name": self.args.zone,
                    "kind": self.args.zoneType,
                    "masters": [],
                    "nameservers": nameservers
                }
            else:
                payload = {
                    "name": self.args.zone,
                    "kind": self.args.zoneType,
                    "masters": masters,
                    "nameservers": []
                }
            zone_check_uri = ("http://%s:%s%s/servers/localhost/zones/%s"
                              % (self.args.apihost, self.args.apiport, self.args.apiversion, self.args.zone))
            zone_check = requests.get(zone_check_uri, headers=self.headers)
            if zone_check.status_code == 200:
                print "DNS Zone '%s' Already Exists..." % self.args.zone
            else:
                dummy_r = requests.post(self.uri, data=json.dumps(
                    payload), headers=self.headers)
                print "DNS Zone '%s' Successfully Added..." % self.args.zone
        elif self.args.readcsv is not None:
            try:
                f = open(self.args.readcsv)
                csv_f = csv.reader(f)
                next(csv_f, None)  # skip headers
                for row in csv_f:
                    masters = []
                    nameservers = []
                    zone_check_uri = ("http://%s:%s%s/servers/localhost/zones/%s"
                                      % (self.args.apihost, self.args.apiport, self.args.apiversion, row[0]))
                    zone_check = requests.get(
                        zone_check_uri, headers=self.headers)
                    if zone_check.status_code == 200:
                        print "DNS Zone '%s' Already Exists...Skipping" % row[0]
                    else:
                        if row[2]:
                            for master in row[2].split(','):
                                masters.append(master)
                        if row[3]:
                            for nameserver in row[3].split(','):
                                nameservers.append(nameserver)
                        if row[1].upper() == "MASTER":
                            payload = {
                                "name": row[0],
                                "kind": row[1],
                                "masters": [],
                                "soa_edit_api": "INCEPTION-INCREMENT",
                                "nameservers": nameservers
                            }
                        elif row[1].upper() == "NATIVE":
                            payload = {
                                "name": row[0],
                                "kind": row[1],
                                "masters": [],
                                "nameservers": nameservers
                            }
                        else:
                            payload = {
                                "name": row[0],
                                "kind": row[1],
                                "masters": masters,
                                "nameservers": []
                            }
                        dummy_r = (requests.post(self.uri,
                                                 data=json.dumps(payload), headers=self.headers))
                        print "DNS Zone '%s' Successfully Added..." % row[0]
            finally:
                f.close()

    def decide_action(self):
        """
        Determine action

        Based on action passed determine which action to take
        """
        if self.args.action == "add_records":
            self.add_records()
        elif self.args.action == "add_zones":
            self.add_zones()
        elif self.args.action == "delete_records":
            self.delete_records()
        elif self.args.action == "delete_zones":
            self.delete_zones()
        elif self.args.action == "query_config":
            self.query_config()
        elif self.args.action == "query_stats":
            self.query_stats()
        elif self.args.action == "query_zones":
            self.query_zones()

    def delete_records(self):
        """
        Delete DNS records

        Delete DNS records of different types
        """
        if self.args.readcsv is None:
            payload = {
                "rrsets": [
                    {
                        "name": self.args.name + '.' + self.args.zone,
                        "type": self.args.recordType,
                        "changetype": "DELETE",
                    }
                ]
            }
            zone_check = requests.get(self.uri, headers=self.headers)
            if zone_check.status_code == 200:
                dummy_r = requests.patch(
                    self.uri, data=json.dumps(payload), headers=self.headers)
                print("DNS Record '%s' Successfully Deleted"
                      % (self.args.name + '.' + self.args.zone))
            else:
                print "DNS Zone '%s' Does Not Exist..." % self.args.zone
        elif self.args.readcsv is not None:
            try:
                f = open(self.args.readcsv)
                csv_f = csv.reader(f)
                next(csv_f, None)  # skip headers
                for row in csv_f:
                    uri = ("http://%s:%s%s/servers/localhost/zones/%s"
                           % (self.args.apihost, self.args.apiport, self.args.apiversion, row[1]))
                    payload = {
                        "rrsets": [
                            {
                                "name": row[0] + '.' + row[1],
                                "type": row[2],
                                "changetype": "DELETE",
                            }
                        ]
                    }
                    zone_check = requests.get(uri, headers=self.headers)
                    if zone_check.status_code == 200:
                        dummy_r = (requests.patch(uri, data=json.dumps(payload),
                                                  headers=self.headers))
                        print("DNS Record '%s' Successfully Deleted"
                              % (row[0] + '.' + row[1]))
                    else:
                        print "DNS Zone '%s' Does Not Exist...Skipping" % row[1]
            finally:
                f.close()

    def delete_zones(self):
        """
        Delete DNS Zones
        """
        payload = {
            "name": self.args.zone
        }
        zone_check = requests.get(self.uri, headers=self.headers)
        if zone_check.status_code == 200:
            dummy_r = requests.delete(
                self.uri, data=json.dumps(payload), headers=self.headers)
            print "DNS Zone '%s' Successfully Deleted..." % self.args.zone
        else:
            print "DNS Zone '%s' Does Not Exist..." % self.args.zone

    def query_config(self):
        """
        Query PDNS Config
        """
        r = requests.get(self.uri, headers=self.headers)
        python_data = json.loads(r.text)
        print json.dumps(python_data, indent=4)

    def query_stats(self):
        """
        Query DNS Stats
        """
        r = requests.get(self.uri, headers=self.headers)
        python_data = json.loads(r.text)
        print json.dumps(python_data, indent=4)

    def query_zones(self):
        """
        Query DNS Zones

        Query existing DNS Zones
        """
        r = requests.get(self.uri, headers=self.headers)
        if r.status_code == 200:
            python_data = json.loads(r.text)
            print json.dumps(python_data, indent=4)
        else:
            print "DNS Zone '%s' Does Not Exist..." % self.args.zone

    def read_cli_args(self):
        """
        Read variables from CLI

        Read CLI variables passed on CLI
        """
        parser = argparse.ArgumentParser(description='PDNS Controls...')
        parser.add_argument('action', help='Define action to take',
                            choices=['add_records', 'add_zones', 'delete_records',
                                     'delete_zones', 'query_config', 'query_stats', 'query_zones'])
        parser.add_argument(
            '--apikey', help='PDNS API Key', default='changeme')
        parser.add_argument(
            '--apihost', help='PDNS API Host', default='127.0.0.1')
        parser.add_argument('--apiversion', help='PDNS API version',
                            choices=['old', '/api/v1'], default='/api/v1')
        parser.add_argument('--apiport', help='PDNS API Port', default='8081')
        parser.add_argument('--content', help='DNS Record content')
        parser.add_argument('--disabled', help='Define if Record is disabled',
                            choices=['True', 'False'], default=False)
        parser.add_argument('--masters', help='DNS zone masters')
        parser.add_argument('--name', help='DNS record name')
        parser.add_argument('--nameservers', help='DNS nameservers for zone')
        parser.add_argument('--priority', help='Define priority', default=0)
        parser.add_argument('--readcsv', help='Read input from CSV')
        parser.add_argument('--recordType', help='DNS record type',
                            choices=['A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT'])
        parser.add_argument('--setPTR', help='Define if PTR record is created',
                            choices=['True', 'False'], default=True)
        parser.add_argument('--ttl', help='Define TTL', default=3600)
        parser.add_argument('--zone', help='DNS zone')
        parser.add_argument('--zoneType', help='DNS Zone Type',
                            choices=['MASTER', 'NATIVE', 'SLAVE'])
        self.args = parser.parse_args()
        if self.args.apiversion == "old":
            self.args.apiversion = ""
        if self.args.action == "add_zones" and (self.args.zoneType == "MASTER" and
                                                self.args.nameservers is None):
            parser.error("--nameservers is required to create MASTER zone")
        if self.args.action == "add_zones" and (self.args.zoneType == "SLAVE" and
                                                self.args.masters is None):
            parser.error("--masters is required to create SLAVE zone")

    def setup_api_call(self):
        """
        Setup API Call

        Based on action setup the correct API call to make
        """
        self.headers = {'X-API-Key': self.args.apikey}
        if (self.args.action == "add_zones" or (self.args.action == "query_zones" and
                                                self.args.zone is None)):
            self.uri = ("http://%s:%s%s/servers/localhost/zones"
                        % (self.args.apihost, self.args.apiport, self.args.apiversion))
        elif ((self.args.action == "add_records" and self.args.readcsv is None)
              or (self.args.action == "delete_records" and self.args.readcsv is None)
              or self.args.action == "delete_zones" or
              (self.args.action == "query_zones" and self.args.zone is not None)):
            self.uri = ("http://%s:%s%s/servers/localhost/zones/%s"
                        % (self.args.apihost, self.args.apiport, self.args.apiversion, self.args.zone))
        elif self.args.action == "query_config":
            self.uri = ("http://%s:%s%s/servers/localhost/config"
                        % (self.args.apihost, self.args.apiport, self.args.apiversion))
        elif self.args.action == "query_stats":
            self.uri = ("http://%s:%s%s/servers/localhost/statistics"
                        % (self.args.apihost, self.args.apiport, self.args.apiversion))


if __name__ == '__main__':
    PDNSControl()
