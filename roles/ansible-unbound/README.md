Role Name
=========

Installs and configured unbound DNS server.. ( https://www.unbound.net )

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-unbound
config_unbound: true  #defines if unbound should be configured
unbound_access_control:  #defines access controls for usage of unbound
  - subnet: 0.0.0.0/0  #Defines allow all
    action: allow  #defines action (allow|deny|refuse|allow_snoop)
#  - subnet: 10.0.0.0/8
#    action: allow  #defines action (allow|deny|refuse|allow_snoop)
#  - subnet: 172.16.0.0/16
#    action: allow  #defines action (allow|deny|refuse|allow_snoop)
#  - subnet: 192.168.0.0/16
#    action: allow  #defines action (allow|deny|refuse|allow_snoop)
unbound_cache_max_ttl: 86400  #Maximum lifetime of cached entries. Default is 86400 seconds (1  day).
unbound_cache_min_ttl: 0  #Minimum lifetime of cache entries in seconds.  Default is 0
unbound_config_dir: /etc/unbound/unbound.conf.d  #defines unbound configuration directory
unbound_enable_prefetch: false  #defines if unbound pre-fetch should be enabled
unbound_enable_optimizations: false  #defines if optimizations defined in unbound_optimizations should be set
unbound_forward_zones:  #defines forwarding zones and addresses to forward to for each zone
  - zone: everythingshouldbevirtual.local
    forward_addresses:
      - 10.0.101.111
      - 10.0.101.112
  - zone: .  #defines all zones not specifically defined to forward to addresses...Google DNS in this example.
    forward_addresses:
      - 8.8.8.8
      - 8.8.4.4
unbound_hide_identity: true  #enable to not answer id.server and hostname.bind queries.
unbound_hide_version: true  #enable to not answer version.server and version.bind queries.
unbound_host_memory: '{{ ansible_memtotal_mb }}' #calculation to determine hosts total memory in mb
unbound_host_threads: '{{ ansible_processor_cores * ansible_processor_count }}'  #calculation to determine hosts number of threads
unbound_listen_addresses:  #defines interface addresses to listen on
  - 0.0.0.0  #Defines listen on all interfaces..comment out and define interfaces to listen on below if not all interfaces desired
#  - 127.0.0.1
#  - ::1
#  - '{{ ansible_default_ipv4.address }}'
unbound_log_queries: false  #defines if all dns queries should be logged.
unbound_logfile: /var/log/messages  #to log elsewhere, set 'use-syslog' to 'false' and set the log file location
unbound_optimizations:  #defines optimzations to be set if unbound_enable_optimizations is true
  infra_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  key_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  msg_cache_size: '{{ (unbound_host_memory|int * 0.0312) | round | int }}m'
  msg_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  num_threads: '{{ unbound_host_threads }}'
  rrset_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  rrset_cache_size: '{{ (unbound_host_memory|int * 0.0625) | round | int }}m'
unbound_setup_forward_zones: false  #defines if unbound forward zones should be configured as in unbound_forward_zones
unbound_use_syslog: true  #default is to use syslog, which will log to /var/log/messages.
````

Dependencies
------------

None

Example Playbook
----------------

````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-unbound
  tasks:
````

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
