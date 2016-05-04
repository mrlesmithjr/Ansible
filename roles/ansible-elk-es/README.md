Role Name
=========

Installs ELK Stack Role (ELK-ES)

Requirements
------------

Prior to using this role you will want to add your nodes to the appropriate inventory group and create the corresponding group_vars/group with variables defined. You should create 3 elk-es nodes. Examples below.
#####hosts inventory
````
[elk-nodes]
elk-es-1
elk-es-2
elk-es-3

[elk-es-nodes]
elk-es-1
elk-es-2
elk-es-3

````

Role Variables
--------------

#####group_vars/elk-nodes
````
---
es_cluster_name: vagrant
es_cluster_setup: true
es_network_publish_host: _eth1:ipv4_
es_min_master_nodes: 2
redis_allow_remote_connections: true
````
#####group_vars/elk-es-nodes
````
---
es_data_node: true
es_master_node: false
es_memory_tuning:  #these settings help eliminate OOM conditions (More memory should be used in most cases but these settings can help) #define here or in group_vars/group
  - name: indices.breaker.fielddata.limit
    set: false
    value: 60%  #default 60%
  - name: indices.breaker.request.limit
    set: false
    value: 40%  #default 40%
  - name: indices.breaker.total.limit
    set: false
    value: 40%  #default 40%
  - name: indices.fielddata.cache.size
    set: true
    value: 40%  #default undefined
````

Dependencies
------------

````
mrlesmithjr.ntp
mrlesmithjr.rsyslog
mrlesmithjr.snmpd
mrlesmithjr.timezone
mrlesmithjr.elasticsearch
````

Example Playbook
----------------

    - hosts: elk-es-nodes
      roles:
        - mrlesmithjr.elk-es
        - { role: mrlesmithjr.ntp }
        - { role: mrlesmithjr.rsyslog }
        - { role: mrlesmithjr.snmpd }
        - { role: mrlesmithjr.timezone }
        - { role: mrlesmithjr.elasticsearch }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
