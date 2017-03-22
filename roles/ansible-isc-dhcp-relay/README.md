Role Name
=========

An [Ansible] role to install ISC-DHCP-Relay

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-isc-dhcp-relay
# Define if ISC-DHCP-Relay should be configured
isc_dhcp_relay_config: true

# Define specific interfaces to listen on
isc_dhcp_relay_interfaces:
  - '{{ ansible_default_ipv4.interface }}'
  # - 'eth0'
  # - 'eth1'
  # - 'enp0s3'
  # - 'enp0s8'

# Define additional start up options
isc_dhcp_relay_options: []
  # - ''

# Define servers to relay DHCP requests to
isc_dhcp_relay_servers:
  - '10.10.10.1'
  - '192.168.1.1'
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
    - role: ansible-isc-dhcp-relay
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- [@mrlesmithjr]
- [EverythingShouldBeVirtual]
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://www.twitter.com/mrlesmithjr>
[EverythingShouldBeVirtual]: <http://www.everythingshouldbevirtual.com>

[Ansible]: <https://www.ansible.com>
