Role Name
=========

An [Ansible] bootstrap role

- useful for adding initial post deployment tasks
- creating initial users
- setting initial user passwords

Requirements
------------

None

Role Variables
--------------

```
---
# Only set to true if desired to set root password...for Debian/Ubuntu systems

bootstrap_debian_set_root_pw: false

# Define root password for hosts
# If Ubuntu/Debian choose wisely if you want to do this
# Generate password (echo password | mkpasswd -s -m sha-512)
# The password below is 'P@55w0rd'
bootstrap_root_password: '$6$8tMUxKP33/$Fb/hZBaYvyzGubO9nrlRJMjUnt3aajXZwxCifH9NYqrhjMlC9COWmNNFiMpnyNGsgmDeNCCn2wKNh0G1E1BBV0'

# Defines if root password should be set
# This only applies to non Debian/Ubuntu systems
bootstrap_set_root_pw: false
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-bootstrap
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
