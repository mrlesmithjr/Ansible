<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-rabbitmq](#ansible-rabbitmq)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Vagrant](#vagrant)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-rabbitmq

An [Ansible](https://www.ansible.com) role to install/configure [RabbitMQ](https://www.rabbitmq.com/)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-rabbitmq.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-rabbitmq)

## Requirements

Ensure hostnames are resolvable prior to clustering...either update /etc/hosts
or ensure DNS is working.

## Vagrant

Spin up a 3 node HA Cluster for testing...
Install Ansible role on your host:

```bash
sudo ansible-galaxy install -r requirements.yml -f
```

Now spin up your environment...

```bash
vagrant up
```

When you are done testing, tear it all down...

```bash
./cleanup.sh
```

## Role Variables

[Role Defaults](./defaults/main.yml)

## Dependencies

None

## Example Playbook

[Example Playbook](./playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
