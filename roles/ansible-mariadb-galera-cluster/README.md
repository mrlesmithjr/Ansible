<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-mariadb-galera-cluster](#ansible-mariadb-galera-cluster)
    -   [Build Status](#build-status)
    -   [Requirements](#requirements)
    -   [Vagrant](#vagrant)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
        -   [Ansible roles](#ansible-roles)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-mariadb-galera-cluster

An [Ansible](https://www.ansible.com) role to install/configure a [MariaDB-Galera Cluster](https://mariadb.com/kb/en/mariadb/what-is-mariadb-galera-cluster/)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-mariadb-galera-cluster.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-mariadb-galera-cluster)

## Requirements

None

## Vagrant

Spin up a test 3-node cluster using Vagrant....

```bash
git clone https://github.com/mrlesmithjr/ansible-mariadb-galera-cluster.git
cd Vagrant
vagrant up
```

When you are done testing tear it all down....

```bash
./cleanup.sh
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

### Ansible roles

-   [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)

## Example Playbook

[Example playbook](./playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

-   @mrlesmithjr
-   <http://everythingshouldbevirtual.com>
-   mrlesmithjr [at] gmail.com
