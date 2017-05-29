Role Name
=========

An [Ansible] role to install, configure and build a [Consul] cluster.

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-consul.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-consul)

Requirements
------------

Define your Ansible host group name of consul servers within ``consul_servers_group``.

Attaching the role to a group of servers NOT being in the group of ``consul_servers_group`` will treat them as consul clients joining the servers inside ``consul_servers_group``.


Vagrant
-------
You can spin up a 5-node Consul environment for testing by doing the following:

Spin up environment
```
vagrant up
```

This should bring up an environment with a 3-node Consul cluster and 2 nodes
running redis and nginx for service discovery and testing.

You can view the consul web-ui by using your browser to open
- [node3]
- [node4]

When you are done testing in a Vagrant environment you can tear it down by doing
the following:
```
./cleanup.sh
```

Role Variables
--------------

```
---
# defaults file for ansible-consul

# Either "allow" or "deny"; defaults to "allow".
consul_acl_default_policy: 'allow'

# Either "allow", "deny" or "extend-cache"; "extend-cache" is the default.
consul_acl_down_policy: 'extend-cache'

consul_acl_master_token_file: '/etc/consul_acl_master_token'

consul_bin_path: '/usr/local/bin'
consul_bin_owner: "{{ consul_user }}"
consul_bin_group: "{{ consul_group }}"
consul_bin_mode: '0750'

# consul_bind_address: "{{ hostvars[inventory_hostname]['ansible_' + consul_bind_interface]['ipv4']['address'] }}"

# Define interface to bind to...(eth0|eth1|enp0s8)
consul_bind_interface: "{{ ansible_default_ipv4['interface'] }}"

# Defines client address to listen on
# either set to 0.0.0.0 (default) or consul_bind_address var.
consul_client_address: '0.0.0.0'

# Defines if setting up cluster (default)
# currently does not work as only standalone but adding in ability for testing
# purposes at a later time
consul_cluster: true

consul_config_dir: '/etc/consul.d'
consul_config_file: '/etc/consul.conf'
consul_data_dir: '/var/consul'

# Defines datacenter name for Consul
consul_datacenter: 'dc1'

consul_dl_file: 'consul_{{ consul_version }}_linux_amd64.zip'
consul_dl_url: 'https://releases.hashicorp.com/consul/{{ consul_version }}'

consul_enable_acls: true

# Defines if dnsmasq should be installed and configured to resolv
# consul dns queries to port 8600
consul_enable_dnsmasq: true

# Generate using 'consul keygen'
# make sure to generate a new key and replace this
# consul_encryption_key: 'qLLp1YCJzp9E/xhg11qkdQ=='

consul_user: 'consul'
consul_group: 'consul'
# Defines weather the consul service should run as consul_user/consul_group or not
consul_runas_user: true
consul_key_file: '/etc/consul.key'

consul_mysql_password: 'consul'
consul_mysql_user: 'consul'

# Defines the Ansible group which contains the consul server(s)
consul_servers_group: 'consul_servers'

# Define services to register and checks to ensure those services
# are running on clients. See playbook.yml for examples.
consul_services: []

consul_ui: false

consul_version: '0.8.1'
consul_wan_group: 'consul_wan'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  vars:
    - consul_servers_group: 'consulservers'
    - pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-ntp
    - role: ansible-rsyslog
    - role: ansible-timezone
    - role: ansible-users
    - role: ansible-consul
  tasks:
```
You can also checkout the included playbook.yml Ansible playbook.

Example DNS query for Redis Service
-----------------------------------
```
vagrant@node4:/etc/consul.d$ dig @127.0.0.1 -p 8600 redis.service.dc1.consul. ANY

; <<>> DiG 9.9.5-3ubuntu0.7-Ubuntu <<>> @127.0.0.1 -p 8600 redis.service.dc1.consul. ANY
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51158
;; flags: qr aa rd; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:

;redis.service.dc1.consul.      IN      ANY

;; ANSWER SECTION:
redis.service.dc1.consul. 0     IN      A       192.168.202.203
redis.service.dc1.consul. 0     IN      A       192.168.202.204

;; Query time: 5 msec
;; SERVER: 127.0.0.1#8600(127.0.0.1)
;; WHEN: Fri Mar 04 20:31:06 EST 2016
;; MSG SIZE  rcvd: 122

vagrant@node4:/etc/consul.d$
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[node3]: <http://192.168.250.13:8500>
[node4]: <http://192.168.250.14:8500>
[Ansible]: <https://www.ansible.com>
[Consul]: <https://www.consul.io/>
