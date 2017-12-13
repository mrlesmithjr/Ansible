Role Name
=========

An Ansible role that installs/configures PowerDNS https://www.powerdns.com/ (MySQL cluster ready)

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-powerdns.svg)](https://travis-ci.org/mrlesmithjr/ansible-powerdns)

Requirements
------------

Install required Ansible roles..  
````
sudo ansible-galaxy install -r requirements.yml
````

Role Variables
--------------

````
---
allow_ddns_updates: false  #define here or globally in group_vars/group
allow_ddns_updates_from: 0.0.0.0/0  #defines subnet to allow DDNS updates from if allowed...define here or globally in group_vars/group
config_logstash: false  #defines if logstash should be configured if installed...define here or globally in group_vars/group
create_pdns_records: false   #defines if dns records should be created/updated
create_pdns_zones: false  #defines if dns zones should be created...pdns_fwd_zones and pdns_fwd_zones
dns_hostmaster: "hostmaster.{{ pri_domain_name }}"  #define here or globally in group_vars/group
enable_pdns_anycast: false  #define here or globally in group_vars/group
enable_pdns_recursive_lookups: true  #define here or globally in group_vars/group
enable_pdns_recursor_fwd_zones: false  #defines if specific forward zones should be defined
enable_pdns_server_logging: false  #define here or globally in group_vars/group
enable_pdns_web_server: false  #define here or globally in group_vars/group
install_logstash: false  #defines if logstash should be installed and configured for DNS logging..define here or globally in group_vars/group
install_pdns_recursor: true   #defines if recursive caching server is to be installed
install_pdns_server: true  #defines if authoriative dns server is to be installed
install_poweradmin: false  #use NSEDIT instead
nsedit_apiip: 127.0.0.1  #defines the IP address of the NSEDIT API IP to connect to...should be localhost in most cases.
pdns_api_key: changeme  #define here or globally in group_vars/all/accounts
pdns_api_url: "http://127.0.0.1:{{ pdns_webserver_port }}/servers/localhost/zones"
pdns_curl_header: "-H 'X-API-Key: {{ pdns_api_key }}'"
pdns_db_cluster: false  #defines if backend db for pdns is clustered...define here or in group_vars/group
pdns_db_host: localhost
pdns_db_name: powerdns  #define here or globally in group_vars/group
pdns_db_pass: powerdns  #define here or globally in group_vars/all/accounts
pdns_db_user: powerdns  #define here or globally in group_vars/all/accounts
pdns_default_soa_mail: "hostmaster.{{ pri_domain_name }}" #define here or globally in group_vars/group
pdns_default_soa_name: "{{ ansible_hostname }}.{{ pri_domain_name }}" #define here or globally in group_vars/group
pdns_download_url: https://downloads.powerdns.com/releases
pdns_json_interface: true
pdns_listen_all_interfaces: true  #defines if PDSN will listen on all interfaces
pdns_ns1: "ns1.{{ pri_domain_name }}"  #define primary nameserver to use when creating zones...IP/Hostname..ns1.example.org
pdns_ns2: "ns2.{{ pri_domain_name }}"  #define secondary nameserver to use when creating zones...IP/Hostname..ns2.example.org
pdns_fwd_zones:  #defines the DNS forward zones to create if create_pdns_zones is true
  - "_msdcs.{{ pri_domain_name }}"
  - "_sites.{{ pri_domain_name }}"
  - "_tcp.{{ pri_domain_name }}"
  - "_udp.{{ pri_domain_name }}"
  - "{{ pri_domain_name }}"
pdns_records:  #define DNS records to create/update...to keep this file small...define in group_vars/all/pdns_records.yml or other...
  - name: vcsa
    zone: "{{ pri_domain_name }}"
    type: A
    changetype: REPLACE
    content: 10.0.101.40
    disabled: false
    ttl: 3600
    priority: 0
  - name: logstash
    zone: "{{ pri_domain_name }}"
    type: A
    changetype: REPLACE
    content: 10.0.101.60
    disabled: false
    ttl: 3600
    priority: 0
  - name: dns
    zone: "{{ pri_domain_name }}"
    type: A
    changetype: REPLACE
    content: 192.168.70.241
    disabled: false
    ttl: 3600
    priority: 0
  - name: ntp1
    zone: "{{ pri_domain_name }}"
    type: CNAME
    changetype: REPLACE
    content: "dns.{{ pri_domain_name }}"
    disabled: false
    ttl: 3600
    priority: 0
pdns_recursive_source_ip: false  #defines if source IP address should be defined for recursive queries...default is 0.0.0.0
pdns_recursor_fwd_zones:  #define forward lookup zone(s) along with DNS servers to use
  - name: blah.example.org
    servers:
      - 192.168.1.5
      - 192.168.1.6
  - name: blah.blah.example.org
    servers:
      - 192.168.2.5
      - 192.168.2.6
pdns_recursor_host: 127.0.0.1  #should be 127.0.0.1 unless recursor is running on a separate host
pdns_recursor_port: 5300  #port pdns_recursor should listen on...default is 53 but needs to be changed to run both pdns services on same host
pdns_recursor_version: 3.7.3-1
pdns_rev_zones:  #defines the DNS reverse zones to create if create_pdns_zones is true
  - 0.0.10.in-addr.arpa
  - 2.0.10.in-addr.arpa
  - 101.0.10.in-addr.arpa
  - 106.0.10.in-addr.arpa
  - 107.0.10.in-addr.arpa
  - 110.0.10.in-addr.arpa
  - 125.0.10.in-addr.arpa
  - 10.10.10.in-addr.arpa
  - 24.16.172.in-addr.arpa
  - 1.168.192.in-addr.arpa
  - 70.168.192.in-addr.arpa
  - 200.168.192.in-addr.arpa
pdns_server_version: 3.4.6-1
pdns_webserver_address: 0.0.0.0
pdns_webserver_allow: "0.0.0.0/0,::/0"
pdns_webserver_password: []  #define here or globally in group_vars/all/accounts
pdns_webserver_port: 8081  #API Webserver port
pdns_zone_types: Native  #defines zone types to create using API..Native,Master,Slave...Native should be used by default...
pdns_zones_dir: pdns_zones  #defines the folder to create locally that will contain the records and zones to be created by pdns_records.yml and pdns_zones.yml
poweradmin_db_host: localhost  #define here or globally in group_vars/group
poweradmin_pass: admin  #define here or globally in group_vars/group
poweradmin_user: admin  #define here or globally in group_vars/group
poweradmin_ver: poweradmin-2.1.7
pri_dns: []  #defines primary dns server on network...define here or globally in group_vars/all
pri_domain_name: example.org  #define here or globally in group_vars/all
sec_dns: []  #defines secondary dns server on network...define here or globally in group_vars/all
web_root: /var/www/html
````

Dependencies
------------

Reference requirements section above...

Example Playbook
----------------

````
- hosts: all
  roles:
    - role: ansible-apache2
    - role: ansible-mariadb-mysql
    - role: ansible-powerdns
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
