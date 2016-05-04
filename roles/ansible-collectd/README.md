Role Name
=========

Installs and configures collectd role. https://collectd.org/ Ready for Grafana/Graphite output...

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-collectd
collectd_collectors:  #defines collectd servers to send metrics to if desired...defined here or in group_vars/all/servers
  - 'logstash-dev.{{ pri_domain_name }}'
  - '{{ logstash_server_fqdn }}'
collectd_db_monitor_pass: collectd  #define here or in group_vars/all/accounts
collectd_db_monitor_user: collectd  #define here or in group_vars/all/accounts
collectd_enable_mysql_monitoring: false  #defines if mysql monitoring should be enabled for collectd
graphite_host: ''  #define here or in in group_vars/all/servers
graphite_host_fqdn: '{{ graphite_host }}.{{ pri_domain_name }}'  #define here or in group_vars/all/servers
graphite_port: 2003
graphite_protocol: tcp
graphite_prefix: collectd.
````
Dependencies
------------

If grafana output is desired...Grab the Ansible Galaxy role....mrlesmithjr/grafana


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.collectd }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
