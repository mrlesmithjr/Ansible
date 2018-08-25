<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [ansible-nginx-load-balancer](#ansible-nginx-load-balancer)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [Usages](#usages)
        -   [HTTP Load Balancing](#http-load-balancing)
        -   [HTTPS Load Balancing](#https-load-balancing)
            -   [SSL Termination](#ssl-termination)
                -   [Self Signed Certs](#self-signed-certs)
        -   [TCP Load Balancing](#tcp-load-balancing)
        -   [UDP Load Balancing](#udp-load-balancing)
        -   [HA (Highly Available) Setup](#ha-highly-available-setup)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-nginx-load-balancer

An [Ansible](https://www.ansible.com) role to install/configure an [NGINX](https://nginx.org) load balancer for HTTP/HTTPS/TCP/UDP

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-nginx-load-balancer.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-nginx-load-balancer)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-nginx-load-balancer

# NGINX load balancer configs
## frontend_listen_port
##
## location
##
## method
### define the load balancing method
### round_robin(default), least_conn, ip_hash
#### round_robin
##### requests to the application servers are distributed in a round-robin fashion
####
#### least_conn
##### next request is assigned to the server with the least number of active connections
####
#### ip_hash
##### a hash-function is used to determine what server should be selected for
##### the next request (based on the client’s IP address)
####
## protocol
### http, https
#### Defines backend protocol
## server_name
##
## ssl
### Defines if SSL listen port for protocol http
##
## upstream
### server
#### Define individual server(s)
###
### servers
#### Define Ansible groups to iterate through hosts
###
### backend_listen_port
#### Define the backend listen port which application is listening on
nginx_load_balancer_configs: []
  # - name: 'google_dns'
  #   frontend_listen_port: 53
  #   method: 'round_robin'
  #   protocol: 'udp'
  #   upstream:
  #     - server: 8.8.8.8
  #       backend_listen_port: 53
  #     - server: 8.8.4.4
  #       backend_listen_port: 53
  # - name: 'web_app'
  #   frontend_listen_port: 80
  #   location: '/'
  #   method: 'round_robin'
  #   protocol: 'http'
  #   server_name:
  #     - 'test.vagrant.local'
  #   ssl: false
  #   upstream:
  #     - servers: "{{ groups['web_servers'] }}"
  #       backend_listen_port: 80
  #       options:
  #         - 'fail_timeout=10s'
  #         - 'max_conns=0'
  #         - 'max_fails=1'
  #         - 'weight=1'
  #     # - server: 192.168.250.11
  #     #   backend_listen_port: 80
  #     #   options:
  #     #     - 'fail_timeout=10s'
  #     #     - 'max_conns=0'
  #     #     - 'weight=1'
  #     # - server: 192.168.250.12
  #     #   backend_listen_port: 80
  #     #   options:
  #     #     - 'backup'
  #     #     - 'fail_timeout=10s'
  #     #     - 'max_conns=0'
  #     #     - 'weight=1'

# Provides the configuration file context in which the directives that affect
# connection processing are specified.
nginx_load_balancer_events:
# Sets the maximum number of simultaneous connections that can be opened by a
# worker process.
# The Ubuntu default is 768
  - 'worker_connections 1024'

nginx_load_balancer_headers: []
  # - 'Host $host'
  # - 'X-Real-IP $remote_addr'
  # - 'X-Forwarded-For $remote_addr'
  # - 'X-Forwarded-Host $remote_addr'

# Includes another file, or files matching the specified mask, into
# configuration. Included files should consist of syntactically correct
# directives and blocks
nginx_load_balancer_includes:
  - '/etc/nginx/modules-enabled/*.conf'

# Defines a file that will store the process ID of the main process
ngninx_load_balancer_pid: '/run/nginx.pid'

# Defines if using a highly available setup. i.e. multiple nginx load balancers
nginx_load_balancer_ha: false

# Defines the prefix path/file for SSL cert(s) when using HA
## We do this in order to generate the keys on the primary and sync the keys to
## all other nodes in the HA setup.
nginx_load_balancer_ha_key_file_prefix: '/etc/ssl/{{ nginx_load_balancer_ha_primary }}'

# Defines the primary host when in HA mode
nginx_load_balancer_ha_primary: 'node0'

# Defines SSL cert(s) info
nginx_load_balancer_ssl: []
  # csr_key_file: "/etc/ssl/{{ inventory_hostname }}-csr.pem"
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

# Defines the user which NGINX runs as
nginx_load_balancer_user: 'www-data'

# Define version to install
# development/stable
nginx_load_balancer_version: 'stable'

# Defines the number of worker processes.
# The optimal value depends on many factors including (but not limited to) the
# number of CPU cores, the number of hard disk drives that store data, and
# load pattern. When one is in doubt, setting it to the number of available CPU
# cores would be a good start (the value “auto” will try to autodetect it).
#
# The default below will detect the number of cpu cores/threads and multiply by
# 4. You may want to scale this up/down or set to auto. You can also experiment
# by using the Apache benchmark tool to see where the sweet spot is.
# ab -c 40 -n 50000 http://192.168.250.200/
nginx_load_balancer_worker_processes: '{{ ansible_processor_vcpus * 4 }}'
```

## Dependencies

The following [Ansible](https://www.ansible.com) roles **should** be used along
with this `ansible-nginx-load-balancer` role.

-   [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)
    -   Provides the ability to update `/etc/hosts` with all hosts which are part of the solution
-   [ansible-keepalived](https://github.com/mrlesmithjr/ansible-keepalived)
    -   Provides the ability to provide the `VIP` for `HA` of multiple `ansible-nginx-load-balancer` nodes.

You can install the above roles using `ansible-galaxy` and the included [requirements](./requirements.yml)

```bash
ansible-galaxy install -r requirements.yml
```

## Example Playbook

[Example playbook](./playbook.yml)

## Usages

### HTTP Load Balancing

### HTTPS Load Balancing

#### SSL Termination

##### Self Signed Certs

### TCP Load Balancing

### UDP Load Balancing

### HA (Highly Available) Setup

## License

MIT

## Author Information

Larry Smith Jr.

-   [mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
