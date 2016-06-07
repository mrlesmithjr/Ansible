Role Name
=========

Installs and configured Elastic filebeat (https://www.elastic.co/products/beats/filebeat)

Requirements
------------

None

Vagrant
-------
Spin up and test  
Spins up 3 nodes to test with following:  
filebeat  - client  
es  - elasticsearch  
logstash  - logstash server  
````
vagrant up
````

Role Variables
--------------

````
---
# defaults file for ansible-es-filebeat
es_filebeat_debian_package: 'filebeat_{{ es_filebeat_version }}_amd64.deb'
es_filebeat_dl_url: 'https://download.elastic.co/beats/filebeat'
es_filebeat_elasticsearch_host: 'es.{{ pri_domain_name }}:9200'
es_filebeat_idle_timeout: '5s'
es_filebeat_outputs:
  - name: elasticsearch
    host: '{{ es_filebeat_elasticsearch_host }}'
    workers: 1
es_filebeat_prospectors:  #define the paths (directories) to watch
  - paths:
      - '/var/log/syslog'
#      - '/var/log/*.log'  #collects all logs from /var/logs/ and not subdirectories
#      - '/var/log/*/.log'  #collects all logs from subdirectories of /var/logs/
    encoding: 'plain'  #plain (Default), utf-8, utf-16be-bom, utf-16be, utf-16le, big5, gb18030, gbk, hz-gb-2312, euc-kr, euc-jp, iso-2022-jp, shift-jis, ...
    input_type: 'log'  #log (Default) | stdin
    document_type: 'syslog'  #The event type to use for published lines read by harvesters. For Elasticsearch output, the value that you specify here is used to set the type field in the output document. The default value is log.
#  - paths:
#      - '/opt/myapp/var/*.log'
#    document_type: 'my_app_log'
es_filebeat_redhat_package: 'filebeat-{{ es_filebeat_version }}-x86_64.rpm'
es_filebeat_registry_file: '/var/lib/filebeat/registry'
es_filebeat_spool_size: 2048  #Event count spool threshold - forces network flush if exceeded
es_filebeat_version: '1.2.2'
pri_domain_name: 'example.org'
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-es-filebeat
  tasks:
````
#### Galaxy
````
- hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.filebeat
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
