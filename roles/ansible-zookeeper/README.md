Role Name
=========

Installs and configures zookeeper (https://zookeeper.apache.org/)

Requirements
------------

Install Ansible role requirements:  
````
sudo ansible-galaxy install -r requirements.yml -f
````

Role Variables
--------------

````
---
# defaults file for ansible-zookeeper
cloudera_hadoop_version: cdh5
pri_domain_name: 'example.org'  #defines primary domain name for your site.
zookeeper_cluster_group: 'zookeeper-nodes'  #define Ansible inventory group which hosts are members of
zookeeper_cluster_master_group: 'zookeeper-master-nodes'  #define Ansible inventory group which Master hosts are members of
zookeeper_cluster_slave_group: 'zookeeper-slave-nodes'  #define Ansible inventory group which Slave hosts are members of
zookeeper_debian_repo_key: 'https://archive.cloudera.com/{{ cloudera_hadoop_version }}/{{ ansible_distribution|lower }}/{{ ansible_distribution_release }}/amd64/cdh/archive.key'
zookeeper_debian_repos:
  - 'deb [arch=amd64] http://archive.cloudera.com/{{ cloudera_hadoop_version }}/{{ ansible_distribution|lower }}/{{ ansible_distribution_release }}/amd64/cdh {{ ansible_distribution_release }}-{{ cloudera_hadoop_version }} contrib'
  - 'deb-src http://archive.cloudera.com/{{ cloudera_hadoop_version }}/{{ ansible_distribution|lower }}/{{ ansible_distribution_release }}/amd64/cdh {{ ansible_distribution_release }}-{{ cloudera_hadoop_version }} contrib'
zookeeper_myid: ''  #define zookeeper myid for cluster node id...this needs to be unique per host
````
Dependencies
------------

- role: ansible-oracle-java8

Example Playbook
----------------

````
---
- name: Installs zookeeper
  hosts: all
  become: true
  vars:
  roles:
    - role: ansible-oracle-java8
    - role: ansible-zookeeper
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
