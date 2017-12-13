<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-django](#ansible-django)
  - [Requirements](#requirements)
  - [Vagrant](#vagrant)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-django

An [Ansible](https://www.ansible.com) role to install [Django](https://www.djangoproject.com)
web framework

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-django.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-django)

## Requirements

None

## Vagrant

Spin up Environment under Vagrant to test.

```bash
vagrant up
```

## Role Variables

```yaml
---
# defaults file for ansible-django

# defines DB type to use...sqlite or mysql
django_db_type: sqlite

# Defines django version to install. set to latest for the latest version or
# use version number...ex. (1.8.7, 1.8.8, 1.9, 1.9.1)
django_version: latest
```

## Dependencies

Install required dependencies as below:

```bash
sudo ansible-galaxy install -r requirements.yml
```

## Example Playbook

```yaml
---
- name: Install Django
  hosts: all
  sudo: true
  vars:
  roles:
    - role: ansible-django
    - role: ansible-mysql
      when: >
            (django_db_type is defined and django_db_type == "mysql")
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
