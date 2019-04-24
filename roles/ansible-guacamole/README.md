<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-guacamole](#ansible-guacamole)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
    - [If using MySQL for authentication](#if-using-mysql-for-authentication)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-guacamole

An [Ansible](https://www.ansible.com) role to install/configure [Guacamole](https://guacamole.incubator.apache.org/)

> NOTE: Apache Guacamole is a clientless remote desktop gateway. It supports
> standard protocols like VNC, RDP, and SSH.

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-guacamole.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-guacamole)

## Requirements

### If using MySQL for authentication

> NOTE: A working MySQL DB must be available as this role does not install MySQL.
> The DB, DB user, and DB populated with this role.

The following Ansible role [ansible-mysql](https://github.com/mrlesmithjr/ansible-mysql)
is what I test with.

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

## Example Playbook

[playbook.yml](playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
