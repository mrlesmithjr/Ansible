Role Name
=========

Installs mysql https://www.mysql.com/
######Configurable options and cacti monitoring ready.

Requirements
------------

None

Docker
------
Run as a Docker container  
````
docker run -d -p 3306:3306 mrlesmithjr/mysql
````

Role Variables
--------------

````
---
# defaults file for ansible-mysql
cacti_db_password: cactiuser  #defines cacti db password for monitoring
cacti_db_user: cactiuser  #defines cacti db user for monitoring
cacti_server_fqdn: 'cacti.{{ pri_domain_name }}'  #defines fqdn of cacti server for monitoring
cacti_server: cacti  #defines hostname of cacti server for monitoring
config_mysqlchk: false  #defines if mysqlchk scripts should be configured for load balancer monitoring
deb_db_password: "{{ mysql_root_password }}"  #defines debian db password...generate using echo password | mkpasswd -s -m sha-512
enable_cacti_monitoring: false  #defines if cacti monitoring should be configured
mysql_allow_remote_connections: false  #defines if mysql should listen on loopback (default) or allow remove connections
mysql_docker_install: false  #defines if mysql is being installed in Docker
mysql_port: 3306  #defines the port for mysql to listen on
mysql_root_password: root #defines mysql root password...generate using echo password | mkpasswd -s -m sha-512
mysqlchk_host: '127.0.0.1'  #defines the host to run mysqlchk against...usually localhost
mysqlchk_opts: '-N -q -A'  #defines mysqlchk options to pass
mysqlchk_user: 'cmon'  #defines mysqlchk user
mysqlchk_pass: 'cmon'  #defines mysqlchk user password
pri_domain_name: example.org
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-mysql
  tasks:
````
#### Galaxy
````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.mysql
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
