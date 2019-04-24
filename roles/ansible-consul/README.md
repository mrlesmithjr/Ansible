<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [ansible-consul](#ansible-consul)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Vagrant](#vagrant)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Example DNS query for Redis Service](#example-dns-query-for-redis-service)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-consul

An [Ansible](https://www.ansible.com) role to install, configure and build a
[Consul](https://www.consul.io/) cluster.

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-consul.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-consul)

## Requirements

Define your Ansible host group name of consul servers within `consul_servers_group`.

Attaching the role to a group of servers NOT being in the group of
`consul_servers_group` will treat them as consul clients joining the servers
inside `consul_servers_group`.

## Vagrant

You can spin up a 5-node Consul environment for testing by doing the following:

Spin up environment

```bash
vagrant up
```

This should bring up an environment with a 3-node Consul cluster and 2 nodes
running redis and nginx for service discovery and testing.

You can view the consul web-ui by using your browser to open

- [node3](http://192.168.250.13:8500)
- [node4](http://192.168.250.14:8500)

When you are done testing in a Vagrant environment you can tear it down by doing
the following:

```bash
./cleanup.sh
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  vars:
    - consul_servers_group: 'consulservers'
    - pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-ntp
    - role: ansible-rsyslog
    - role: ansible-timezone
    - role: ansible-users
    - role: ansible-consul
  tasks:
```

You can also checkout the included playbook.yml Ansible playbook.

## Example DNS query for Redis Service

```bash
vagrant@node4:/etc/consul.d$ dig @127.0.0.1 -p 8600 redis.service.dc1.consul. ANY

; <<>> DiG 9.9.5-3ubuntu0.7-Ubuntu <<>> @127.0.0.1 -p 8600 redis.service.dc1.consul. ANY
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51158
;; flags: qr aa rd; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:

;redis.service.dc1.consul.      IN      ANY

;; ANSWER SECTION:
redis.service.dc1.consul. 0     IN      A       192.168.202.203
redis.service.dc1.consul. 0     IN      A       192.168.202.204

;; Query time: 5 msec
;; SERVER: 127.0.0.1#8600(127.0.0.1)
;; WHEN: Fri Mar 04 20:31:06 EST 2016
;; MSG SIZE  rcvd: 122

vagrant@node4:/etc/consul.d$
```

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
