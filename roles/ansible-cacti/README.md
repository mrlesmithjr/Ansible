Role Name
=========

Installs and configures Cacti  
http://cacti.net/

Requirements
------------

Install requirements using Ansible Galaxy
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up Vagrant environment
````
vagrant up
````
Open your browser of choice and connect to:  
http://127.0.0.1:8080/cacti  
And follow the prompts to complete install.  
Log in with the following:  
````
user: admin
password: admin
````

Role Variables
--------------

````
---
# defaults file for ansible-cacti
cacti_cli: '{{ cacti_site_dir }}/cli'
cacti_config_file: '{{ cacti_site_dir }}/include/config.php'
cacti_cron_schedule:
  minute: '*/5'
  hour: '*'
  day: '*'
  month: '*'
cacti_db_info:
  host: '127.0.0.1'
  port: '3306'
  db_name: 'cactidb'
  user: 'cactiuser'
  password: 'cacti'
cacti_debian_packages:
  - php5-cli
  - php5-gd
  - php5-mysql
  - php5-snmp
  - python-mysqldb
  - python-passlib
  - rrdtool
  - snmp
  - zlib1g
  - zlib1g-dev
cacti_dl_file: 'cacti-{{ cacti_version }}.tar.gz'
cacti_dl_url: 'http://www.cacti.net/downloads/'
cacti_import_templates: true  #defines if Cacti templates included should be added and imported
cacti_redhat_packages:
  - MySQL-python
  - net-snmp-libs
  - net-snmp-utils
  - php
  - php-cli
  - php-common
  - php-devel
  - php-gd
  - php-mbstring
  - php-mysql
  - php-pear
  - php-snmp
  - rrdtool
cacti_site_dir: "{{ cacti_web_root }}/cacti"
cacti_snmp_queries:
  - f5_bigip_ifStat.xml
  - f5_bigip_pm.xml
  - f5_bigip_pool.xml
  - f5_bigip_vs.xml
  - f5_gtm_poolStat.xml
  - f5_gtm_wip.xml
  - snmp_informant_standard_cpu.xml
  - snmp_informant_standard_disk.xml
  - snmp_informant_standard_memory.xml
  - snmp_informant_standard_network.xml
  - snmp_informant_standard_objects.xml
cacti_snmp_templates:
  - cacti_host_template_f5_big-ip.xml
  - cacti_data_query_snmp_informant_standard_-_cpu_statistics.xml
  - cacti_data_query_snmp_informant_standard_-_disk_statistics.xml
  - cacti_data_query_snmp_informant_standard_-_memory_statistics.xml
  - cacti_data_query_snmp_informant_standard_-_network_statistics.xml
  - cacti_data_query_snmp_informant_standard_-_objects_statistics.xml
  - cacti_host_template_snmp_informant_windows.xml
cacti_url_path: '/cacti/'
cacti_user_info:
  name: 'cactiuser'
  password: 'cacti'
  comment: 'Cacti User Account'
cacti_version: '0.8.8f'
cacti_webserver_type: 'apache2'  #defines web server type (apache2|lighttpd|nginx)
````

Dependencies
------------

https://github.com/mrlesmithjr/ansible-apache2.git  
https://github.com/mrlesmithjr/ansible-cacti.git  
https://github.com/mrlesmithjr/ansible-lighttpd.git  
https://github.com/mrlesmithjr/ansible-mariadb-mysql.git  
https://github.com/mrlesmithjr/ansible-ntp.git  
https://github.com/mrlesmithjr/ansible-snmpd.git  
https://github.com/mrlesmithjr/ansible-timezone.git  

Install all dependencies following requirements section.

Example Playbook
----------------

#### GitHub
````
---
- hosts: all
  become: true
  vars:
    - cacti_webserver_type: 'apache2'
    - pri_domain_name: 'vagrant.local'
  roles:
    - role: ansible-apache2
      when: cacti_webserver_type == "apache2"
    - role: ansible-lighttpd
      when: cacti_webserver_type == "lighttpd"
    - role: ansible-nginx
      when: cacti_webserver_type == "nginx"
    - role: ansible-mariadb-mysql
    - role: ansible-ntp
    - role: ansible-snmpd
    - role: ansible-timezone
    - role: ansible-cacti
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
