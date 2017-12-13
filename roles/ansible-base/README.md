<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-base](#ansible-base)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-base

An [Ansible](https://www.ansible.com) role to define a base configuration state.

-   Configure/update dhcp client,update dns servers

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-base

base_arch_packages:
  - 'base-devel'
  - 'curl'
  - 'git'
  - 'git-core'
  - 'ntp'
  - 'sg3_utils'

base_debian_packages:
  - 'build-essential'
  - 'software-properties-common'
  - 'curl'
  - 'git'
  - 'git-core'
  - 'ntp'
  - 'scsitools'

# Define DNS servers to update to if update_dns_nameservers = true
base_dns_nameservers:
  - '8.8.8.8'
  - '8.8.4.4'

# Defines if /etc/network/interfaces dns-nameservers is present or not
# Only used when update_dns_nameservers=true
base_dns_nameservers_state: 'present'

# Defines dns-search for /etc/network/interfaces
base_dns_search: 'example.org'

# Defines if /etc/network/interfaces dns-search is present or not
# Only used if base_update_dns_search=true
base_dns_search_state: 'present'

# Defines if apt-get udpate should be forced
base_force_apt_update: false

base_redhat_packages:
  - 'curl'
  - 'git'
  - 'nano'
  - 'net-tools'
  - 'ntp'
  - 'sg3_utils'

# Defines if dhcp client config should be updated
base_update_dhcpclient_conf: false

# Defines if dns servers should be updated
base_update_dns_nameservers: false

# Defines if dns search domain should be updated
base_update_dns_search: false
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: all
  become: true
  vars:
  roles:
    role: ansible-bootstrap
    role: ansible-base
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
