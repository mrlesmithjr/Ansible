<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-nginx-load-balancer](#ansible-nginx-load-balancer)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Usages](#usages)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-nginx-load-balancer

An [Ansible](https://www.ansible.com) role to install/configure an [NGINX](https://nginx.org) load balancer for HTTP/HTTPS/TCP/UDP

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-nginx-load-balancer.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-nginx-load-balancer)

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

The following [Ansible](https://www.ansible.com) roles **should** be used along
with this `ansible-nginx-load-balancer` role.

- [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)
  - Provides the ability to update `/etc/hosts` with all hosts which are part of the solution
- [ansible-keepalived](https://github.com/mrlesmithjr/ansible-keepalived)
  - Provides the ability to provide the `VIP` for `HA` of multiple `ansible-nginx-load-balancer` nodes.

You can install the above roles using `ansible-galaxy` and the included [requirements](./requirements.yml)

```bash
ansible-galaxy install -r requirements.yml
```

## Example Playbook

[Example playbook](./playbook.yml)

## Usages

- HTTP Load Balancing

- HTTPS Load Balancing

  - SSL Termination

  - Self Signed Certs

- TCP Load Balancing

- UDP Load Balancing

- HA (Highly Available) Setup

## License

MIT

## Author Information

Larry Smith Jr.

- [mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
