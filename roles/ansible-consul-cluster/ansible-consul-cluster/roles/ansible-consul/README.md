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

consul_bin_path: '/usr/local/bin'
consul_bin_owner: "{{ consul_user }}"
consul_bin_group: "{{ consul_group }}"
consul_bin_mode: '0750'

consul_bind_address: "{{ hostvars[inventory_hostname]['ansible_' + consul_bind_interface]['ipv4']['address'] }}"

# Define interface to bind to...(eth0|eth1|enp0s8)
consul_bind_interface: "{{ ansible_default_ipv4['interface'] | replace('-', '_') }}"

# Defines client address to listen on
# either set to 0.0.0.0 (default) or consul_bind_address var.
consul_client_address: '0.0.0.0'

# Defines the name of the node inside the Consul cluster.
consul_node_name: "{{ ansible_hostname }}"

consul_config_dir: '/etc/consul.d'
consul_config_file: '/etc/consul.conf'
consul_data_dir: '/var/consul'

# Defines datacenter name for Consul
consul_datacenter: 'dc1'

consul_dl_file: 'consul_{{ consul_version }}_linux_amd64.zip'
consul_dl_url: 'https://releases.hashicorp.com/consul/{{ consul_version }}'

# Set dns_config options for Consul. See official documentation for all options possible.
consul_dns_config: {}
#  enable_truncate: true
#  udp_answer_limit: 5

# Defines if Consul enables it's ACL functions
consul_enable_acls: true
# Defines if Consul will replicate it's ACLs from consul_acl_datacenter to all other consul_datacenter's
consul_enable_acl_replication: false
# Optional static definition of a Consul replication token
# You may leave this empty and use the agent token API to generate a replication token
consul_acl_replication_token: ''

# Generated using 'uuidgen'
# make sure to generate a new token and replace this one
consul_acl_master_token: 'a5ac5cb6-c0d1-4aa3-bf9a-ca3507adc7ed'

# Define the additional and optional tokens for the agent. See official documentation for details.
consul_acl_agent_master_token: ''
consul_acl_agent_token: ''
consul_acl_token: ''

# Defines the acl_datacenter which is authoritative for ACL information.
consul_acl_datacenter: "{{ consul_datacenter }}"

# Define Consul ACLs within YAML
# To apply ACLs, consul_enable_acls needs to be true and consul_acl_datacenter needs to be set.
# The role will apply the ACLs only in consul_acl_datacenter as they are available in the whole WAN pool.
# The role will also apply the ACLs only against one server as this is sufficient to set ACLs globally.
# The double dash in rules in required as the Ansible module consul_acl expects one list with additional lists in it.
# consul_acl:
#   - mgmt_token: '3d3ae8b5-675e-467f-9616-2f0a82552742'
#     name: 'Foo access'
#     token: '3cfc812f-6dc2-43f1-bceb-f10e8678f35d'
#     rules:
#       - - key: 'foo'
#           policy: 'read'
#         - key: 'private/foo'
#           policy: 'write'
#   - mgmt_token: "{{ variable_somewhere_else }}"
#     name: 'Foo access 2'
#     token: "{{ may_come_from_elsewhere_too }}"
#     rules:
#       - - node: 'my-node'
#           policy: 'read'
#         - service: ''
#           policy: 'write'

# Defines if this role will install required Python modules on servers in consul_acl_datacenter in order to set ACLs via Ansible
# Set to false if you wan't to install them in another way.
consul_acl_install_requirements: true

# Control if role will deploy a pre-populated peers.json for outage recovery purposes.
# Checkout the official Consul documentation on "Outage Recovery" for details.
consul_peers_json_prepared: false
# Path where prepared json file should get placed at
consul_peers_json_prepared_path: "{{ consul_data_dir }}/raft"

# Defines if dnsmasq should be installed and configured to resolv
# consul dns queries to port 8600
consul_enable_dnsmasq: true

# Defines if Consul should log to syslog
consul_enable_syslog: true
# Defines Consul's log level
consul_log_level: 'INFO'

# Generate using 'consul keygen'
# make sure to generate a new key and replace this
# also update key if you changed the it in your cluster via 'consul keyring',
# otherwise the role may deploy an outdated key to additional nodes which then can't join the cluster
consul_encryption_key: 'qLLp1YCJzp9E/xhg11qkdQ=='

consul_user: 'consul'
consul_group: 'consul'
# Defines weather the consul service should run as consul_user/consul_group or not
consul_runas_user: true

consul_mysql_password: 'consul'
consul_mysql_user: 'consul'

# An array of servers to use for retry-join to join existing cluster. # See official documentation of `-retry-join` for possible use cases.
# If empty, the role will populate the array with the IP addresses from hosts in `consul_servers_group` which need to be part of the play.
# Thus defining values here act as an override of the auto population and allows more fine grained plays with out servers in it.
consul_retry_join: []

# An array of remote servers to use for retry-join-wan to join existing federation setup.
# If you populate the array for all your Consul servers in one place, you may want to empty it again for your servers in the target datacenter again elsewhere.
# Consul in the target datacenter won't complain if it's instructed to joint itself via WAN, but it might look a bit strange.
consul_retry_join_wan: []
# Static example
# consul_retry_join_wan:
#   - 266.277.288.299
#   - 266.277.288.301
#   - 266.277.288.302
# Dynamic example when Ansible executing machine is running in Consul DNS aware environment
# Note that the lookup requires dnspython on the Ansible executing machine to work
# consul_retry_join_wan: "{{ lookup('dig', 'consul.service.nyc.consul.', wantlist=True) | ipaddr }}"

# Defines the Ansible group which contains the consul server(s)
consul_servers_group: 'consul_servers'

# Define services to register and checks to ensure those services
# are running on clients. See playbook.yml for examples.
consul_services: []

# Set performance options for Consul. See official documentation for all options possible.
consul_performance: {}
#   raft_multiplier: 1

# Set telemetry options for Consul. See official documentation for all options possible.
consul_telemetry: {}
#   statsd_address: '127.0.0.1:9125'
#   disable_hostname: true

consul_ui: false

consul_version: '0.9.0'

# Defines if role upgrades consul binary on servers to consul_version
# Downgrades are not considered
# Recommendation: When set to true and after raising `consul_version, consider using `--forks=1` on next Ansible run to keep Consul cluster impact low on Upgrade.
consul_upgrade: false
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
