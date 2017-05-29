Role Name
=========

An [Ansible] role to install [KVM]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-kvm.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-kvm)

Requirements
------------

Install [required](./requirements.yml) [Ansible] roles:
```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------

[Role Defaults](defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: kvm_hosts
  become: true
  vars:
  roles:
    - role: ansible-kvm
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

[Ansible]: <https://www.ansible.com>
[KVM]: <https://www.linux-kvm.org/page/Main_Page>
