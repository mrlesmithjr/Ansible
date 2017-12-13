# ansible-bind

An [Ansible](https://www.ansible.com) role to install/configure [Bind DNS](https://www.isc.org/downloads/bind/)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-bind
# Define acls for defining ip addresses or networks allowed to query bind
bind_acls: []
  # - name: lan
  #   networks:
  #     - 10.0.0.0/8
  #     - localhost
  #     - localnets
  # - name: wireless
  #   networks:
  #     - 172.16.0.0/16
  # - name: dmz
  #   networks:
  #     - 192.168.0.0/16

# Defines if bind should query root-hints servers for unknown queries
# Set bind_forwarding_server: false
bind_caching_server: true

bind_config: false

bind_forward_zones: []
  # - zone: "{{ bind_pri_domain_name }}"
  #   expire: 2419200
  #   hostmaster: "hostmaster.{{ bind_pri_domain_name }}"
  #   masters:
  #     - 192.168.202.200
  #   nameservers:
  #     - "node0.{{ bind_pri_domain_name }}"
  #     - "node1.{{ bind_pri_domain_name }}"
  #     - "node2.{{ bind_pri_domain_name }}"
  #   neg_cache_ttl: 604800
  #   records:
  #     - name: node0
  #       address: 192.168.202.200
  #       type: A
  #     - name: node1
  #       address: 192.168.202.201
  #       type: A
  #     - name: node2
  #       address: 192.168.202.202
  #       type: A
  #     - name: test01
  #       address: 192.168.202.111
  #       type: A
  #     - name: test02
  #       address: 192.168.202.112
  #       type: A
  #     - name: dev
  #       address: "test02.{{ bind_pri_domain_name }}"
  #       type: CNAME
  #     - name: test03
  #       address: 192.168.202.113
  #       type: A
  #     - name: test04
  #       address: 192.168.202.114
  #       type: A
  #   refresh: 604800
  #   retry: 86400
  #   slaves:
  #     - 192.168.202.201
  #     - 192.168.202.202
  #   soa: "{{ ansible_hostname }}.{{ bind_pri_domain_name }}"
  #   ttl: 604800

# Defines if bind should forward unknown queries to bind_forwarders
# Set bind_caching_server: false
bind_forwarding_server: false

# Defines forwarding addresses to be used if bind_forwarding_server: true
bind_forwarders: []
  # - 8.8.8.8
  # - 8.8.4.4

bind_manage_zones: false

# Defines Ansible group which defines the Bind masters
bind_masters_group: bind-masters
bind_pri_domain_name: vagrant.local

bind_reverse_zones: []
  # - zone: 192.168
  #   expire: 2419200
  #   hostmaster: "hostmaster.{{ bind_pri_domain_name }}"
  #   masters:
  #     - 192.168.202.200
  #   nameservers:
  #     - "node0.{{ bind_pri_domain_name }}"
  #     - "node1.{{ bind_pri_domain_name }}"
  #     - "node2.{{ bind_pri_domain_name }}"
  #   neg_cache_ttl: 604800
  #   records:
  #     - name: "node0.{{ bind_pri_domain_name }}"
  #       address: 200.202
  #     - name: "node1.{{ bind_pri_domain_name }}"
  #       address: 201.202
  #     - name: "node2.{{ bind_pri_domain_name }}"
  #       address: 202.202
  #     - name: "test01.{{ bind_pri_domain_name }}"
  #       address: 111.202
  #     - name: "test02.{{ bind_pri_domain_name }}"
  #       address: 112.202
  #     - name: "test03.{{ bind_pri_domain_name }}"
  #       address: 113.202
  #   refresh: 604800
  #   retry: 86400
  #   slaves:
  #     - 192.168.202.201
  #     - 192.168.202.202
  #   soa: "{{ ansible_hostname }}.{{ bind_pri_domain_name }}"
  #   ttl: 604800

bind_slaves_group: bind-slaves
bind_zones_dir: /etc/bind/zones
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-bind
  tasks:
```

## License

BSD

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
