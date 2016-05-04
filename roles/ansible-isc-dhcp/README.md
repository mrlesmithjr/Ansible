Role Name
=========

Installs isc-dhcp server(s) https://www.isc.org/downloads/dhcp/ (Configurable options...failover and load balancing ready)

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-isc-dhcp.svg)](https://travis-ci.org/mrlesmithjr/ansible-isc-dhcp)

Requirements
------------

If setting up dhcp failover...define the following variables in host_vars/host...one host primary and the other as secondary
````
failover_role: primary|secondary
failover_peer_address:   #define ip address of opposite dhcp server
````

Role Variables
--------------

````
---
# defaults file for ansible-isc-dhcp
authoritative: false  #defines if DHCP server should be authoritative for subnet...define here or in group_vars/group
ddns_update_style: 'none'   #defines ddns update style...options are none, interim...define here or in group_vars/group
ddns_updates: false  #defines if ddns updates should be enabled between dhcp and dns...define here or in group_vars/group
default_lease_time: 86400
dhcp_dns_fwd_zones: [] #isc-dhcp
#  - dhcp_dns_fwd_zone: '{{ dhcp_domain_name }}'
#    dhcp_dns_primary: '{{ dhcp_dns_primary }}'
dhcp_dns_rev_zones: [] #isc-dhcp
#  - dhcp_dns_rev_zone: 0.0.10
#    dhcp_dns_primary: '{{ dhcp_dns_primary }}'
#  - dhcp_dns_rev_zone: 101.0.10
#    dhcp_dns_primary: '{{ dhcp_dns_primary }}'
#  - dhcp_dns_rev_zone: 125.0.10
#    dhcp_dns_primary: '{{ dhcp_dns_primary }}'
dhcp_domain_name: '{{ pri_domain_name }}'  #defines domain name to assign to dhcp clients...define here or in group_vars/group
dhcp_name_servers: '{{ pri_dns }}, {{ sec_dns }}'  #defines dns servers to assign to dhcp clients...define here or in group_vars/group
dhcp_scopes: [] #defines dhcp scopes to create...define here or in group_vars/group
#  - dhcp_range: '10.0.0.128 10.0.0.224'
#    dhcp_subnet: 10.0.0.0
#    dhcp_netmask: 255.255.255.0
#    dhcp_routers: 10.0.0.1
#    dhcp_subnet_mask: 255.255.255.0
#    dhcp_broadcast_address: 10.0.0.255
#    dhcp_domain_name_servers: '{{ dhcp_name_servers }}'
#    dhcp_default_lease_time: '{{ default_lease_time }}'
#    dhcp_max_lease_time: '{{ max_lease_time }}'
#  - dhcp_range: '10.0.101.128 10.0.101.224'
#    dhcp_subnet: 10.0.101.0
#    dhcp_netmask: 255.255.255.0
#    dhcp_routers: 10.0.101.1
#    dhcp_subnet_mask: 255.255.255.0
#    dhcp_broadcast_address: 10.0.101.255
#    dhcp_domain_name_servers: '{{ dhcp_name_servers }}'
#    dhcp_default_lease_time: '{{ default_lease_time }}'
#    dhcp_max_lease_time: '{{ max_lease_time }}'
enable_dhcp: true  #defines if dhcp should be enabled or not...define here or in group_vars/group
enable_dhcp_failover: false  #defines if dhcp load balancing and failover should be configured between dhcp servers...define here or in group_vars/group
enable_pxe_boot: false  #defines if TFTP/PXE boot options should be enabled...define here or in group_vars/group
failover_address: '{{ ansible_default_ipv4.address }}'  #defines failover address for dhcp failover setup
max_lease_time: 86400  #defines max lease time for clients
#ntp_servers:  #defines internal ntp servers for clients to poll...define here or globally in group_vars/all
#  - 'ntp1.{{ pri_domain_name }}'
#  - 'ntp2.{{ pri_domain_name }}'
pri_domain_name: example.org  #defines primary domain name for environment...define here or in group_vars/all
pri_dns: []  #define primary dns server for environment...define here or in group_vars/all
pxe_boot_file: pxelinux.0  #defines boot file used for pxe boot
pxe_boot_server: []  #defines tftp server to PXE/TFTP from......define here or in group_vars/group
sec_dns: []  #define secondary dns server for environment...define here or in group_vars/all
````

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrlesmithjr.isc-dhcp }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
