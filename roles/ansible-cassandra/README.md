Role Name
=========

An [Ansible] role to install [Cassandra]

Requirements
------------

- Oracle Java 8

Install [Ansible] requirements `ansible-galaxy install -r requirements.yml`

Role Variables
--------------

```
---
# defaults file for ansible-cassandra
cassandra_cluster_group: 'cassandra-cluster-nodes'
cassandra_cluster_name: 'Test Cluster'
cassandra_cluster_setup: false
cassandra_commitlog_directory: '/var/lib/cassandra/commitlog'
cassandra_config: false
cassandra_debian_repo_info:
  repo: 'deb http://www.apache.org/dist/cassandra/debian 36x main'
  repo_key: 'https://www.apache.org/dist/cassandra/KEYS'
cassandra_data_file_directories:
  - '/var/lib/cassandra/data'
cassandra_hints_directory: '/var/lib/cassandra/hints'
cassandra_listen_address: "{{ hostvars[inventory_hostname]['ansible_' + cassandra_listen_interface]['ipv4']['address'] }}"
cassandra_listen_interface: 'eth1'
cassandra_log_dir: '/var/log/cassandra'
cassandra_root_dir: '/etc/cassandra'
cassandra_saved_caches_directory: '/var/lib/cassandra/saved_caches'
cassandra_seeds: '127.0.0.1' # Only used if not setting up a cluster
cassandra_version: '3.6'
```

Dependencies
------------

Reference requirements

Example Playbook
----------------

```
---
- hosts: cassandra-cluster-nodes
  become: true
  vars:
    cassandra_cluster_setup: true
    cassandra_config: true
    pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-oracle-java8
    - role: ansible-cassandra
  tasks:
```

License
-------

BSD

Author Information
------------------


Larry Smith Jr.
- [@mrlesmithjr]
- [EveryThingShouldBeVirtual]
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://twitter.com/mrlesmithjr>
[EveryThingShouldBeVirtual]: <http://everythingshouldbevirtual.com>
[Ansible]: <https://www.ansible.com>
[Cassandra]: <http://cassandra.apache.org/>
