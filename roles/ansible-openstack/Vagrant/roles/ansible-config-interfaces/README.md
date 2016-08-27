Role Name
=========

Configures network interfaces for either static, dhcp or manual. Ability to create VLAN, Bond and Bridge interfaces as well.

Requirements
------------

All Interfaces, vlans, Bridges and Bond information must be defined either in group_vars/group or host_vars/host...Ensure that you do not define IP addresses in group_vars otherwise duplicate IP addresses will be present.

Role Variables
--------------
These variables for most occasions should remain as they are. The actual variables should be defined within host_vars/host for each host requiring configurations.
````
---
---
# defaults file for ansible-config-interfaces
config_network_bonds: false  #defines if kvm_network_bonds should be configured as defined...define in host_vars/host
config_network_bridges: false  #defines if kvm_network_bridges should be configured as defined...define in host_vars/host
config_network_interfaces: false  #defines if kvm_network_interfaces should be configured as defined...define in host_vars/host
config_network_vlans: false  #defines if kvm_network_vlans should be configured as defined...define in host_vars/host
dns_nameservers: '{{ pri_dns }} {{ sec_dns }}'  #defines all dns servers to configure...define here or globally in group_vars/all
dns_search: '{{ pri_domain_name }}'  #defines your global dns suffix search...define here or globally in group_vars/all
enable_configured_interfaces_after_defining: false  #defines if interfaces, bonds, bridges and vlans should be brought up after defining.
kvm_mgmt_ip: 0.0.0.0  #defines management IP for var on network_bridges....This is for demo purposes only
kvm_mgmt_gateway: 0.0.0.0  #defines management gateway for var on network_bridges....This is for demo purposes only
kvm_nfs1_ip: 0.0.0.0  #defines IP address to define on Storage interface.....This is for demo purposes only
network_bonds:  #define network bonds and settings if desired (Define separately for each node in host_vars) - https://help.ubuntu.com/community/UbuntuBonding
  - name: bond0
    configure: true
    comment: Management Networks
    method: manual
    slaves: eth0 eth1
    primary: eth0
    addl_settings:
#      - bond_mode balance-alb
      - bond_miimon 100
  - name: bond1
    configure: true
    comment: Storage Networks
    method: manual
    slaves: eth3 eth4
    primary: eth3
    addl_settings:
#      - bond_mode balance-alb
      - bond_miimon 100
  - name: bond2
    configure: true
    comment: VM Traffic Networks
    method: manual
    slaves: eth2 eth5
    primary: eth2
    addl_settings:
      - bond_mode balance-alb
      - bond_miimon 100
network_bridges:  #define network bridges and settings if desired (Define separately for each node in host_vars) - https://help.ubuntu.com/community/NetworkConnectionBridge
  - name: br0
    configure: true
    comment: Management - VLAN106
    method: static
    address: "{{ kvm_mgmt_ip }}"
    netmask: 255.255.255.0
    netmask_cidr: 24
    gateway: "{{ kvm_mgmt_gateway }}"
    ports: bond0.106
    addl_settings:
      - "up route add default gw {{ kvm_mgmt_gateway }}"
      - bridge_stp off
      - bridge_fd 0
  - name: br1
    configure: true
    comment: NFS-1 - VLAN127
    method: static
    address: "{{ kvm_nfs1_ip }}"
    netmask: 255.255.255.0
    netmask_cidr: 24
    gateway:
    ports: bond1.127
    addl_settings:
      - bridge_stp off
      - bridge_fd 0
  - name: vmbr100
    configure: true
    comment: Orange-DMZ - Virtual Networking
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    ports: bond2.100
    addl_settings:
      - bridge_stp off
      - bridge_fd 0
  - name: vmbr101
    configure: true
    comment: Green-Servers - Virtual Networking
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    ports: bond2.101
    addl_settings:
      - bridge_stp off
      - bridge_fd 0
network_interfaces:  #define interfaces and settings. (Define separately for each node in host_vars) - Anything not defined can be added to addl_settings.
  - name: eth0
    configure: true
    comment:
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
#    wireless_network: false  #defines if the interface is a wireless interface...not working so keep false or not defined
#    wpa_ssid: wireless  #defines the wireless SSID to connect to
#    wpa_psk: wpapassword  #defines the wireless key
    addl_settings:
      - bond_master bond0
  - name: eth1
    configure: true
    comment:
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - bond_master bond0
  - name: eth2
    configure: true
    comment:
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - bond_master bond2
  - name: eth3
    configure: true
    comment:
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - bond_master bond1
  - name: eth4
    configure: true
    comment:
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - bond_master bond1
  - name: eth5
    configure: true
    comment:
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - bond_master bond2
network_vlans:  #define vlans and settings if desired. (Define separately for each node in host_vars)
  - name: bond2.100
    configure: true
    comment: Orange-DMZ
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: bond2
    addl_settings:
  - name: bond2.101
    configure: true
    comment: Green-Servers
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: bond2
    addl_settings:
  - name: bond0.106
    configure: true
    comment: Management
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: bond0
    addl_settings:
  - name: bond1.127
    configure: true
    comment: NFS-1
    method: manual
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: bond1
    addl_settings:
pri_domain_name: example.org
pri_dns:  #defines primary dns server...define here or globally in group_vars/all
sec_dns:  #defines secondary dns server...define here or globally in group_vars/all
````

Dependencies
------------

If interface is wireless you will need to define as such as well as provide the SSID and key.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.config-interfaces }

Example /etc/network/interfaces generated from the example variables
--------------------------------------------------------------------
````
# Ansible managed: /etc/ansible/roles/mrlesmithjr.config-interfaces/templates/etc/network/interfaces.j2 modified on 2015-10-16 21:21:14 by root on node-1
# Any changes made here will be lost

auto lo
iface lo inet loopback

########## Network Interfaces
auto eth0
iface eth0 inet manual
  bond_master bond0

auto eth1
iface eth1 inet manual
  bond_master bond0

auto eth2
iface eth2 inet manual
  bond_master bond2

auto eth3
iface eth3 inet manual
  bond_master bond1

auto eth4
iface eth4 inet manual
  bond_master bond1

auto eth5
iface eth5 inet manual
  bond_master bond2

########## End of Network Interfaces

########## Network Bonds
# Management
auto bond0
iface bond0 inet manual
  bond_slaves eth0 eth1
  bond_primary eth0
  bond_miimon 100

# Storage
auto bond1
iface bond1 inet manual
  bond_slaves eth3 eth4
  bond_primary eth3
  bond_mode balance-alb
  bond_miimon 100

# VMs
auto bond2
iface bond2 inet manual
  bond_slaves eth2 eth5
  bond_primary eth2
  bond_mode balance-alb
  bond_miimon 100

########## End of Network Bonds

########## Network VLANS
# Orange-DMZ
auto vlan100
iface vlan100 inet manual
  vlan_raw_device bond2

# Green-Servers
auto vlan101
iface vlan101 inet manual
  vlan_raw_device bond2

# Management
auto vlan106
iface vlan106 inet static
  address 10.0.106.51
  netmask 255.255.255.0
  gateway 10.0.106.51
  up route add default gw 10.0.106.1
  vlan_raw_device bond0

# NFS-1
auto vlan127
iface vlan127 inet static
  address 10.0.127.151
  netmask 255.255.255.0
  vlan_raw_device bond1

########## End of Network VLANS

########## Network Bridges
# Orange-DMZ - Virtual Networking
auto vmbr100
iface vmbr100 inet manual
  bridge_stp off
  bridge_fd 0
  bridge_ports vlan100

# Green-Servers - Virtual Networking
auto vmbr101
iface vmbr101 inet manual
  bridge_stp off
  bridge_fd 0
  bridge_ports vlan101

########## End of Network Bridges

dns-nameservers 192.168.70.240 192.168.70.241
dns-search example.org
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
