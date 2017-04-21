Role Name
=========

An [Ansible] role to configure network interfaces
- Static, DHCP or Manual.
- Ability to create VLAN, Bond and Bridge interfaces as well.

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-config-interfaces

config_interfaces_debian_packages:
  - 'bridge-utils'
  - 'lldpd'
  - 'vlan'

# Defines if network bonds should be configured as defined
config_network_bonds: false

# Defines if network bridges should be configured as defined
config_network_bridges: false

# Defines if interfaces should be configured as defined
config_network_interfaces: false

# Defines if vlans should be configured as defined
config_network_vlans: false

# Defines all dns servers to configure
dns_nameservers:
  - '8.8.8.8'
  - '8.8.4.4'

# Defines your global dns suffix search
dns_search: '{{ pri_domain_name }}'

# Defines if interfaces, bonds, bridges and vlans should be brought up after defining.
enable_configured_interfaces_after_defining: false

# Define network bonds and settings if desired
# (Define separately for each node in host_vars)
# https://help.ubuntu.com/community/UbuntuBonding
network_bonds:
  - name: 'bond0'
    configure: true
    comment: 'Management Networks'
    method: 'manual'
    slaves:
      - 'eth0'
      - 'eth1'
    primary: 'eth0'
    addl_settings:
#      - 'bond_mode balance-alb'
      - 'bond_miimon 100'
  - name: 'bond1'
    configure: true
    comment: 'Storage Networks'
    method: 'manual'
    slaves:
      - 'eth3'
      - 'eth4'
    primary: 'eth3'
    addl_settings:
#      - 'bond_mode balance-alb'
      - 'bond_miimon 100'
  - name: 'bond2'
    configure: true
    comment: 'VM Traffic Networks'
    method: 'manual'
    slaves:
      - 'eth2'
      - 'eth5'
    primary: 'eth2'
    addl_settings:
      - 'bond_mode balance-alb'
      - 'bond_miimon 100'

# Define network bridges and settings if desired
# (Define separately for each node in host_vars)
# https://help.ubuntu.com/community/NetworkConnectionBridge
network_bridges:
  - name: 'br0'
    configure: true
    comment: 'Management - VLAN106'
    method: 'static'
    address: '10.0.106.50'
    netmask: '255.255.255.0'
    netmask_cidr: '24'
    gateway: '10.0.106.1'
    ports: 'bond0.106'
    addl_settings:
      - 'up route add default gw 10.0.106.1'
      - 'bridge_stp off'
      - 'bridge_fd 0'
  - name: 'br1'
    configure: true
    comment: 'NFS-1 - VLAN127'
    method: 'static'
    address: '10.0.127.50'
    netmask: '255.255.255.0'
    netmask_cidr: '24'
    gateway:
    ports: 'bond1.127'
    addl_settings:
      - 'bridge_stp off'
      - 'bridge_fd 0'
  - name: 'vmbr100'
    configure: true
    comment: 'Orange-DMZ - Virtual Networking'
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    ports: 'bond2.100'
    addl_settings:
      - 'bridge_stp off'
      - 'bridge_fd 0'
  - name: 'vmbr101'
    configure: true
    comment: 'Green-Servers - Virtual Networking'
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    ports: 'bond2.101'
    addl_settings:
      - 'bridge_stp off'
      - 'bridge_fd 0'

# Define interfaces and settings.
# (Define separately for each node in host_vars)
# Anything not defined can be added to addl_settings.
network_interfaces:
  - name: 'eth0'
    configure: true
    comment:
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    # Defines if the interface is a wireless interface
    # not working so keep false or not defined
#    wireless_network: false
#    wpa_ssid: wireless  #defines the wireless SSID to connect to
#    wpa_psk: wpapassword  #defines the wireless key
    addl_settings:
      - 'bond_master bond0'
  - name: 'eth1'
    configure: true
    comment:
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - 'bond_master bond0'
  - name: 'eth2'
    configure: true
    comment:
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - 'bond_master bond2'
  - name: 'eth3'
    configure: true
    comment:
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - 'bond_master bond1'
  - name: 'eth4'
    configure: true
    comment:
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - 'bond_master bond1'
  - name: 'eth5'
    configure: true
    comment:
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    addl_settings:
      - 'bond_master bond2'

# Define vlans and settings if desired.
# (Define separately for each node in host_vars)
network_vlans:
  - name: 'bond2.100'
    configure: true
    comment: 'Orange-DMZ'
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: 'bond2'
    addl_settings:
  - name: 'bond2.101'
    configure: true
    comment: 'Green-Servers'
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: 'bond2'
    addl_settings:
  - name: 'bond0.106'
    configure: true
    comment: 'Management'
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: 'bond0'
    addl_settings:
  - name: 'bond1.127'
    configure: true
    comment: 'NFS-1'
    method: 'manual'
    address:
    netmask:
    netmask_cidr:
    gateway:
    vlan_device: 'bond1'
    addl_settings:
pri_domain_name: 'example.org'
```

Dependencies
------------

If interface is wireless you will need to define as such as well as provide the
SSID and key.

Example Playbook
----------------

```
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-config-interfaces
  tasks:
```

Example `/etc/network/interfaces`:
----------------------------------

```
# Ansible managed
# Any changes made here will be lost

auto lo
iface lo inet loopback

########## Network Interfaces
auto enp4s0
iface enp4s0 inet manual
  bond_master bond0

auto enp6s0
iface enp6s0 inet manual
  bond_master bond0

########## End of Network Interfaces

########## Network Bonds
# Primary Network Bond
auto bond0
iface bond0 inet manual
  bond_slaves enp4s0 enp6s0
  bond_primary enp4s0
  bond_mode 4
  bond_miimon 100

########## End of Network Bonds

########## Network VLANS
# LAB-101
auto bond0.101
iface bond0.101 inet manual
  vlan_raw_device bond0

# MAAS-102
auto bond0.102
iface bond0.102 inet manual
  vlan_raw_device bond0

# DMZ-201
auto bond0.201
iface bond0.201 inet manual
  vlan_raw_device bond0

########## End of Network VLANS

########## Network Bridges
# LAB-101
auto vmbr101
iface vmbr101 inet static
  address 10.0.101.51
  netmask 255.255.255.0
  gateway 10.0.101.1
  bridge_stp off
  bridge_fd 0
  bridge_ports bond0.101

# MAAS-Deployments
auto vmbr102
iface vmbr102 inet manual
  bridge_stp off
  bridge_fd 0
  bridge_ports bond0.102

# DMZ-201
auto vmbr201
iface vmbr201 inet manual
  bridge_stp off
  bridge_fd 0
  bridge_ports bond0.201

########## End of Network Bridges

dns-nameservers 10.10.10.1 172.16.24.1
dns-search etsbv.internal
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

[Ansible]: <https://www.ansible.com>
