Role Name
=========

An [Ansible] role to install/configure [InfluxDB]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-influxdb
influxdb_config_databases: true
influxdb_databases:
  - host: 'localhost'
    name: 'site'
    state: 'present'
    retention_policy: # Defines the retention policy
      enabled: true
      name: 'test-1w'
      duration: '1w' # Define in hour(h), days(d), weeks(w) or Infinite(INF)
      replication: '1'
influxdb_debian_pre_reqs:
  - 'apt-transport-https'
  - 'python-pip'
influxdb_debian_repo: 'deb https://repos.influxdata.com/{{ ansible_distribution|lower }} {{ ansible_distribution_release|lower }} stable'
influxdb_debian_repo_key: 'https://repos.influxdata.com/influxdb.key'
influxdb_python_modules:
  - 'influxdb'
influxdb_redhat_pre_reqs:
  - 'python-pip'
influxdb_redhat_repo: 'https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable'
influxdb_redhat_repo_key: 'https://repos.influxdata.com/influxdb.key'
```

Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-influxdb
  tasks:
```
License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- [@mrlesmithjr]
- [EveryThingShouldBeVirtual]
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://twitter.com/mrlesmithjr>
[EveryThingShouldBeVirtual]: <http://everythingshouldbevirtual.com>
[Ansible]: <https://www.ansible.com>
[InfluxDB]: <https://www.influxdata.com/time-series-platform/influxdb/>
