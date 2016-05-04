Role Name
=========

Installs various Hashicorp utilities https://hashicorp.com/

Requirements
------------

None

Vagrant
-------

You can spin up a Vagrant box and test all of these tools out without installing anywhere as well.
````
vagrant up
````

Role Variables
--------------

````
---
# defaults file for ansible-hashicorp-toolbelt
hashicorp_install_dir: /usr/local/bin/
hashicorp_tools:
  - name: nomad
    version: 0.2.3
    state: present
  - name: otto
    version: 0.2.0
    state: present
  - name: packer
    version: 0.8.6
    state: present
  - name: terraform
    version: 0.6.9
    state: present
  - name: vagrant  #Debian package
    version: 1.8.1
    state: present
  - name: vault
    version: 0.4.0
    state: present
hashicorp_url: https://releases.hashicorp.com
````

Dependencies
------------

None

Example Playbook
----------------

#### GitHub
````
- hosts: desktops
  sudo: true
  vars:
  roles:
    - role: ansible-hashicorp-toolbox
  tasks:
````

#### Galaxy
````
- hosts: desktops
  sudo: true
  vars:
  roles:
    - role: mrlesmithjr.hashicorp-toolbox
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
