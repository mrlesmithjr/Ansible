<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Role Name](#role-name)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Role Name

An [Ansible](https://www.ansible.com) role that installs/configures [PowerDNS](https://www.powerdns.com/)

-   (MySQL cluster ready)

## Requirements

Install required Ansible roles..

```bash
sudo ansible-galaxy install -r requirements.yml
```

## Role Variables

```yaml
---
# defaults file for ansible-powerdns-authoritative

# Defines if Dynamic DNS is allowed
pdns_allow_ddns_updates: false

# Defines subnet to allow DDNS updates from if allowed
pdns_allow_ddns_updates_from: 0.0.0.0/0

#Defines if additional nameservers should be notified of zone updates.
pdns_also_notify:
  configure: false
  notify_ips:
    - 192.168.200.201
    - 192.168.200.202

# Defines the API Key
pdns_api_key: 'changeme'

# Defines the API URL
pdns_api_url: 'http://127.0.0.1:{{ pdns_webserver_port }}/servers/localhost/zones'

# Defines the listen port
pdns_auth_port: 53

# Defines the Carbon server info for metrics
pdns_carbon_info:
  interval: 30
  ourname: '{{ ansible_hostname }}'
  server: 192.168.200.201 # Must be defined as IP otherwise will not work

# Set to true if setting up Master/Slave
# Otherwise Master zones will not update their SOA in order to transfer
pdns_config_soa_edit_api: false

# Defines if dns records should be created/updated
pdns_create_pdns_records: false

# Defines if dns zones should be created...pdns_fwd_zones and pdns_fwd_zones
pdns_create_pdns_zones: false

# Defines the curl header for managing records via API URL
pdns_curl_header: "-H 'X-API-Key: {{ pdns_api_key }}'"

# Defines hosts where {{ pdns_db_user }} can login from
pdns_db_allow_access_from_hosts:
  - '{{ ansible_hostname }}'
  - 127.0.0.1
  - '::1'
  - 'localhost'
 # Allows from everywhere
  - '%'

# Defines if backend db for pdns is clustered
pdns_db_cluster: false

# Defines the host where the MySQL DB resides
pdns_db_host: 'localhost'
pdns_db_name: 'powerdns'
pdns_db_pass: 'powerdns'
pdns_db_user: 'powerdns'
pdns_default_soa_mail: 'hostmaster.{{ pri_domain_name }}'
pdns_default_soa_name: '{{ ansible_hostname }}.{{ pri_domain_name }}'
pdns_download_url: 'https://downloads.powerdns.com/releases'


# Defines if Anycast networking should be enabled
pdns_enable_pdns_anycast: false

# Defines if API should be enabled
pdns_enable_pdns_api: true

# Defines is Carbon metrics are enabled for monitoring statistics
pdns_enable_pdns_carbon_metrics: false

# Defines if recursive lookups should be enabled
pdns_enable_pdns_recursive_lookups: false

# Defines if DNS logging should be enabled
pdns_enable_pdns_server_logging: false

# Defines if web server should be enabled
pdns_enable_pdns_web_server: false

# Defines the DNS forward zones to create if pdns_create_pdns_zones is true
pdns_fwd_zones: []
  # - '_msdcs.{{ pri_domain_name }}'
  # - '_sites.{{ pri_domain_name }}'
  # - '_tcp.{{ pri_domain_name }}'
  # - '_udp.{{ pri_domain_name }}'
  # - '{{ pri_domain_name }}'

pdns_repo_baseurl: 'http://repo.powerdns.com'
pdns_repo_gpgkey: 'https://repo.powerdns.com/FD380FBB-pub.asc'
pdns_json_interface: true

# Defines if PDNS will listen on all interfaces
pdns_listen_all_interfaces: true

# Defines if node should perform as PDNS Master
pdns_master: false

# Define nameservers to use when creating zones..
pdns_nameservers:
  - 'ns1.{{ pri_domain_name }}'
  - 'ns2.{{ pri_domain_name }}'

# Define DNS records to create/update
pdns_records: []
  # - name: 'vcsa'
  #   zone: '{{ pri_domain_name }}'
  #   type: 'A'
  #   changetype: 'REPLACE'
  #   content: 10.0.101.40
  #   disabled: false
  #   ttl: 3600
  #   priority: 0
  # - name: 'logstash'
  #   zone: '{{ pri_domain_name }}'
  #   type: 'A'
  #   changetype: 'REPLACE'
  #   content: 10.0.101.60
  #   disabled: false
  #   ttl: 3600
  #   priority: 0
  # - name: 'dns'
  #   zone: '{{ pri_domain_name }}'
  #   type: 'A'
  #   changetype: 'REPLACE'
  #   content: 192.168.70.241
  #   disabled: false
  #   ttl: 3600
  #   priority: 0
  # - name: 'ntp1'
  #   zone: '{{ pri_domain_name }}'
  #   type: 'CNAME'
  #   changetype: 'REPLACE'
  #   content: 'dns.{{ pri_domain_name }}'
  #   disabled: false
  #   ttl: 3600
  #   priority: 0

# Defines PDNS recursor host
pdns_recursor_host: 127.0.0.1

# Defines PDNS recursor port
pdns_recursor_port: 5300

# Defines the DNS reverse zones to create if pdns_create_pdns_zones is true
pdns_rev_zones: []
  # - '0.0.10.in-addr.arpa'
  # - '2.0.10.in-addr.arpa'
  # - '101.0.10.in-addr.arpa'
  # - '106.0.10.in-addr.arpa'
  # - '107.0.10.in-addr.arpa'
  # - '110.0.10.in-addr.arpa'
  # - '125.0.10.in-addr.arpa'
  # - '10.10.10.in-addr.arpa'
  # - '24.16.172.in-addr.arpa'
  # - '1.168.192.in-addr.arpa'
  # - '70.168.192.in-addr.arpa'
  # - '200.168.192.in-addr.arpa'

# Defines version to install
# To install 3.4.10-1 change to 3.4.10-1
# To install 4.x change to 4.x
pdns_server_version: '4.x'

# Defines if node should perform as PDNS Slave
pdns_slave: false
pdns_slaves:
  - 172.28.128.4/32
  - 172.28.128.6/32
pdns_webserver_address: 0.0.0.0
pdns_webserver_allow: '0.0.0.0/0,::/0'
pdns_webserver_password: 'changeme'

# Defines API Webserver port
pdns_webserver_port: 8081

# Defines zone types to create using API
# Native,Master,Slave
# Native should be used by default...
pdns_zone_types: 'Native'

# Defines the folder to create locally that will contain the records and
# zones to be created by pdns_records.yml and pdns_zones.yml
pdns_zones_dir: 'pdns_zones'

# Defines primary domain name of environment
pri_domain_name: 'example.org'

pdns_soa_edit_api: 'INCEPTION-INCREMENT'
```

## Dependencies

Reference requirements section above...

## Example Playbook

## License

BSD

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
