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

```
---
# defaults file for ansible-zfs
zfs_create_filesystems: false  #defines if ZFS filesystem(s) are created
zfs_create_pools: false  #defines if ZFS pool(s) are created
zfs_create_volumes: false  #defines if ZFS volumes(s) are created
zfs_debian_package_key: 'http://zfsonlinux.org/4D5843EA.asc'
zfs_debian_package_url: 'http://archive.zfsonlinux.org/debian/pool/main/z/zfsonlinux'
zfs_debian_package_version: 6
zfs_debian_package: 'zfsonlinux_{{ zfs_debian_package_version }}_all.deb'
zfs_enable_auto_snapshots: true
zfs_enable_iscsi: false  #defines if iscsitarget is installed to server iSCSI volumes
zfs_enable_nfs: false  #defines if NFS Kernel Server should be installed to serve NFS
zfs_enable_performance_tuning: false  #defines if paramaters defined in zfs_performance_tuning are applied
zfs_enable_samba: false # Defines if Samba is installed and configured
zfs_filesystems:  #defines filesystems to manage
  - name: 'nfs'
    pool: 'tank'
    atime: 'off'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    logbias: 'latency'  # latency (default) | throughput
    # mountpoint: '/var/lib/docker'  #define an alternate mountpoint
    primarycache: 'all'  # all (default) | none | metadata
    quota: '3G'
    recordsize: '16K'  #defines recordsize.. 16K | 32K | 64K | 128K (default) | and etc.
    sharenfs: 'on'
    sync: 'disabled'  # standard (default) | always | disabled
    state: 'present'
  - name: 'Shares/Movies'
    compression: 'lz4'
    group: 'nogroup'
    mountpoint: '/TANK/Shares/Movies'
    owner: 'nobody'
    pool: 'TANK'
    quota: 'none'
    sharesmb: true
    smb_options:
      browseable: 'yes'
      comment: ''
      create_directory_mask: '0755'
      create_mask: '0777'
      guest_ok: 'yes'
      read_only: 'no'
      share_name: 'Movies'
      writable: 'yes'
    state: 'present'
    sync: 'disabled' #standard (default) | always | disabled
zfs_iscsistarget_enable: '{{ zfs_enable_iscsi }}'  #defines if iscsitarget service is enabled
zfs_iscsistarget_iqn: iqn.2001-04.org.example  #define your FQDN in reverse...(local.vagrant)
zfs_iscsistarget_max_sleep: 3
zfs_iscsistarget_options: ''
zfs_iscsitarget_target_portals:
  - ALL  #define IP address to listen for iSCSI connections | ALL (default) | cidr (x.x.x.x/xx) | disable ALL if defining cidr
#  - 10.0.2.0/24
#  - 192.168.2.0/24
zfs_manage_filesystem_permissions: false # Defines if ZFS Filesystem mountpoint permissions are managed
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
  - name: 'SSD-TANK'
    action: 'create'
#    atime: 'on'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-INTEL_SSDSC2BW240A4_CVDA352100YL2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_BTDA329505KM2403GN'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'SSD-TANK'
    action: 'add'
#    atime: 'on'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-INTEL_SSDSC2BW240A4_CVDA352100GP2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_CVDA401000Q02403GN'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'SSD-TANK'
    action: 'add'
#    atime: 'on'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-INTEL_SSDSC2BW240A4_CVDA4010045B2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_BTDA329501102403GN'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
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
```

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

Advanced Example ZPool Creation
-------------------------------
```
zfs_pools:  #defines zpool(s) to manage
  - name: 'SSD-TANK'
    action: 'create'
#    atime: 'on'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-INTEL_SSDSC2BW240A4_CVDA352100YL2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_BTDA329505KM2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_CVDA352100GP2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_CVDA401000Q02403GN'
      - 'ata-INTEL_SSDSC2BW240A4_CVDA4010045B2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_BTDA329501102403GN'
      - 'ata-INTEL_SSDSC2BW240A4_BTDA329503XM2403GN'
      - 'ata-INTEL_SSDSC2BW240A4_CVDA4010011R2403GN'
    type: 'raidz2'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'SSD-TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:
      - 'ata-INTEL_SSDSC2BW240A4_BTDA3300022F2403GN'
    type: 'spare'
    state: 'present'
  - name: 'TANK'
    action: 'create'
#    atime: 'on'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-ST2000VN000-1HJ164_W522KVAS'
      - 'ata-ST2000VN000-1HJ164_W522KW2J'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-ST2000DM001-1CH164_Z1E957EP'
      - 'ata-ST2000DM001-1ER164_W4Z08B5M'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-ST2000DM001-1ER164_W4Z08FPX'
      - 'ata-ST2000DM001-1ER164_W5009JQ4'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-ST2000DM001-1CH164_W1E3XCBV'
      - 'ata-ST2000DM001-1CH164_W1E3V7VA'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-ST31000340NS_9QJ814GW'
      - 'ata-ST31000340NS_9QJ80NQK'
    type: 'mirror'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-INTEL_SSDSC2CW120A3_CVCV248102U3120BGN'
    type: 'cache'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-INTEL_SSDSC2CW120A3_CVCV2515011Y120BGN'
    type: 'cache'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
  - name: 'TANK'
    action: 'add'
    compression: 'lz4'  # on | off (default) | lzjb | gzip | gzip-1 | gzip-2 | gzip-3 | gzip-4 | gzip-5 | gzip-6 | gzip-7 | gzip-8 | gzip-9 | lz4 | zle
    devices:  #define devices to create pool with...can define multiple by | sdb sdc sdd sde sdf | all on one line w/spaces
      - 'ata-ST2000DL003-9VT166_5YD48V54'
    type: 'spare'  #define pool type... | basic (no-raid) | mirror | raidz | raidz2 | raidz3
    state: 'present'
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
