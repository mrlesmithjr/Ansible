<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-phpipam](#ansible-phpipam)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-phpipam

An [Ansible](https://www.ansible.com) role that installs/configures [phpIPAM](http://phpipam.net/)

- Options are in place for HA DB setup if desired.

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-phpipam.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-phpipam)

## Requirements

Install required Ansible role dependencies...

```bash
sudo ansible-galaxy install -r requirements.yml
```

## Usage

Logging into phpIPAM...
http://iporhostname/phpipam/?page=login

Default phpIPAM login is

```bash
admin/ipamadmin
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

Reference [requirements](#requirements)

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-apache2
    - role: ansible-mariadb-mysql
    - role: ansible-phpipam
```

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
