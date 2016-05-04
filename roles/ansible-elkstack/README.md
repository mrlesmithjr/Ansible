Role Name
=========

Downloads all roles required to build a complete ELK-Stack.

Requirements
------------
To install all required roles execute the following:
````
ansible-galaxy install -r requirements.yml
````
You may need to force the install or ignore errors if the existing role(s) is installed. To ensure you have the latest versions of roles.
To ensure that you do not overwrite any existing roles installed in /etc/ansible/roles I would create comment out the roles_path in the included
ansible.cfg file to store roles in the directory of this role.

ansible.cfg
````
[defaults]
ansible_managed=Ansible managed, do not edit directly: {file} by {uid} on {host}
ask_vault_pass = False
#gathering = smart
#fact_caching = redis
#fact_caching_timeout = 86400
forks=10
host_key_checking=False
#roles_path = ./roles
````

Install
-------


Role Variables
--------------

Below are some examples to get you started.

group_vars/all/network
````
---
pri_domain_name: vagrant.local
````
group_vars/all/servers
````
---
logstash_server_fqdn: 10.0.15.100
````
group_vars/all/snmp
````
---
snmpd_authorized_networks:  #define read-only snmpd settings
  - network: 10.0.15.0/24
    community: vagrant
````
group_vars/all/syslog
````
---
configure_rsyslog: true
syslog_servers:
  - name: '{{ logstash_server_fqdn }}'
    proto: tcp
    port: 514
````
group_vars/elk-broker-nodes
````
---
es_data_node: false
es_master_node: true
````
group_vars/elk-es-nodes
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
group_vars/elk-haproxy-nodes
````
---
config_haproxy: true
config_keepalived: true
keepalived_router_id: 50
keepalived_vip: 10.0.15.100
keepalived_vip_int: eth1
````
group_vars/elk-nodes
````
---
config_hosts_file: true
es_cluster_name: vagrant
es_cluster_setup: true
es_network_publish_host: _eth1:ipv4_
es_min_master_nodes: 2
redis_allow_remote_connections: true
vagrant_deployment: true
````
group_vars/elk-processor-nodes
````
---
es_data_node: false
es_master_node: false
````

Dependencies
------------

All dependencies are installed from above using requirements.yml.

Example Playbook
----------------

inventory hosts file
````
[elk-nodes]
elk-broker-[1:3]
elk-es-[1:2]
elk-haproxy-[1:2]
elk-pre-processor-[1:2]
elk-processor-[1:2]

[elk-broker-nodes]
elk-broker-[1:3]

[elk-es-nodes]
elk-es-[1:2]

[elk-haproxy-nodes]
elk-haproxy-[1:2]

[elk-pre-processor-nodes]
elk-pre-processor-[1:2]

[elk-processor-nodes]
elk-processor-[1:2]
````
elkstack-core.yml
````
---
# Playbook to provion core ELKStack components...Only required on initial provisioning and/or role updates
- name: Configure Common Roles on ELK-Nodes
  hosts: elk-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-network-tweaks
    - role: ansible-ntp
    - role: ansible-postfix
    - role: ansible-rsyslog
    - role: ansible-snmpd
    - role: ansible-timezone

- name: Configure ELK-Broker-Nodes
  hosts: elk-broker-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-redis
      when: use_redis is defined and use_redis
    - role: ansible-rabbitmq
      when: use_rabbitmq is defined and use_rabbitmq
    - role: ansible-elasticsearch

- name: Configure ELK-ES-Nodes
  hosts: elk-es-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elasticsearch

- name: Configure ELK-Processor-Nodes
  hosts: elk-processor-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elasticsearch
    - role: ansible-logstash
    - role: ansible-dnsmasq

- name: Configure ELK-Pre-Processor-Nodes
  hosts: elk-pre-processor-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-logstash
    - role: ansible-dnsmasq

- name: Configure ELK-Haproxy-Nodes
  hosts: elk-haproxy-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-logstash
    - role: ansible-keepalived
    - role: ansible-haproxy
````
elkstack.yml
````
---
# Playbook to install ELKStack specific roles to configure environment...Run elkstack-core.yml to initially provision environment and/or update core roles.
- name: Configure ELK-Broker-Nodes
  hosts: elk-broker-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elk-kibana
    - role: ansible-elk-broker

- name: Configure ELK-ES-Nodes
  hosts: elk-es-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elk-es

- name: Configure ELK-Processor-Nodes
  hosts: elk-processor-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elk-processor

- name: Configure ELK-Pre-Processor-Nodes
  hosts: elk-pre-processor-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elk-pre-processor

- name: Configure ELK-Haproxy-Nodes
  hosts: elk-haproxy-nodes
  remote_user: remote
  sudo: true
  roles:
    - role: ansible-elk-haproxy
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
