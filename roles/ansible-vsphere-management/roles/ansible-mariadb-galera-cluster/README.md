<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-mariadb-galera-cluster](#ansible-mariadb-galera-cluster)
    -   [Build Status](#build-status)
    -   [Requirements](#requirements)
    -   [Vagrant](#vagrant)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
        -   [Ansible roles](#ansible-roles)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-mariadb-galera-cluster

An [Ansible](https://www.ansible.com) role to install/configure a [MariaDB-Galera Cluster](https://mariadb.com/kb/en/mariadb/what-is-mariadb-galera-cluster/)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-mariadb-galera-cluster.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-mariadb-galera-cluster)

## Requirements

None

## Vagrant

Spin up a test 3-node cluster using Vagrant....

```bash
git clone https://github.com/mrlesmithjr/ansible-mariadb-galera-cluster.git
cd Vagrant
vagrant up
```

When you are done testing tear it all down....

```bash
./cleanup.sh
```

## Role Variables

```yaml
---
# defaults file for ansible-mariadb-galera-cluster

# Define the cacti user info for cacti db monitoring - If used. May remove later.
cacti_db_password: 'cactiuser'
cacti_db_user: 'cactiuser'

# Defines if root logins should be allowed from any host
galera_allow_root_from_any: false

# Define bind address for galera cluster
galera_cluster_bind_address: "{{ hostvars[inventory_hostname]['ansible_' + galera_cluster_bind_interface]['ipv4']['address'] }}"
# Define interface in which to bind
# ex. eth0|eth1|enp0s3|enp0s8
galera_cluster_bind_interface: 'enp0s8'

# Define the name of the cluster
galera_cluster_name: 'vagrant-test'

# Define Ansible group in which the nodes exist to be part of the cluster
galera_cluster_nodes_group: 'galera-cluster-nodes'

# Defines debian db password
# generate using echo password | mkpasswd -s -m sha-512
galera_deb_db_password: '{{ mariadb_mysql_root_password }}'

# Defines email address to receive notifications
galera_email_notifications: 'notifications@{{ mariadb_smtp_domain_name }}'

# Defines if cacti monitoring should be enabled for mysql - If used. May remove later.
galera_enable_cacti_monitoring: false

galera_enable_galera_monitoring_script: false

# Defines if we should enable the MariaDB repo or use version within OS repos.
galera_enable_mariadb_repo: true

# https://mariadb.com/kb/en/mariadb/wsrep_provider_options/
galera_extra_wsrep_provider_options: []
  # evs.auto_evict: 1
  # evs.delayed_margin: 'PT5S'
  # evs.delayed_keep_period: 'PT45S'

# Define which network segment this node is in.
# value is an integer from 0 to 255
# By default all nodes are placed in the same segment (0)
# http://galeracluster.com/documentation-webpages/galeraparameters.html#gmcast-segment
galera_gmcast_segment: '0'

# Address to listen on for Incremental State Transfer.
# By default this is the <address>:<port+1> from wsrep_node_address.
galera_ist_recv_addr: '{{ galera_cluster_bind_address }}'
galera_ist_recv_addr_port: '{{ galera_wsrep_node_address_port|int + 1 }}'

# This option defines the address to which the node will bind in order to
# receive Incremental State Transfers. When this option is not set, it takes
# its value from ist.recv_addr or, in the event that that is also not set,
# from wsrep_node_address. You may find it useful when the node runs behind a
# NAT or in similar cases where the public and private addresses differ.
galera_ist_recv_bind: '{{ galera_cluster_bind_address }}'

galera_monitor_script_name: 'galeranotify.py'
galera_monitor_script_path: '/etc/mysql'

# Defines the which node should be considered the master in the cluster
# Used to bootstrap cluster
galera_mysql_master_node: '{{ groups[galera_cluster_nodes_group][0] }}'

# Define email address that cluster notifications will be sent from
galera_notify_mail_from: 'galeranotify@{{ mariadb_smtp_domain_name }}'
# Define email address that cluster notification will be sent to
galera_notify_mail_to: '{{ galera_email_notifications }}'

# Define smtp server to send notifications through
galera_notify_smtp_server: '{{ mariadb_smtp_server }}'

# Defines if the cluster should be reconfigured
galera_reconfigure_galera: false

galera_wsrep_node_address: '{{ galera_cluster_bind_address }}:{{ galera_wsrep_node_address_port }}'

galera_wsrep_node_address_port: 4567

# MariaDB Repo Info
mariadb_debian_repo: 'deb [arch=amd64,i386,ppc64el] https://mirrors.evowise.com/mariadb/repo/{{ mariadb_version }}/{{ ansible_distribution|lower }} {{ ansible_distribution_release|lower }} main'
mariadb_debian_repo_key: '0xF1656F24C74CD1D8'
mariadb_debian_repo_keyserver: 'keyserver.ubuntu.com'
mariadb_debian_repo_pin: 'mirrors.evowise.com'
mariadb_redhat_repo: 'http://yum.mariadb.org/{{ mariadb_version }}/{{ ansible_distribution|lower }}{{ ansible_distribution_major_version|int}}-amd64'
mariadb_redhat_repo_key: 'https://yum.mariadb.org/RPM-GPG-KEY-MariaDB'
mariadb_version: '10.1'

mariadb_mysql_mem_multiplier: .25

# Define listen port
mariadb_mysql_port: 3306

# Define mysql root password
# generate using echo password | mkpasswd -s -m sha-512
mariadb_mysql_root_password: 'root'

mariadb_mysql_settings:
  collation_server: 'latin1_swedish_ci'
  character_set_client: 'latin1'
  expire_logs_days: 10
  # ON|OFF
  innodb_buffer_pool_size: 128M
  innodb_doublewrite: 'ON'
  innodb_flush_log_at_timeout: 1
  innodb_read_io_threads: 4
  innodb_write_io_threads: 4
  join_buffer_size: 1M
  #Default is 16M
  key_buffer_size: '{{ (ansible_memtotal_mb | int * mariadb_mysql_mem_multiplier) | round | int }}M'
  max_allowed_packet: 16M
  max_binlog_size: 100M
  max_connections: 150
  max_heap_table_size: 16M
  query_cache_limit: 1M
  query_cache_size: 16M
  thread_cache_size: 8
  thread_stack: 192K
  tmp_table_size: 16M

# Define additional MySQL users
mariadb_mysql_users: []
#   - name: example
#     hosts:
#       - "%"
#       - "127.0.0.1"
#       - "::1"
#       - "localhost"
#     password: secret
#     encrypted: no (default)
#     priv: *.*:USAGE (default}
#     state: present (default)
#     append_privs: no (default)

# Define the primary domain name of your environment
mariadb_pri_domain_name: 'example.org'

# Define smtp domain for email
mariadb_smtp_domain_name: '{{ mariadb_pri_domain_name }}'

# Define smtp server to send email through
mariadb_smtp_server: 'smtp.{{ mariadb_pri_domain_name }}'
```

## Dependencies

### Ansible roles

-   [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)

## Example Playbook

[Example playbook](./playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

-   @mrlesmithjr
-   <http://everythingshouldbevirtual.com>
-   mrlesmithjr [at] gmail.com
