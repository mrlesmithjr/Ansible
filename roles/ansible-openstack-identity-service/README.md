<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-openstack-identity-service](#ansible-openstack-identity-service)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
        -   [Ansible Roles](#ansible-roles)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-openstack-identity-service

An [Ansible](https://www.ansible.com) role to install/configure [OpenStack Identity Services](https://docs.openstack.org/ocata/install-guide-ubuntu/common/get-started-identity.html)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-openstack-identity-service

# Defines the default OpenStack admin user info
# Generate password with:
# openssl rand -hex 10
openstack_identity_service_admin_info:
  pass: '{{ openstack_identity_service_admin_pass }}'
  user: 'admin'
  admin_url: '{{ openstack_identity_service_keystone_endpoint_url }}:35357/v3/'
  internal_url: '{{ openstack_identity_service_keystone_endpoint_url }}:5000/v3/'
  public_url: '{{ openstack_identity_service_keystone_endpoint_url }}:5000/v3/'
  region_id: 'RegionOne'

# Define admin pass
openstack_identity_service_admin_pass: []

# HA info
## Define as true if using HA
openstack_identity_service_ha: false
## Define host which should be identified as HA master
openstack_identity_service_ha_master: 'controller01'

# Defines Keystone DB info
openstack_identity_service_keystone_db_info:
  db: 'keystone'
  pass: 'keystone'
  host: 'localhost'
  user: 'keystone'

# Defines the default Keystone endpoint url
# Do not append the port or api version
openstack_identity_service_keystone_endpoint_url: 'http://{{ inventory_hostname }}'

# Management IP Info
openstack_identity_service_management_interface: 'enp0s8'
openstack_identity_service_management_ip: "{{ hostvars[inventory_hostname]['ansible_'+openstack_compute_service_compute_management_interface]['ipv4']['address'] }}"

# RabbitMQ Connection Info
openstack_identity_service_rabbit_hosts:
  - 127.0.0.1
openstack_identity_service_rabbit_pass: 'openstack'
openstack_identity_service_rabbit_user: 'openstack'
```

## Dependencies

### Ansible Roles

The following [Ansible](https://www.ansible.com) roles are required as part of
this role.

-   [ansible-chrony](https://github.com/mrlesmithjr/ansible-chrony)
-   [ansible-config-interfaces](https://github.com/mrlesmithjr/ansible-config-interfaces)
-   [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)
-   [ansible-memcached](https://github.com/mrlesmithjr/ansible-memcached)
-   [ansible-mysql](https://github.com/mrlesmithjr/ansible-mysql)
-   [ansible-openstack-base](https://github.com/mrlesmithjr/ansible-openstack-base)
-   [ansible-openstack-openrc](https://github.com/mrlesmithjr/ansible-openstack-openrc)
-   [ansible-rabbitmq](https://github.com/mrlesmithjr/ansible-rabbitmq)

The above roles can be installed using `ansible-galaxy` along with [requirements.yml](./requirements.yml):

```bash
ansible-galaxy install -r requirements.yml
```

## Example Playbook

[Example Playbook](./playbook.yml)

## To-Do

-   [ ] Implement Fernet keys
-   [ ] Finish example playbook
-   [ ] Provide usable variables for example playbook
    -   [ ] vars file?
    -   [ ] group_vars?

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
    ail.com
    .com
        ail.com
