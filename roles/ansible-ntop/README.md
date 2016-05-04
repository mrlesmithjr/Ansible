Role Name
=========

Installs NTOP Monitoring...http://www.ntop.org/

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-ntop
ntop_debian_apt_url: 'http://apt-stable.ntop.org/{{ ansible_distribution_version }}/all'
ntop_debian_package: apt-ntop-stable.deb
ntop_dns_mode: 1  #defines NTOP dns resolution mode
ntop_http_port: 3000  #defines listen port for integrated NTOP web interface
ntop_listen_interfaces:  #define interface(s) for ntop to listen on
  - eth0
#  - eth1
ntop_local_networks:  #define network(s) which should be considered local in reports
  - 10.0.0.0/8
  - 172.16.0.0/16
  - 192.168.0.0/16
````

Dependencies
------------

Ansible Galaxy role(s)
- mrlesmithjr.redis

````
ansible-galaxy install -r ntop_requirements.yml
````


Example Playbook
----------------

---
- name: NTOP Network Monitoring
  hosts: ntop-servers
  remote_user: remote
  sudo: true
  vars:
  roles:
    - mrlesmithjr.redis
    - mrlesmithjr.ntop
  tasks:

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
