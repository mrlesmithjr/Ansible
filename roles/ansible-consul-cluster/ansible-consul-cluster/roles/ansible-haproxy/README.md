<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-haproxy](#ansible-haproxy)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Example `haproxy.cfg` (from default vars):](#example-haproxycfg-from-default-vars)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-haproxy

An [Ansible](https://www.ansible.com) role to install/configure [HAProxy](http://www.haproxy.org/)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-haproxy.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-haproxy)

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

[Example Playbook](./playbook.yml)

## Example `haproxy.cfg` (from default vars):

```bash
# Ansible managed

global
    log /dev/log local0
    log /dev/log local1 notice
    daemon
    chroot /var/lib/haproxy
    group haproxy
    maxconn 40000
    spread-checks 3
    stats socket /var/run/haproxy.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    # Default SSL material locations
    ca-base /etc/ssl/certs
    crt-base /etc/ssl/private

    # Default ciphers to use on SSL-enabled listening sockets.
    # For more information, see ciphers(1SSL).
    ssl-default-bind-ciphers kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL
    ssl-default-bind-options no-sslv3

defaults
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http
    log global
    maxconn 40000
    mode tcp
    option dontlognull
    option redispatch
    option tcp-smart-accept
    option tcp-smart-connect
    option tcplog
    retries 3
    timeout client 50000
    timeout connect 50000
    timeout queue 5000
    timeout server 50000

userlist STATSUSERS
    group admin users admin
    user admin insecure-password admin

listen stats
    bind *:9090
    mode http
    stats enable
    stats refresh 60s
    stats uri /
    acl AuthOkay_ReadOnly http_auth(STATSUSERS)
    acl AuthOkay_Admin http_auth_group(STATSUSERS) admin
    stats http-request auth realm stats unless AuthOkay_ReadOnly

frontend web-in-80
    mode http
    bind 192.168.250.10:80
    default_backend web-servers-80

backend web-servers-80
    mode http
    balance roundrobin
    cookie HA_BACKEND_ID insert indirect nocache
    default-server maxconn 256 maxqueue 128 weight 100
    server 192.168.250.11 192.168.250.11:80 check cookie 1
    server 192.168.250.12 192.168.250.12:80 check cookie 2
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
