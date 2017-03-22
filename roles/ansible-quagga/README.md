Role Name
=========

An [Ansible] role to install [Quagga]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-quagga
quagga_bgp_router_configs: [] # Define BGP configurations for all router nodes
  # - name: 'node0'
  #   local_as: '64512'
  #   neighbors:
  #     - neighbor: '192.168.1.11'
  #       announce_default_route: false
  #       description: 'node1'
  #       remote_as: '64512'
  #       prefix_lists: # Define specific BGP neighbore prefix lists
  #         - name: 'FILTER01-out' # Define name of filter
  #           direction: 'out' # define direction (in|out)
  #           orf: 'send' # Define outbound route filter (send|receive|both)
  #     - neighbor: '192.168.2.12'
  #       announce_default_route: false
  #       description: 'node2'
  #       prefix_lists:
  #         - name: 'FILTER02-in'
  #           direction: 'in'
  #           orf: 'receive'
  #       remote_as: '64513'
  #     - neighbor: '192.168.3.13'
  #       description: 'node3'
  #       remote_as: '64514'
  #   network_advertisements:  #networks to advertise
  #     - '10.0.0.10/32'
  #     - '192.168.1.0/24'
  #     - '192.168.2.0/24'
  #     - '192.168.3.0/24'
  #   router_id: '10.0.0.10'
  #   prefix_lists:
  #     - name: 'FILTER01-out'
  #       action: 'permit'
  #       network: '10.0.0.10/32'
  #       sequence: '10'
  #     - name: 'FILTER01-out'
  #       action: 'permit'
  #       network: '192.168.1.0/24'
  #       sequence: '20'
  #     - name: 'FILTER01-out'
  #       action: 'permit'
  #       network: '192.168.2.0/24'
  #       sequence: '30'
  #     - name: 'FILTER01-out'
  #       action: 'deny'
  #       network: 'any'
  #       sequence: '40'
  # - name: 'node1'
  #   local_as: '64512'
  #   neighbors:
  #     - neighbor: '192.168.1.10' # Peering with loopback address for iBGP
  #       announce_default_route: false
  #       description: 'node0'
  #       remote_as: '64512'
  #       prefix_lists:
  #         - name: 'FILTER01-in'
  #           direction: 'in'
  #           orf: 'receive'
  #   network_advertisements:  #networks to advertise
  #     - '10.1.1.11/32'
  #     - '192.168.1.0/24'
  #   router_id: '10.1.1.11'
  # - name: 'node2'
  #   local_as: '64513'
  #   neighbors:
  #     - neighbor: '192.168.2.10'
  #       announce_default_route: false
  #       description: 'node0'
  #       prefix_lists:
  #         - name: 'FILTER02-out'
  #           direction: 'out'
  #           orf: 'send'
  #       remote_as: '64512'
  #   network_advertisements:  #networks to advertise
  #     # - '10.2.2.12/32'
  #     - '192.168.2.0/24'
  #   prefix_lists:
  #     - name: 'FILTER02-out'
  #       action: 'permit'
  #       network: '192.168.2.0/24'
  #       sequence: '10'
  #     - name: 'FILTER01-out'
  #       action: 'deny'
  #       network: 'any'
  #       sequence: '20'
  #   router_id: '10.2.2.12'
  # - name: 'node3'
  #   local_as: '64514'
  #   neighbors:
  #     - neighbor: '192.168.3.10'
  #       announce_default_route: false
  #       description: 'node0'
  #       remote_as: '64512'
  #   network_advertisements:  #networks to advertise
  #     - '10.3.3.13/32'
  #     - '192.168.3.0/24'
  #   router_id: '10.3.3.13'
quagga_bgp_routerid: '{{ ansible_default_ipv4.address }}'
quagga_config: false
#defines if quagga bgpd should be configured based on quagga_bgp_router_configs
#makes it easy to disable auto routing in order to define your routes manually
quagga_config_bgpd: false
quagga_config_interfaces: false
#defines if quagga ospfd should be configured based on quagga_ospf_ vars...
#makes it easy to disable auto routing in order to define your routes manually
quagga_config_ospfd: false
quagga_configs:
  - name: 'daemons'
    group: 'root'
    mode: 'u=rw,g=r,o=r'
    owner: 'root'
  - name: 'debian.conf'
    group: 'quagga'
    mode: 'u=rw,g=r,o=r'
    owner: 'quagga'
  - name: 'vtysh.conf'
    group: 'quagga'
    mode: 'u=rw,g=r,o=r'
    owner: 'quagga'
  - name: 'Quagga.conf'
    group: 'quaggavty'
    owner: 'root'
    mode: 'u=rw,g=r,o='
quagga_debugging:
  bgp:
    enabled: false
    debug:
      # - 'as4'
      # - 'as4 segment'
      - 'events'
      # - 'filters'
      # - 'fsm'
      - 'keepalives'
      - 'updates'
      # - 'updates in'
      # - 'updates out'
      # - 'zebra'
  ospf:
    enabled: false
    debug:
      - 'event'
      # - 'ism'
      # - 'ism events'
      # - 'ism status'
      # - 'ism timers'
      # - 'lsa'
      # - 'lsa flooding'
      # - 'lsa generate'
      # - 'lsa install'
      # - 'lsa refresh'
      # - 'nsm'
      # - 'nsm events'
      # - 'nsm status'
      # - 'nsm timers'
      # - 'nssa'
      # - 'packet all'
      # - 'packet all detail'
      # - 'packet all recv'
      # - 'packet all send'
      # - 'packet dd'
      # - 'packet dd detail'
      # - 'packet dd recv'
      # - 'packet dd send'
      # - 'packet hello'
      # - 'packet hello detail'
      # - 'packet hello recv'
      # - 'packet hello send'
      # - 'packet ls-ack'
      # - 'packet ls-ack detail'
      # - 'packet ls-ack recv'
      # - 'packet ls-ack send'
      # - 'packet ls-request'
      # - 'packet ls-request detail'
      # - 'packet ls-request recv'
      # - 'packet ls-request send'
      # - 'packet ls-update'
      # - 'packet ls-update detail'
      # - 'packet ls-update recv'
      # - 'packet ls-update send'
  zebra:
    enabled: true
    debug:
      - 'events'
      # - 'fpm'
      - 'kernel'
      # - 'packet'
      # - 'packet recv'
      # - 'packet send'
      # - 'rib'
      # - 'rib queue'

# Defines if quagga_interfaces are defined within Quagga configuration or
# /etc/network/interfaces.d/
quagga_defined_interfaces: false

quagga_enable_bgpd: false
quagga_enable_ospfd: false
quagga_enable_password: 'quagga' #define here or in group_vars/group
quagga_hostname: '{{ ansible_hostname }}'

# Define interfaces to configure if desired
quagga_interfaces: []
# - int: 'enp0s9'
#   configure: true
#   method: 'static'
#   address: '192.168.1.10'
#   # gateway: '10.1.1.1'
#   cidr: '24'
#   netmask: '255.255.255.0'
# #   addl_settings:
# #     - 'bond_master bond0'
# - int: 'enp0s10'
#   configure: true
#   method: 'static'
#   address: '192.168.2.10'
#   # gateway: '10.1.1.1'
#   cidr: '24'
#   netmask: '255.255.255.0'
# #   addl_settings:
# #     - 'bond_master bond0'

#define network bonds and settings if desired
#https://help.ubuntu.com/community/UbuntuBonding
quagga_interfaces_bonds: []
  # - int: 'bond0'
  #   address: '192.168.1.10'
  #   cidr: '24'
  #   comment: 'Network Bond'
  #   configure: true
  #   # gateway: '192.168.1.1'
  #   method: 'static'
  #   netmask: '255.255.255.0'
  #   slaves:
  #     - 'enp0s9'
  #     - 'enp0s10'
  #   primary: 'enp0s9'
  #   addl_settings:
  #     - 'bond_mode balance-alb'
  #     - 'bond_miimon 100'

# Define addresses to assign on loopback interface...Can be multiple as well
# We are defining these as sub-interfaces on the loopback adapter lo
quagga_interfaces_lo: []
  # - int: "lo{{ ':' }}0"
  #   address: '10.0.0.10/32'
  #   method: 'static'
  #   configure: true
  # # - int: "lo{{ ':' }}1"
  # #   address: '10.0.0.11/32'
  # #   method: 'static'
  # #   configure: false
  # # - int: "lo{{ ':' }}2"
  # #   address: '10.0.0.12/32'
  # #   method: 'static'
  # #   configure: false

# Defines if host faces the internet and is used as the default route to other
# hosts to get to the internet. By setting this to true, an iptables masquerade
# rule will be created.
quagga_internet_gateway: false
quagga_internet_gateway_info:
  ext_int: '{{ ansible_default_ipv4.interface }}' # Define interface which faces the internet
quagga_ip_forwarding:
  ipv4: true
  ipv6: true
quagga_logging:
  facility:
    enabled: false
    facility: 'daemon' # auth|cron|daemon|kern|local0|local1|local2|local3|local4|local5|local6|local7|lpr|mail|news|syslog|user|uucp
  file:
    enabled: true
    filename: '/var/log/quagga/zebra.log'
    level: 'debugging' # alerts|critical|debugging|emergencies|errors|informational|notifications|warnings
  monitor:
    enabled: false
    level: 'debugging' # alerts|critical|debugging|emergencies|errors|informational|notifications|warnings
  record_priority: false
  stdout:
    enabled: false
    level: 'debugging' # alerts|critical|debugging|emergencies|errors|informational|notifications|warnings
  syslog:
    enabled: false
    level: 'debugging' # alerts|critical|debugging|emergencies|errors|informational|notifications|warnings
  timestamp:
    enabled: false
    precision: 0 # 0-6
  trap:
    enabled: false
    level: 'debugging' # alerts|critical|debugging|emergencies|errors|informational|notifications|warnings
quagga_no_passive_int: [] # Define any interfaces to not advertise routes on
  # - 'eth0'
  # - 'eth1'
quagga_ospf_area: '51'  #defines the desired area mapping for OSPF routing with upstream OSPF routers
quagga_ospf_area_config: []
  # - network: '192.168.1.0/24'
  #   area: '{{ quagga_ospf_area }}'
  # - network: '192.168.2.0/24'
  #   area: '{{ quagga_ospf_area }}'
  # - network: '192.168.3.0/24'
  #   area: '{{ quagga_ospf_area }}'
quagga_ospf_redistribute:
  - 'connected'
#  - 'kernel'
#  - 'static'
#  - 'isis'
#  - 'rip'
quagga_ospf_routerid: '{{ ansible_default_ipv4.address }}'  #defines the router id IP address for OSPF
quagga_passive_int: []
quagga_password: 'quagga' #define in group_vars/all/accounts
quagga_root_dir: '/etc/quagga'
quagga_static_routes: [] # Define any static routes
  # - destination: '192.168.60.0/24'
  #   next_hop: '192.168.20.16' # Define IP or outbound interface 'enp0s9'
quagga_sysctl_network_settings:
  - name: 'net.ipv4.ip_forward'
    value: '1'
  - name: 'net.ipv4.conf.all.forwarding'
    value: '1'
  - name: 'net.ipv4.conf.default.forwarding'
    value: '1'
  - name: 'net.ipv4.tcp_tw_reuse'
    value: '1'
  - name: 'net.ipv4.ip_local_port_range'
    value: '1024 65023'
  - name: 'net.ipv4.tcp_max_syn_backlog'
    value: '40000'
  - name: 'net.ipv4.tcp_max_tw_buckets'
    value: '400000'
  - name: 'net.ipv4.tcp_max_orphans'
    value: '60000'
  - name: 'net.ipv4.tcp_syncookies'
    value: '1'
  - name: 'net.ipv4.tcp_synack_retries'
    value: '3'
  - name: 'net.core.somaxconn'
    value: '40000'
  - name: 'net.ipv4.tcp_fin_timeout'
    value: '5'
quagga_user: 'quagga'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-quagga
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

[Ansible]: <https://ansible.com>
[Quagga]: <http://www.nongnu.org/quagga/>
