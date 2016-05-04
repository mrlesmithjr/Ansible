Role Name
=========

Installs and configured Elastic topbeat (https://www.elastic.co/products/beats/topbeat)

Requirements
------------

None

Vagrant
-------
Spin up and test  
Spins up 3 nodes to test with following:  
topbeat  - client  
es  - elasticsearch  
logstash  - logstash server  
````
vagrant up
````

Role Variables
--------------

````
---
# defaults file for ansible-es-topbeat
es_topbeat_dashboard_dir: 'beats-dashboards-{{ es_topbeat_version }}'
es_topbeat_dashboard_dl: 'http://download.elastic.co/beats/dashboards/{{ es_topbeat_dashboard_package }}'
es_topbeat_dashboard_package: 'beats-dashboards-{{ es_topbeat_version }}.zip'
es_topbeat_debian_dl: 'https://download.elastic.co/beats/topbeat/{{ es_topbeat_debian_package }}'
es_topbeat_debian_package: 'topbeat_{{ es_topbeat_version }}_amd64.deb'
es_topbeat_elasticsearch_host: 'es.{{ pri_domain_name }}:9200'
es_topbeat_redhat_dl: 'https://download.elastic.co/beats/topbeat/topbeat-{{ es_topbeat_version }}-x86_64.rpm'
es_topbeat_version: '1.1.1'
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
    - role: ansible-es-topbeat
  tasks:
````
#### Galaxy
````
- hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.topbeat
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
