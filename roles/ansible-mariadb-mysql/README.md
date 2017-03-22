Role Name
=========

An [Ansible] role to install/configure [MariaDB] mysql

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-mariadb-mysql.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-mariadb-mysql)

Requirements
------------

None

Vagrant
-------
```
vagrant up
```

Role Variables
--------------
```
---
# defaults file for ansible-mariadb-mysql

# Define the cacti info for cacti db monitoring - If used. May remove later.
cacti_db_password: 'cactiuser'
cacti_db_user: 'cactiuser'
cacti_server_fqdn: 'cacti.{{ mariadb_pri_domain_name }}'
cacti_server: 'cacti'
enable_cacti_monitoring: false

# Defines debian db password
# generate using echo password | mkpasswd -s -m sha-512
mariadb_deb_db_password: "{{ mariadb_mysql_root_password }}"

# Defines if we should enable the MariaDB repo or use version within OS repos.
mariadb_enable_mariadb_repo: true

# MariaDB Repo Info
mariadb_debian_repo: 'deb [arch=amd64,i386,ppc64el] https://mirrors.evowise.com/mariadb/repo/{{ mariadb_version }}/{{ ansible_distribution|lower }} {{ ansible_distribution_release|lower }} main'
mariadb_debian_repo_key: '0xF1656F24C74CD1D8'
mariadb_debian_repo_keyserver: 'keyserver.ubuntu.com'
mariadb_debian_repo_pin: 'mirrors.evowise.com'
mariadb_redhat_repo: 'http://yum.mariadb.org/{{ mariadb_version }}/{{ ansible_distribution|lower }}{{ ansible_distribution_major_version|int}}-amd64'
mariadb_redhat_repo_key: 'https://yum.mariadb.org/RPM-GPG-KEY-MariaDB'
mariadb_version: '10.1'

# Defines if mysql should listen on loopback (default) or allow remove connections
mariadb_mysql_allow_remote_connections: false

# Defines the port for mysql to listen on
mariadb_mysql_port: '3306'

# Defines mysql root password
# generate using echo password | mkpasswd -s -m sha-512
mariadb_mysql_root_password: root

# Define mysql login user
mariadb_mysql_user: 'root'

# Define the primary domain name of your environment
mariadb_pri_domain_name: 'example.org'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: db_hosts
  become: true
  vars:
  roles:
    - role: ansible-mariadb-mysql
  tasks:
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

[Ansible]: <https://www.ansible.com>
[MariaDB]: <https://mariadb.org/>
