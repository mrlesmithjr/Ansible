Role Name
=========

Ansible role to install/configure Bind DNS.

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-bind
bind_acls:  #define acls for defining ip addresses or networks allowed to query bind
  - name: 'lan'
    networks:
      - '10.0.0.0/8'
      - 'localhost'
      - 'localnets'
  - name: 'wireless'
    networks:
      - '172.16.0.0/16'
  - name: 'dmz'
    networks:
      - '192.168.0.0/16'
bind_caching_server: true  #defines if bind should query root-hints servers for unknown queries...set bind_forwarding_server: false
bind_config: true
bind_forward_zones:
  - zone: '{{ pri_domain_name }}'
    expire: 2419200
    hostmaster: 'hostmaster.{{ pri_domain_name }}'
    masters:
      - '192.168.202.200'
    nameservers:
      - 'node0.{{ pri_domain_name }}'
      - 'node1.{{ pri_domain_name }}'
      - 'node2.{{ pri_domain_name }}'
    neg_cache_ttl: 604800
    records:
      - name: 'node0'
        address: '192.168.202.200'
        type: 'A'
      - name: 'node1'
        address: '192.168.202.201'
        type: 'A'
      - name: 'node2'
        address: '192.168.202.202'
        type: 'A'
      - name: 'test01'
        address: '192.168.202.111'
        type: 'A'
      - name: 'test02'
        address: '192.168.202.112'
        type: 'A'
      - name: 'dev'
        address: 'test02.{{ pri_domain_name }}'
        type: 'CNAME'
      - name: 'test03'
        address: '192.168.202.113'
        type: 'A'
      - name: 'test04'
        address: '192.168.202.114'
        type: 'A'
    refresh: 604800
    retry: 86400
    slaves:
      - '192.168.202.201'
      - '192.168.202.202'
    soa: '{{ ansible_hostname }}.{{ pri_domain_name }}'
    ttl: 604800
bind_forwarding_server: false  #defines if bind should forward unknown queries to bind_forwarders...set bind_caching_server: false
bind_forwarders:  #Define forwarding addresses to be used if bind_forwarding_server: true
  - 8.8.8.8
  - 8.8.4.4
bind_manage_zones: false
bind_masters_group: 'bind-masters'
bind_reverse_zones:
  - zone: '192.168'
    expire: 2419200
    hostmaster: 'hostmaster.{{ pri_domain_name }}'
    masters:
      - '192.168.202.200'
    nameservers:
      - 'node0.{{ pri_domain_name }}'
      - 'node1.{{ pri_domain_name }}'
      - 'node2.{{ pri_domain_name }}'
    neg_cache_ttl: 604800
    records:
      - name: 'node0.{{ pri_domain_name }}'
        address: '200.202'
      - name: 'node1.{{ pri_domain_name }}'
        address: '201.202'
      - name: 'node2.{{ pri_domain_name }}'
        address: '202.202'
      - name: 'test01.{{ pri_domain_name }}'
        address: '111.202'
      - name: 'test02.{{ pri_domain_name }}'
        address: '112.202'
      - name: 'test03.{{ pri_domain_name }}'
        address: '113.202'
    refresh: 604800
    retry: 86400
    slaves:
      - '192.168.202.201'
      - '192.168.202.202'
    soa: '{{ ansible_hostname }}.{{ pri_domain_name }}'
    ttl: 604800
bind_slaves_group: 'bind-slaves'
bind_zones_dir: '/etc/bind/zones'
pri_domain_name: 'vagrant.local'
```

Dependencies
------------

None

Example Playbook
----------------

````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-bind
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
