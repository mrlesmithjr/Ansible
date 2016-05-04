Role Name
=========

Installs and configures tftpd-hpa role.

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-tftpd-hpa.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-tftpd-hpa)

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-tftpd-hpa
tftp_directory: '/var/lib/tftpboot'  #defines tftp root directory
tftp_options: '--secure -c'  #defines tftp options for daemon...(-c allow new files to be created)
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-tftpd-hpa
  tasks:
````

#### Galaxy
````
- hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.tftpd-hpa
  tasks:
````

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
