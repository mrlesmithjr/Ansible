Role Name
=========

Installs ELK Stack Role (ELK-HAProxy)

Requirements
------------

Prior to using this role you will want to add your nodes to the appropriate inventory group and create the corresponding group_vars/group with variables defined. You should create 2 elk-haproxy nodes. Examples below.
#####hosts inventory
````
[elk-nodes]
elk-haproxy-1
elk-haproxy-2

[elk-haproxy-nodes]
elk-haproxy-1
elk-haproxy-2
````

Role Variables
--------------
defaults/main.yml
````
---
# defaults file for ansible-elk-haproxy
clear_logstash_config: false
config_hosts_file: false  #defines if /etc/hosts should include ELK hosts...if DNS not configured...Vagrant testing.
config_logstash: false
enable_haproxy_admin_page: true
enable_haproxy_remote_syslog: false  #defines if logs should be sent to remote syslog server
haproxy_admin_password: admin  #defines password for admin user to login to admin page
haproxy_admin_port: 9090  #defines http port to listen on for admin page
haproxy_admin_user: admin  #defines admin user to login to admin page
kibana_port: 5601
logstash_config_dir: /etc/logstash/conf.d
logstash_configs:
  - 000_inputs
#  - 001_filters
#  - 002_metrics  #comment out if metrics for logstash processing are not required..good for keeping track of throughput...removed because of incompatabilities w/ES 2.x
  - 999_outputs
logstash_file_inputs:
  - path: /var/log/haproxy.log
    type: haproxy-log
  - path: /var/log/nginx/access.log
    type: nginx-access
  - path: /var/log/nginx/error.log
    type: nginx-error
  - path: /var/log/mail.log
    type: postfix-log
  - path: /var/log/redis/redis-server.log
    type: redis-server
logstash_inputs: []
#  - prot: tcp
#    codec: json
#    port: '{{ rundeck_logstash_port }}'
#    type: rundeck
#  - prot: udp
#    buffer_size: 1452
#    codec: collectd
#    port: 25826
#    type: collectd
logstash_log_dir: /var/log/logstash
logstash_outputs:
  - output: redis
    output_host: '{{ logstash_server_fqdn }}'
#  - output: rabbitmq
#    exchange: logstash
#    exchange_type: fanout
#    host: 10.0.101.128
logstash_server_fqdn: []  #defines logstash server...should be vip fqdn for elk-haproxy-nodes...define here or globally in group_vars/elk-nodes
reset_logstash_config: false
rundeck_logstash_port: 9700
syslog_servers:
  - name: 'logstash.{{ pri_domain_name }}'
    proto: tcp
    port: 514
use_redis: true
vagrant_deployment: false  #defines if elkstack environment is setup using vagrant
````
vars/main.yml
````
syslog_servers:  #defines syslog_servers for elk-haproxy nodes...define here or globally in group_vars/elk-haproxy-nodes
  - name: '{{ logstash_server_fqdn }}'
    port: 514
    proto: tcp
````

Dependencies
------------

````
mrlesmithjr.ntp
mrlesmithjr.rsyslog
mrlesmithjr.snmpd
mrlesmithjr.timezone
mrlesmithjr.logstash
mrlesmithjr.keepalived
mrlesmithjr.haproxy
````

Example Playbook
----------------

- hosts: elk-haproxy-nodes
  roles:
     - { role: mrlesmithjr.ntp }
     - { role: mrlesmithjr.rsyslog }
     - { role: mrlesmithjr.snmpd }
     - { role: mrlesmithjr.timezone }
     - { role: mrlesmithjr.logstash }
     - { role: mrlesmithjr.keepalived }
     - { role: mrlesmithjr.haproxy }
     - { role: mrlesmithjr.elk-haproxy }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
