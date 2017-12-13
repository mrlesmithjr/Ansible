<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-elasticsearch](#ansible-elasticsearch)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Vagrant](#vagrant)
    - [Spinning up](#spinning-up)
    - [Tearing down](#tearing-down)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-elasticsearch

An [Ansible](https://www.ansible.com) role to install/configure [Elasticsearch](https://www.elastic.co/products/elasticsearch)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-elasticsearch.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-elasticsearch)

## Requirements

None

## Role Variables

[default vars](./defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-elasticsearch
  tasks:
```

## Vagrant

Included is a [Vagrant](https://www.vagrantup.com) testing environment.

### Spinning up

You can easily spin up this environment by doing the following:

```bash
cd Vagrant
vagrant up
```

### Tearing down

You can easily tear down this environment by doing the following:

```bash
./cleanup.sh
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
