Role Name
=========

Installs ntp

Requirements
------------

Define ntp_master for your group of servers which should be used for your internal ntp servers for clients to connect to.
ex. group_vars/ntp_masters

Role Variables
--------------

````
ntp_master: false  #defines if host is ntp_master....set ntp_master to true on specific group_vars/group
ntp_master_servers:  #define your ntp_master_servers....set in group_vars/all/configs
  - 0.ubuntu.pool.ntp.org
  - 1.ubuntu.pool.ntp.org
  - 2.ubuntu.pool.ntp.org
  - 3.ubuntu.pool.ntp.org
#ntp_servers:  #defines internal ntp servers for clients to poll
#  - 'ntp1.{{ pri_domain_name }}'
#  - 'ntp2.{{ pri_domain_name }}'
pri_domain_name: example.org  #defines your primary domain name...define here or globally in group_vars/all
````

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrlesmithjr.ntp }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
