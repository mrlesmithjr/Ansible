Role Name
=========

Installs Redis http://redis.io/

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-redis
redis_allow_remote_connections: false  #defines if redis should allow connections on all interfaces
redis_enable_tweaks: false  #Defines if redis related tweaks should be enabled
````

Dependencies
------------

None

Example Playbook
----------------

````
---
- hosts: all
  become: true
  vars:
  roles:
    - ansible-redis
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
