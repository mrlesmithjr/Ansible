<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-openstack-openrc](#ansible-openstack-openrc)
  - [Info](#info)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-openstack-openrc

An [Ansible](https://www.ansible.com) role to configure [OpenStack](https://www.openstack.org/)
`openrc` and `clouds.yaml` files to use for management.

## Info

-   [openrc](https://docs.openstack.org/user-guide/common/cli-set-environment-variables-using-openstack-rc.html)
-   [clouds.yaml](https://docs.openstack.org/developer/os-client-config/)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-openstack-openrc

# Define openrc clouds definitions
# These will be used to generate the following:
# $HOME/username-openrc
# $HOME/.config/openstack/clouds.yaml
#
# Generate passwords using:
# openssl rand -hex 10
openstack_openrc_clouds:
  - name: 'default'
    auth_url: 'http://127.0.0.1:35357/v3'
    endpoint_type: 'internalURL'
    identity_api_version: 3
    interface: 'internal'
    password: []
    project_domain_name: 'Default'
    project_name: 'admin'
    region_name: 'RegionOne'
    tenant_name: 'admin'
    user_domain_name: 'Default'
    username: 'admin'
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: openstack
  vars:
  roles:
    - role: ansible-openstack-openrc
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
