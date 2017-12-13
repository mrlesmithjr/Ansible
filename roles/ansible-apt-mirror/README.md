<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-apt-mirror](#ansible-apt-mirror)
  - [Requirements](#requirements)
  - [Vagrant](#vagrant)
  - [Docker](#docker)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-apt-mirror

Installs and configures apt-mirror (Local APT Repository).
Also configures clients if extra-var passed.

## Requirements

Lot's of disk space required for repos...At the time of putting this together
Ubuntu Trusty w/defaults in this role requires 139GB+

Install Ansible role requirements:

```bash
sudo ansible-galaxy install -r requirements.yml -f
```

## Vagrant

Spin up Environment under Vagrant to test.

```bash
vagrant up
```

## Docker

Spin up Docker container (apt mirror repos not populated...will update on cron schedule)

```bash
docker run -d -p 80:80 --name apt-mirror mrlesmithjr/apt-mirror
```

To immediately update cache (Will take a long time...so do not cancel)

```bash
docker exec -it apt-mirror apt-mirror
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

ansible-apache2 and mrlesmithjr.apache2 (Installed as part of requirements.yml)

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: ansible-apache2
    - role: ansible-apt-mirror

- hosts: clients
  roles:
    - { role: ansible-apt-mirror, apt_mirror_client: true }
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
