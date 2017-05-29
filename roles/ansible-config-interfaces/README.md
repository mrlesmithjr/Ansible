Role Name
=========

An [Ansible] role to configure network interfaces
- Static, DHCP or Manual.
- Ability to create VLAN, Bond and Bridge interfaces as well.

Requirements
------------

See [Example Playbook](#example-playbook) for examples of how to define specific
network configurations.

Role Variables
--------------

[Role Defaults](defaults/main.yml)

Dependencies
------------

If interface is wireless you will need to define as such as well as provide the
SSID and key.

Example Playbook
----------------

[Example Playbook](./playbook.yml)

Example `/etc/network/interfaces`:
----------------------------------

```
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
