Role Name
=========

Installs and configures iscsitarget (http://iscsitarget.sourceforge.net/)  
Currently only supports FileIO (File-based LUN creations)

Requirements
------------

Install requirements using Ansible Galaxy.
````
sudo ansible-galaxy install -r requirements.yml -f
````

Role Variables
--------------

````
---
# defaults file for ansible-iscsitarget
iscsitarget_debian_packages:
  - iscsitarget
  - iscsitarget-dkms
iscsitarget_dedicated_hd: '/dev/sdb'  #define the dedicated hard drive to use for creating iscsi luns on.
iscsitarget_device_dir: '/storage'
iscsitarget_enable: true  #defines if iscsitarget service is enabled
iscsitarget_file_devices:  #size=bs*count (ex. 1M*5120=5G)
  - name: lun0.img
    lun: 0
    bs: 1M
    count: 5120
    allow:
      - ALL
    enabled: false
  - name: lun1.img
    lun: 1
    bs: 1M
    count: 1024
    allow:
      - 10.0.2.0/24
      - 192.168.202.0/24
    enabled: true
iscsitarget_iqn: iqn.2001-04.org.example  #define your FQDN in reverse...(local.vagrant)
iscsitarget_max_sleep: 3
iscsitarget_options: ''
iscsitarget_use_dedicated_hd: false  #defines if you would like to use a dedicated hard drive for creating iscsi luns on..not presenting raw disks.
````

Dependencies
------------

https://github.com/mrlesmithjr/ansible-network-tweaks.git

Example Playbook
----------------

#### GitHub
````
---
- hosts: all
  become: true
  vars:
    - iscsitarget_iqn: iqn.2001-04.local.vagrant
    - iscsitarget_use_dedicated_hd: true
    - pri_domain_name: 'vagrant.local'
  roles:
    - role: ansible-iscsitarget
    - role: ansible-network-tweaks
  tasks:
````
#### Galaxy
````
---
- hosts: all
  become: true
  vars:
    - iscsitarget_iqn: iqn.2001-04.local.vagrant
    - iscsitarget_use_dedicated_hd: true
    - pri_domain_name: 'vagrant.local'
  roles:
    - role: mrlesmithjr.iscsitarget
    - role: mrlesmithjr.network-tweaks
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
