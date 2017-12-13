<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-openstack-networking-service-compute](#ansible-openstack-networking-service-compute)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
    - [Ansible Roles](#ansible-roles)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-openstack-networking-service-compute

An [Ansible](https://www.ansible.com) role to install/configure
[OpenStack Networking Service Compute](https://docs.openstack.org/ocata/install-guide-ubuntu/neutron-compute-install.html)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-openstack-networking-service-compute

# keystone_authtoken
openstack_networking_service_compute_keystone_authtoken:
  auth_type: 'password'
  auth_uri: '{{ openstack_networking_service_compute_keystone_service_endpoint_url }}:5000'
  auth_url: '{{ openstack_networking_service_compute_keystone_service_endpoint_url }}:35357'
  memcached_servers: '{{ openstack_networking_service_compute_memcached_servers }}'
  password: "{{ openstack_networking_service_compute_neutron_user_info['password'] }}"
  project_domain_name: "{{ openstack_networking_service_compute_neutron_user_info['domain_id'] }}"
  project_name: "{{ openstack_networking_service_compute_neutron_user_info['project'] }}"
  user_domain_name: "{{ openstack_networking_service_compute_neutron_user_info['domain_id'] }}"
  username: "{{ openstack_networking_service_compute_neutron_user_info['name'] }}"

# Defines the default Keystone endpoint url
# Do not append the port or api version
openstack_networking_service_compute_keystone_service_endpoint_url: 'http://{{ inventory_hostname }}'

# Management IP Info
openstack_networking_service_compute_management_interface: 'enp0s8'
openstack_networking_service_compute_management_ip: "{{ hostvars[inventory_hostname]['ansible_'+openstack_compute_service_compute_management_interface]['ipv4']['address'] }}"

# Define memcached servers
openstack_networking_service_compute_memcached_servers:
  - 127.0.0.1

# Neutron info
## Define Neutron user info
openstack_networking_service_compute_neutron_user_info:
  description: 'Neutron user'
  domain_id: 'default'
  enabled: true
  name: 'neutron'
  # Generate with openssl rand -hex 10
  password: '{{ openstack_networking_service_compute_neutron_user_pass }}'
  project: 'service'
  role: 'admin'
  state: 'present'

## Define Neutron user password
openstack_networking_service_compute_neutron_user_pass: []

# Provider network info
openstack_networking_service_compute_provider_interface: 'enp0s9'

# RabbitMQ connection info
openstack_networking_service_compute_rabbit_hosts:
  - 127.0.0.1
openstack_networking_service_compute_rabbit_pass: 'openstack'
openstack_networking_service_compute_rabbit_user: 'openstack'
```

## Dependencies

### Ansible Roles

The following [Ansible](https://www.ansible.com) roles are required as part of
this role.

-   [ansible-chrony](https://github.com/mrlesmithjr/ansible-chrony)
-   [ansible-config-interfaces](https://github.com/mrlesmithjr/ansible-config-interfaces)
-   [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)
-   [ansible-openstack-base](https://github.com/mrlesmithjr/ansible-openstack-base)
-   [ansible-openstack-compute-service-compute](https://github.com/mrlesmithjr/ansible-openstack-compute-service-compute)
-   [ansible-openstack-openrc](https://github.com/mrlesmithjr/ansible-openstack-openrc)

The above roles can be installed using `ansible-galaxy` along with [requirements.yml](./requirements.yml):

```bash
ansible-galaxy install -r requirements.yml
```

## Example Playbook

[Example Playbook](./playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
