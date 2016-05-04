Role Name
=========

Installs and configures Mesosphere and Marathon cluster (https://mesosphere.com/)

Requirements
------------

Install required Ansible roles as below:
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up a five node Vagrant environment for testing
````
vagrant up
````
For additional host_vars check in host_vars/
````
host_vars/node0.yml
host_vars/node1.yml
host_vars/node2.yml
host_vars/node3.yml
host_vars/node4.yml
````

Role Variables
--------------

````
---
# defaults file for ansible-mesosphere
mesosphere_debian_repo: 'deb http://repos.mesosphere.com/{{ ansible_distribution|lower }} {{ ansible_distribution_release }} main'
mesosphere_debian_repo_key_id: 'E56151BF'
mesosphere_debian_repo_key_server: 'hkp://keyserver.ubuntu.com:80'
pri_domain_name: 'example.org'  #defines primary domain name for your site.
zookeeper_myid: ''  #define zookeeper myid for cluster node id...this needs to be unique per host
zookeeper_cluster_group: 'zookeeper-nodes'
zookeeper_cluster_master_group: 'zookeeper-master-nodes'
zookeeper_cluster_slave_group: 'zookeeper-slave-nodes'
````

Dependencies
------------

Reference Requirements section.

Example Playbook
----------------

````
---
- name: Installs mesosphere
  hosts: all
  become: true
  vars:
    - pri_domain_name: 'vagrant.local'
  roles:
    - role: ansible-ntp
    - role: ansible-oracle-java8
    - role: ansible-zookeeper
    - role: ansible-mesosphere
  tasks:
    - name: updating /etc/hosts
      lineinfile:
        dest: /etc/hosts
        regexp: "^{{ hostvars[item].ansible_ssh_host }} {{ item }} {{ item }}.{{ pri_domain_name }}"
        line: "{{ hostvars[item].ansible_ssh_host }} {{ item }} {{ item }}.{{ pri_domain_name }}"
        state: present
      with_items: groups['all']
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
