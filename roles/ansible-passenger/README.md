Role Name
=========

Installs Phusion Passenger for Apache2 and/or NGINX https://www.phusionpassenger.com

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-passenger
passenger_debian_repo_key: '561F9B9CAC40B2F7'
passenger_debian_repo_keyserver: 'hkp://keyserver.ubuntu.com:80'
passenger_debian_repo: 'deb https://oss-binaries.phusionpassenger.com/apt/passenger {{ ansible_distribution_release }} main'
passenger_webserver: 'apache2'  #defines webserver type....apache2 or nginx
````

Dependencies
------------

#### Apache2
````
ansible-apache2
mrlesmithjr.apache2
````
#### NGINX
````
ansible-nginx
mrlesmithjr.nginx
````
You can install dependencies as follows:
````
sudo ansible-galaxy install -r requirements.yml -f
````

Example Playbook
----------------

#### GitHub
````
- hosts: all
  become: true
  vars:
    - passenger_webserver: apache2
  roles:
    - role: ansible-apache2
      when: passenger_webserver == "apache2"
    - role: ansible-nginx
      when: passenger_webserver == "nginx"
  tasks:
````
#### Galaxy
````
- hosts: all
  become: true
  vars:
    - passenger_webserver: apache2
  roles:
    - role: mrlesmithjr.apache2
      when: passenger_webserver == "apache2"
    - role: mrlesmithjr.nginx
      when: passenger_webserver == "nginx"
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
