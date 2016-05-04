Role Name
=========

Installs and configures open-iscsi initiator (http://www.open-iscsi.org/)

Requirements
------------

In order to attach to iSCSI targets, they must exist on your NAS/SAN prior to attaching  
to them.

Role Variables
--------------

````
---
# defaults file for ansible-open-iscsi
config_open_iscsi: false
config_open_iscsi_lvm_groups: false
config_open_iscsi_targets: false
open_iscsi_debian_pre_req_packages:
  - lvm2
  - scsitools
  - xfsprogs
open_iscsi_lvm_groups:
  - 'glusterfs-vg'
open_iscsi_mode: 'automatic'
open_iscsi_targets:
  - name: '{{ ansible_hostname }}'
    discover: true
    automatic: true
    portal: 'node0.{{ pri_domain_name }}'
    target: 'iqn.2001-04.org.example:storage.{{ ansible_hostname }}'
    login: true
pri_domain_name: 'example.org'
````
Dependencies
------------

None

Example Playbook
----------------

````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-open-iscsi
  tasks:

````

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
