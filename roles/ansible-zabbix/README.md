Role Name
=========

Installs and configures Zabbix server/agent monitoring (https://www.zabbix.com)  
Define version to install by setting zabbix_version: x.x (2.2|2.4|3.0)

Requirements
------------

Install required Ansible roles:
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up a test environment using Vagrant:  
````
sudo ansible-galaxy install -r requirements.yml -f
vagrant up
````
Once the environment is up connect to http://127.0.0.1:8080/zabbix using
your browswer of choice.  
Login using:  
````
username: Admin
password: zabbix
````
You are now ready to begin testing and using Zabbix.  
When you are done with your testing you can tear down by:  
````
./cleanup.sh
````

Role Variables
--------------

````
---
# defaults file for ansible-zabbix
zabbix_advanced_parameters:  #define add'l advanced parameters
  - name: StartVMwareCollectors
    value: '{{ zabbix_vmware_instances|int * 2 }}'
  - name: VMwareCacheSize
    value: 8M
  - name: VMwareFrequency
    value: 60
  - name: VMwarePerfFrequency
    value: 60
  - name: VMwareTimeout
    value: 10
zabbix_agent_group: all  #define Ansible inventory that zabbix agents are members of
zabbix_agent_listen_port: 10050
zabbix_change_mysql_root_password: true  #defines if mysql root password should be changed
zabbix_db_info:  #defines db info
  host: localhost  #define db host
  name: zabbix  #define db name
  password: zabbix  #define db password
  port: 3306  #define db port
  user: zabbix  #define db user
zabbix_debian_pre_req_packages:  #defines pre-req packages for debian
  - automysqlbackup
  - gzip
  - python-dev
  - python-mysqldb
  - python-pip
zabbix_debian_repo_info:  #defines Debian based package repo info
  package: 'zabbix-release_{{ zabbix_version }}-1+{{ ansible_distribution_release|lower }}_all.deb'
  url: 'http://repo.zabbix.com/zabbix/{{ zabbix_version }}/{{ ansible_distribution|lower }}/pool/main/z/zabbix-release'
zabbix_frontend_php_settings:  #defines php settings to be added to Apache configuration
  - name: max_execution_time
    value: 300
  - name: memory_limit
    value: 128M
  - name: post_max_size
    value: 16M
  - name: upload_max_filesize
    value: 2M
  - name: max_input_time
    value: 300
  - name: always_populate_raw_post_data
    value: -1
  - name: date.timezone
    value: America/New_York
zabbix_host_groups:
  - test
zabbix_manage_groups: false  #defines if zabbix groups should be managed
zabbix_manage_hosts: false  #defines if zabbix hosts should be managed
zabbix_mysql_root_password: 'zabbix'  #define mysql root password to be set to if change_mysql_root_password: true
zabbix_mysql_schema_archive: '/usr/share/doc/zabbix-server-mysql/create.sql.gz'  #defines db schema archive
zabbix_package_dir: '/usr/local/src'  #define directory to save packages to
zabbix_python_modules:
  - zabbix-api
zabbix_server_group: 'zabbix-servers'  #define Ansible inventory group that zabbix servers are members of
zabbix_server_listen_ip: 0.0.0.0  #List of comma delimited IP addresses that the trapper should listen on
zabbix_server_logfile_size: 0  #defines Maximum size of log file in MB (0-1024) 0=disable
zabbix_server_logfile: /var/log/zabbix/zabbix_server.log
zabbix_server_port: 10051  #define zabbix server port
zabbix_server_timeout: 4  #Specifies how long we wait for agent
zabbix_server: 'node0.{{ pri_domain_name }}'  #define zabbix server for agents
zabbix_server_info:
  url: 'http://127.0.0.1/zabbix'
  login_user: 'Admin'
  login_password: 'zabbix'
zabbix_version: 3.0  #define zabbix version to install (2.2|2.4|3.0)
zabbix_vmware_instances: 1  #define number of VMware services to monitor (if used)...vCenter,ESXi hosts and etc.
````

Dependencies
------------

None

Example Playbook
----------------

````
- hosts: all
  become: true
  vars:
    - pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-zabbix
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
