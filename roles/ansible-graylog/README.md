Role Name
=========

Installs graylog role https://www.graylog.org/

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-graylog.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-graylog)

Requirements
------------

None

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Role Variables
--------------
````
---
# defaults file for ansible-graylog
enable_graylog_server: true
enable_graylog_web: true
es_cluster_name: graylog
es_data_node: true  #defines if node should be a data node in the cluster...default is true...define here or in group_vars/group
es_master_node: true  #defines if node should be a master node in the cluster...default is true...define here or in group_vars/group
es_replicas: 0 #set to the number of replicas to set for the elasticsearch cluster - this applies to graylog server settings and elasticsearch
es_shards: 4 #set to the number of shards to set for the elasticsearch cluster - this applies to graylog server settings and elasticsearch
graylog_debian_file: 'graylog-{{ graylog_version }}-repository-{{ ansible_distribution|lower }}{{ ansible_distribution_version }}_latest.deb'
graylog_package_url: https://packages.graylog2.org/repo/packages
graylog_server_master: true #default is true unless installing multiple instances
graylog_server_password_secret: X4S0oYP9DcGjgpX6uAGOfHS3NbB5OpSHWVKwQP94mJxaDCM3WPP0QP5zd8uqZs2tDBPiKET6r81IJEumQkqAk6WOnqKwvCu1  #define in group_vars/all/accounts or generate new pw using...pwgen -N 1 -s 96
graylog_server_rest_listen_uri: http://127.0.0.1:12900/
graylog_server_root_password: fd74bdd901857b89f5737e5352a2a8a2d1f000aa4bed4aee47c95afaa37d0f99 #hashed password here is "P@55w0rd"...define in group_vars/all/accounts or generate new pw using...echo -n yourpassword | shasum -a 256
graylog_server_syslog_input_port: 10514 #set to port to be defined in graylog inputs
graylog_server_syslog_input_protocol: udp #udp or tcp
graylog_version: 1.3
graylog_web_application_secret: X4S0oYP9DcGjgpX6uAGOfHS3NbB5OpSHWVKwQP94mJxaDCM3WPP0QP5zd8uqZs2tDBPiKET6r81IJEumQkqAk6WOnqKwvCu1  #define in group_vars/all/accounts or generate new pw using...pwgen -N 1 -s 96
graylog_web_server_uri: '{{ graylog_server_rest_listen_uri }}' #set to same as graylog_server_rest_listen_uri unless not installing both server and web on same host
port_redirects:  #define ports to port forward from system to graylog_server - only required for ports below 1024
  - syslog_dport: 514
    graylog_dport: 10514
    prot: udp
````

Dependencies
------------

#### Galaxy
````
mrlesmithjr.snmpd
mrlesmithjr.timezone
mrlesmithjr.elasticsearch
mrlesmithjr.mongodb
````
#### GitHub
````
ansible-snmpd
ansible-timezone
ansible-elasticsearch
ansible-mongodb
````

requirements.yml
````
---
- src: https://github.com/mrlesmithjr/ansible-snmpd
- src: https://github.com/mrlesmithjr/ansible-timezone
- src: https://github.com/mrlesmithjr/ansible-elasticsearch
- src: https://github.com/mrlesmithjr/ansible-mongodb
- src: https://github.com/mrlesmithjr/ansible-graylog
- src: mrlesmithjr.snmpd
- src: mrlesmithjr.timezone
- src: mrlesmithjr.elasticsearch
- src: mrlesmithjr.mongodb
- src: mrlesmithjr.graylog
````

To install dependencies you can execute the following.
````
sudo ansible-galaxy install -r requirements.yml -f
````

Example Playbook
----------------

#### Galaxy
-----------
    - hosts: servers
      roles:
         - mrlesmithjr.snmpd
         - mrlesmithjr.timezone
         - mrlesmithjr.elasticsearch
         - mrlesmithjr.mongodb
         - mrlesmithjr.graylog
#### GitHub
-----------
    - hosts: servers
      roles:
        - ansible-snmpd
        - ansible-timezone
        - ansible-elasticsearch
        - ansible-mongodb
        - ansible-graylog

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
