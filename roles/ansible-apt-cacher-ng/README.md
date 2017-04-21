Role Name
=========

An [Ansible] role to install/configure [apt-cacher-ng]
- (Client/server configurations)

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-apt-cacher-ng
apt_cacher_configs:
  - 'acng.conf'
  - 'security.conf'
apt_cacher_ng_account:
  - name: 'admin'
    password: 'admin'
apt_cacher_ng_cachedir: '/var/cache/apt-cacher-ng'
apt_cacher_ng_port: '3142'

# Defines hostname of server
apt_cacher_server: []

apt_cacher_passthrough_patterns:
  # Allowing everything to be cached and connected to
  - '.*'

# Defines if apt-caching should be used for clients
enable_apt_caching: false
```

Dependencies
------------

None

Example Playbook
----------------
```
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-apt-cacher-ng
  tasks:
```

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
[apt-cacher-ng]: <https://www.unix-ag.uni-kl.de/~bloch/acng/>
