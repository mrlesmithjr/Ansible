<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-grafana](#ansible-grafana)
  - [Requirements](#requirements)
  - [Information](#information)
  - [Vagrant](#vagrant)
  - [Usage](#usage)
      - [Vagrant](#vagrant-1)
      - [Non-Vagrant](#non-vagrant)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-grafana

An [Ansible](https://www.ansible.com) role to install/configure [Grafana](https://grafana.com/)

## Requirements

Install all Ansible role requirements.

```bash
sudo ansible-galaxy install -r requirements.yml -f
```

## Information

Example dashboards are included in `dashboards/`. I would love to see some others
being added via PR's!

## Vagrant

Spin up Environment under Vagrant to test.

```bash
vagrant up
```

## Usage

```yaml
username: admin
password: admin
```

#### Vagrant

<http://127.0.0.1:3000>

#### Non-Vagrant

<http://iporhostname:3000>

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

Reference [Requirements](#Requirements)

## Example Playbook

```yaml
---
- name: provisions grafana
  hosts: all
  become: true
  vars:
  roles:
    - role: ansible-collectd
    - role: ansible-snmpd
    - role: ansible-timezone
    - role: ansible-grafana
    - role: ansible-graphite
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
