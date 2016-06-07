Role Name
=========

An Ansible role to deploy an Ansible Inventory system using MySQL as the back-end.  

Intentions
----------
The intention of this role is to build a dynamic inventory system by leveraging  
Ansible gathered facts and storing those in the MySQL DB. This inventory system  
can be extended to provide for example...
- A dynamic inventory for Ansible
- Ability to drive additional tasks
  - Run Ansible playbooks based on hosts/groups and etc.
  - Become and Ansible module for manipulating data in MySQL (instead of raw shell commands)
  - Tie into CI/CD tools for integrations
  - Tie into logging systems (ELK) directly
  - Tie into Maintenance scheduling and notifications
  - Many other abilities

So think of this as a building block for something potentially bigger than  
collecting a bunch of Ansible facts. But giving the ability to tenants/users  
to take actions based on this collection of data.  

Does this make sense? Maybe, maybe not. I have a lot of thoughts in mind for  
this. But it may not make any sense to pursue. Time will tell. I am of course  
open to any input and contributions.  

My additional thought is to wrap possibly Django around the front-end.

Requirements
------------

Install required Ansible roles...  
````
ansible-galaxy install -r requirements.yml
````

Role Variables
--------------

````
---
# defaults file for ansible-inventory
inventory_db_name: 'ansible_inventory'  #Defines the Inventory DB Name
inventory_db_host: 'node0'  #Defines the inventory_hostname in which the Inventory DB is to reside
inventory_db_host_access:  #Defines the Host Access to the DB User
  - '127.0.0.1'
  - 'localhost'
  - '::1'
  - '{{ ansible_hostname }}'
  - '%'
inventory_db_user: 'ansible'  #Defines the Inventory DB User Name
inventory_db_password: 'ansible'  #Defines the Inventory DB User Password
inventory_group_vars:  #Define specific Ansible group vars to add
  - group: 'all'
    vars:
      - name: 'pri_domain_name'
        value: 'vagrant.local'
      - name: 'email_notifications'
        value: 'mrlesmithjr@gmail.com'
      - name: 'pri_dns'
        value: '8.8.8.8'
      - name: 'sec_dns'
        value: '8.8.4.4'
  - group: 'db-nodes'
    vars:
      - name: 'mysql_allow_remote_connections'
        value: 'true'
      - name: 'mysql_root_password'
        value: 'root'
inventory_groups:  #Define specific Ansible groups to define...All groups are discovered and added during scans as well
  - 'db-nodes'
  - 'elk-nodes'
  - 'openstack-nodes'
inventory_host_vars:  #Define any specific hostvars to add
  - host: 'node0'
    vars:
      - name: 'ansiblevar'
        value: 'ansibleval'
      - name: 'es_packetbeat_interface'
        value: 'eth0'
  - host: 'node2'
    vars:
      - name: 'es_packetbeat_interface'
        value: 'any'
inventory_hosts:  #Define hosts to be added to the inventory (ip is optional-if DNS works)
  - name: 'test-node-01'
    ip: '192.168.202.201'
  - name: 'test-node-02'
    ip: '192.168.202.202'
````

Dependencies
------------

None

Example Playbook
----------------
````
- hosts: db-nodes
  become: true
  vars:
    - mysql_allow_remote_connections: true
    - mysql_root_password: root
    - pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-apache2
    - role: ansible-mariadb-mysql
  tasks:

- hosts: all
  become: true
  vars:
    - pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-inventory
  tasks:
````
Example Ansible playbook execution
----------------------------------
Using the included python script (library/ansible_play.py) you can  
use the back-end DB for your dynamic inventory...
````
ansible-playbook -i library/ansible_play.py playbook.yml --list-hosts

playbook: playbook.yml

  play #1 (all): all	TAGS: []
    pattern: [u'all']
    hosts (5):
      node1
      node0
      node3
      node2
      node4

  play #2 (db-nodes): db-nodes	TAGS: []
    pattern: [u'db-nodes']
    hosts (1):
      node0

  play #3 (all): all	TAGS: []
    pattern: [u'all']
    hosts (5):
      node1
      node0
      node3
      node2
      node4

  play #4 (mixed-nodes): mixed-nodes	TAGS: []
    pattern: [u'mixed-nodes']
    hosts (3):
      node1
      node2
      node4

  play #5 (all): all	TAGS: []
    pattern: [u'all']
    hosts (5):
      node1
      node0
      node3
      node2
      node4
````
To view the contents of the dynamic inventory...
````
./library/ansible_play.py                                      
{
  "all": {
    "hosts": [
      "node2",
      "node0",
      "node1",
      "node4",
      "node3",
      "test-node-01",
      "test-node-02"
    ],
    "vars": {
      "sec_dns": "8.8.4.4",
      "pri_domain_name": "vagrant.local",
      "pri_dns": "8.8.8.8",
      "email_notifications": "mrlesmithjr@gmail.com"
    }
  },
  "_meta": {
    "hostvars": {
      "node1": {
        "ansible_ssh_host": "172.28.128.4"
      },
      "node0": {
        "ansible_ssh_host": "172.28.128.3",
        "es_packetbeat_interface": "eth0",
        "parentvar": {
          "childvar": "childval"
        },
        "ansiblevar": "ansibleval"
      },
      "node3": {
        "ansible_ssh_host": "172.28.128.6"
      },
      "node2": {
        "ansible_ssh_host": "172.28.128.5",
        "es_packetbeat_interface": "any"
      },
      "node4": {
        "ansible_ssh_host": "172.28.128.7",
        "SNMP_Communities": {
          "Allowed_From": "10.0.0.0/24",
          "community": "Public"
        }
      }
    }
  },
  "db-nodes": {
    "hosts": [
      "node0"
    ],
    "vars": {
      "mysql_root_password": "root",
      "mysql_allow_remote_connections": "true"
    }
  },
  "renamed-nodes": {
    "hosts": [
      "node1"
    ]
  },
  "mixed-nodes": {
    "hosts": [
      "node1",
      "node4"
    ]
  },
  "ungrouped": {
    "hosts": [
      "node2"
    ]
  },
  "test-nodes": {
    "hosts": [
      "node3"
    ]
  },
  "random-nodes": {
    "hosts": [
      "node4"
    ]
  }
}
````

Example Queries
---------------
Using the included python script (library/ansible_inventory.py) to execute  
queries.

````
library/ansible_inventory.py
````

Show script help..
````
ansible_inventory.py -h
````
````
usage: ansible_inventory.py [-h] [--dbhost DBHOST] [--dbname DBNAME]
                            --dbpassword DBPASSWORD --dbuser DBUSER
                            [--group GROUP] [--host HOST]
                            {queryall,queryallgroups,queryallhosts,querygroup,queryhost,queryhostdetails}

Ansible Inventory...

positional arguments:
  {queryall,queryallgroups,queryallhosts,querygroup,queryhost,queryhostdetails}
                        Define action to take

optional arguments:
  -h, --help            show this help message and exit
  --dbhost DBHOST       Database Host, [default: 127.0.0.1]
  --dbname DBNAME       Database Name, [default: ansible_inventory]
  --dbpassword DBPASSWORD
                        Database Password
  --dbuser DBUSER       Database User
  --group GROUP         Query Group, Define Group to Query
  --host HOST           Query Host, Define Host to Query
````
Query all groups...
````
ansible_inventory.py queryallgroups --dbuser ansible --dbpassword ansible
````
````
[
    {
        "group_names": "all"
    },
    {
        "group_names": "db-nodes"
    },
    {
        "group_names": "elk-nodes"
    },
    {
        "group_names": "mixed-nodes"
    },
    {
        "group_names": "openstack-nodes"
    },
    {
        "group_names": "random-nodes"
    },
    {
        "group_names": "renamed-nodes"
    },
    {
        "group_names": "test-nodes"
    },
    {
        "group_names": "ungrouped"
    }
]
````
Query all hosts...
````
ansible_inventory.py queryallhosts --dbuser ansible --dbpassword ansible
````
````
[
    {
        "inventory_hostname": "jumpbox"
    },
    {
        "inventory_hostname": "node0"
    },
    {
        "inventory_hostname": "node1"
    },
    {
        "inventory_hostname": "node2"
    },
    {
        "inventory_hostname": "node3"
    },
    {
        "inventory_hostname": "node4"
    },
    {
        "inventory_hostname": "smtp"
    },
    {
        "inventory_hostname": "test-node-01"
    },
    {
        "inventory_hostname": "test-node-02"
    }
]
````
Query a specific group...
````
ansible_inventory.py querygroup --dbuser ansible --dbpassword ansible --group mixed-nodes
````
````
[
    {
        "ansible_hostname": "node1",
        "ansible_ssh_host": "172.28.128.10",
        "inventory_hostname": "node1",
        "group_names": "mixed-nodes"
    },
    {
        "ansible_hostname": "node4",
        "ansible_ssh_host": "172.28.128.13",
        "inventory_hostname": "node4",
        "group_names": "mixed-nodes"
    }
]
````
Query a specific host...
````
ansible_inventory.py queryhost --dbuser ansible --dbpassword ansible --host node1
````
````
[
    {
        "ansible_hostname": "node1",
        "ansible_ssh_host": "172.28.128.10",
        "inventory_hostname": "node1",
        "group_names": "all"
    },
    {
        "ansible_hostname": "node1",
        "ansible_ssh_host": "172.28.128.10",
        "inventory_hostname": "node1",
        "group_names": "mixed-nodes"
    },
    {
        "ansible_hostname": "node1",
        "ansible_ssh_host": "172.28.128.10",
        "inventory_hostname": "node1",
        "group_names": "renamed-nodes"
    }
]
````
Query a specific host for all details...
````
ansible_inventory.py queryhostdetails --dbuser ansible --dbpassword ansible --host node1
````
````
[
    {
        "ansible_default_ipv4.macaddress": "08:00:27:55:7c:f9",
        "ansible_distribution_version": "14.04",
        "ansible_virtualization_type": "virtualbox",
        "ansible_processor_cores": 1,
        "ansible_default_ipv4.interface": "eth0",
        "ansible_default_ipv4.gateway": "10.0.2.2",
        "ansible_bios_version": "VirtualBox",
        "ansible_processor": "GenuineIntelIntel(R) Core(TM) i7-4870HQ CPU @ 2.50GHz",
        "ansible_default_ipv4.netmask": "255.255.255.0",
        "ansible_memtotal_mb": 489,
        "ansible_architecture": "x86_64",
        "ansible_ssh_host": "172.28.128.10",
        "ansible_swapfree_mb": 510,
        "HostDetailsId": 3,
        "ansible_distribution_release": "trusty",
        "ansible_system_vendor": "innotek GmbH",
        "ansible_os_family": "Debian",
        "ansible_swaptotal_mb": 511,
        "ansible_product_name": "VirtualBox",
        "ansible_memfree_mb": 95,
        "ansible_distribution": "Ubuntu",
        "HostId": 3,
        "ansible_processor_count": 1,
        "ansible_hostname": "node1",
        "ansible_bios_date": "12/01/2006",
        "ansible_date_time.tz": "EDT",
        "LastUpdateTime": "2016-06-05T00:40:11",
        "ansible_kernel": "4.2.0-30-generic",
        "ansible_fqdn": "node1",
        "ansible_default_ipv4.address": "10.0.2.15",
        "ansible_nodename": "node1"
    }
]
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
