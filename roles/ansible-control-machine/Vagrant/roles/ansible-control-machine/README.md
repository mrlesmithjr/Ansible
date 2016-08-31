Role Name
=========

An Ansible role to configure an Ansible Control Machine  
Installs the following versions of Ansible in Python virtual environments..

`1.9.4`
`1.9.5`
`1.9.6`
`2.0.0.1`
`2.0.0.2`
`2.0.1.0`
`2.0.2.0`
`2.1.0.0`
`2.1.1.0`

Requirements
------------

Python `2.x` `MUST` be installed on the following (Until Ansible supports Python `3.x`)...

`Fedora 23+`
```
sudo dnf -y install python-devel python-dnf
sudo dnf -y group install "C Development Tools and Libraries"
```

`Ubuntu 15.04+`
```
sudo apt-get -y install python-simplejson
```

Role Variables
--------------

```
---
# defaults file for ansible-control-machine
ansible_playbooks:
  - repo: 'https://github.com/mrlesmithjr/ansible-playbooks.git'
    dest: 'mrlesmithjr'
ansible_playbooks_dir: '/opt/playbooks'
ansible_roles:
  - repo: 'https://github.com/mrlesmithjr/ansible-base.git'
    dest: 'ansible-base'
  - repo: 'https://github.com/mrlesmithjr/ansible-bootstrap.git'
    dest: 'ansible-bootstrap'
  - repo: 'https://github.com/mrlesmithjr/ansible-manage-ssh-keys.git'
    dest: 'ansible-manage-ssh-keys'
  - repo: 'https://github.com/mrlesmithjr/ansible-ntp.git'
    dest: 'ansible-ntp'
  - repo: 'https://github.com/mrlesmithjr/ansible-postfix.git'
    dest: 'ansible-postfix'
  - repo: 'https://github.com/mrlesmithjr/ansible-rsyslog.git'
    dest: 'ansible-rsyslog'
ansible_roles_dir: '/etc/ansible/roles'
ansible_versions:
  - ver: '1.9.4'
    addl_modules: []
  - ver: '1.9.5'
    addl_modules: []
  - ver: '1.9.6'
    addl_modules:
      - 'ndg-httpsclient'
      - 'pyasn1'
      - 'pyopenssl'
      - 'pysphere'
      - 'pyvmomi'
  - ver: '2.0.0.1'
    addl_modules: []
  - ver: '2.0.0.2'
    addl_modules: []
  - ver: '2.0.1.0'
    addl_modules: []
  - ver: '2.0.2.0'
    addl_modules: []
  - ver: '2.1.0.0'
    addl_modules:
      - 'ndg-httpsclient'
      - 'pyasn1'
      - 'pyopenssl'
      - 'pysphere'
      - 'pyvmomi'
  - ver: '2.1.1.0'
    addl_modules:
      - 'ndg-httpsclient'
      - 'pyasn1'
      - 'pyopenssl'
      - 'pysphere'
      - 'pyvmomi'
ansible_virtualenv_dir: '/opt/ansible_virtualenvs'
easy_install_pip: false
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
    - role: ansible-control-machine
  tasks:
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
