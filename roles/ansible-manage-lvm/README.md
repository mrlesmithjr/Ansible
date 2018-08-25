# Role Name

An [Ansible] role to manage LVM Groups/Logical Volumes.

> NOTE: Can be used to create, extend or resize LVM Groups and volumes.

## Requirements

Devices/disks to be members of the LVM setup **must be** identified prior to
using this role.

> NOTE: Ensure that you select the correct devices/disks.
>
> NOTE: To create an LVM VG w/out creating LVM LVOLS...define lvname w/ var as
> `None` as in the below example.

## Role Variables

```yaml
---
# defaults file for ansible-manage-lvm
lvm_groups: []
  # - vgname: ubuntu-vg
  #   disks:
  #     - /dev/sda5
  #     - /dev/sdc
  #     - /dev/sdd
  #   # defines if VG should exist or be removed
  #   # true or false
  #   create: true
  #   lvnames:
  #     - lvname: swap_1
  #       # Define size of lvol
  #       # 100%FREE, 10g, 1024 (megabytes by default)
  #       size: 5g
  #       # Defines additional lvcreate options (e.g. stripes, stripesize, etc)
  #       opts: ''
  #       # Defines if lvol should exist or be removed
  #       # true or false
  #       create: true
  #       # Defines filesystem to format lvol as
  #       filesystem: swap
  #       # Defines if filesystem should be mounted
  #       mount: false
  #       # Defines mountpoint for lvol
  #       mntp: []
  #       # Defines additional mount options (e.g. noatime, noexec, etc)
  #       mopts: ''
  #     - lvname: root
  #       size: 40g
  #       create: true
  #       filesystem: ext4
  #       mount: true
  #       mntp: /
  # - vgname: test-vg
  #   disks:
  #     - /dev/sdb
  #   create: true
  #   lvnames:
  #     - lvname: test_1
  #       size: 5g
  #       create: true
  #       filesystem: ext4
  #       mount: true
  #       mntp: /mnt/test_1
  #     - lvname: test_2
  #       size: 10g
  #       create: true
  #       filesystem: ext4
  #       mount: true
  #       mntp: /mnt/test_2
  # - vgname: cinder-volumes
  #   disks:
  #     - /dev/cciss/c0d1
  #   create: true
  #   lvnames:
  #   # Set to None to only create LVM VG w/out creating LVM LVOLS
  #    - None

# Defines if LVM will be managed by role
# default is false to ensure nothing is changed by accident.
manage_lvm: false
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: test-nodes
  vars:
    lvm_groups:
      - vgname: test-vg
        disks:
          - /dev/sdb
          - /dev/sdc
        create: true
        lvnames:
          - lvname: test_1
            size: 5g
            create: true
            filesystem: ext4
            mount: true
            mntp: /mnt/test_1
          - lvname: test_2
            size: 10g
            create: true
            filesystem: ext4
            mount: true
            mntp: /mnt/test_2
    manage_lvm: true
    pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-manage-lvm
  tasks:
```

## License

BSD

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr]
-   <http://everythingshouldbevirtual.com>
-   mrlesmithjr [at] gmail.com

[@mrlesmithjr]: https://www.twitter.com/mrlesmithjr

[ansible]: https://www.ansible.com
