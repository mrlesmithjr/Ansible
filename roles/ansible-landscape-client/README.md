<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-landscape-client](#ansible-landscape-client)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-landscape-client

An [Ansible](https://www.ansible.com) role to install/configure [Canonical Landscape Client](https://landscape.canonical.com/)

## Requirements

A fully configured and ready to accept clients Landscape App Deployment. An
[Ansible](https://www.ansible.com) role ready for use: [ansible-landscape-app](https://github.com/mrlesmithjr/ansible-landscape-app).

## Role Variables

```yaml
---
# defaults file for ansible-landscape-client

# Landscape App Info
## Define below if using https://github.com/mrlesmithjr/ansible-landscape-app to
## deploy Landscape App
### define landscape primary app server
landscape_client_app_server: "{{ groups['landscape_app'][0] }}"
### defines server cert on client which will be created
landscape_client_app_server_cert: '/etc/landscape/server.pem'
### defines if client should be configured as being managed by an internal
### Landscape App Server
landscape_client_app_server_config: false
### defines the ssl cert on the primary app server which should be captured
### and copied to the client
landscape_client_app_ssl_cert_file: '/etc/ssl/certs/ssl-cert-snakeoil.pem'


landscape_client_data_path: '/var/lib/landscape/client'
landscape_client_log_level: 'info'
landscape_client_ping_url: 'http://landscape.canonical.com/ping'
landscape_client_url: 'https://landscape.canonical.com/message-system'
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: landscape_clients
  vars:
    landscape_client_ping_url: 'http://node2.{{ pri_domain_name }}/ping'
    landscape_client_url: 'https://node2.{{ pri_domain_name }}/message-system'
    pri_domain_name: 'vagrant.local'
  roles:
    - role: ansible-landscape-client
      tags:
        - 'landscape_client'
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
