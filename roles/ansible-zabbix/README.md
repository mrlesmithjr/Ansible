Role Name
=========

An [Ansible] role to install/configure [Zabbix] Server.

Requirements
------------

Install required Ansible roles:
```
sudo ansible-galaxy install -r requirements.yml -f
```

Vagrant
-------
Spin up a test environment using Vagrant:  
```
sudo ansible-galaxy install -r requirements.yml -f
vagrant up
```
Once the environment is up connect to http://127.0.0.1:8080/zabbix using
your browswer of choice.  
Login using:  
```
username: Admin
password: zabbix
```
You are now ready to begin testing and using Zabbix.  
When you are done with your testing you can tear down by:  
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
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[Zabbix]: <https://www.zabbix.com>
