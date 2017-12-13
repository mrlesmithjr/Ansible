Role Name
=========

Installs snmpd

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-snmpd.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-snmpd)

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------
````
config_snmpd: true
enable_snmpd: true
snmpd_authorized_networks: []  #define read-only snmpd settings
#  - network: 10.0.101.0/24
#    community: example
````
Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrlesmithjr.snmpd }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
