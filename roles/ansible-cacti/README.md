Role Name
=========

An [Ansible] role to install and configure [Cacti]

Requirements
------------

Install requirements using Ansible Galaxy
```
sudo ansible-galaxy install -r requirements.yml -f
```

Vagrant
-------
Spin up Vagrant environment
```
vagrant up
```
Open your browser of choice and connect to:  
http://127.0.0.1:8080/cacti  
And follow the prompts to complete install.  
Log in with the following:  
```
user: admin
password: admin
```

Role Variables
--------------

```
---
# defaults file for ansible-cacti
cacti_cli: '{{ cacti_site_dir }}/cli'
cacti_config_file: '{{ cacti_site_dir }}/include/config.php'
cacti_cron_schedule:
  minute: '*/5'
  hour: '*'
  day: '*'
  month: '*'

# Defines if the cacti user account should be able to login from anywhere vs. localhost
cacti_db_allow_all_hosts: false

cacti_db_info:
  host: '127.0.0.1'
  port: '3306'
  db_name: 'cactidb'
  user: 'cactiuser'
  password: 'cacti'
cacti_debian_packages:
  # - 'mysql-client'
  - 'php{{ cacti_php_version }}'
  - 'php-cli'
  - 'php{{ cacti_php_version }}-fpm'
  - 'php{{ cacti_php_version }}-gd'
  - 'php{{ cacti_php_version }}-json'
  - 'php-ldap'
  - 'php-mbstring'
  - 'php{{ cacti_php_version }}-mysql'
  - 'php{{ cacti_php_version }}-snmp'
  - 'php{{ cacti_php_version }}-xml'
  - 'php{{ cacti_php_version }}-gmp'
  - 'python-mysqldb'
  - 'python-passlib'
  - 'rrdtool'
  - 'snmp'
  - 'zlib1g'
  - 'zlib1g-dev'
cacti_dl_file: 'cacti-{{ cacti_version }}.tar.gz'
cacti_dl_url: 'http://www.cacti.net/downloads/'

# Defines if Cacti templates included should be added and imported
cacti_import_templates: true
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
cacti_remote_db: false
cacti_replace_cacti_db_schema: false
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
cacti_trees:
  - name: Infrastructure
    sub_trees:
      - Network
      - Servers
      - UCS
  - Linux
  - Windows
cacti_url_path: '/cacti/'
cacti_user_info:
  name: 'cactiuser'
  password: 'cacti'
  comment: 'Cacti User Account'
cacti_version: '1.0.3'
cacti_webserver_type: 'apache2'  #defines web server type (apache2|lighttpd|nginx)
mysql_root_password: root
```

Dependencies
------------

Follow requirements section

Example Playbook
----------------

```
---
- hosts: cacti_nodes
  become: true
  vars:
    apache2_config_php: true
    apache2_install_php: true
    cacti_webserver_type: 'apache2'
    mysql_settings:
      collation_server: 'latin1_swedish_ci'
      character_set_client: 'latin1'
      expire_logs_days: '10'
      # ON|OFF
      innodb_doublewrite: 'OFF'
      innodb_flush_log_at_timeout: '3'
      innodb_read_io_threads: '32'
      innodb_write_io_threads: '16'
      join_buffer_size: '64M'
      #Default is 16M
      key_buffer_size: '{{ (ansible_memtotal_mb | int * mysql_mem_multiplier) | round | int }}M'
      max_allowed_packet: '16M'
      max_binlog_size: '100M'
      max_connections: '150'
      max_heap_table_size: '24M'
      query_cache_limit: '1M'
      query_cache_size: '16M'
      thread_cache_size: '8'
      thread_stack: '192K'
      tmp_table_size: '64M'
  roles:
    - role: ansible-ntp
    - role: ansible-snmpd
    - role: ansible-timezone
    - role: ansible-apache2
      when: cacti_webserver_type == "apache2"
    - role: ansible-lighttpd
      when: cacti_webserver_type == "lighttpd"
    - role: ansible-nginx
      when: cacti_webserver_type == "nginx"
    - role: ansible-mysql
    - role: ansible-cacti
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

[Ansible]: <https://www.ansible.com>
[Cacti]: <http://cacti.net/>
