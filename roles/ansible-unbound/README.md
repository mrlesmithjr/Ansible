# Role Name

An [Ansible](https://www.ansible.com) to install/confgiure [Unbound DNS server](https://www.unbound.net)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-unbound

# Defines if unbound should be configured
config_unbound: false

# Defines access controls for usage of unbound
# Available actions (allow|deny|refuse|allow_snoop)
unbound_access_control:
  - subnet: 0.0.0.0/0
    action: 'allow'
#  - subnet: 10.0.0.0/8
#    action: 'allow'
#  - subnet: 172.16.0.0/16
#    action: 'allow'
#  - subnet: 192.168.0.0/16
#    action: 'allow'

# Define authoritative zones and A records.
# If you would like PTR(reverse) records to be created set
# create_ptr_records: true
# otherwise set create_ptr_records: false
unbound_authoritative_zones: []
  # - zone: 'vagrant.local'
  #   a_records:
  #     - name: 'srv01'
  #       ip: 192.168.250.101
  #     - name: 'srv02'
  #       ip: 192.168.250.102
  #   create_ptr_records: true

# Maximum lifetime of cached entries.
# Default is 86400 seconds (1  day).
unbound_cache_max_ttl: 86400

# Minimum lifetime of cache entries in seconds.
# Default is 0
unbound_cache_min_ttl: 0

# Defines unbound configuration directory
unbound_config_dir: '/etc/unbound/unbound.conf.d'

# Defines if unbound pre-fetch should be enabled
unbound_enable_prefetch: false

# Defines if optimizations defined in unbound_optimizations should be set
unbound_enable_optimizations: false

# Defines forwarding zones and addresses to forward to for each zone
unbound_forward_zones: []
  # - zone: everythingshouldbevirtual.local
  #   forward_addresses:
  #     - 10.0.101.111
  #     - 10.0.101.112
    # Defines all zones not specifically defined to forward to addresses
    # Google DNS in this example.
  # - zone: '.'
  #   forward_addresses:
  #     - 8.8.8.8
  #     - 8.8.4.4

# Enable to not answer id.server and hostname.bind queries.
unbound_hide_identity: true

# Enable to not answer version.server and version.bind queries.
unbound_hide_version: true

# Calculation to determine hosts total memory in mb
unbound_host_memory: '{{ ansible_memtotal_mb }}'

# Calculation to determine hosts number of threads
unbound_host_threads: '{{ ansible_processor_cores * ansible_processor_count }}'

# Defines interface addresses to listen on
unbound_listen_addresses:
  - 0.0.0.0
#  - 127.0.0.1
#  - ::1
#  - '{{ ansible_default_ipv4.address }}'

# Defines if all dns queries should be logged.
unbound_log_queries: false

# To log elsewhere, set 'use-syslog' to 'false' and set the log file location
unbound_logfile: '/var/log/messages'

# Defines optimzations to be set if unbound_enable_optimizations is true
unbound_optimizations:
  infra_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  key_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  msg_cache_size: '{{ (unbound_host_memory|int * 0.0312) | round | int }}m'
  msg_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  num_threads: '{{ unbound_host_threads }}'
  rrset_cache_slabs: '{{ unbound_host_threads|int * 2 }}'
  rrset_cache_size: '{{ (unbound_host_memory|int * 0.0625) | round | int }}m'

# Default is to use syslog, which will log to /var/log/messages.
unbound_use_syslog: true
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-unbound
  tasks:
```

## License

BSD

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
