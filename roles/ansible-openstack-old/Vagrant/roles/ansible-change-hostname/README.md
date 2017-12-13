Role Name
=========

Changes the hostname on a node to match the inventory hostname.

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-change-hostname
change_hostname_reboot: true  #defines if the node should reboot after changing the hostname
````

Dependencies
------------

None

Example Playbook
----------------

````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-change-hostname
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
