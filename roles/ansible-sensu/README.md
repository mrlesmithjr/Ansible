Role Name
=========

Installs and configures Sensu monitoring.  https://sensuapp.org/

Requirements
------------

Install all requirements using Ansible Galaxy.  
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------

Spin up environment using Vagrant.  
````
vagrant up
````

Role Variables
--------------

```yaml
---
# defaults file for ansible-sensu
email_notifications: 'notifications@{{ pri_domain_name }}'
logstash_server_fqdn: 'logstash.{{ pri_domain_name }}'
notification_email_to: '{{ email_notifications }}'      #set to email address to send alerts to
notification_email_from: 'sensu@{{ smtp_domain_name }}'
pri_domain_name: 'example.org'
sensu_api_auth: false  #enable user/pass auth for api access...default is false...no user/pass required
sensu_api_pass: sensu
sensu_api_user: sensu
sensu_check_plugins:
  - check-cpu.rb
  - check-disk.rb
  - check-es-cluster-status.rb
  - check-es-file-descriptors.rb
  - check-es-heap.rb
  - check-haproxy.rb
  - check-procs.rb
  - check-redis-ping.rb
  - es-cluster-metrics.rb
sensu_client: true  #defines if host is a sensu client/server
sensu_client_debian_packages:
  - erlang-nox
  - build-essential
  - make
  - sensu
  - ruby2.0
  - ruby2.0-dev
sensu_client_services:
  - sensu-client
sensu_config_dir: '{{ sensu_root_dir }}/conf.d'
sensu_config_handlers_def:  #sensu definitions - added to /etc/sensu/conf.d
  - handler_default
  - handler_email
  - handler_logstash
  - handler_mailer
  - logstash
  - mailer
sensu_config_handlers_mod:  #sensu ruby handlers - added to /etc/sensu/handlers
  - logstash
  - mailer
sensu_debian_repo: 'deb http://repos.sensuapp.org/apt sensu main'
sensu_debian_repo_key: 'http://repos.sensuapp.org/apt/pubkey.gpg'
sensu_default_handler: default  #leave set to default...this is a built-in plugin that does nothing
sensu_default_handlers:
  - logstash
#  - mailer
sensu_enable_cpu_monitors: true
sensu_enable_disk_monitors: true
sensu_enable_es_monitors: false
sensu_enable_handlers: true  #to use handlers for events - configure sensu_config_handlers_def, sensu_config_handlers_mod, sensu_default_handler and sensu_default_handlers as appropriate
sensu_enable_haproxy_monitors: false
sensu_enable_process_monitors: true
sensu_enable_redis_monitors: false
sensu_handlers_dir: '{{ sensu_root_dir }}/handlers'
sensu_host: 'sensu.{{ pri_domain_name }}'
sensu_host_port: 3000
sensu_monitor_cpu:  #set enabled to either (y)es or (n)o below
  - name: cpu
    interval: 300
    sub: ALL
    enabled: true
  - name: cpu_iowait
    interval: 300
    sub: ALL
    enabled: true
sensu_monitor_es: #set enabled to either (y)es or (n)o below
  - name: cluster-status
    interval: 60
    sub: elasticsearch
    enabled: true
  - name: file-descriptors
    interval: 60
    sub: elasticsearch
    enabled: true
  - name: heap
    interval: 60
    sub: elasticsearch
    enabled: false
sensu_monitor_processes:  #set enabled to either (y)es or (n)o below
  - name: apache
    interval: 60
    sub: apache
    enabled: true
  - name: cron
    interval: 60
    sub: ALL
    enabled: true
  - name: dhcpd
    interval: 60
    sub: dhcpd
    enabled: true
  - name: dnsmasq
    interval: 60
    sub: dnsmasq
    enabled: true
  - name: elasticsearch
    interval: 60
    sub: elasticsearch
    enabled: true
  - name: exim4
    interval: 60
    sub: exim4
    enabled: true
  - name: graylog
    interval: 60
    sub: graylog
    enabled: true
  - name: haproxy
    interval: 60
    sub: haproxy
    enabled: true
  - name: keepalived
    interval: 60
    sub: keepalived
    enabled: true
  - name: logstash
    interval: 60
    sub: logstash
    enabled: true
  - name: mongo
    interval: 60
    sub: mongodb
    enabled: true
  - name: mysql
    interval: 60
    sub: mysql
    enabled: true
  - name: nginx
    interval: 60
    sub: nginx
    enabled: true
  - name: pdns_server
    interval: 60
    sub: powerdns
    enabled: true
  - name: pdns_recursor
    interval: 60
    sub: powerdns
    enabled: true
  - name: rabbitmq
    interval: 60
    sub: rabbit
    enabled: true
  - name: redis
    interval: 60
    sub: redis
    enabled: true
  - name: rsyslogd
    interval: 60
    sub: ALL
    enabled: true
  - name: sensu-api
    interval: 60
    sub: sensu
    enabled: true
  - name: sensu-client
    interval: 60
    sub: ALL
    enabled: true
  - name: sensu-server
    interval: 60
    sub: sensu
    enabled: true
  - name: snmpd
    interval: 60
    sub: ALL
    enabled: false
  - name: squid
    interval: 60
    sub: squid
    enabled: true
  - name: sshd
    interval: 60
    sub: ALL
    enabled: true
  - name: uchiwa
    interval: 60
    sub: sensu
    enabled: true
  - name: zabbix_agentd
    interval: 60
    sub: ALL
    enabled: false
sensu_monitor_redis:
  - name: ping
    interval: 60
    sub: redis
sensu_multiple_handlers: true  #defines the use of using multiple handlers if enable_handlers is true and more than one default_handler is required
sensu_plugins:
  - json
  - mail
  - redis
  - rest-client
  - sensu-plugin
sensu_plugins_dir: '{{ sensu_root_dir }}/plugins'
sensu_rabbitmq_info:
  user: 'sensu'
  password: 'sensu'
  vhost: '/sensu'
sensu_root_dir: '/etc/sensu'
sensu_server: false  #defines if host to be considered the sensu server
sensu_server_debian_packages:
  - build-essential
  - erlang-nox
  - mailutils
  - make
  - ruby2.0
  - ruby2.0-dev
  - sensu
  - uchiwa
sensu_server_services:
  - sensu-server
  - sensu-client
  - sensu-api
  - uchiwa
smtp_domain_name: '{{ pri_domain_name }}'
smtp_server: 'smtp.{{ pri_domain_name }}'
smtp_server_port: 25
```

Dependencies
------------

https://github.com/mrlesmithjr/ansible-rabbitmq.git  
https://github.com/mrlesmithjr/ansible-redis.git  
https://github.com/mrlesmithjr/ansible-sensu.git  

Example Playbook
----------------

#### GitHub
```yaml
---
- hosts: all
  become: true
  vars:
    - pri_domain_name: 'vagrant.local'
    - sensu_host: 127.0.0.1
    - sensu_server: true
  roles:
    - role: ansible-rabbitmq
    - role: ansible-redis
    - role: ansible-sensu
  tasks:
```


#### Galaxy

```yaml
---
- hosts: all
  become: true
  vars:
    - pri_domain_name: 'vagrant.local'
    - sensu_host: 127.0.0.1
    - sensu_server: true
  roles:
    - role: mrlesmithjr.rabbitmq
    - role: mrlesmithjr.redis
    - role: mrlesmithjr.sensu
  tasks:
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
