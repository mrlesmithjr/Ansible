# ansible-base

An [Ansible](https://www.ansible.com) role to define a base configuration state.

- Configure/update dhcp client,update dns servers

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-base.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-base)

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

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

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr.com](http://mrlesmithjr.com)
- mrlesmithjr [at] gmail.com
