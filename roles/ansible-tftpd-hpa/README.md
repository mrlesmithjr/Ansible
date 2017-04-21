Role Name
=========

An [Ansible] role to install/configure [tftpd-hpa]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-tftpd-hpa

# Defines tftp root directory
tftp_directory: '/var/lib/tftpboot'

# Defines tftp options for daemon...(-c allow new files to be created)
tftp_options: '--secure -c'

tftp_netboot_file: 'netboot.tar.gz'
tftp_netboot_url: 'http://archive.ubuntu.com/ubuntu/dists/trusty-updates/main/installer-amd64/current/images/netboot'
```

Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: tftp_servers
  become: true
  vars:
  roles:
    - role: ansible-tftpd-hpa
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
[tftpd-hpa]: <https://help.ubuntu.com/community/TFTP>
