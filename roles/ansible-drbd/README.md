<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-drbd](#ansible-drbd)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-drbd

An [Ansible](https://www.ansible.com) role to install/configure [DRBD](https://docs.linbit.com/)

> NOTE: This role by default installs/configures [heartbeat](http://www.linux-ha.org/wiki/Heartbeat)
> to provide HA for DRBD. This may change at some point to use [Pacemaker](https://www.clusterlabs.org/)
> rather than `heartbeat`. But for simple DRBD setups `heartbeat` is sufficient
> and much easier to setup. If you are interested in an `Ansible` Pacemaker role,
> I have [ansible-pacemaker](https://github.com/mrlesmithjr/ansible-pacemaker).

## Requirements

The following requirements are needed for this role:

-   Unpartitioned disk
-   VIP

The additional required roles are included in [requirements.yml](requirements.yml)
which can be installed using `ansible-galaxy`:

```bash
ansible-galaxy install -r requirements.yml
```

## Role Variables

```yaml
---
# defaults file for ansible-drbd

drbd_disks:
  - device: /dev/drbd0
    disk: /dev/sdb
    filesystem: ext4
    partitions: 1
    mountpoint: /opt/nfs
    resource: r0
    state: present
    use_partition: /dev/sdb1

drbd_group: test_nodes

drbd_interface: enp0s8

drbd_network_shared_secret: wXE8MqVa

drbd_vip: 192.168.250.100
```

## Dependencies

-   [ansible-ntp](https://github.com/mrlesmithjr/ansible-ntp)
-   [ansible-etc-hosts](https://github.com/mrlesmithjr/ansible-etc-hosts)

## Example Playbook

```yaml
---
- hosts: test_nodes
  vars:
    etc_hosts_add_all_hosts: true
    pri_domain_name: test.vagrant.local
  roles:
    - role: ansible-ntp
    - role: ansible-etc-hosts
    - role: ansible-drbd
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
