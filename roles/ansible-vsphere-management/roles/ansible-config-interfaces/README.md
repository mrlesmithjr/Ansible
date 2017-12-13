<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-config-interfaces](#ansible-config-interfaces)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Examples](#examples)
    - [Example (standard) `/etc/network/interfaces`:](#example-standard-etcnetworkinterfaces)
    - [Example (Open vSwitch) `/etc/network/interfaces`:](#example-open-vswitch-etcnetworkinterfaces)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-config-interfaces

An [Ansible](https://www.ansible.com) role to configure network interfaces

-   Define dhcp, static, and manual settings
-   Create VLAN, bonds, bridges, and interfaces
-   Create Open vSwitch bridges, bonds, and interfaces

## Requirements

See [Example Playbook](#example-playbook) for examples of how to define specific
network configurations.

> NOTE: If creating Open vSwitch configurations you will need to use the [ansible-openvswitch](https://github.com/mrlesmithjr/ansible-openvswitch) [Ansible](https://www.ansible.com) role

## Role Variables

```yaml
---
# defaults file for ansible-config-interfaces

# Defines if network bonds should be configured as defined
config_network_bonds: false

# Defines if network bridges should be configured as defined
config_network_bridges: false

# Defines if interfaces should be configured as defined
config_network_interfaces: false

# Defines if vlans should be configured as defined
config_network_vlans: false

# Defines if Open vSwitch bonds should be configured as defined
config_ovs_bonds: false

# Defines if Open vSwitch bridges should be configured as defined
config_ovs_bridges: false

# Defines if Open vSwitch interfaces should be configured as defined
config_ovs_interfaces: false

# Defines all dns servers to configure
dns_nameservers:
  - '8.8.8.8'
  - '8.8.4.4'

# Defines your global dns suffix search
dns_search: '{{ pri_domain_name }}'

# Defines if interfaces, bonds, bridges, vlans, ovs_bonds, ovs_bridges and
# ovs_interfaces should be brought up after defining.
enable_configured_interfaces_after_defining: false

# Defines non Open vSwitch network bonds
network_bonds: []
  # - name: 'bond0'
  #   address: '192.168.1.10'
  #   netmask: '255.255.255.0'
  #   configure: true
  #   comment: 'Bond Group 0'
  #   method: 'static'
  #   parameters:
  #     - param: 'bond_mode'
  #       val: 'active-backup'
  #     - param: 'bond_miimon'
  #       val: '100'
  #     # - param: 'miimon'
  #     #   val: '100'
  #     # - param: 'mode'
  #     #   val: 'active-backup'
  #     - param: 'primary'
  #       val: 'enp0s9'
  #   slaves:
  #     - 'enp0s9'
  #     - 'enp0s10'

# Defines non Open vSwitch network bridges
network_bridges: []
  # - name: 'br0'
  #   configure: true
  #   comment: 'Bridge 0'
  #   method: 'static'
  #   address: '192.168.1.11'
  #   netmask: '255.255.255.0'
  #   netmask_cidr: '24'
  #   # gateway: '192.168.1.1'
  #   parameters:
  #     - param: 'bridge_stp'
  #       val: 'off'
  #     - param: 'bridge_fd'
  #       val: '0'
  #     # - param: 'up route add default gw'
  #     #   val: '10.0.106.1'
  #   ports:
  #     - 'enp0s16'

# Defines non Open vSwitch network interfaces
network_interfaces: []
  # - name: 'enp0s3'
  #   configure: true
  #   method: 'dhcp'
  #   parameters:
  #     - param: 'pre-up sleep'
  #       val: '2'
  # - name: 'enp0s8'
  #   configure: true
  #   method: 'static'
  #   address: '192.168.250.10'
  #   netmask: '255.255.255.0'
  # - name: 'enp0s9'
  #   configure: true
  #   comment: 'bond0 member'
  #   method: 'manual'
  #   parameters:
  #     - param: 'bond_master'
  #       val: 'bond0'
  # - name: 'enp0s10'
  #   configure: true
  #   comment: 'bond0 member'
  #   method: 'manual'
  #   parameters:
  #     - param: 'bond_master'
  #       val: 'bond0'
  # - name: 'enp0s16'
  #   configure: true
  #   comment: 'br0 member'
  #   method: 'manual'

# Defines non Open vSwitch network vlans
network_vlans: []
  # - name: 'enp0s8.100'
  #   configure: true
  #   comment: 'VLAN 100'
  #   method: 'manual'
  #   address:
  #   netmask:
  #   netmask_cidr:
  #   gateway:
  #   vlan_device: 'enp0s8'

# Defines Open vSwitch bonds
ovs_bonds: []
  # - name: 'bond0'
  #   # address:
  #   bridge: 'vmbr0'
  #   comment: 'OVS Bond'
  #   configure: true
  #   # gateway:
  #   method: 'manual'
  #   # netmask:
  #   # netmask_cidr:
  #   options:
  #     - opt: 'bond_mode'
  #       val: 'active-backup'
  #     - opt: 'lacp'
  #       val: 'off'
  #   # parameters:
  #   #   - param: ''
  #   #     val: ''
  #   ports:
  #     - 'enp0s9'
  #     - 'enp0s10'

# Defines Open vSwitch bridges
ovs_bridges: []
  # - name: 'vmbr0'
  #   # address:
  #   comment: 'OVS Bridge'
  #   configure: true
  #   # gateway:
  #   method: 'manual'
  #   # netmask:
  #   # netmask_cidr:
  #   # options:
  #   #   - opt: ''
  #   #     val: ''
  #   # parameters:
  #   #   - param: ''
  #   #     val: ''
  #   ports:
  #     # - 'enp0s9'
  #     # - 'enp0s10'
  #     - 'bond0'
  #     - 'vlan1'

# Defines Open vSwitch interfaces
ovs_interfaces: []
  # - name: 'vlan1'
  #   address:
  #   bridge: 'vmbr0'
  #   comment: 'VLAN1'
  #   configure: true
  #   gateway:
  #   method: 'static'
  #   netmask:
  #   netmask_cidr:
  #   # options:
  #   #   - opt: 'vlan_mode'
  #   #     val: 'access'
  #   # parameters:

pri_domain_name: 'example.org'
```

## Dependencies

If interface is wireless you will need to define as such as well as provide the
SSID and key.

## Example Playbook

[Example Playbook](./playbook.yml)

## Examples

### Example (standard) `/etc/network/interfaces`:

```bash
# Ansible managed
# Any changes made here will be lost

auto lo
iface lo inet loopback

########## Network Interfaces
auto enp0s3
iface enp0s3 inet dhcp
  pre-up sleep 2

auto enp0s8
iface enp0s8 inet static
  address 192.168.250.10
  netmask 255.255.255.0

# bond0 member
auto enp0s9
iface enp0s9 inet manual
  bond_master bond0

# bond0 member
auto enp0s10
iface enp0s10 inet manual
  bond_master bond0

# br0 member
auto enp0s16
iface enp0s16 inet manual

########## End of Network Interfaces

########## Network Bonds
# Bond Group 0
auto bond0
iface bond0 inet static
  address 192.168.1.10
  netmask 255.255.255.0
  bond_slaves enp0s9 enp010
  bond_primary enp0s9
  bond_mode active-backup
  bond_miimon 100

########## End of Network Bonds


########## Network Bridges
# Bridge 0
auto br0
iface br0 inet static
  address 192.168.1.11
  netmask 255.255.255.0
  bridge_stp off
  bridge_fd 0
  bridge_ports enp0s16

########## End of Network Bridges

dns-nameservers 8.8.8.8 8.8.4.4
dns-search test.vagrant.local
```

### Example (Open vSwitch) `/etc/network/interfaces`:

```bash
# Ansible managed
# Any changes made here will be lost

auto lo
iface lo inet loopback

########## Network Interfaces
auto enp0s3
iface enp0s3 inet dhcp
  pre-up sleep 2

auto enp0s8
iface enp0s8 inet static
  address 192.168.250.10
  netmask 255.255.255.0

########## End of Network Interfaces




########## OVS Bonds
# OVS Bond
allow-vmbr0 bond0
iface bond0 inet manual
  ovs_bridge vmbr0
  ovs_type OVSBond
  ovs_bonds enp0s9 enp0s10
  ovs_options bond_mode=active-backup lacp=off

########## End of OVS Bonds

########## OVS Bridges
# OVS Bridge
auto vmbr0
allow-ovs vmbr0
iface vmbr0 inet manual
  ovs_type OVSBridge
  ovs_ports bond0 vlan1

########## End of OVS Bridges

########## OVS Interfaces
# VLAN1
allow-vmbr0 vlan1
iface vlan1 inet static
  address 192.168.250.100
  netmask 255.255.255.0
  ovs_bridge vmbr0
  ovs_type OVSIntPort

########## End of OVS Interfaces

dns-nameservers 8.8.8.8 8.8.4.4
dns-search test.vagrant.local
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
