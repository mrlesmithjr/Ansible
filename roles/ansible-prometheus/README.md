Role Name
=========

An [Ansible] role to install/configure [Prometheus]

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-prometheus
#
# The following will be auto generated using `templates/prometheus.yml.j2` to
# proper YAML. Make sure this block is correct.
prometheus_config:
  global:
    # Set the scrape interval to every 15 seconds. Default is every 1 minute.
    scrape_interval: 15s
    # Evaluate rules every 15 seconds. The default is every 1 minute.
    evaluation_interval: 15s
    # scrape_timeout is set to the global default (10s).
    # Attach these labels to any time series or alerts when communicating with
    # external systems (federation, remote storage, Alertmanager).
    external_labels:
        monitor: 'codelab-monitor'
  # Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
  rule_files:
    # - "first.rules"
    # - "second.rules"
  # A scrape configuration containing exactly one endpoint to scrape:
  # Here it's Prometheus itself.
  scrape_configs:
    # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
    - job_name: 'prometheus'
      # metrics_path defaults to '/metrics'
      # scheme defaults to 'http'.
      static_configs:
        - targets:
          - 'localhost:9090'
          labels:
            group: 'production'
    - job_name: '{{ ansible_hostname }}'
      scrape_interval: 15s
      static_configs:
        - targets:
          - 'localhost:9100'

prometheus_config_file: "{{ prometheus_install_dir }}/prometheus/prometheus.yml"
prometheus_download_url: 'https://github.com/prometheus/prometheus/releases/download'
prometheus_download: '{{ prometheus_download_url }}/v{{ prometheus_version }}/prometheus-{{ prometheus_version }}.linux-amd64.tar.gz'
prometheus_install_dir: '/opt'
prometheus_local_storage: '/var/lib/prometheus/data'
prometheus_source_dir: '/usr/local/src'
prometheus_user_info:
  group: 'prometheus'
  user: 'prometheus'
prometheus_version: '1.6.1'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: monitoring_server
  vars:
    pri_domain_name: 'test.vagrant.local'
    prometheus_config:
      global:
        scrape_interval: 1m
        scrape_timeout: 10s 
        evaluation_interval: 1m
      rule_files:
      scrape_configs:
        - job_name: 'node'
          static_configs:
            - targets:
                - '127.0.0.1:9100'
              labels:
                host: 'node0'
            - targets:
                - '192.168.250.11:9100'
              labels:
                host: 'node1'
            - targets:
                - '192.168.250.12:9100'
              labels:
                host: 'node2'
        - job_name: 'containers'
          static_configs:
            - targets:
                - '192.168.250.11:8080'
              labels:
                docker_host: 'node1'
            - targets:
                - '192.168.250.12:8080'
              labels:
                docker_host: 'node2'
  roles:
    - role: ansible-prometheus
    - role: ansible-grafana
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
[Prometheus]: <https://prometheus.io/>
