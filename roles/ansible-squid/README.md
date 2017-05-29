Role Name
=========

An [Ansible] role to install/configure [Squid]
* Configurable and cache peering

Requirements
------------

If you want to use haproxy and/or keepalived you will need to install the roles
under dependencies and configure each role. Each role
(haproxy, keepalived and squid) should be configured using group_vars/group
and host_vars/host. Ensure correct configurations within each role. If you
only require squid then you may disregard the haproxy and keepalived roles.

Install all [Ansible] [role requirements](./requirements.yml).

```
sudo ansible-galaxy install -r requirements.yml -f
```

Vagrant
-------
Spin up Environment under Vagrant to test.
```
vagrant up
```

Role Variables
--------------

[Role Defaults](defaults/main.yml)

Dependencies
------------


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
[Squid]: <http://www.squid-cache.org/>
