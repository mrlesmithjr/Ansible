Role Name
=========

An [Ansible] role to install various [Hashicorp] utilities

- [consul]
- [nomad]
- [packer]
- [terraform]
- [vagrant]
- [vault]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-hashicorp-toolbox.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-hashicorp-toolbox)

Requirements
------------

None

Vagrant
-------

You can spin up a Vagrant box and test all of these tools out without
installing anywhere as well.
```
vagrant up
```

Role Variables
--------------

```
---
# defaults file for ansible-hashicorp-toolbox
hashicorp_install_dir: /usr/local/bin/
hashicorp_tools:
  - name: 'consul'
    version: '0.8.1'
    state: 'present'
  - name: 'nomad'
    version: '0.5.6'
    state: 'present'
  - name: 'packer'
    version: '1.0.0'
    state: 'present'
  # - name: serf
  #   version: 0.7.0
  #   state: present
  - name: 'terraform'
    version: '0.9.3'
    state: 'present'
    #Debian package
  - name: 'vagrant'
    version: '1.9.3'
    state: 'present'
  - name: 'vault'
    version: '0.7.0'
    state: 'present'
hashicorp_url: 'https://releases.hashicorp.com'
```
Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-hashicorp-toolbox
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[consul]: <https://www.consul.io/>
[nomad]: <https://www.nomadproject.io/>
[packer]: <https://www.packer.io/>
[terraform]: <https://www.terraform.io/>
[vagrant]: <https://www.vagrantup.com/>
[vault]: <https://www.vaultproject.io/>
[Ansible]: <https://www.ansible.com>
[Hashicorp]: <https://hashicorp.com/>
