Role Name
=========

An Ansible role to install and configure CTDB (https://ctdb.samba.org/)

CTDB is a cluster implementation of the TDB database used by Samba and other projects to store temporary data.

Requirements
------------

Install additional Ansible required roles...  
````
ansible-galaxy install -r requirements.yml
````

Role Variables
--------------

````
---
# defaults file for ansible-ctdb
config_ctdb: false
ctdb_backup_configs: true
ctdb_glusterfs_mount: '/mnt/ctdb'  #NEEDS TO BE A GLUSTERFS MOUNT....or LOCKING FAILS
ctdb_glusterfs_client_mount: '/data/shares'  #Defines root mount for creating shares
ctdb_install_samba: true  #define if samba is to be installed using this role or set to false if you use another ansible role to install samba
ctdb_install_winbind: true
ctdb_lock_directory: '{{ ctdb_glusterfs_mount }}/lock'
ctdb_lockfile: '{{ ctdb_lock_directory }}/lockfile'
ctdb_manages_nfs: false
ctdb_manages_samba: true
ctdb_manages_winbind: false  #enable if using Samba in AD or LDAP
ctdb_nodes_cluster_address_int: 'eth1'  #ensure the address associated with this interface is already configured (eth0|eth1|eth2|enp0s3|enp0s8|etc...)
ctdb_nodes_file: '/etc/ctdb/nodes'
ctdb_nodes_group: 'ctdb-servers'
ctdb_public_addresses:
  - address: 192.168.202.100  #samba
    bind_interface: '{{ ansible_eth1.device }}'
    cidr: 24
  - address: 192.168.202.101  #nfs
    bind_interface: '{{ ansible_eth1.device }}'
    cidr: 24
ctdb_public_addresses_file: '/etc/ctdb/public_addresses'
ctdb_public_network: 192.168.202.0/24
ctdb_samba_active_directory_info:
  domain_join_user: 'ansible'
  domain_join_password: 'domainpassword'
  idmap_range: '10000-99999'
  kdc:
    - 'dc01.{{ pri_domain_name }}'
    - 'dc02.{{ pri_domain_name }}'
  netbios_name: 'SMBCLUSTER'
  preferred_master: 'no'
  realm: '{{ pri_domain_name }}'
  winbind_enum_users: 'yes'  #if set to no then getent passwd will not output domain users
  winbind_enum_groups: 'yes'  #if set to no then getent group will not output domain groups
  winbind_cache_time: '900'
  winbind_use_default_domain: 'yes'
  workgroup: 'EXAMPLE'
ctdb_samba_config: '{{ ctdb_glusterfs_mount }}/etc/samba/smb.conf'  #defines shared smb.conf between nodes...stored on GlusterFS mounts
ctdb_samba_ctdbd_socket_file: '/var/lib/run/ctdb/ctdbd.socket'
ctdb_samba_global_options:
  clustering: 'yes'  #defines if CTDB clustering is used...(yes|no)
  dns_proxy: 'no'
  deadtime: '0'  #defines idle disconnects..(default 0)...A deadtime of zero indicates that no auto-disconnection should be performed
  idmap_range: '100000-299999'
  max_log_size: '1000'
  netbios_name: 'SMBCLUSTER'
  restrict_anonymous: '2'
  server_string: '%h server (Samba, Ubuntu)'  #MAY NEED TO SET THIS TO A VAR SO ALL NODES SHARE THE SAME NETBIOS NAME
  strict_locking: 'no'  #set to no if sharing same shares via NFS/CIFS..otherwise set to yes
  unix_password_sync: 'yes'
  usershare_allow_guests: 'no'
  wins_server: []
  wins_support: false
  workgroup: 'WORKGROUP'
ctdb_samba_restrict_access_to_public_addresses_only: false  #defines if samba should only allow connections via public address...DOES NOT WORK YET!!!
ctdb_samba_join_domain: false
ctdb_samba_master_node: 'node1'  #only used to join domain..
ctdb_samba_shares:  #only creating base shares directory...manage from Windows to define add's ACL's
  - name: 'public'
    acls:
      - etype: 'group'
        entity: ''
        perms: 'rx'
        recurse: false
        default: true
      - etype: 'group'
        entity: 'Domain Admins'
        perms: 'rwx'
        recurse: false
        default: false
      - etype: 'group'
        entity: 'Domain Admins'
        perms: 'rwx'
        recurse: false
        default: true
      - etype: 'group'
        entity: 'Domain Users'
        perms: 'rwx'
        recurse: false
        default: false
      - etype: 'group'
        entity: 'Domain Users'
        perms: 'rwx'
        recurse: false
        default: true
      - etype: 'user'
        entity: 'Domain Admins'
        perms: 'rwx'
        recurse: false
        default: false
      - etype: 'user'
        entity: 'Domain Admins'
        perms: 'rwx'
        recurse: false
        default: true
      - etype: 'user'
        entity: 'Domain Users'
        perms: 'rwx'
        recurse: false
        default: false
      - etype: 'user'
        entity: 'Domain Users'
        perms: 'rwx'
        recurse: false
        default: true
      - etype: 'user'
        entity: 'root'
        perms: 'rwx'
        recurse: false
        default: false
      - etype: 'user'
        entity: 'root'
        perms: 'rwx'
        recurse: false
        default: true
    browseable: 'yes'
    comment: 'Public Share(Open)'
    directory_perms: 'u=rwx,g=rwx,o='
    group: 'Domain Admins'
    owner: 'root'
    path: '{{ ctdb_samba_shares_root_dir }}/public'
    read_only: 'no'
    recurse_directory_perms: false
ctdb_samba_shares_root_dir: '{{ ctdb_glusterfs_client_mount }}'  #defines root directory where shares will be created
ctdb_samba_shares_root_perms:
  owner: 'root'
  group: 'root'
  directory_perms: 'u=rwx,g=rx,o=rx'
ctdb_ulimit: 10000
pri_domain_name: 'example.org'
````

Dependencies
------------

Install Ansible role requirements following the requirements section.  

Example Playbook
----------------

````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-change-hostname
  tasks:

- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-etc-hosts
    - role: ansible-config-interfaces
#    - role: ansible-network-tweaks
    - role: ansible-ntp

#- hosts: iscsi-servers
#  become: true
#  any_errors_fatal: true
#  vars:
#  roles:
#    - role: ansible-zfs
#      tags:
#        - glusterfs-resize-lvm
#  tasks:

- hosts: glusterfs-nodes
  become: true
  any_errors_fatal: true
  vars:
  roles:
    - role: ansible-open-iscsi
      tags:
        - glusterfs-resize-lvm
      when: inventory_hostname not in groups['glusterfs-arbiter-nodes']

- hosts: glusterfs-nodes
  become: true
  any_errors_fatal: true
  vars:
    - manage_glusterfs: true  #defines if role should be ran after initial setup
  roles:
    - role: ansible-glusterfs
      when: manage_glusterfs
  tasks:

- hosts: ctdb-servers
  become: true
  any_errors_fatal: true
  serial: 1  #we do this to ensure that any changes to ctdb/samba and etc do affect any existing connections.
  vars:
  roles:
    - role: ansible-ctdb
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
