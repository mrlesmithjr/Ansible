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

drbd_common:
  disk: ''
  net: |
    cram-hmac-alg sha1;
    shared-secret "{{ drbd_network_shared_secret }}";
  handlers: ''
  startup: ''
  options: ''

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

Additional variables include

```
drbd_use_heartbeat: true
drbd_use_parted: true
```

## Platform Specific Notes

Debian Stretch and Ubuntu Xenial contains DRBD in kernel, and supports Heartbeat.  They have the most out of the box support for the defaults.

DRBD packages for CentOS can be built from [linbit](https://www.linbit.com), or from [ELREPO](http://elrepo.org/) repository. These should be included in the `drbd_rpm_packages` list.  See vagrant-box-templates `playbook.yml` examples below.

Heartbeat is available for CentOS6, but not for CentOS7.  Heartbeat is now optional through a toggle `drbd_use_heartbeat`. You will be required to handle reboots and failover by other means. Toggle is `true` by default.

The behaviour of loop disk partitions is has only become more consistent in later linux distributions. To maintain compatibility, the option to toggle off parted `drbd_use_parted` is provided. Toggle is `true` by default.

## Unicast Mode

For platforms supporting Heartbeat, but not multi-cast UDP, we support a toggle for unicast support. Toggle is `false` by default.

```
drbd_unicast_mode: true
drbd_unicast_port: 694
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

## Testing

Testing makes use of [vagrant-box-templates](https://github.com/mrlesmithjr/vagrant-box-templates.git), where the following systems have been tested.

* CentOS6 / CentOS7
* Debian stretch64
* Ubuntu xenial64

The `nodes.yml` and `playbook.yml` files have been included as working examples. See the `tests/` directory for further information.

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
