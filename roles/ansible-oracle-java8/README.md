Role Name
=========

Installs Oracle Java8

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-oracle-java8
oracle_java8_debian_repo: 'ppa:webupd8team/java'
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
    - role: ansible-oracle-java8
  tasks:
````
#### Galaxy
````
---
- hosts: all
  become: true
  vars:
  roles:
    - role: mrlesmithjr.oracle-java8
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
