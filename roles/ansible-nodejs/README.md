Role Name
=========

Installs NodeJS (https://nodejs.org/en/)

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-nodejs
nodejs_debian_packages:
  - 'build-essential'
  - 'nodejs'
nodejs_debian_repo_info:
  id: '68576280'
  repo_key: 'https://keyserver.ubuntu.com/pks/lookup?op=get&fingerprint=on&search=0x1655A0AB68576280'
  repos:
    - 'deb https://deb.nodesource.com/node_{{ nodejs_version }} {{ ansible_distribution_release|lower }} main'
    - 'deb-src https://deb.nodesource.com/node_{{ nodejs_version }} {{ ansible_distribution_release|lower }} main'
nodejs_version: '4.x'  #defines nodejs version to install..( 4.x|5.x )
```

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
