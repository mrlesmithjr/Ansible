Role Name
=========

Installs grafana http://grafana.org/

Requirements
------------

Install all Ansible role requirements.
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Usage
-----

````
username: admin
password: admin
````  

#### Vagrant
http://127.0.0.1:3000

#### Non-Vagrant
http://iporhostname:3000

Role Variables
--------------

````
---
# defaults file for ansible-grafana
grafana_apt_key: 'https://packagecloud.io/gpg.key'
grafana_apt_repo: 'deb https://packagecloud.io/grafana/stable/debian/ wheezy main'
graphite_host: localhost
````

Dependencies
------------

#### GitHub
````
ansible-collectd
ansible-snmpd
ansible-timezone
ansible-grafana
ansible-graphite
````
#### Galaxy
````
mrlesmithjr.collectd
mrlesmithjr.snmpd
mrlesmithjr.timezone
mrlesmithjr.grafana
mrlesmithjr.graphite
````

Example Playbook
----------------

#### GitHub
````
---
- name: provisions grafana
  hosts: all
  become: true
  vars:
  roles:
    - role: ansible-collectd
    - role: ansible-snmpd
    - role: ansible-timezone
    - role: ansible-grafana
    - role: ansible-graphite
  tasks:
````
#### Galaxy
````
---
- name: provisions grafana
  hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.collectd
    - role: mrlesmithjr.snmpd
    - role: mrlesmithjr.timezone
    - role: mrlesmithjr.grafana
    - role: mrlesmithjr.graphite
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
