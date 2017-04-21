Ansible Playbooks and Roles
===========================

From me [@mrlesmithjr] to the community  

The goal of this repo is to maintain a consistent configuration across hosts.  

This repo will always be updated on a continuous basis and all feedback is
encouraged and welcomed.

Requirements
------------

The majority of variables are configurable in `group_vars/all`  
The goal of this is to keep a consistent single place to update site-wide
variables.

To ensure all roles are current and up to date you can run the following in
the root of this repo..  
```
ansible-galaxy install -r requirements.yml -f -p ./roles --ignore-errors
```

##### Playbooks
`bootstrap.yml`
Used as phase one of deployments... bootstraps hosts

`site.yml`
Phase two of deployments... configures base settings and install base packages
that should be site-wide

`sensu.yml`
Installs Sensu Server and Sensu Clients

`elkstack_prod.yml`
Builds ELKStack Highly Available, Scalable environment

ELKStack - Requirements
-----------------------

- Build out the following hosts and modify hosts to reflect name changes
lines with [] define a group name to be added to hosts.  
- Lines that contain [1:x] are regex values to define multiple hosts.

```
[elk-p-nodes]
elk-p-haproxy-[1:2]
elk-p-broker-[1:3]
elk-p-es-[1:3]
elk-p-pre-processor-[1:2]
elk-p-processor-[1:4]

[elk-p-haproxy-nodes]
elk-p-haproxy-[1:2]

[elk-p-broker-nodes]
elk-p-broker-[1:3]

[elk-p-es-nodes]
elk-p-es-[1:3]

[elk-p-pre-processor-nodes]
elk-p-pre-processor-[1:2]

[elk-p-processor-nodes]
elk-p-processor-[1:4]
```
You will need to update group_vars and host_vars to tailor to your environment... Ex. Host naming and etc.
```
group_vars/all
group_vars/elk-p-broker-nodes
group_vars/elk-p-es-nodes
group_vars/elk-p-haproxy-nodes
group_vars/elk-p-nodes
group_vars/elk-p-pre-processor-nodes
group_vars/elk-p-processor-nodes
host_vars/elk-p-haproxy-1
host_vars/elk-p-haproxy-2
```
Example Playbook
----------------
ELKStack example playbook....included in this repo
```
---
- hosts: elk-p-nodes
  remote_user: remote
  sudo: yes
  roles:
    - role: ansible-base
    - role: ansible-network-tweaks

- hosts: elk-p-broker-nodes
  remote_user: remote
  sudo: yes
  roles:
    - role: ansible-redis
      when: use_redis
    - role: ansible-rabbitmq
      when: use_rabbitmq
    - role: ansible-nginx
    - role: ansible-elasticsearch
    - role: ansible-elk-broker
    - role: ansible-elk-kibana

- hosts: elk-p-es-nodes
  remote_user: remote
  sudo: yes
  roles:
    - role: ansible-elasticsearch
    - role: ansible-elk-es

- hosts: elk-p-pre-processor-nodes
  remote_user: remote
  sudo: yes
  roles:
    - role: ansible-logstash
    - role: ansible-elk-pre-processor
    - role: ansible-dnsmasq

- hosts: elk-p-processor-nodes
  remote_user: remote
  sudo: yes
  roles:
    - role: ansible-elasticsearch
    - role: ansible-logstash
    - role: ansible-elk-processor
    - role: ansible-dnsmasq

- hosts: elk-p-haproxy-nodes
  remote_user: remote
  sudo: yes
  roles:
    - role: ansible-logstash
    - role: ansible-haproxy
    - role: ansible-elk-haproxy
```

License
-------
GNU General Public License Version 2

Author Information
------------------
Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://www.twitter.com/mrlesmithjr>
