Role Name
=========

Installs conntrackd http://conntrack-tools.netfilter.org/conntrackd.html

Requirements
------------

Each host must be configured with more than one network interface. A dedicated interface is used for syncing.

Role Variables
--------------

````
config_conntrackd: false  #defines if conntrackd should be configured
conntrackd_ignore_addresses:
  - '{{ ansible_default_ipv4.address }}'
  - '{{ conntrackd_sync_ip }}'
conntrackd_sync_ip: 1.1.1.1  #defines ip address to use for syncing...each host unique...define in host_vars/host
conntrackd_sync_int: eth1  #defines interface to use for syncing...must be a dedicated interface
enable_conntrackd: true  #defines if conntrackd should be enabled
````

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrlesmithjr.conntrackd }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
