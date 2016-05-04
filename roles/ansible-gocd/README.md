Role Name
=========

Installs GoCD (Go Continuous Delivery) https://www.go.cd

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-gocd.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-gocd)

Requirements
------------

None

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Usage
-----

#### Vagrant
http://127.0.0.1:8153/go

#### Non-Vagrant
http://iporhostname:8153/go

Role Variables
--------------

````
---
# defaults file for ansible-gocd
gocd_agent: true  #defines if go-agent should be installed. All hosts require an agent
gocd_apt_packages:  #defines additional apt packages to install
  - name: python-dev
    state: present
  - name: python-pip
    state: present
gocd_python_modules:  #defines additional python modules to install
  - name: ansible
    state: present
  - name: pysphere
    state: present
  - name: pyvmomi
    state: present
  - name: redis
    state: present
gocd_repo_key: 'https://bintray.com/user/downloadSubjectPublicKey?username=gocd'
gocd_repo: 'deb http://dl.bintray.com/gocd/gocd-deb/ /'
gocd_server: false  #defines if go-server should be installed. You will want to define this as true only on specific hosts to function as a server
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
- name: Install GoCD
  hosts: all
  sudo: true
  vars:
  roles:
    - role: ansible-gocd
    - role: ansible-redis
  tasks:
````

#### Galaxy
````
---
- name: Install GoCD
  hosts: all
  sudo: true
  vars:
  roles:
    - role: mrlesmithjr.gocd
    - role: mrlesmithjr.redis
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
