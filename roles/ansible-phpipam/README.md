Role Name
=========

An Ansible role that installs/configures phpIPAM http://phpipam.net/  
Options are in place for HA DB setup if desired.

Requirements
------------
Install required Ansible role dependencies...  
````
sudo ansible-galaxy install -r requirements.yml
````

Usage
-----

Logging into phpIPAM...  
http://iporhostname/phpipam/?page=login  

Default phpIPAM login is
````
Admin/ipamadmin
````

Role Variables
--------------

````
---
# defaults file for ansible-phpipam
date: "{{ lookup('pipe', 'date +%Y%m%d-%H%M') }}"
enable_phpipam_db_backups: true
phpipam_base: /phpipam/  #defines root of phpipam web...if using http url headers...change this to '/'
phpipam_db_backup_name_prefix: phpipam_bkp
phpipam_db_backup_root: /backups/db/phpipam
phpipam_db_cluster: false #defines if backend db for pdns is clustered...define here or in group_vars/group

phpipam_db_host: localhost  #define db host
phpipam_db_name: phpipam  #define db name
phpipam_db_pass: phpipam  #define db password or define in group_vars/group
phpipam_db_user: phpipam  #define db user or define in group_vars/group
phpipam_define_cron_jobs: false  #defines if cron jobs for scanning and etc. should be defined.
phpipam_download: 'https://sourceforge.net/projects/phpipam/files/{{ phpipam_download_file }}'
phpipam_download_file: 'phpipam-{{ phpipam_version }}.tar'
phpipam_patch_discovery: false  #defines if current discovery functionality should be patched
phpipam_patch_email: false  #defines if current email test functionality should be patched
phpipam_pre_load_db: true
phpipam_prettify_links: true  #defines if Apache2 should be configured in order to enable prettify links
phpipam_primary: 'node0'  #define if using a clustered mariadb mysql and define a single node as primary
phpipam_root: '{{ web_root }}/phpipam'  #defines the root folder of where phpipam is to be installed
phpipam_timezone: 'America/New_York'
phpipam_upgrade: false  #defines if phpipam is to be upgraded
phpipam_url: 'ipam.{{ pri_domain_name }}'  #defines the phpipam url to configure apache2 for if configured for url rewrite
phpipam_version: 1.2.1
pri_domain_name: example.org  #defines the primary domain name...define here or globally in group_vars/all
web_root: /var/www/html
````

Dependencies
------------

Reference requirements section..

Example Playbook
----------------

````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-apache2
    - role: ansible-mariadb-mysql
    - role: ansible-phpipam
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
