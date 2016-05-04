Role Name
=========

Installs Jekyll https://jekyllrb.com/

Transform your plain text into static websites and blogs.

Requirements
------------

Install Jekyll role
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Docker
------
Spin up Docker container for testing (With NGINX)
````
docker run -d -p 80:80 -p 4000:4000 mrlesmithjr/jekyll
````

Test-Site
---------
In order to just test out Jekyll you can do the following either in Docker container or Vagrant Box.
````
cd ~
jekyll new test-site
cd test-site
jekyll build
sudo cp -R _site/* /usr/share/nginx/html
````
Using your browser:
###### Vagrant
http://localhost:8080
###### Docker
http://localhost:80

Role Variables
--------------

````
---
# defaults file for ansible-jekyll
jekyll_importers:  #define specific gems required to be installed for the specific importer type
  - name: wordpress
    gems:
      - unidecode
      - sequel
      - mysql2
      - htmlentities
````

Dependencies
------------

ansible-nginx (Installed as part of requirements.yml)

Example Playbook
----------------

###### Galaxy
    - hosts: servers
      roles:
         - role: mrlesmithjr.jekyll

###### GitHub
    - hosts: servers
      roles:
        - role: ansible-jekyll

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
