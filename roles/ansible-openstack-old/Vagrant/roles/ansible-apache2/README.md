Role Name
=========

Installs apache2 http://httpd.apache.org/

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-apache2.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-apache2)

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-apache2
apache2_config_php: false  #defines if php.ini should be configured for Apache2
apache2_install_php_sqlite: false
apache2_install_php: false
apache2_php_max_memory: 128M  #defines max memory for Apache php....default is 128M
````

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.apache2 }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
