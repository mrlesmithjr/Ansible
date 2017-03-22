Role Name
=========

An [Ansible] role that installs/configures [PowerDNS] Recursor

Requirements
------------

Install required [Ansible] roles..  
```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------
If you would like to install PDNS 4.x version change `pdns_recursor_version` to
`4.x`.

```
---
# defaults file for ansible-powerdns-recursor

pdns_recursor_download_url: 'https://downloads.powerdns.com/releases'

# Defines if specific forward zones should be defined
pdns_recursor_enable_fwd_zones: false

# Define forward lookup zone(s) along with DNS servers to use
pdns_recursor_fwd_zones:
  - name: 'blah.example.org'
    servers:
      - '192.168.1.5'
      - '192.168.1.6'
  - name: 'blah.blah.example.org'
    servers:
      - '192.168.2.5'
      - '192.168.2.6'
pdns_recursor_local_address: '0.0.0.0'

# Defines port pdns_recursor should listen on
# default is 53 but needs to be changed to run both pdns services on same host
pdns_recursor_port: '5300'

# Defines if source IP address should be defined for recursive queries
# default is 0.0.0.0
pdns_recursor_source_ip: false

# Defines version to install
# To install 4.x change to 4.x
pdns_recursor_version: '3.7.3-1'
```

Dependencies
------------

Reference requirements section above...

Example Playbook
----------------

````
- hosts: all
  roles:
    - role: ansible-powerdns-recursor
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

[Ansible]: <https://www.ansible.com>
[PowerDNS]: <https://www.powerdns.com/>
