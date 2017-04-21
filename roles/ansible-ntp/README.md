Role Name
=========

An [Ansible] role to install/configure NTP

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-ntp.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-ntp)

Requirements
------------

Define ntp_master for your group of servers which should be used for your
internal ntp servers for clients to connect to.
ex. group_vars/ntp_masters

Role Variables
--------------

```
---
# defaults file for ansible-ntp
# Defines if host is ntp_master
# set ntp_master to true on specific group_vars/group
ntp_master: false

# Define your ntp_master_servers
ntp_master_servers:
  - 0.ubuntu.pool.ntp.org
  - 1.ubuntu.pool.ntp.org
  - 2.ubuntu.pool.ntp.org
  - 3.ubuntu.pool.ntp.org

# Defines your primary domain name (FQDN)
ntp_pri_domain_name: 'example.org'

# Defines internal ntp servers for clients to poll
# ntp_servers:
#  - 'ntp1.{{ ntp_pri_domain_name }}'
#  - 'ntp2.{{ ntp_pri_domain_name }}'
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
    - role: ansible-ntp
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
