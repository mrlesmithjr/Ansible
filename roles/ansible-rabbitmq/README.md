Role Name
=========

An [Ansible] role to install/configure [RabbitMQ]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-rabbitmq.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-rabbitmq)

Requirements
------------

Ensure hostnames are resolvable prior to clustering...either update /etc/hosts
or ensure DNS is working.

Vagrant
-------

Spin up a 3 node HA Cluster for testing...  
Install Ansible role on your host:  
```
sudo ansible-galaxy install -r requirements.yml -f
```
Now spin up your environment...  
```
vagrant up
```
When you are done testing, tear it all down...  
```
./cleanup.sh
```

Role Variables
--------------

[Role Defaults](./defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------

[Example Playbook](./playbook.yml)

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- [@mrlesmithjr]
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://www.twitter.com/mrlesmithjr>

[Ansible]: <https://www.ansible.com>
[RabbitMQ]: <https://www.rabbitmq.com/>
