Role Name
=========

An Ansible role that Installs/configures logstash https://www.elastic.co/products/logstash

Requirements
------------

Default config if config_logstash=true is to open tcp/udp 10514 because ports < 1024 require root access.  
Configure clients to send to udp/tcp 10514.  
You can configure rsyslog to listen on tcp/udp 514 and redirect rsyslog to send to localhost on tcp/udp 10514
to accomodate clients which cannot send to a different port. See example below.  
###### /etc/rsyslog.d/50-default.conf
tcp
````
*.* @@localhost:10514
````
udp
````
*.* @localhost:10514
````

Vagrant
-------
Spin up a Vagrant test environment  
````
vagrant up
````
When done testing you can tear-down  
````
./cleanup.sh
````

Docker
------
Latest version

````
docker run -d mrlesmithjr/logstash -f /etc/logstash/conf.d
````
Specific version  
````
docker run -d mrlesmithjr/logstash:2.2 -f /etc/logstash/conf.d
````  

Role Variables
--------------

````
---
# defaults file for ansible-logstash
clear_logstash_config: false  #defines if logstash_config_dir should be cleared out
config_logstash: false  #defines if logstash should be configured
logstash_config_dir: '/etc/logstash/conf.d'
logstash_base_configs:
  - '000_inputs'
#  - '001_filters'
#  - '002_metrics'  #comment out if metrics for logstash processing are not required..good for keeping track of throughput...removed because of incompatabilities w/ES 2.x
  - '999_outputs'
logstash_base_file_inputs:
  - path: '/var/log/nginx/access.log'
    type: 'nginx-access'
  - path: '/var/log/nginx/error.log'
    type: 'nginx-error'
  - path: '/var/log/mail.log'
    type: 'postfix-log'
  - path: '/var/log/redis/redis-server.log'
    type: 'redis-server'
logstash_base_inputs:  #define inputs below to configure
  - prot: 'tcp'
    port: '10514'  #gets around port < 1024 (Note...Configure clients to send to 10514 instead of default 514)
    type: 'syslog'
  - prot: 'udp'
    port: '10514'  #gets around port < 1024 (Note...Configure clients to send to 10514 instead of default 514)
    type: 'syslog'
#  - type: 'beats'
#    port: '5044'
#  - type: redis
#    batch_count: '1000'
#    host: '{{ logstash_server_fqdn }}'
#    threads: '2'
#  - type: 'syslog'
#    port: '514'  #reminder....ports < 1024 require root access..
logstash_deb_repo: 'deb {{ logstash_repo_url }}/{{ logstash_version }}/debian stable main'
logstash_folder: '/opt/logstash'
logstash_base_outputs:
  - output: 'redis'
    output_host: '{{ logstash_server_fqdn }}'
logstash_log_dir: '/var/log/logstash'
logstash_plugins:
  - 'logstash-codec-nmap'
  - 'logstash-filter-elasticsearch'
  - 'logstash-filter-json_encode'
  - 'logstash-filter-translate'
#  - 'logstash-filter-zeromq'
  - 'logstash-input-beats'
#  - 'logstash-output-jira'
  - 'logstash-output-slack'
logstash_repo_key: 'https://packages.elastic.co/GPG-KEY-elasticsearch'
logstash_repo_url: 'http://packages.elastic.co/logstash'
logstash_server_fqdn: 'logstash.{{ pri_domain_name }}'  #defines logstash server to send to...fqdn or localhost
logstash_version: '2.2'
#logstash_version: '2.1'
#logstash_version: '1.5'
pri_domain_name: 'example.org'
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
---
- hosts: all
  sudo: true
  vars:
    - config_logstash: true
  roles:
    - role: ansible-logstash
  tasks:
````
#### Galaxy
````
---
- hosts: all
  sudo: true
  vars:
    - config_logstash: true
  roles:
    - role: mrlesmithjr.logstash
  tasks:
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
