Role Name
=========

Installs and configured Elastic Packetbeat (https://www.elastic.co/products/beats/packetbeat)

Requirements
------------

None

Vagrant
-------
Spin up and test  
Spins up 3 nodes to test with following:  
packetbeat  - client  
es  - elasticsearch  
logstash  - logstash server  
````
vagrant up
````

Role Variables
--------------

````
---
# defaults file for ansible-es-packetbeat
es_packetbeat_dashboard_dir: 'beats-dashboards-{{ es_packetbeat_version }}'
es_packetbeat_dashboard_dl: 'http://download.elastic.co/beats/dashboards/{{ es_packetbeat_dashboard_package }}'
es_packetbeat_dashboard_package: 'beats-dashboards-{{ es_packetbeat_version }}.zip'
es_packetbeat_debian_dl: 'https://download.elastic.co/beats/packetbeat/{{ es_packetbeat_debian_package }}'
es_packetbeat_debian_package: 'packetbeat_{{ es_packetbeat_version }}_amd64.deb'
es_packetbeat_elasticsearch_host: 'es.{{ pri_domain_name }}:9200'
es_packetbeat_interface: 'any'  #defines interface to sniff on... (any, eth0, eth1, etc.)
es_packetbeat_outputs:
  - name: elasticsearch
    host: '{{ es_packetbeat_elasticsearch_host }}'
    workers: 1
es_packetbeat_protocols:
  - name: dns
    ports:
      - 53
    include_additionals: true  #whether or not the dns.additionals field (additional resource records) is added to messages
    include_authorities: true  #whether or not the dns.authorities field (authority resource records) is added to messages
    send_request: false
    send_response: false
  - name: http
    ports:
      - 80
      - 8080
  - name: memcache
    ports:
      - 11211
  - name: mongodb
    ports:
      - 27017
  - name: mysql
    ports:
      - 3306
  - name: redis
    ports:
      - 6379
es_packetbeat_redhat_dl: 'https://download.elastic.co/beats/packetbeat/packetbeat-{{ es_packetbeat_version }}-x86_64.rpm'
es_packetbeat_version: '1.1.1'
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
    - role: ansible-es-packetbeat
  tasks:
````
#### Galaxy
````
- hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.packetbeat
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
