Role Name
=========

An [Ansible] role to install/configure [HAProxy]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-haproxy.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-haproxy)

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-haproxy

# Defines password for admin user to login to admin page
haproxy_admin_password: 'admin'

# Defines http port to listen on for admin page
haproxy_admin_port: '9090'

# Defines admin user to login to admin page
haproxy_admin_user: 'admin'

# Defines is HAProxy should be configured
haproxy_config: false

# Defines load balancer configurations to enable/disable
haproxy_configs:
  - name: 'web-http'
    # Defines if backend server checks are to be performed (true|false)
    backend_checks: true
    # Defines name of backend-name config
    backend_name: 'web-servers'
    # Defines the port that backend servers listen on
    backend_servers_bind_port: '80'
    # Define Ansible inventory group host resides in
    backend_servers_group: 'web_nodes'
    # Define load balancing method
    # (roundrobin|static-rr|leastconn|first|source|uri|url_param)
    balance: 'roundrobin'
    # Define default-server options
    default_server_options:
      - name: 'maxconn'
        value: '256'
      - name: 'maxqueue'
        value: '128'
      - name: 'weight'
        value: '100'
    # Defines if config is enabled or not (true|false)
    enabled: true
    frontend_bind_address: '{{ haproxy_lb_vip }}'
    # Defines the port that frontend server listens on
    frontend_bind_port: '80'
    # Defines frontend name to create
    frontend_name: 'http-in'
    # Defines listen mode (http|tcp)
    mode: 'http'
    # Defines options to add to backend group
    # (not the same as default_server_options)
    options:
      - 'httplog'
      - 'httpchk'
#      - httpchk HEAD / HTTP/1.1\r\nHost:localhost  #Works for default NGINX health checks

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
haproxy_syslog_servers:
  - name: 'logstash.{{ haproxy_pri_domain_name }}'
    proto: 'tcp'
    port: '514'
haproxy_version: '1.7'
```

Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-haproxy
  tasks:
```

Example `haproxy.cfg` (from default vars):
---------------------------------------
```
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

frontend http-in-80
    mode http
    bind 10.0.2.15:80
    default_backend web-servers-80

backend web-servers-80
    mode http
    balance roundrobin
    option httplog
    option httpchk
    default-server maxconn 256 maxqueue 128 weight 100
    server node1 node1:80 check
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[HAProxy]: <http://www.haproxy.org/>
