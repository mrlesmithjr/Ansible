<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-samba](#ansible-samba)
  - [Requirements](#requirements)
  - [Vagrant](#vagrant)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-samba

An [Ansible](https://www.ansible.com) role to install/configure [Samba](https://www.samba.org/)

- Ability to create AD Domains, file servers

## Requirements

Install all Ansible role requirements.

```bash
sudo ansible-galaxy install -r requirements.yml -f
```

## Vagrant

Spin up Environment under Vagrant to test.

```bash
vagrant up
```

Will spin up an Ubuntu server to function as an Active Directory domain controller as well as a Server2012 server to manage from.

## Role Variables

```yaml
---
# defaults file for ansible-samba
pri_domain_name: example.org
samba_ad_info: []
  # ad_dc_hostname: "{{ ansible_hostname }}"
  # ad_dns_domain_name: "{{ pri_domain_name }}"
  # adminpass: P@55w0rd
  # allow_dns_updates: disabled
  # backend_dns: internal
  # dns_forwarder: 8.8.8.8
  # kerberos_realm: '{{ pri_domain_name }}'
  # netbios_domain_name: "{{ samba_netbios_domain_name[0]|upper }}"

# Allow users who've been granted usershare privileges
# to create public shares, not just authenticated ones
samba_allow_guests: "yes"

# Defines if you are building an Active Directory domain controller
samba_create_domain_controller: false

# Defines if users defined in samba_domain_users list should be created
samba_create_domain_users: false

# Define Ansible group which contains your Samba domain controllers
samba_domain_controllers_group: samba_domain_controllers

samba_domain_users: []
  # - name: test01
  #   password: P@55w0rd
  # - name: test02
  #   password: P@55w0rd

# Define samba groups to create
samba_groups: []
  # - nogroup
  # - securedgroup
  # - testgroup

samba_netbios_domain_name: "{{ pri_domain_name.split('.') }}"

# Define which Ansible host should be considered the primary domain controller
samba_primary_domain_controller: "{{ groups[samba_domain_controllers_group][0] }}"

# Defines samba security
samba_security: user

# Defines server role
# (standalone server or active directory domain controller)
samba_server_role: standalone server

# Defines root folder for samba shares to be created
samba_share_path: /mnt/samba/shares
samba_shares: []
  # - name: allaccess
  #   browsable: "yes"
  #   folder_perms: "0755"
  #   group: nogroup
  #   guest_ok: "yes"
  #   owner: nobody
  #   read_only: "no"
  #   writable: "yes"
  # - name: public
  #   browsable: "yes"
  #   folder_perms: "0777"
  #   group: nogroup
  #   guest_ok: "yes"
  #   owner: nobody
  #   read_only: "no"
  #   writable: "yes"
  # - name: secured
  #   browsable: "yes"
  #   folder_perms: "0770"
  #   group: securedgroup
  #   guest_ok: "no"
  #   valid_users: '@securedgroup'
  #   writable: "yes"
  # - name: test
  #   browsable: "yes"
  #   folder_perms: "0770"
  #   group: testgroup
  #   guest_ok: "no"
  #   valid_users: '@testgroup'
  #   writable: "yes"

# Define users to create
samba_users: []
  #   # Define user name to create
  # - name: vagrant
  #   # Define groups to add user to
  #   # ensure samba_groups names exist.
  #   groups:
  #     - nogroup
  #     - securedgroup
  #     - testgroup
  #   # Define samba user password
  #   smbpasswd: P@55w0rd
samba_workgroup: "{{ samba_netbios_domain_name[0]|upper }}"
```

## Dependencies

You can install dependencies as follows:

```bash
sudo ansible-galaxy install -r requirements.yml -f
```

## Example Playbook

```yaml
---
- name: provisions samba
  hosts: all
  become: true
  vars:
    - enable_dhcp_services: false
    - samba_create_domain_controller: true
    - samba_server_role: 'active directory domain controller'
  roles:
    - role: ansible-isc-dhcp
      when: >
            enable_dhcp_services is defined and
            enable_dhcp_services
    - role: ansible-ntp
    - role: ansible-samba
  tasks:
```

## License

BSD

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- mrlesmithjr [at] gmail.com
