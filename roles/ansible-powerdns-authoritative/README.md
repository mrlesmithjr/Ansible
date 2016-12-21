Role Name
=========

An Ansible role that installs/configures [PowerDNS] (MySQL cluster ready)


Requirements
------------

Install required Ansible roles..  
```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------
If you would like to install PDNS 4.x version change `pdns_server_version` to
`4.x`.

```
---
# defaults file for ansible-powerdns-authoritative
allow_ddns_updates: false  #define here or globally in group_vars/group
allow_ddns_updates_from: '0.0.0.0/0'  #defines subnet to allow DDNS updates from if allowed...define here or globally in group_vars/group
config_soa_edit_api: false  #set to true if setting up Master/Slave...Otherwise Master zones will not update their SOA in order to transfer
create_pdns_records: false   #defines if dns records should be created/updated
create_pdns_zones: false  #defines if dns zones should be created...pdns_fwd_zones and pdns_fwd_zones
dns_hostmaster: 'hostmaster.{{ pri_domain_name }}'  #define here or globally in group_vars/group
enable_pdns_anycast: false  #define here or globally in group_vars/group
enable_pdns_api: true  # Defines if API should be enabled
enable_pdns_carbon_metrics: false
enable_pdns_recursive_lookups: false  #define here or globally in group_vars/group
enable_pdns_server_logging: false  #define here or globally in group_vars/group
enable_pdns_web_server: false  #define here or globally in group_vars/group
install_pdns_server: true  #defines if authoriative dns server is to be installed
pdns_also_notify:  #Defines if additional nameservers should be notified of zone updates.
  configure: false  #Set to true to enable.
  notify_ips:
    - '192.168.200.201'
    - '192.168.200.202'
pdns_api_key: 'changeme'  #define here or globally in group_vars/all/accounts
pdns_api_url: 'http://127.0.0.1:{{ pdns_webserver_port }}/servers/localhost/zones'
pdns_auth_port: '53'
pdns_carbon_info:
  interval: '30'
  ourname: '{{ ansible_hostname }}'
  server: '192.168.200.201' # Must be defined as IP otherwise will not work
pdns_curl_header: "-H 'X-API-Key: {{ pdns_api_key }}'"
pdns_db_allow_access_from_hosts:  #defines hosts where {{ pdns_db_user }} can login from
  - '{{ ansible_hostname }}'
  - '127.0.0.1'
  - '::1'
  - 'localhost'
  - '%' # Allows from everywhere
pdns_db_cluster: false  #defines if backend db for pdns is clustered...define here or in group_vars/group
pdns_db_host: 'localhost'
pdns_db_name: 'powerdns'  #define here or globally in group_vars/group
pdns_db_pass: 'powerdns'  #define here or globally in group_vars/all/accounts
pdns_db_user: 'powerdns'  #define here or globally in group_vars/all/accounts
pdns_default_soa_mail: 'hostmaster.{{ pri_domain_name }}' #define here or globally in group_vars/group
pdns_default_soa_name: '{{ ansible_hostname }}.{{ pri_domain_name }}' #define here or globally in group_vars/group
pdns_download_url: 'https://downloads.powerdns.com/releases'
pdns_json_interface: true
pdns_listen_all_interfaces: true  #defines if PDSN will listen on all interfaces
pdns_master: false  #Defines if node should perform as PDNS Master
pdns_nameservers:  #define nameservers to use when creating zones..
  - 'ns1.{{ pri_domain_name }}'
  - 'ns2.{{ pri_domain_name }}'
pdns_fwd_zones:  #defines the DNS forward zones to create if create_pdns_zones is true
  - '_msdcs.{{ pri_domain_name }}'
  - '_sites.{{ pri_domain_name }}'
  - '_tcp.{{ pri_domain_name }}'
  - '_udp.{{ pri_domain_name }}'
  - '{{ pri_domain_name }}'
pdns_records:  #define DNS records to create/update...to keep this file small...define in group_vars/all/pdns_records.yml or other...
  - name: 'vcsa'
    zone: '{{ pri_domain_name }}'
    type: 'A'
    changetype: 'REPLACE'
    content: '10.0.101.40'
    disabled: false
    ttl: '3600'
    priority: '0'
  - name: 'logstash'
    zone: '{{ pri_domain_name }}'
    type: 'A'
    changetype: 'REPLACE'
    content: '10.0.101.60'
    disabled: false
    ttl: '3600'
    priority: '0'
  - name: 'dns'
    zone: '{{ pri_domain_name }}'
    type: 'A'
    changetype: 'REPLACE'
    content: '192.168.70.241'
    disabled: false
    ttl: '3600'
    priority: '0'
  - name: 'ntp1'
    zone: '{{ pri_domain_name }}'
    type: 'CNAME'
    changetype: 'REPLACE'
    content: 'dns.{{ pri_domain_name }}'
    disabled: false
    ttl: '3600'
    priority: '0'
pdns_recursor_host: '127.0.0.1'  #should be 127.0.0.1 unless recursor is running on a separate host
pdns_recursor_port: '5300'  #port pdns_recursor should listen on...default is 53 but needs to be changed to run both pdns services on same host
pdns_rev_zones:  #defines the DNS reverse zones to create if create_pdns_zones is true
  - '0.0.10.in-addr.arpa'
  - '2.0.10.in-addr.arpa'
  - '101.0.10.in-addr.arpa'
  - '106.0.10.in-addr.arpa'
  - '107.0.10.in-addr.arpa'
  - '110.0.10.in-addr.arpa'
  - '125.0.10.in-addr.arpa'
  - '10.10.10.in-addr.arpa'
  - '24.16.172.in-addr.arpa'
  - '1.168.192.in-addr.arpa'
  - '70.168.192.in-addr.arpa'
  - '200.168.192.in-addr.arpa'
pdns_server_version: '3.4.10-1' # Defines version to install...To install 4.x change to 4.x
pdns_slave: false  #Defines if node should perform as PDNS Slave
pdns_slaves:
  - '172.28.128.4/32'
  - '172.28.128.6/32'
pdns_webserver_address: '0.0.0.0'
pdns_webserver_allow: '0.0.0.0/0,::/0'
pdns_webserver_password: 'changeme'  #define here or globally in group_vars/all/accounts
pdns_webserver_port: '8081'  #API Webserver port
pdns_zone_types: 'Native'  #defines zone types to create using API..Native,Master,Slave...Native should be used by default...
pdns_zones_dir: 'pdns_zones'  #defines the folder to create locally that will contain the records and zones to be created by pdns_records.yml and pdns_zones.yml
pri_dns: []  #defines primary dns server on network...define here or globally in group_vars/all
pri_domain_name: 'example.org'  #define here or globally in group_vars/all
sec_dns: []  #defines secondary dns server on network...define here or globally in group_vars/all
soa_edit_api: 'INCEPTION-INCREMENT'
```

Dependencies
------------

Reference requirements section above...

Example Playbook
----------------

```
- hosts: all
  roles:
    - role: ansible-mysql
    - role: ansible-powerdns-authoritative
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

[PowerDNS]: <https://www.powerdns.com/>
