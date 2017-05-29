Role Name
=========

An [Ansible] role to install/configure [Prometheus Node Exporter]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-prometheus-node-exporter
prometheus_node_exporter_download: '{{ prometheus_node_exporter_download_url }}/v{{ prometheus_node_exporter_version }}/node_exporter-{{ prometheus_node_exporter_version }}.linux-amd64.tar.gz'
prometheus_node_exporter_download_url: 'https://github.com/prometheus/node_exporter/releases/download'
prometheus_node_exporter_install_dir: '/opt'
prometheus_node_exporter_listen_port: '9100'
prometheus_node_exporter_source_dir: '/usr/local/src'
prometheus_node_exporter_version: '0.14.0'

prometheus_node_exporter_user_info:
  group: 'prometheus'
  user: 'prometheus'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  vars:
  roles:
    - role: ansible-prometheus-node-exporter
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
[Prometheus Node Exporter]: <https://github.com/prometheus/node_exporter>
