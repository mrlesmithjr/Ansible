<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-apt-sources](#ansible-apt-sources)
  - [Build status](#build-status)
  - [Role info](#role-info)
  - [Role purpose](#role-purpose)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-apt-sources

## Build status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-apt-sources.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-apt-sources)

## Role info

An [Ansible](https://www.ansible.com) role to configure `/etc/apt/sources.list`
on `Debian/Ubuntu` systems.

## Role purpose

The purpose of this role is to configure systems `/etc/apt/sources.list`
consistently or independently.

> NOTE: This role is **not** intended to manage repositories other than the
> distribution sources.

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-apt-sources
# deb or deb-src, indicates the type of archive
apt_sources_archive_types:
  - 'deb'
  - 'deb-src'

# main consists of DFSG-compliant packages, which do not rely on software
# outside this area to operate. These are the only packages considered part of
# the Debian distribution.
#
# contrib packages contain DFSG-compliant software, but have dependencies not
# in main (possibly packaged for Debian in non-free).
#
# non-free contains software that does not comply with the DFSG.
#
# Specific to Debian not Ubuntu
apt_sources_debian_components:
  - 'main'
  - 'contrib'
  - 'non-free'

# The release class (oldstable, stable, testing, unstable) respectively.
#
# Specific to Debian not Ubuntu
apt_sources_debian_distribution: 'stable'

# Specific to Debian not Ubuntu
apt_sources_debian_repository_url: 'http://deb.debian.org'

apt_sources_enable_backports: true

apt_sources_enable_proposed: false

apt_sources_enable_security: true

apt_sources_enable_updates: true

# Specific to Ubuntu not Debian
apt_sources_ubuntu_components:
  - 'main'
  - 'multiverse'
  - 'restricted'
  - 'universe'

# Specific to Ubuntu not Debian
apt_sources_ubuntu_repository_url: 'http://archive.ubuntu.com'
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: all
  vars:
  roles:
    - role: ansible-apt-sources
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
