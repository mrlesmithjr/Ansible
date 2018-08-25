# ansible-isc-dhcp

An [Ansible](https://www.ansible.com) role to install/configure [ISC-DHCP](https://www.isc.org/downloads/dhcp/) server(s)

-   Configurable options
-   Failover and load balancing ready

## Requirements

### Scopes

Define your DHCP Scopes

```yaml
isc_dhcp_scopes:
  - subnet: 192.168.250.0
    default_lease_time: "{{ isc_dhcp_default_lease_time }}"
    max_lease_time: "{{ isc_dhcp_max_lease_time }}"
    netmask: 255.255.255.0
    # Define scope specific options to configure
    options:
      - name: routers
        value: 192.168.250.1
      - name: subnet-mask
        value: 255.255.255.0
      - name: broadcast-address
        value: 192.168.250.255
      - name: domain-name-servers
        value: "{{ isc_dhcp_name_servers|join (', ') }}"
    range_start: 192.168.250.128
    range_end: 192.168.250.224
```

### Failover scopes

For failover define the following vars to fit your deployment...

```yaml
isc_dhcp_failover_info:
  # ansible_default_ipv4.address|ansible_enp0s8.ipv4.address
  # Defines failover address for dhcp failover setup
  failover_address: "{{ ansible_default_ipv4.address }}"
  # Define Ansible inventory group that nodes belong to
  failover_group: dhcp-nodes
  # Define the node in which should be considered the primary
  primary: "{{ groups['dhcp-nodes'][0] }}"
  # Define the port to be used on primary node
  primary_port: "519"
  # Define the node in which should be considered the secondary
  secondary: "{{ groups['dhcp-nodes'][1] }}"
  # Define the port to be used on secondary node
  secondary_port: "520"
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: dhcp-nodes
  vars:
    isc_dhcp_scopes:
      - subnet: 192.168.250.0
        default_lease_time: "{{ isc_dhcp_default_lease_time }}"
        max_lease_time: "{{ isc_dhcp_max_lease_time }}"
        netmask: 255.255.255.0
        # Define scope specific options to configure
        options:
          - name: routers
            value: 192.168.250.1
          - name: subnet-mask
            value: 255.255.255.0
          - name: broadcast-address
            value: 192.168.250.255
          - name: domain-name-servers
            value: "{{ isc_dhcp_name_servers|join (', ') }}"
        range_start: 192.168.250.128
        range_end: 192.168.250.224
  roles:
    - role: ansible-isc-dhcp
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
