Role Name
=========

An [Ansible] role to install/configure [MAAS]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-maas
maas_adminusers:
  - username: 'root'
    email: 'admin@{{ maas_dns_domain }}'
    password: 'r00tm3'
maas_dns_domain: 'vagrant.local'
maas_region_controller: '192.168.250.10'
maas_region_controller_url: 'http://{{ maas_region_controller }}:5240/MAAS'
maas_repo: 'ppa:maas/stable'

# Defines if maas user should generate ssh keys
# Usable for remote KVM/libvirt power actions
maas_setup_user: false

maas_single_node_install: true
```

Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: maas
  vars:
  roles:
    - role: ansible-maas
  tasks:
```

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
[MAAS]: <https://maas.io/>
