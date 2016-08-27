Role Name
=========

Installs and configures ZFS On Linux (http://zfsonlinux.org/)

Requirements
------------

At least one un-used physical hard-drive to create ZFS Pool

Vagrant
-------
Spin up a test environment using Vagrant  
````
vagrant up
````
This will spin up a server w/ some ZFS volumes including iSCSI devices...  
You can view/use iSCSI volumes from the client node...  
````
vagrant ssh client
sudo iscsiadm -m discovery -t st -p 192.168.202.201
sudo iscsiadm -m node --login
````
You should now have /dev/sdb and /dev/sdc on your client to format and mount  
````
sudo fdisk -l
````
````
Disk /dev/sdb: 1073 MB, 1073741824 bytes
34 heads, 61 sectors/track, 1011 cylinders, total 2097152 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/sdb doesn't contain a valid partition table

Disk /dev/sdc: 2147 MB, 2147483648 bytes
67 heads, 62 sectors/track, 1009 cylinders, total 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/sdc doesn't contain a valid partition table
vagrant@client:~$ sudo fdisk /dev/sdb
Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel
Building a new DOS disklabel with disk identifier 0xa1af287f.
Changes will remain in memory only, until you decide to write them.
After that, of course, the previous content won't be recoverable.
````

Role Variables
--------------

````
---
# defaults file for ansible-zfs
create_zfs_pools: false  #defines if ZFS pool(s) are created
create_zfs_filesystems: false  #defines if ZFS filesystem(s) are created
create_zfs_volumes: false  #defines if ZFS volumes(s) are created
zfs_debian_package: 'zfsonlinux_{{ zfs_debian_package_version }}_all.deb'
zfs_debian_package_key: 'http://zfsonlinux.org/4D5843EA.asc'
zfs_debian_package_url: 'http://archive.zfsonlinux.org/debian/pool/main/z/zfsonlinux'
zfs_debian_package_version: 6
zfs_enable_iscsi: false  #defines if iscsitarget is installed to server iSCSI volumes
zfs_enable_nfs: false  #defines if NFS Kernel Server should be installed to serve NFS
zfs_enable_performance_tuning: false  #defines if paramaters defined in zfs_performance_tuning are applied
zfs_filesystems:  #defines filesystems to manage
  - name: 'nfs'
    pool: 'tank'
    atime: 'off'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    logbias: 'latency'  # latency (default) | throughput
    primarycache: 'all'  # all (default) | none | metadata
    quota: '3G'
    recordsize: '16K'  #defines recordsize.. 16K | 32K | 64K | 128K (default) | and etc.
    sharenfs: 'on'
    sync: 'disabled'  # standard (default) | always | disabled
    state: 'present'
zfs_iscsistarget_enable: '{{ zfs_enable_iscsi }}'  #defines if iscsitarget service is enabled
zfs_iscsistarget_iqn: iqn.2001-04.org.example  #define your FQDN in reverse...(local.vagrant)
zfs_iscsistarget_max_sleep: 3
zfs_iscsistarget_options: ''
zfs_iscsitarget_target_portals:
  - ALL  #define IP address to listen for iSCSI connections | ALL (default) | cidr (x.x.x.x/xx) | disable ALL if defining cidr
#  - 10.0.2.0/24
#  - 192.168.2.0/24
zfs_performance_tuning:
  - param: 'zfs_prefetch_disable'
    value: '1'
  - param: 'zfs_txg_timeout'
    value: '5'
  - param: 'zfs_arc_max'
    value: '{{ (ansible_memtotal_mb | int * 1024 * 1024 * 0.5) | round | int }}'  # 1/2 total system memory
  - param: 'zfs_arc_meta_limit'
    value: '{{ (ansible_memtotal_mb | int * 1024 * 1024 * 0.125) | round | int }}'  # 1/4 zfs_arc_max
  - param: 'zfs_arc_min'
    value: '{{ (ansible_memtotal_mb | int * 1024 * 1024 * 0.0625) | round | int }}'  # 1/2 zfs_arc_meta_limit
zfs_pools:  #defines zpool(s) to manage
  - name: tank
#    atime: 'on'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - '/dev/sdb'
      - '/dev/sdc'
    type: basic  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: present
zfs_ubuntu_ppa: 'ppa:zfs-native/stable'
zfs_volumes:  #defines block-device volumes to manage
  - name: 'backups'
    pool: 'tank'
    shareiscsi: 'on'  #defines if iscsitarget should serve volume... | on | off | or not defined
    volsize: '1G'  #defines volsize for block devices
    lun: 0
    allow:
      - ALL
    state: 'present'
  - name: 'data'
    pool: 'tank'
    shareiscsi: 'on'
    volsize: '2G'
    lun: 1
    allow:
#      - 10.0.0.0/8
      - 192.168.202.0/24
    state: 'present'
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
---
- name: Installs ZFS On Linux
  hosts: all
  become: true
  vars:
    - zfs_iscsistarget_iqn: iqn.2001-04.local.vagrant  #define your FQDN in reverse...(local.vagrant)
    - zfs_iscsitarget_target_portals:
        - 192.168.202.0/24
    - zfs_enable_iscsi: true
    - zfs_enable_nfs: true
  roles:
    - role: ansible-zfs
  tasks:
````
#### Galaxy
````
---
- name: Installs ZFS On Linux
  hosts: all
  become: true
  vars:
    - zfs_iscsistarget_iqn: iqn.2001-04.local.vagrant  #define your FQDN in reverse...(local.vagrant)
    - zfs_iscsitarget_target_portals:
        - 192.168.202.0/24
    - zfs_enable_iscsi: true
    - zfs_enable_nfs: true
  roles:
    - role: mrlesmithjr.zfs
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
