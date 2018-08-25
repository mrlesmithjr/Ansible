Role Name
=========

Installs and configures Shorewall firewall (http://shorewall.net)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-shorewall.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-shorewall)

Requirements
------------

None

Role Variables
--------------

[defaults/main.yml](defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------

````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-shorewall
  tasks:
````
License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
