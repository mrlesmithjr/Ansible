Role Name
=========

Installs and configures a ready to use Owncloud deployment (https://owncloud.org)

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
Login to WebUI using defined owncloud_admin_user and owncloud_admin_pass vars (http://iporhostname/owncloud)

###### Vagrant
Login to WebUI using defined owncloud_admin_user and owncloud_admin_pass vars (http://127.0.0.1:8080/owncloud)

Role Variables
--------------

````
---
# defaults file for ansible-owncloud
apache2_webroot: /var/www/html
mysql_root_password: root
owncloud_admin_user: owncloudadmin
owncloud_admin_pass: owncloudadmin
owncloud_db_name: owncloud  #define the owncloud db name to create and use
owncloud_db_password: owncloud  #define the owncloud db password to create and use
owncloud_db_user: owncloud  #define the owncloud db username to create and use
owncloud_debian_repo_key: 'https://download.owncloud.org/download/repositories/stable/{{ ansible_distribution }}_{{ ansible_distribution_version }}/Release.key'
owncloud_debian_repo: 'deb http://download.owncloud.org/download/repositories/stable/{{ ansible_distribution }}_{{ ansible_distribution_version }}/ /'
owncloud_dl_file: 'owncloud-{{ owncloud_version }}.tar.bz2'
owncloud_dl_url: https://download.owncloud.org/community
owncloud_version: 8.2.2
owncloud_webroot: '{{ apache2_webroot }}/owncloud'
````

Dependencies
------------

````
ansible-apache2
ansible-mariadb-mysql
````

Example Playbook
----------------

````
---
- name: provisions owncloud
  hosts: all
  sudo: true
  vars:
    - apt_mirror_client: false
    - mysql_root_password: root
    - pri_domain_name: example.org
  roles:
    - role: ansible-apache2
    - role: ansible-mariadb-mysql
    - role: ansible-owncloud
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
