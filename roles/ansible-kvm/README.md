Role Name
=========

An [Ansible] role to install KVM/Libvirt

Requirements
------------

Install required [Ansible] roles:
```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------

```
---
# defaults file for ansible-kvm

# Defines if ssh should be configured to allow root logins
# mainly for managing KVM/Libvirt remotely using virt-manager or other.
allow_root_ssh: false

# Defines if kvm/libvirt should be configured
config_kvm: false

# Defines if kvm_users should be added to libvirtd for managing KVM
config_kvm_users: false

# Defines if kvm virtual networks should be configured
# if set to true ensure that your underlying bridges have been created
# using mrlesmithjr.config-interfaces role from Ansible Galaxy.
config_kvm_virtual_networks: false

# Defines if NFS mountpoints should be mounted from nfs_mounts
config_nfs_mounts: false

# Defines if nfs mountpoints should have permissions set or not
# this defaults to root
config_nfs_permissions: false

# Defines if libvirt should be advertised over mDNS - Avahi
# default is false.
enable_kvm_mdns: false

# Defines if unencrypted tcp connections are desired
# default is false
enable_kvm_tcp: false

# Defines if remote tls connections are desired
# default is true.
enable_kvm_tls: true

enable_libvirtd_syslog: false

# I experienced an issue with bridges no longer working on Ubuntu 16.04
# for some reason. And the following settings below from the link provided
# solved this issue.
# https://wiki.libvirt.org/page/Networking#Debian.2FUbuntu_Bridging
kvm_sysctl_settings:
  - name: 'net.bridge.bridge-nf-call-ip6tables'
    value: 0
    state: "present"
  - name: 'net.bridge.bridge-nf-call-iptables'
    value: 0
    state: "present"
  - name: 'net.bridge.bridge-nf-call-arptables'
    value: 0
    state: "present"

kvm_users:
  - remote
kvm_virtual_networks:
  - name: DMZ_ORANGE_VLAN100
    mode: bridge
    bridge_name: vmbr100
    autostart: true
    # active, inactive, present and absent
    state: active
  - name: Green_Servers_VLAN101
    mode: bridge
    bridge_name: vmbr101
    autostart: true
    state: active
nfs_mounts:
  - server: 10.0.127.50
    export: /volumes/HD-Pool/kvm/NFS
    mount_options: hard,intr,nfsvers=3,tcp,bg,_netdev,auto,nolock
    mountpoint: /mnt/kvm
  - server: 10.0.127.50
    export: /volumes/HD-Pool/builds
    mount_options: hard,intr,nfsvers=3,tcp,bg,_netdev,auto,nolock
    mountpoint: /mnt/builds
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: kvm_hosts
  become: true
  vars:
  roles:
    - role: ansible-kvm
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
