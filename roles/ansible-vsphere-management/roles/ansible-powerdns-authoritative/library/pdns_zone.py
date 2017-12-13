#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Jan-Piet Mens <jpmens () gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import os
try:
    import json
except ImportError:
    import simplejson as json
import fileinput
import fnmatch


DOCUMENTATION = '''
---
module: pdns_zone
short_description: Create/delete PowerDNS authoritative master/slave zones
description:
     - Lists, creates and deletes zones (a.k.a domains) of type master or slave in an
       authoritative PowerDNS server using its RESTful API.
     - By default the C(/etc/powerdns/pdns.conf) file is consulted to retrieve
       the I(api_key), I(api_host), and I(api_port).
version_added: "1.8"
options:
  zone:
    description:
      - The zone name, mandatory except when I(action) is C(list), and if it is,
        I(zone) may contain a shell-style glob pattern to list only zones which
        match said pattern, e.g. C(zone=*.org).
    required: true
    default: null
    aliases: [ "name", "domain" ]
  action:
    description:
      - The action to perform.
      - If C(action) equals C(delete), the zone is removed. Otherwise, if C(slave),
        C(master), or C(native), the respective type of zone is created.
      - If action equals C(list), an array of zone names / kinds is returned.
    required: true
    default: null
    choices: [ "slave", "master", "native", "delete", "list" ]
  pdnsconf:
    description:
      - The path to the PowerDNS configuration file from which I(api_key),
        I(api_host), and I(api_port) are read. This parameter can be omitted
        if you want to specify the three values manually. Failure to read
        the file is silently ignored.
    required: false
    default: "/etc/powerdns/pdns.conf"
  api_key:
    description:
      - The PowerDNS I(API key) which, by default is read from C(pdns.conf).
    required: true
    default: null
  api_host:
    description:
      - The hostname / IP address of the PowerDNS API which, by default, is read
        from C(pdns.conf)
    required: true
    default: localhost
  api_port:
    description:
      - The TCP port number of the PowerDNS API which on I(api_host); by default is read
        from C(pdns.conf)
    required: true
    default: null
  masters:
    description:
      - A comma-separated list of the names or addresses (or C(address:port))
        of the master server for a slave zone.  This parameter is required for
        action=C(slave).
    required: false
    default: null
  soa:
    description:
      - The I(rdata) for the SOA resource record. This parameter is required for
        action=C(master).
    required: false
    default: null
  nsset:
    description:
      - A comma-separated list of NS I(names) for a master zone (required for
        action=C(master) and C(native). Each element in the list will become a name server
        for the specified zone, configured with the specified C(ttl).
    required: false
    default: null
  ttl:
    description:
      - The TTL for the SOA and NS record sets for action=C(master).
    required: false
    default: 86400
  comment:
    description:
      - A comment to add to the C(comments) table when state=C(master) or C(slave).
    required: false
    default: "Ansible-managed"
notes:
    - It is not possible to convert a zone from slave to master or vice versa.
    - See also the M(dnsupdate) module.
# informational: requirements for nodes
# requirements: None
author: Jan-Piet Mens
'''

EXAMPLES='''
- name: Create a slave zone; obtain config from specific file
  action: pdns_zone zone="example.org"
            action=slave
            masters="127.0.0.2:5301"
            pdnsconf={{pdnsconf}}

- name: Delete all zones (master or slave) contained in the "zonelist" file
  action: pdns_zone zone={{ item }}
          action=delete
          api_key={{ api_key }}
          api_host={{ api_host }}
          api_port={{ api_port }}
   with_lines: cat zonelist

- name: Create a master zone with 3 NS records
  action: pdns_zone zone="example.com"
          action=master
          soa="ns.example.net hostmaster.example.com 1 1800 900 604800 3602"
          nsset="ns1.example.net,ns.example.com,xo.example.org"
          api_key={{ api_key }}
          api_host={{ api_host }}
          api_port={{ api_port }}
'''

headers = {
    "Accept" : "application/json",
    "X-API-Key" : None,
}
api_host = None
api_port = None
api_key  = None

# ==============================================================
def read_pdns_conf(path='/etc/powerdns/pdns.conf'):

    global api_host
    global api_port
    global api_key

    try:
        for line in fileinput.input([path]):
            if line[0] == '#' or line[0] == '\n':
                continue
            try:
                (key, val) = line.rstrip().split('=')
                if key == 'webserver-address':
                    api_host = val
                elif key == 'webserver-port':
                    api_port = int(val)
                elif key == 'experimental-api-key':
                    api_key = val
            except:
                pass
    except:
        raise

def zone_exists(module, base_url, zone):
    ''' Check if zone is configured in PowerDNS. Return
        kind of zone (native, master, slave) uppercased or None '''

    url = "{0}/{1}".format(base_url, zone)

    response, info = fetch_url(module, url, headers=headers)
    if info['status'] == 422:  # not found
        return None

    if info['status'] != 200:
        module.fail_json(msg="failed to check zone %s at %s: %s" % (zone, url, info['msg']))

    content = response.read()
    data = json.loads(content)

    kind = data.get('kind', None)
    if kind is not None:
        kind = kind.upper()
    return kind

def zone_list(module, base_url, zone=None):
    ''' Return list of existing zones '''

    list = []
    url = "{0}".format(base_url)

    response, info = fetch_url(module, url, headers=headers)
    if info['status'] != 200:
        module.fail_json(msg="failed to enumerate zones at %s: %s" % (url, info['msg']))

    content = response.read()
    data = json.loads(content)
    for z in data:
        if zone is None or fnmatch.fnmatch(z['name'], zone):
            list.append({
                'name'      : z['name'],
                'kind'      : z['kind'].lower(),
                'serial'    : z['serial'],
            })
    return list

def zone_delete(module, base_url, zone):
    ''' Delete a zone in PowerDNS '''

    url = "{0}/{1}".format(base_url, zone)

    response, info = fetch_url(module, url, headers=headers, method='DELETE')
    if info['status'] == 422:
        return False
    if info['status'] != 200:
        module.fail_json(msg="failed to delete zone %s at %s: %s" % (zone, url, info['msg']))

    return True


def zone_add_slave(module, base_url, zone, masters, comment):
    ''' Add a new Slave zone to PowerDNS '''

    kind = zone_exists(module, base_url, zone)
    if kind == 'SLAVE':
        return False

    if kind == 'MASTER' or kind == 'NATIVE':
        module.fail_json( msg="zone %s is %s. Cannot convert to slave" % (zone, kind))

    masters = masters.split(',')

    data = {
        'kind'      : 'Slave',
        'masters'   : masters,
        'name'      : zone,
        'comments'      : [{
                            'name'  : zone,
                            'type'  : 'SOA',
                            'account' : '',
                            'content' : comment,
                          }],
    }
    payload = json.dumps(data)

    response, info = fetch_url(module, base_url, data=payload, headers=headers, method='POST')
    if info['status'] != 200:
        module.fail_json(msg="failed to create slave zone %s at %s: %s" % (zone, base_url, info['msg']))

    return True

def zone_add_master(module, base_url, zone, soa_rdata, ns_rrset, comment, ttl=60, wantkind='Master'):
    ''' Add a new Master/Native zone to PowerDNS '''

    kind = zone_exists(module, base_url, zone)
    if kind == 'MASTER' or kind == 'NATIVE':
        return False

    if kind == 'MASTER':
        if kind == 'SLAVE' or kind == 'NATIVE':
            module.fail_json( msg="zone %s is %s. Cannot convert to master" % (zone, kind))
    if kind == 'NATIVE':
        if kind == 'SLAVE' or kind == 'MASTER':
            module.fail_json( msg="zone %s is %s. Cannot convert to native" % (zone, kind))

    records = []
    data = {
        'kind'          : str(wantkind).lower().title(),
        'masters'       : [ ],
        'name'          : zone,
        'nameservers'   : [],   # I'm creating records "manually" below to avoid automatic TTL=3600
        'records'       : records,
        'comments'      : [{
                            'name'  : zone,
                            'type'  : 'SOA',
                            'account' : '',
                            'content' : comment,
                          }],
    }

    records.append({
        'type'      : 'SOA',
        'name'      : zone,
        'ttl'       : ttl,
        'disabled'  : False,
        'content'   : soa_rdata,
    })

    for ns in ns_rrset.split(','):
        records.append({
            'type'      : 'NS',
            'name'      : zone,
            'ttl'       : ttl,
            'disabled'  : False,
            'content'   : ns,
        })


    payload = json.dumps(data)

    response, info = fetch_url(module, base_url, data=payload, headers=headers, method='POST')
    if info['status'] != 200:
        module.fail_json(msg="failed to create %s zone %s at %s: %s" % (kind, zone, base_url, info['msg']))

    return True

# ==============================================================
# main

def main():

    global api_host
    global api_port
    global api_key

    api_host = 'localhost'

    argument_spec = url_argument_spec()
    argument_spec.update(
        pdnsconf = dict(required=False, default='/etc/powerdns/pdns.conf'),
        api_key  = dict(required=False),
        api_host = dict(required=False),
        api_port = dict(required=False, type='int'),
        zone     = dict(required=False, default=None, aliases=['name', 'domain']),
        action   = dict(required=True, choices=['list', 'master', 'native', 'slave', 'delete']),
        masters  = dict(required=False),
        soa      = dict(required=False),
        nsset    = dict(required=False),
        comment  = dict(required=False, default='Ansible-managed'),
        ttl      = dict(required=False, type='int', default=86400)

    )

    module = AnsibleModule(
        argument_spec = argument_spec,
    )

    # Read default pdns.conf for defaults; allow module args
    # to override those
    read_pdns_conf(path=module.params['pdnsconf'])

    api_key   = module.params['api_key'] if module.params['api_key'] else api_key
    api_host  = module.params['api_host'] if module.params['api_host'] else api_host
    api_port  = module.params['api_port'] if module.params['api_port'] else api_port
    zone      = module.params['zone']
    masters   = module.params['masters']
    action    = module.params['action']
    soa       = module.params['soa']
    nsset     = module.params['nsset']
    comment   = module.params['comment']
    ttl       = module.params['ttl']

    base_url = 'http://{0}:{1}/servers/localhost/zones'.format(api_host, api_port)
    headers['X-API-Key'] = api_key

    if api_host is None or api_key is None or api_port is None:
        module.fail_json(msg="Zone %s requires api_host, api_key, api_port" % (zone))

    changed=True

    if action == 'master':
        if soa is None:
            module.fail_json( msg="Master zone %s requires SOA" % (zone))
        if nsset is None:
            module.fail_json( msg="Master zone %s requires NS set" % (zone))

        changed = zone_add_master(module, base_url, zone, soa, nsset, comment, ttl, 'master')

    if action == 'native':
        if soa is None:
            module.fail_json( msg="Native zone %s requires SOA" % (zone))
        if nsset is None:
            module.fail_json( msg="Native zone %s requires NS set" % (zone))

        changed = zone_add_master(module, base_url, zone, soa, nsset, comment, ttl, 'native')

    if action == 'slave':
        if masters is None:
            module.fail_json( msg="Slave zone %s requires masters" % (zone))

        changed = zone_add_slave(module, base_url, zone, masters, comment)

    if action == 'delete':
        changed = zone_delete(module, base_url, zone)

    if action == 'list':
        list = zone_list(module, base_url, zone)
        module.exit_json(zone=zone, changed=False, zones=list)

    # Mission accomplished

    module.exit_json(zone=zone, changed=changed, msg='OK')

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
main()
