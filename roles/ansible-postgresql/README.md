Role Name
=========

An [Ansible] role to install/configure [Postgresql]

Requirements
------------

Install [required](./requirements.yml) [Ansible] roles:
```
sudo ansible-galaxy install -r requirements.yml
```

If setting up replication:

`defaults/main.yml`
```
# Define Ansible group which contains the hosts to setup replication
postgresql_replication_group: 'postgres_replication'
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
[Postgresql]: <https://www.postgresql.org/>
