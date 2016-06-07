#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ansible_inventory.py: Query/Manage Ansible Facts

   This script will query or manage Ansible Facts into a useable inventory"""
from __future__ import print_function

# Import modules
import argparse
import json
import MySQLdb

__author__ = "Larry Smith Jr."
__email___ = "mrlesmithjr@gmail.com"
__maintainer__ = "Larry Smith Jr."
__status__ = "Development"
# http://everythingshouldbevirtual.com
# @mrlesmithjr

# Setup arguments
parser = argparse.ArgumentParser(description='Ansible Inventory...')
parser.add_argument('--addhost', required=False, help='Add Hostname')
parser.add_argument('--db', default='ansible_inventory', required=False,
                    help='Database Name')
parser.add_argument('--function', default='all', required=False,
                    help='Function to Execute...\n'
                    'valid function choices are\n'
                    '[addhost | all | groups | hosts | querygroup | queryhost]')
parser.add_argument('--host', default='127.0.0.1', required=False,
                    help='Database Host, [default: 127.0.0.1]')
parser.add_argument('--password', required=True, help='Database Password')
parser.add_argument('--querygroup', required=False,
                    help='Query Group, Define Group to Query')
parser.add_argument('--queryhost', required=False,
                    help='Query Host, Define Host to Query')
parser.add_argument('--user', required=True, help='Database User')
args = parser.parse_args()

# Defined functions
def add_host():
    """Add a new host to the inventory

    This will add a new host to the inventory.

    Keyword arguments:
    :args.addhost -- The name of the host to add to the inventory.

    Ex.
    ansible_inventory.py --user ansible --password ansible --function addhost
        --addhost testnode1
    """

    sql = "INSERT INTO Hosts(HostName) VALUES('%s')" %(args.addhost)
    con = MySQLdb.connect(args.host, args.user, args.password, args.db)
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
        cur.close()
        con.close()
    except MySQLdb.IntegrityError as e:
        print("IntegrityError")
        print(e)

def all_groups():
    """Query all groups

    This will query all groups in the inventory and return the results.

    Ex.
    ansible_inventory.py --user ansible --password --ansible --function groups
    """

    sql = "SELECT DISTINCT GroupName FROM Groups"
    con = MySQLdb.connect(args.host, args.user, args.password, args.db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append(row)
    print(json.dumps(results))
    cur.close()
    con.close()

def all_hosts():
    """Query all hosts

    This will query all hosts in the inventory and return the results.

    Ex.
    ansible_inventory.py --user ansible --password ansible --function hosts
    """
    sql = "SELECT DISTINCT HostName FROM Hosts"
    con = MySQLdb.connect(args.host, args.user, args.password, args.db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append(row)
    print(json.dumps(results))
    cur.close()
    con.close()

def all_inventory():
    """Query all hosts/groups

    This will query all hosts/groups in the inventory and return the results.
    This is also the default when executed as below...
    ansible_inventory.py --user ansible --password ansible

    Ex.
    ansible_inventory.py --user ansible --password ansible --function all
    """

    sql = """
        SELECT HostName,AnsibleSSHHost,HostDistribution,
        HostDistributionRelease,HostDistributionVersion,
        GroupName FROM inventory"""
    con = MySQLdb.connect(args.host, args.user, args.password, args.db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    results = []
    for HostName, AnsibleSSHHost, HostDistribution, HostDistributionRelease, \
        HostDistributionVersion, GroupName in rows: \
        results.append({'host': HostName, 'ansible_ssh_host': AnsibleSSHHost, \
        'ansible_distribution': HostDistribution, \
        'ansible_distribution_release': HostDistributionRelease, \
        'ansible_distribution_version': HostDistributionVersion, \
        'groups': GroupName})
    print(json.dumps(results, sort_keys=True))
    cur.close()
    con.close()

def query_group():
    """Query a specific group

    This will query a specific group and return the results.

    Ex.
    ansible_inventory.py --user ansible --password ansible --function querygroup
        --querygroup test-nodes

    Keyword arguments:
    args.querygroup -- actual group to query
    """

    sql = """SELECT HostName,AnsibleSSHHost FROM inventory WHERE
        GroupName='%s' ORDER BY HostName""" %(args.querygroup)
    con = MySQLdb.connect(args.host, args.user, args.password, args.db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    results = []
    for HostName, AnsibleSSHHost in rows:
        results.append({'host': HostName, 'ansible_ssh_host': AnsibleSSHHost})
    print(json.dumps(results))
    cur.close()
    con.close()

def query_host():
    """Query a specific host

    This will query a specific group and return the results.

    Ex.
    ansible_inventory.py --user ansible --password ansible --function queryhost
        --queryhost node0

    Keyword arguments:
    args.queryhost -- actual host to query
    """

    sql = """SELECT HostName,AnsibleSSHHost,GroupName FROM inventory
        WHERE HostName='%s'""" %(args.queryhost)
    con = MySQLdb.connect(args.host, args.user, args.password, args.db)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    results = []
    for HostName, AnsibleSSHHost, GroupName in rows:
        results.append({'host': HostName, 'ansible_ssh_host': AnsibleSSHHost,
                        'groups': GroupName})
    print(json.dumps(results, sort_keys=True))
    cur.close()
    con.close()

# Decide which function to execute
if args.function == "addhost":
    add_host()
if args.function == "all":
    all_inventory()
elif args.function == "groups":
    all_groups()
elif args.function == "hosts":
    all_hosts()
elif args.function == "queryhost":
    query_host()
elif args.function == "querygroup":
    query_group()
