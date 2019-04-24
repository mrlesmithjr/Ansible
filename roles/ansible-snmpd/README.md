Role Name
=========

An [Ansible] role to install/configure [SNMPD]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-snmpd.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-snmpd)

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-snmpd
snmpd_config: true
snmpd_enable: true
snmpd_trap: false

# Define read-only snmpd settings
snmpd_authorized_networks: []
#  - network: 10.0.101.0/24
#    community: example

snmpd_sysLocation: "Sitting on the Dock of the Bay"
snmpd_sysContact: "Me <me@example.org>"
```

Dependencies
------------

None

Example Playbook
----------------
```
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-snmpd
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[SNMPD]: <http://net-snmp.sourceforge.net/>
