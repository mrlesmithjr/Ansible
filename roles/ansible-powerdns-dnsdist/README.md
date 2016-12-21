Role Name
=========

An [Ansible] role to install [PowerDNS DNSDist].

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-powerdns-dnsdist
config_pdns_dnsdist: true
enable_pdns_dnsdist_acls: true # http://dnsdist.org/README/#acl-who-can-use-dnsdist
enable_pdns_dnsdist_cache: true # http://dnsdist.org/README/#caching
enable_pdns_dnsdist_carbon_metrics: false # http://dnsdist.org/README/#carbongraphitemetronome
enable_pdns_dnsdist_control_socket: true
enable_pdns_dnsdist_domain_blocks: false
enable_pdns_dnsdist_pool_rules: true
enable_pdns_dnsdist_webserver: true # http://dnsdist.org/README/#webserver
pdns_dnsdist_acls:
  - '10.0.0.0/8'
  # - '100.64.0.0/10'
  - '169.254.0.0/16'
  - '192.168.0.0/16'
  - '172.16.0.0/12'
  - '::1/128'
  - 'fc00::/7'
  - 'fe80::/10'
pdns_dnsdist_cache:
  - name: 'pc'
    max_entries: '10000' # Required
    max_lifetime: '86400' # Not required
    min_ttl: '0' # Not required
    pool: '' # Required...the default is blank as it creates a cache for the default pool..otherwise define a pool name
    ttl_server_failure_response: '60' # Not required
    ttl_stale_cache: '60' # Not required
pdns_dnsdist_carbon_metrics_info:
  interval: '30' # Defines the interval in which to send metrics
  reporting_hostname: '{{ ansible_hostname }}' # Defines the hostname which shows in metrics collection
  server: 'graphite.{{ pri_domain_name }}' # Defines the server to send metrics to
pdns_dnsdist_debian_pre_reqs:
  - 'libsystemd-dev'
pdns_dnsdist_debian_repo: 'deb [arch=amd64] {{ pdns_dnsdist_repo_url }}/{{ ansible_distribution|lower }} {{ ansible_distribution_release|lower }}'
pdns_dnsdist_debian_repo_key: 'https://repo.powerdns.com/FD380FBB-pub.asc'
pdns_dnsdist_domain_blocks: # Defines domains in which to block inbound traffic from
  - 'ezdns.it.'
  - 'sh43354.cn.'
pdns_dnsdist_downstream_servers:
  - address: '192.168.202.201'
    # order: '1' # Define order if order based selection is desired
    # pool: "test" # Defines a pool name to assign the server to
    # port: '5300' # Defines a different port for downstream server
    # qps: '1000' # Defines the Queries Per Second limit
    # recv_timeout: '2' # Defines receive timeout (default is '2')
    # send_timeout: '2' # Defines send timeout (default is '2')
  - address: '8.8.8.8'
    pool: "google"
  - address: '8.8.4.4'
    pool: 'google'
  - address: '208.67.222.222'
    pool: 'opendns'
  - address: '208.67.220.220'
    pool: 'opendns'
pdns_dnsdist_local_address: '0.0.0.0'
pdns_dnsdist_pool_rules:
  - query:
      - 'conviva.com'
    pool: 'google'
  - query:
      - 'facebook.com.'
    pool: 'opendns'
pdns_dnsdist_redhat_pre_reqs:
  - 'epel-release'
  - 'yum-plugin-priorities'
pdns_dnsdist_repo_url: 'http://repo.powerdns.com'
pdns_dnsdist_server_policy: 'leastOutstanding' # firstAvailable|RoundRobin|whashed|wrandom|leastOutstanding

# Make sure to change this key...generate a new one by running the following
# on your dnsdist server as I have not been able to get Ansible to automate
# the capturing of a generated key
# echo "makeKey()" | sudo dnsdist
pdns_dnsdist_setkey: 'bKKPxcw4ieTkt29PenVFRcXzt1Nwc78TK+hHdUvqMCo='
#

pdns_dnsdist_ver: '1.0.x' # Define version to install...(1.0.x|1.1.x)
pdns_dnsdist_webserver_info:
  address: '0.0.0.0'
  api_key: 'changeme'
  port: '8083'
  password: 'changeme'
pri_domain_name: 'example.org'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-powerdns-dnsdist
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- [@mrlesmithjr]
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://www.twitter.com/mrlesmithjr>
[PowerDNS]: <https://www.powerdns.com/>
[PowerDNS DNSDist]: <http://dnsdist.org/>
