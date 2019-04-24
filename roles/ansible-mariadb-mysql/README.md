<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [ansible-mariadb-mysql](#ansible-mariadb-mysql)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-mariadb-mysql

An [Ansible](https://www.ansible.com) role to install/configure [MariaDB](https://mariadb.org/) mysql

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-mariadb-mysql.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-mariadb-mysql)

## Requirements

None

## Role Variables

## Dependencies

None

## Example Playbook

```yaml
- hosts: db_hosts
  become: true
  vars:
  roles:
    - role: ansible-mariadb-mysql
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
