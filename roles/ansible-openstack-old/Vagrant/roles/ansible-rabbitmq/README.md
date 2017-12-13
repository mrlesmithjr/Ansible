Role Name
=========

Installs rabbitmq https://www.rabbitmq.com/ (Configurable...HA and Clustering ready)

Requirements
------------

Ensure hostnames are resolvable prior to clustering...either update /etc/hosts or ensure DNS is working.

Vagrant
-------

Spin up a 3 node HA Cluster for testing...  
Install Ansible role on your host:  
````
sudo ansible-galaxy install -r requirements.yml -f
````
Now spin up your environment...  
````
vagrant up
````
When you are done testing, tear it all down...  
````
./cleanup.sh
````

Role Variables
--------------

````
---
# defaults file for ansible-rabbitmq
config_rabbitmq_ha: false  #defines if rabbitmq ha should be configured...define here or in group_vars/group
enable_rabbitmq_clustering: false  #defines if setting up a rabbitmq cluster...define here or in group_vars/group
erlang_cookie: 'LSKNKBELKPSTDBBCHETL'  #define erlang cookie for cluster...define here or in group_vars/group
erlang_cookie_file: '/var/lib/rabbitmq/.erlang.cookie'
rabbitmq_config:
  - queue_name: logstash
    durable: true
    exchange_name: logstash
    type: direct
    routing_key: logstash
    tags: 'ha-mode=all,ha-sync-mode=automatic'
rabbitmq_debian_repo: 'deb http://www.rabbitmq.com/debian/ testing main'
rabbitmq_debian_repo_key: 'http://www.rabbitmq.com/rabbitmq-signing-key-public.asc'
rabbitmq_master: []  #defines the inventory host that should be considered master...define here or in group_vars/group
rabbitmq_redhat_repo_key: 'https://www.rabbitmq.com/rabbitmq-signing-key-public.asc'
rabbitmq_redhat_package: 'rabbitmq-server-{{ rabbitmq_redhat_version }}-1.noarch.rpm'
rabbitmq_redhat_url: 'http://www.rabbitmq.com/releases/rabbitmq-server/v{{ rabbitmq_redhat_version }}'
rabbitmq_redhat_version: '3.6.1'
rabbitmq_users:  #define admin user to create in order to login to WebUI
  - name: rabbitmqadmin
    password: rabbitmqadmin
    vhost: /
    configure_priv: '.*'
    read_priv: '.*'
    write_priv: '.*'
    tags: 'administrator'  #define comma separated list of tags to assign to user....management,policymaker,monitoring,administrator...required for management plugin. https://www.rabbitmq.com/management.html
````

example...
group_vars/rabbitmq-cluster-nodes
````
---
enable_rabbitmq_clustering: true
config_rabbitmq_ha: false
rabbitmq_master: ans-test-1
````

Dependencies
------------

None

Example Playbook
----------------

````
---
- hosts: all
  become: true
  vars:
    - pri_domain_name: 'test.vagrant.local'
  roles:
  tasks:
    - name: updating /etc/hosts
      lineinfile:
        dest: /etc/hosts
        regexp: "^{{ hostvars[item].ansible_ssh_host }} {{ item }} {{ item }}.{{ pri_domain_name }}"
        line: "{{ hostvars[item].ansible_ssh_host }} {{ item }} {{ item }}.{{ pri_domain_name }}"
        state: present
      with_items: groups['all']

- hosts: all
  become: true
  vars:
    - config_rabbitmq_ha: true
    - enable_rabbitmq_clustering: true
    - pri_domain_name: 'test.vagrant.local'
    - rabbitmq_master: 'node0'
  roles:
    - role: ansible-rabbitmq
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
