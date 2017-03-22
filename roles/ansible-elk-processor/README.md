Role Name
=========

Installs ELK Stack Role (ELK-Processor)

Requirements
------------

Prior to using this role you will want to add your nodes to the appropriate
inventory group. You should create 2 elk-processor nodes. Examples below.
`Inventory`:
```
[elk-nodes]
elk-processor-1
elk-processor-2

[elk-processor-nodes]
elk-processor-1
elk-processor-2
```

Role Variables
--------------

```
---
# defaults file for ansible-elk-processor
alert_throttles:
  - tag: HardDrive-Failure
    settings:
      - name: period
        value: 300
      - name: before_count
        value: -1
      - name: after_count
        value: 1
      - name: key
        value: "%{host}%{message}"
clear_logstash_config: false
config_hosts_file: false  #defines if /etc/hosts should include ELK hosts...if DNS not configured...Vagrant testing.
config_logstash: true
email_notifications: 'notifications@{{ pri_domain_name }}'  #defines email address for logstash to send alerts to
enable_dns_blacklist_filtering: false  #defines if DNS blacklist filtering should be done...uncomment 361_filters_powerdns_blacklists under logstash_configs if set to true
enable_logstash_slack_output: false  #defines if logstash should be configured for sending alerts to slack
es_cluster_name: ansible-test #defines es_cluster_name if not specified in group_vars
logstash_alerts_domain: '{{ pri_domain_name }}'  #defines domain name to configure email alerts...generally should be the same as pri_domain_name
logstash_alerts_email: 'logstash_alerts@{{ pri_domain_name }}'  #defines email account to send alerts from
logstash_blacklists_dir: /etc/logstash/blacklists
logstash_config_dir: /etc/logstash/conf.d
logstash_configs:
  - 000_inputs
  - 001_filters
  - 100_filters_cisco_asa
  - 200_filters_syslog
  - 201_filters_monit
  - 210_filters_iptables
  - 220_filters_haproxy
  - 230_filters_keepalived
  - 240_filters_ssh
  - 241_filters_dhcp
  - 250_filters_snort
  - 260_filters_citrix_netscaler
  # - 270_filters_apache
  # - 280_filters_nginx
  - 290_filters_windows_eventlog
  - 300_filters_windows_updates
  - 310_filters_windows_iis
  - 320_filters_exim4
  - 330_filters_postfix
  - 340_filters_redis
  # - 341_filters_rundeck
  - 350_filters_zfs
  - 360_filters_powerdns
#  - 361_filters_powerdns_blacklists
  - 370_filters_vmware_nsx
  - 900_filters
  - 910_filters_source_host_ip
  - 920_filters_alerting
  - 990_filters_cleanup
  - 991_filters_tagging
  - 999_outputs
logstash_configs_remove:  #define configs that were in logstash_configs but no longer needed below to remove them nodes.
  - 002_metrics  #comment out if metrics for logstash processing are not required..good for keeping track of throughput...removed because of incompatabilities w/ES 2.x
  - 101_filters_monit  #renamed to 201_filters_monit
logstash_custom_template: false  #defines if a custom elasticsearch template for logstash is desired.
logstash_file_inputs:
  - path: /var/log/nginx/access.log
    type: nginx-access
  - path: /var/log/nginx/error.log
    type: nginx-error
  - path: /var/log/mail.log
    type: postfix-log
  - path: /var/log/redis/redis-server.log
    type: redis-server
logstash_grok_patterns:
  - IPTABLES
  - NGINXERROR
logstash_inputs:
  - type: redis
    batch_count: 1000
    host: '{{ logstash_server_fqdn }}'
    threads: 2
logstash_log_dir: /var/log/logstash
logstash_major_ver: '5.x' # Define major version installed (2.x|5.x)
logstash_outputs:
  - output: elasticsearch
    hosts: '{{ logstash_server_fqdn }}:9200'
    protocol: http  #node, transport or http....http is the only protocol supported in 2.x+
    flush_size: 5000
#  - output: gelf
#    host: 10.0.101.196
logstash_pre_tagging:
  - type: apache
    tags:
      - apache
  - type: eventlog
    tags:
      - WindowsEventLog
  - type: exim-log
    tags:
      - exim-log
  - type: iis
    tags:
      - IIS
  - type: logstash-log
    tags:
      - logstash-log
  - type: Netscaler
    tags:
      - Netscaler
  - type: nginx
    tags:
      - nginx
  - type: postfix-log
    tags:
      - postfix-log
  - type: redis-server
    tags:
      - redis-server
  - type: rundeck
    tags:
      - rundeck
  - type: snort
    tags:
      - snort
logstash_post_tagging:
  - type: ESXi
    tags:
      - VMware
  - type: NSX
    tags:
      - VMware
  - type: NSX-FW
    tags:
      - VMware
  - type: NSX-NAT
    tags:
      - VMware
  - type: vCenter
    tags:
      - VMware
logstash_server_fqdn: 'logstash.{{ pri_domain_name }}'  #defines logstash server...should be vip fqdn for elk-haproxy-nodes...define here or globally in group_vars/elk-nodes
logstash_slack_api_webhook_url: [] #define the slack api webhook api url assigned when adding an incoming slack webhook.
logstash_slack_channel: logstash  #defines the slack channel where logstash alerts should be sent to. Ensure enable_logstash_slack_output is set to true if slack output is required.
logstash_slack_output_tags:  #define specific tags to look for to alert on and send to slack
  - SSH_Failed_Login
#logstash_workers: 1  #defines the number of worker processes for logstash to spawn/cpu...default is 1/cpu...define here or in group_vars/group
powerdns_blacklists:
#  - malware
  - social_networking
  - spyware
pri_domain_name: example.org  #defines primary domain name...define here or globally in group_vars/all
smtp_server: 'smtp.{{ pri_domain_name }}'  #defines smtp server to send emails through...define here or globally in group_vars/all
```

Dependencies
------------

Install all required Ansible roles from `requirements.yml`:
```
sudo ansible-galaxy install -r requirements.yml
```

Example Playbook
----------------

```
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-ntp
    - role: ansible-rsyslog
    - role: ansible-snmpd
    - role: ansible-timezone
    - role: ansible-logstash
    - role: ansible-dnsmasq
    - role: ansible-elk-processor
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
