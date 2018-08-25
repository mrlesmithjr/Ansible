<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-bootstrap](#ansible-bootstrap)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-bootstrap

An [Ansible](https://www.ansible.com) bootstrap role

-   useful for adding initial post deployment tasks
-   creating initial users
-   setting initial user passwords

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-bootstrap.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-bootstrap)

## Requirements

None

## Role Variables

```yaml
---
# Only set to true if desired to set root password...for Debian/Ubuntu systems

bootstrap_debian_set_root_pw: false

# Define root password for hosts
# If Ubuntu/Debian choose wisely if you want to do this
# Generate password (echo password | mkpasswd -s -m sha-512)
# The password below is 'P@55w0rd'
bootstrap_root_password: '$6$8tMUxKP33/$Fb/hZBaYvyzGubO9nrlRJMjUnt3aajXZwxCifH9NYqrhjMlC9COWmNNFiMpnyNGsgmDeNCCn2wKNh0G1E1BBV0'

# Defines if root password should be set
# This only applies to non Debian/Ubuntu systems
bootstrap_set_root_pw: false
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-bootstrap
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
