Role Name
=========

An [Ansible] role to install/configure a [MariaDB-Galera Cluster]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-mariadb-galera-cluster.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-mariadb-galera-cluster)

Requirements
------------

None

Vagrant
-------
Spin up a test 3-node cluster using Vagrant....
````
git clone https://github.com/mrlesmithjr/ansible-mariadb-galera-cluster.git
cd Vagrant
vagrant up
````
When you are done testing tear it all down....  
````
./cleanup.sh
````

Role Variables
--------------

[Role Defaults](./defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------


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
[MariaDB-Galera Cluster]: <https://mariadb.com/kb/en/mariadb/what-is-mariadb-galera-cluster/>
