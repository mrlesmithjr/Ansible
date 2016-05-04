Role Name
=========

Installs and configures OpenNMS http://www.opennms.org/

Requirements
------------

Install all Ansible role requirements.
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Usage
-----
````
user: admin
pass: admin
````

###### Non-Vagrant
Login to WebUI (http://iporhostname:8980/opennms)

###### Vagrant
Login to WebUI (http://127.0.0.1:8980/opennms)

Role Variables
--------------

````
---
# defaults file for ansible-opennms
opennms_debian_repo_key: 'https://debian.opennms.org/OPENNMS-GPG-KEY'
opennms_debian_repos:
  - 'deb http://debian.opennms.org stable main'
  - 'deb-src http://debian.opennms.org stable main'
````

Dependencies
------------

#### GitHub
````
ansible-ntp
ansible-postgresql
ansible-postfix
ansible-oracle-java8
ansible-opennms
````
#### Galaxy
````
mrlesmithjr.ntp
mrlesmithjr.postgresql
mrlesmithjr.postfix
mrlesmithjr.oracle-java8
mrlesmithjr.opennms
````
Follow instructions in requirements to install dependencies.

Example Playbook
----------------

#### GitHub
````
---
- name: provisions OpenNMS
  hosts: all
  become: true
  vars:
  roles:
    - role: ansible-ntp
    - role: ansible-postgresql
    - role: ansible-postfix
    - role: ansible-oracle-java8
    - role: ansible-opennms
  tasks:
````
#### Galaxy
````
---
- name: provisions OpenNMS
  hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.ntp
    - role: mrlesmithjr.postgresql
    - role: mrlesmithjr.postfix
    - role: mrlesmithjr.oracle-java8
    - role: mrlesmithjr.opennms
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
