Role Name
=========

An [Ansible] role to install/configure [memcached]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-memcached.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-memcached)

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-memcached
memcached_config: false
memcached_connections_in_limit: '1024'
memcached_listen_address: '127.0.0.1'
memcached_log_file: '/var/log/memcached.log'
memcached_memory_cap: '64'
memcached_port: '11211'
memcached_verbose: false
memcached_verbose_verbose: false
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: memcached_hosts
  become: true
  vars:
  roles:
    - role: ansible-memcached
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
[memcached]: <http://memcached.org/>
