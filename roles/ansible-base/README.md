Role Name
=========

An [Ansible] role to define a base configuration state.
Should be ran after mrlesmithjr.bootstrap role.
- Configure/update dhcp client,update dns servers

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-base

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

Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: all
  become: true
  vars:
  roles:
    role: ansible-bootstrap
    role: ansible-base
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

[Ansible]: <https://www.ansible.com>
