Role Name
=========

Installs apt-cacher-ng https://www.unix-ag.uni-kl.de/~bloch/acng/ (Client/server configurations)

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

````
apt_cacher_configs:
  - acng.conf
  - security.conf
apt_cacher_ng_account:
  - name: admin
    password: admin
apt_cacher_ng_cachedir: /var/cache/apt-cacher-ng
apt_cacher_ng_port: 3142
apt_cacher_server: []  #defines hostname of server...define here or gloabally group_vars/all/servers
apt_cacher_passthrough_patterns:
  - .*  #allowing everything to be cached and connected to
enable_apt_caching: false  #defines if apt-caching should be used for clients...define here or globally group_vars/all/configs
````

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrlesmithjr.apt-cacher-ng }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
