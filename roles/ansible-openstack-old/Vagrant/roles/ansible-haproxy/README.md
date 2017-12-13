Role Name
=========

Installs haproxy http://www.haproxy.org/

Requirements
------------

None...unless using GlusterFS

Role Variables
--------------

````
---
# defaults file for ansible-haproxy
config_haproxy: false #only set to true to actually configure a base HAProxy config which is already installed by default
debian_haproxy_repo: ppa:vbernat/haproxy-1.5
enable_haproxy_admin_page: true
enable_haproxy_remote_syslog: false  #defines if logs should be sent to remote syslog server
haproxy_admin_password: admin  #defines password for admin user to login to admin page
haproxy_admin_port: 9090  #defines http port to listen on for admin page
haproxy_admin_user: admin  #defines admin user to login to admin page
haproxy_backup_dir: /etc/haproxy.backup  #defines location to backup haproxy to when using with GlusterFS
haproxy_configs:  #defines load balancer configurations to enable/disable
  - name: web-http
    backend_checks: true  #Defines if backend server checks are to be performed (true|false)
    backend_name: web-servers  #Defines name of backend-name config
    backend_servers_bind_port: 80  #Defines the port that backend servers listen on
    backend_servers_group: 'web-nodes'  #Define Ansible inventory group host resides in
    balance: roundrobin  #Define load balancing method (roundrobin|static-rr|leastconn|first|source|uri|url_param)
    default_server_options:  #Define default-server options
      - name: maxconn
        value: 256
      - name: maxqueue
        value: 128
      - name: weight
        value: 100
    enabled: true  #defines if config is enabled or not (true|false)
    frontend_bind_address: '{{ haproxy_lb_vip }}'
    frontend_bind_port: 80  #Defines the port that frontend server listens on
    frontend_name: http-in  #Defines frontend name to create
    mode: http  #Defines listen mode (http|tcp)
    options:  #Defines options to add to backend group (not the same as default_server_options)
      - httplog
      - httpchk
#      - httpchk HEAD / HTTP/1.1\r\nHost:localhost  #Works for default NGINX health checks
haproxy_defaults:  #defines default configurations for default block
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
haproxy_docker_install: false  #defines if haproxy is being installed in Docker
haproxy_global:  #defines global settings for global block
  - 'chroot /var/lib/haproxy'
  - 'group haproxy'
  - 'maxconn 40000'
  - 'spread-checks 3'
  - 'stats socket {{ haproxy_socket_file }} mode 660 level admin'
  - 'stats timeout 30s'
  - 'user haproxy'
haproxy_home: /etc/haproxy  #defines haproxy default location
haproxy_lb_vip: '{{ ansible_default_ipv4.address }}'
haproxy_mnt: ''  #define if using GlusterFS
haproxy_socket_file: /var/run/haproxy.sock
pri_domain_name: example.org
primary_gfs_server: ''  #define if using GlusterFS
secondary_gfs_server: ''  #define if using GlusterFS
sync_haproxy: false  #this is only needed when using GlusterFS
syslog_servers:
  - name: 'logstash.{{ pri_domain_name }}'
    proto: tcp
    port: 514
````

Dependencies
------------

None...unless using GlusterFS

Example Playbook
----------------

#### GitHub
````
- hosts: all
  remote_user: remote
  become: true
  vars:
  roles:
    - role: ansible-haproxy
  tasks:
````
#### Galaxy
````
- hosts: all
  remote_user: remote
  become: true
  vars:
  roles:
    - role: mrlesmithjr.haproxy
  tasks:
````

Example haproxy.cfg (from default vars)
---------------------------------------
````
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
    server node2 node2:80 check
````

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
