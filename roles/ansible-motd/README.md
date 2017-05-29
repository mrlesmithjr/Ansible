Role Name
=========

An [Ansible] role to manage [MOTD]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-motd
#
# Defines default directory for MOTD scripts
motd_default_dir: '/etc/update-motd.d'

# Defines a default message to apply above any custom messages
motd_default_message: 'Welcome to your DEV environment'

# Defines if all default MOTD scripts in motd_default_dir should be disabled
motd_disable_defaults: true
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
    - role: ansible-motd
  tasks:
```

Example MOTD
------------

```
Last login: Tue Apr  4 22:36:34 2017 from 10.0.2.2

****************Ansible Managed MOTD****************
Welcome to your Dev Environment

System Information For Hostname: node0

Distribution: Fedora
Distribution Release: Twenty Five
Distribution Version: 25
DNS Search: etsbv.internal
DNS Server(s): 10.0.2.3
Interfaces: lo(127.0.0.1) eth1(192.168.250.10)(08:00:27:44:8a:09) eth0(10.0.2.15)(08:00:27:00:92:30)
Kernel: 4.8.6-300.fc25.x86_64
Memory Installed: 0.5GB
Memory Swapfile: 1.2GB
Mounts: Mount: /dev/sda3(/)(15.0GB) Mount: /dev/sda1(/boot)(1.0GB)
Processors: 1
Python Version: 2.7.13
Timezone: EDT(-0400)

************End Of Ansible Managed MOTD*************
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
[MOTD]: <https://en.wikipedia.org/wiki/Motd_(Unix)>
