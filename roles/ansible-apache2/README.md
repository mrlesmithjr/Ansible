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
apache2_default_port: 80
apache2_install_php_sqlite: false
apache2_install_php: false
apache2_php_max_memory: '128M'  #defines max memory for Apache php....default is 128M
apache2_server_admin: 'webmaster@localhost'
apache2_virtual_hosts:
  - documentroot: '/var/www/example.com'
    default_site: false
    port: 80
    serveradmin: '{{ apache2_server_admin }}'
    servername: 'www.example.com'
  - documentroot: '/var/www/example.org'
    default_site: false
    port: 80
    serveradmin: '{{ apache2_server_admin }}'
    servername: 'www.example.org'
  - documentroot: '/var/www/html'
    default_site: true
    port: 80
    serveradmin: '{{ apache2_server_admin }}'
    servername: ''
config_apache2: false
config_apache2_virtual_hosts: false
pri_domain_name: 'example.org'
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
