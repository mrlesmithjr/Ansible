<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-nfs-client](#ansible-nfs-client)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-nfs-client

An [Ansible](https://www.ansible.com) role to install/configure an NFS Client

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-nfs-client
nfs_client_mounts: []
  # - mount:
  #   fstype: 'nfs'
  #   opts:
  #     - 'rsize=8192'
  #     - 'wsize=8192'
  #     - 'intr'
  #   path: '/opt/nfs/test1'
  #   src: '192.168.250.10:/opt/nfs/test1'
  #   state: 'mounted'
  # - mount:
  #   fstype: 'nfs'
  #   opts:
  #     - 'rsize=8192'
  #     - 'wsize=8192'
  #     - 'intr'
  #   path: '/opt/nfs/test2'
  #   src: '192.168.250.10:/opt/nfs/test2'
  #   state: 'mounted'
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: nfs_client
  vars:
  roles:
    - role: ansible-nfs-client
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
