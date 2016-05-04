Role Name
=========

Installs Django web framework https://www.djangoproject.com/  

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-django.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-django)

Requirements
------------

None

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Role Variables
--------------

````
---
# defaults file for ansible-django
django_db_type: sqlite  #defines DB type to use...sqlite or mysql
django_version: latest  #defines django version to install. set to latest for the latest version or use version number...ex. (1.8.7, 1.8.8, 1.9, 1.9.1)
````

Dependencies
------------

Install required dependencies as below:
````
sudo ansible-galaxy install -r requirements.yml
````

Example Playbook
----------------

#### GitHub
````
---
- name: Install Django
  hosts: all
  sudo: true
  vars:
  roles:
    - role: ansible-django
    - role: ansible-mysql
      when: >
            (django_db_type is defined and django_db_type == "mysql")
  tasks:
````

#### Galaxy
````
---
- name: Install Django
  hosts: all
  sudo: true
  vars:
  roles:
    - role: mrlesmithjr.django
    - role: mrlesmithjr.mysql
      when: >
            (django_db_type is defined and django_db_type == "mysql")
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
