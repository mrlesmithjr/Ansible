Role Name
=========

Installs ELK Stack Role (ELK-Pre-Processor)

Requirements
------------

Prior to using this role you will want to add your nodes to the appropriate inventory group. You should create 2 elk-pre-processor nodes. Examples below.
#####hosts inventory
````
[elk-nodes]
elk-pre-processor-1
elk-pre-processor-2

[elk-pre-processor-nodes]
elk-pre-processor-1
elk-pre-processor-2
````

Role Variables
--------------
defaults/main.yml
````
---
# defaults file for ansible-elk-pre-processor
clear_logstash_config: false
config_hosts_file: false  #defines if /etc/hosts should include ELK hosts...if DNS not configured...Vagrant testing.
config_logstash: true
esxinaming:  #define your VMware ESXi naming standards if used...this should be set to host pattern...example - esxi01.everythingshouldbevirtual.local - define as esxi
  - esxi
hadoopnaming: [] #define your Hadoop naming standards if used...this should be set to host pattern...example - hd01.everythingshouldbevirtual.local - define as hd
#  - hd  #uncomment and remove '' above if setting
logstash_config_dir: /etc/logstash/conf.d
logstash_log_dir: /var/log/logstash
logstash_configs:  #define configs to load...either comment out the ones to not load or move them to logstash_configs_remove
  - 000_inputs
  - 001_filters
  - 200_filters_syslog
  - 210_filters_pfsense
  - 220_filters_esxi
  - 230_filters_vcenter
  - 240_filters_quagga
  - 999_outputs
logstash_configs_remove:  #define configs that were in logstash_configs but no longer needed below to remove them nodes. Move to logstash_configs to enable...
  - 002_metrics  #comment out if metrics for logstash processing are not required..good for keeping track of throughput...removed because of incompatabilities w/ES 2.x
  - 250_filters_vmware_nsx  #not working
  - 260_filters_mysql  #not working
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
  - prot: tcp
    port: 10514
    type: syslog
  - prot: tcp
    port: 1514
    type: VMware
  - prot: tcp
    port: 1515
    type: vCenter
  - prot: tcp
    port: 1517
    type: Netscaler
  - prot: tcp
    port: 28778
    type: elasticsearch-curator
  - prot: tcp
    format: json
    port: 3515
    type: eventlog
  - prot: tcp
    codec: json_lines
    port: 3525
    type: iis
  - prot: tcp
    codec: json
    port: '{{ rundeck_logstash_port }}'
    type: rundeck
logstash_outputs:
  - output: redis
    host: '{{ logstash_server_fqdn }}'
#  - output: rabbitmq
#    exchange: logstash
#    exchange_type: fanout
#    host: 10.0.101.128
logstash_server_fqdn: []  #defines logstash server...should be vip fqdn for elk-haproxy-nodes...define here or globally in group_vars/elk-nodes
netscalernaming: [] #define your Citrix Netscaler naming standards if used...this should be set to host pattern...example - nsvpx01.everythingshouldbevirtual.local - define as nsvpx
#  - nsvpx  #uncomment and remove '' above if setting
nsxnaming: [] #define your VMware NSX naming standards if used...this should be set to host pattern...example - nsx-rt01.everythingshouldbevirtual.local - define as nsx-rt
#  - vShield-edge  #uncomment and remove '' above if setting
#  - nsx-rt  #uncomment and remove '' above if setting
pfsensenaming:  #define your PFSense firewall naming standards if used...this should be set to host pattern...example - pfsense01.everythingshouldbevirtual.local - define as pfsense
  - pfsense
reset_logstash_config: false
rundeck_logstash_port: 9700
vcenter_version: vcsa_6  #defines vcenter version...options- windows_5, windows_6, vcsa_5 or vcsa_6
````
vars/main.yml
````
syslog_servers:
  - name: localhost
    port: 10514
    proto: tcp
````

Dependencies
------------

````
mrlesmithjr.ntp
mrlesmithjr.rsyslog
mrlesmithjr.snmpd
mrlesmithjr.timezone
mrlesmithjr.logstash
mrlesmithjr.dnsmasq
````
Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: mrlesmithjr.ntp }
        - { role: mrlesmithjr.rsyslog }
        - { role: mrlesmithjr.snmpd }
        - { role: mrlesmithjr.timezone }
        - { role: mrlesmithjr.logstash }
        - { role: mrlesmithjr.dnsmasq }
        - { role: mrlesmithjr.elk-pre-processor }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
