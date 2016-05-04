Role Name
=========

Ansible role to install KVM...Installs and configures KVM/Libvirt...

Requirements
------------

Install and configure the additional roles below.
mrlesmithjr.openvswitch

##### Install every role required by running the following.

````
ansible-galaxy install mrlesmithjr.config-interfaces
ansible-galaxy install mrlesmithjr.openvswitch
ansible-galaxy install mrlemsithjr.kvm
````

You may also install the required roles by running the following.
````
ansible-galaxy install mrlesmithjr.kvm
ansible-galaxy install -r /etc/ansible/roles/mrlesmithjr.kvm/requirements.yml
````

Role Variables
--------------

Define variables for each of the additional ansible roles installed as requirements.
mrlesmithjr.config-interfaces
mrlesmithjr.openvswitch

mrlesmithjr.kvm vars to define.
````
---
# defaults file for ansible-kvm
allow_root_ssh: false  #defines if ssh should be configured to allow root logins...mainly for managing KVM/Libvirt remotely using virt-manager or other.
config_kvm: false  #defines if kvm/libvirt should be configured
config_kvm_users: false  #defines if kvm_users should be added to libvirtd for managing KVM
config_kvm_virtual_networks: false  #defines if kvm virtual networks should be configured...if set to true ensure that your underlying bridges have been created...using mrlesmithjr.config-interfaces role from Ansible Galaxy.
config_nfs_mounts: false  #defines if NFS mountpoints should be mounted from nfs_mounts
config_nfs_permissions: false  #defines if nfs mountpoints should have permissions set or not...this defaults to root
enable_libvirtd_syslog: false
config_nfs_permissions: false  #defines if nfs mount permissions should be set
enable_kvm_mdns: false  #defines if libvirt should be advertised over mDNS - Avahi...default is false.
enable_kvm_tcp: false  #defines if unencrypted tcp connections are desired...default is false
enable_kvm_tls: true  #defines if remote tls connections are desired...default is true.
kvm_users:
  - remote
kvm_virtual_networks:
  - name: DMZ_ORANGE_VLAN100
    mode: bridge
    bridge_name: vmbr100
    autostart: true
    state: active  #options are active, inactive, present and absent
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
````

mrlesmithjr.openvswitch vars to define. Only if openvswitch is desired.
````
---
# defaults file for ansible-openvswitch
add_repos: false  #defines if apt repos should be added for obtaining newer code...only for testing.
apt_repos:
  - ppa:project-calico/kilo  #openstack kilo repo
  - ppa:tomeichhorn/ovs  #openvswitch repo
interfaces:  #define interfaces here to be configured that are not part of ovs_bridges
  - name: eth0
    address:
    configure: true
    gateway:
    method: dhcp
    netmask:
    netmask_cidr:
    network:
    wireless_network: false
    wpa_ssid:
    wpa_psk:
  - name: wlan0
    address:
    configure: false
    gateway:
    method: dhcp
    netmask:
    netmask_cidr:
    network:
    wireless_network: true
    wpa_ssid: wirelessssid
    wpa_psk: wirelesskey
ovs_bridges:
  - name: ext-br  #defines the name of the ovs bridge to create
    add_interfaces: true
    interfaces:
      - em1
    state: present  #defines if the bridge should exist or not
    config_etc_interfaces: true  #defines if /etc/network/interfaces should be updated to include the configuration..config between reboots
    comment: external network  #defines the comment if desired to add to /etc/network/interfaces
    method: dhcp  #defines the method on how the interface should be configured...static,dhcp or manual
    address:  #define IP address if method=static
    netmask:  #define network subnet mask if method=static
    gateway:  #define the gateway if required when method=static
    wireless_network: false  #defines if the interface is a wireless interface...not working so keep false or not defined
    wpa_ssid: wireless  #defines the wireless SSID to connect to
    wpa_psk: wpapassword  #defines the wireless key
  - name: int-br
    add_interfaces: false
    interfaces:
      - None  #define as None and set add_interfaces to false if the desire is to not have nay interfaces added.
    state: present
    config_etc_interfaces: true
    comment: internal network
    method: static
    address: 192.168.203.69
    netmask: 255.255.255.0
#    gateway: 172.16.24.1
uninstall: false  #defines is OVS should be uninstalled and OVS Bridges destroyed
````

Dependencies
------------

Additionally to this role you SHOULD use the following additional roles from Ansible Galaxy
mrlesmithjr.openvswitch

requirements.yml includes all of the additional roles to install

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.config-interfaces }
         - { role: mrlesmithjr.openvswitch }
         - { role: mrlesmithjr.kvm }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
