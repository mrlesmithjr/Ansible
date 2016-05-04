Role Name
=========

Installs and configures Snorby https://github.com/Snorby/snorby  
Snorby is a web-frontend for Snort, Suricata and Sagan

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

###### Non-Vagrant
http://iporhostname

###### Vagrant
http://127.0.0.1:8080

###### Initial Login
E-mail: snorby@example.com
Password: snorby

Role Variables
--------------

````
---
# defaults file for ansible-snorby
apache_root_dir: /var/www/html  #defines apache root directory
mysql_root_password: root
pri_domain_name: example.org  #defines your primary domain name
snorby_authentication_mode: database
snorby_db_info:  #defines Snorby DB Info
  name: snorby  #DB Name
  host: localhost  #DB Host
  user: snorby  #DB User
  pass: snorby  #DB Pass
snorby_db_info_setup:  #defines Snorby DB Info for initial setup
  name: snorby
  host: localhost
  user: root
  pass: '{{ mysql_root_password }}'
snorby_mail_sender: 'snorby@{{ pri_domain_name }}'
snorby_reconfigure_gemfile: true  #defines if Gemfile pulled down should be overwritten due to https://github.com/Snorby/snorby/pull/388
snorby_root_dir: '{{ apache_root_dir }}/snorby'
snorby_ssl: false
snorby_webserver: apache2  #defines webserver type...apache2 or nginx
snorby_webserver_name: 'snorby.{{ pri_domain_name }}'
snort_barnyard2_logdir: /var/log/snort
snort_barnyard2_waldo_file: '{{ snort_barnyard2_logdir }}/barnyard2.waldo'
````

Dependencies
------------

You can install dependencies as follows:
````
sudo ansible-galaxy install -r requirements.yml -f
````

Example Playbook
----------------

#### GitHub
````
- name: Installs Snorby
  hosts: all
  become: true
  vars:
    - passenger_webserver: apache2
  roles:
    - role: ansible-ntp
    - role: ansible-apache2
      when: passenger_webserver == "apache2"
    - role: ansible-nginx
      when: passenger_webserver == "nginx"
    - role: ansible-passenger
    - role: ansible-mysql
    - role: ansible-snort
    - role: ansible-snorby
````
#### Galaxy
````
- name: Installs Snorby
  hosts: all
  become: true
  vars:
    - passenger_webserver: apache2
  roles:
    - role: mrlesmithjr.ntp
    - role: mrlesmithjr.apache2
      when: passenger_webserver == "apache2"
    - role: mrlesmithjr.nginx
      when: passenger_webserver == "nginx"
    - role: mrlesmithjr.passenger
    - role: mrlesmithjr.mysql
    - role: mrlesmithjr.snort
    - role: mrlesmithjr.snorby
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
