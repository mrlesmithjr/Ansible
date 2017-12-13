<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-firewalld](#ansible-firewalld)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-firewalld

An [Ansible](https://www.ansible.com) role to manage [firewalld](http://www.firewalld.org/)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-firewalld

# Defines any custom zones to create/delete
# zone - name of zone
#
# present - whether custom zone is created/deleted
## present: true
### creates zone if not already present
## present: false
### deletes zone if present
firewalld_custom_zones: []
  # - zone: 'docker'
  #   state: 'enabled'
  #   present: false
  # - zone: 'privateDNS'
  #   state: 'enabled'
  #   present: true

# Defines firewall rules
firewalld_rules: []
  # # - service: 'dhcp'
  # #   permanent: true
  # #   zone: 'public'
  # - service: 'http'
  #   state: 'enabled'
  #   permanent: true
  #   zone: 'public'
  # - service: 'https'
  #   state: 'enabled'
  #   permanent: true
  #   zone: 'public'
  # - service: 'ssh'
  #   state: 'enabled'
  #   permanent: true
  #   zone: 'public'

# Defines firewall zones (default zones - not custom zones)
firewalld_zones: []
  # - zone: 'home'
  #   permanent: true
  #   state: 'enabled'
  #   interface: 'enp0s3'
  # - zone: 'public'
  #   permanent: true
  #   state: 'enabled'
  #   interface: 'enp0s8'
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: test-nodes
  vars:
    firewalld_custom_zones:
      - zone: 'privateDNS'
        state: 'enabled'
        present: true
    firewalld_enable_immediately: true
    firewalld_rules:
      - service: 'dhcp'
        permanent: true
        state: 'enabled'
      - service: 'dns'
        permanent: true
        state: 'enabled'
        zone: 'privateDNS'
      - service: 'http'
        state: 'enabled'
        permanent: true
        zone: 'public'
      - service: 'https'
        state: 'enabled'
        permanent: true
        zone: 'public'
      - service: 'ssh'
        state: 'enabled'
        permanent: true
    firewalld_zones:
      - zone: 'home'
        permanent: true
        state: 'enabled'
        interface: 'enp0s3'
      - zone: 'public'
        permanent: true
        state: 'enabled'
        interface: 'enp0s8'
    pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-firewalld
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
