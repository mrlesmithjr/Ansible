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

```yaml
---
# defaults file for ansible-haproxy

# Defines password for admin user to login to admin page
haproxy_admin_password: 'admin'

# Defines http port to listen on for admin page
haproxy_admin_port: 9090

# Defines admin user to login to admin page
haproxy_admin_user: 'admin'

# Defines is HAProxy should be configured
haproxy_config: false

# Defines load balancer configurations to enable/disable
#
# backend_backups - Defines if all but one host should be a backup(standby) to the primary
#
# backend_backups_primary - Defines the host which should be considered the primary
# when setting backend_backups: true
#
# Example of using backups(standby)
# backend openstack_controllers-3306
#     balance source
#     default-server inter 2000 rise 2 fall 5
#     server controller01 controller01:3306 check
#     server controller02 controller02:3306 backup check
#     server controller03 controller03:3306 backup check
#
# backend_checks - Defines if host checks should be enabled
#
haproxy_configs: []
  # - name: 'squid-3128'
  #   backend_backups: false
  #   backend_backups_primary: 'node1'
  #   backend_checks: true
  #   backend_name: 'squid-servers'
  #   backend_servers_bind_port: 3128
  #   backend_servers:
  #     - 192.168.250.10
  #     - 192.168.250.11
  #   balance: 'roundrobin'
  #   default_server_options:
  #     - name: 'maxconn'
  #       value: 256
  #     - name: 'maxqueue'
  #       value: 128
  #     - name: 'weight'
  #       value: 100
  #   enabled: true
  #   frontend_bind_address: '{{ haproxy_lb_vip }}'
  #   frontend_bind_port: 8080
  #   frontend_name: 'squid-in'
  #   frontend_ssl: false
  #   frontend_ssl_cert: "{{ haproxy_load_balancer_ssl['bundled_cert'] }}"
  #   mode: 'tcp'
  #   options:
  #     - 'tcplog'
  #     # - 'httpchk'

# Defines default configurations for default block
haproxy_defaults:
  - 'errorfile 400 /etc/haproxy/errors/400.http'
  - 'errorfile 403 /etc/haproxy/errors/403.http'
  - 'errorfile 408 /etc/haproxy/errors/408.http'
  - 'errorfile 500 /etc/haproxy/errors/500.http'
  - 'errorfile 502 /etc/haproxy/errors/502.http'
  - 'errorfile 503 /etc/haproxy/errors/503.http'
  - 'errorfile 504 /etc/haproxy/errors/504.http'
  - 'log global'
  - 'maxconn 40000'
  - 'mode tcp'
  - 'option dontlognull'
  - 'option redispatch'
  - 'option tcp-smart-accept'
  - 'option tcp-smart-connect'
  - 'option tcplog'
  - 'retries 3'
  - 'timeout client 50000'
  - 'timeout connect 50000'
  - 'timeout queue 5000'
  - 'timeout server 50000'

haproxy_debian_repo: 'ppa:vbernat/haproxy-{{ haproxy_version }}'

haproxy_enable_admin_page: true

# Defines if logs should be sent to remote syslog server
haproxy_enable_remote_syslog: false

# Defines global settings for global block
haproxy_global:
  - 'chroot /var/lib/haproxy'
  - 'group haproxy'
  - 'maxconn 40000'
  - 'spread-checks 3'
  - 'stats socket {{ haproxy_socket_file }} mode 660 level admin'
  - 'stats timeout 30s'
  - 'user haproxy'

# Defines haproxy default location
haproxy_home: '/etc/haproxy'

haproxy_lb_vip: '{{ ansible_default_ipv4.address }}'

haproxy_pri_domain_name: 'example.org'

haproxy_socket_file: '/var/run/haproxy.sock'

haproxy_syslog_servers: []
  # - name: 'logstash.{{ haproxy_pri_domain_name }}'
  #   proto: 'tcp'
  #   port: 514

# Defines if using a highly available setup. i.e. multiple haproxy load balancers
haproxy_load_balancer_ha: false

# Defines the prefix path/file for SSL cert(s) when using HA
## We do this in order to generate the keys on the primary and sync the keys to
## all other nodes in the HA setup.
haproxy_load_balancer_ha_key_file_prefix: '/etc/ssl/{{ haproxy_load_balancer_ha_primary }}'

# Defines the primary host when in HA mode
haproxy_load_balancer_ha_primary: 'node0'

# Defines SSL cert(s) info
haproxy_load_balancer_ssl: []
  # bundled_cert: '/etc/ssl/{{ inventory_hostname }}-bundle.pem'
  # csr_key_file: '/etc/ssl/{{ inventory_hostname }}-csr.pem'
  # enabled: false
  # generate_keys: false
  # private_key_file: '/etc/ssl/private/{{ inventory_hostname }}-key.pem'
  # private_key_size: 4096
  # private_key_type: 'RSA'
  # protocols:
  #   - 'TLSv1'
  #   - 'TLSv1.1'
  #   - 'TLSv1.2'
  # public_key_file: '/etc/ssl/public/{{ inventory_hostname }}-cert.pem'
  # public_key_valid_days: 1825
  # regenerate_keys: false

haproxy_version: '1.7'
```

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

frontend web_servers-in-443
    mode http
    bind 192.168.250.200:443 ssl crt /etc/ssl/node1-bundle.pem
    default_backend web_servers-80

backend web_servers-80
    mode http
    balance roundrobin
    option httplog
    default-server maxconn 256 maxqueue 128 weight 100
    server node2 node2:80 check
    server node3 node3:80 check
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
