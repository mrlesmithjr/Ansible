Role Name
=========

Installs rsyslog (Configurable and remote syslog server ready)

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-rsyslog
configure_rsyslog: false  #defines if rsyslog should be reconfigured
pri_domain_name: example.org  #defines primary domain name...define here or globally in group_vars/all
rsyslog_allow_tcp: false  #defines if rsyslog should be configured to listen on tcp/514
rsyslog_allow_udp: false  #defines if rsyslog should be configured to listen on udp/514
syslog_servers: []  #defines remote syslog servers...define here or globally in group_vars/all
#  - name: 'graylog.{{ pri_domain_name }}'
#    proto: udp
#    port: 514
#  - name: 'logstash.{{ pri_domain_name }}'
#    proto: tcp
#    port: 514
#  - name: localhost  #good for redirecting back itself..ex. logstash running on tcp/udp 10514...to get around logstash running on ports < 1024
#    proto: tcp
#    port: 10514
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
- hosts: all
  become: true
  vars:
  roles:
    - ansible-rsyslog
  tasks:
````
#### Galaxy
````
- hosts: all
  become: true
  vars:
  roles:
    - mrlesmithjr.syslog
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
