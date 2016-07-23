Role Name
=========

Installs mongodb https://www.mongodb.org/

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-mongodb
mongodb_apt_keyserver: 'keyserver.ubuntu.com'
mongodb_apt_gpg_key: 'EA312927'
mongodb_debian_apt_repo: 'deb http://repo.mongodb.org/apt/{{ ansible_distribution|lower }} {{ ansible_distribution_release }}/mongodb-org/{{ mongodb_version }} main'
mongodb_ubuntu_apt_repo: 'deb http://repo.mongodb.org/apt/{{ ansible_distribution|lower }} {{ ansible_distribution_release }}/mongodb-org/{{ mongodb_version }} multiverse'
mongodb_version: '3.2'
````

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.mongodb }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
