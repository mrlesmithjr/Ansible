<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-openstack-base](#ansible-openstack-base)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-openstack-base

An [Ansible](https://www.ansible.com) role to install [OpenStack](https://www.openstack.org/)
base components.

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-openstack-base

openstack_base_pre_reqs:
  - 'python-dev'
  - 'python-pip'
  - 'python-setuptools'
  - 'software-properties-common'
  - 'ubuntu-cloud-keyring'

openstack_base_release: 'ocata'

openstack_base_repo: 'deb http://ubuntu-cloud.archive.canonical.com/{{ ansible_distribution| lower }} {{ ansible_distribution_release| lower }}-updates/{{ openstack_base_release }} main'
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: openstack
  vars:
  roles:
    - role: ansible-openstack-base
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
