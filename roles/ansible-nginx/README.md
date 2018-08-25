<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [ansible-nginx](#ansible-nginx)
    -   [Build Status](#build-status)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-nginx

An [Ansible](https://www.ansible) role to install/configure [NGINX](http://nginx.org)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-nginx.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-nginx)

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-nginx
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
