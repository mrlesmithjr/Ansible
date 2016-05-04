Role Name
=========

Installs NodeJS (https://nodejs.org/en/)

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-nodejs
nodejs_debian_packages:
  - 'build-essential'
  - 'nodejs'
nodejs_debian_repo_info:
  repo_key: 'https://deb.nodesource.com/gpgkey/nodesource.gpg.key'
  repos:
    - 'deb https://deb.nodesource.com/node_{{ nodejs_version }} {{ ansible_distribution_release|lower }} main'
    - 'deb-src https://deb.nodesource.com/node_{{ nodejs_version }} {{ ansible_distribution_release|lower }} main'
nodejs_version: '4.x'  #defines nodejs version to install..( 4.x|5.x )
````

Dependencies
------------

None

Example Playbook
----------------

````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-nodejs
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
