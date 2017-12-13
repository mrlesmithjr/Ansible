<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-nfs-server](#ansible-nfs-server)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-nfs-server

An [Ansible](https://www.ansible.com) role to install/configure an NFS Server

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-nfs-server

# Define export info
## Define any exports to be available to clients
##
### hostname
#### define by hostname, fqdn, ip address, ip subnet or * for all
####
### options
#### define any options or leave commented out
####
### mode
#### define the folder permissions to set which also apply to client mounts
nfs_server_exports: []
  # - export:
  #   access:
  #     # - hostname: '172.16.24.0/24'
  #     #   options:
  #     #     - 'ro'
  #     #     - 'sync'
  #     #     - 'no_subtree_check'
  #     #     - 'no_root_squash'
  #     - hostname: '192.168.250.0/24'
  #       options:
  #         - 'rw'
  #         - 'sync'
  #         - 'no_subtree_check'
  #         - 'no_root_squash'
  #   mode: "u=rwx,g=rx,o=rx"
  #   path: '/opt/nfs/test1'
  # - export:
  #   access:
  #     - hostname: '*'
  #       options:
  #         - 'rw'
  #         - 'sync'
  #         - 'no_subtree_check'
  #         - 'no_root_squash'
  #   mode: "u=rwx,g=rwx,o=rwx"
  #   path: '/opt/nfs/test2'

# Options for rpc.mountd.
# If you have a port-based firewall, you might want to set up
# a fixed port here using the --port option. For more information,
# see rpc.mountd(8) or http://wiki.debian.org/SecuringNFS
# To disable NFSv4 on the server, specify '--no-nfs-version 4' here
nfs_server_rpcmountdopts:
  - '--manage-gids'
  # - '--no-nfs-version 4'
  # - '--port 2000'

# Number of servers to start up
nfs_server_rpcnfsdcount: 8

# Options for rpc.nfsd.
nfs_server_rpcnfsdopts: []
  # - '--port 2049'
  # - '--no-nfs-version 4'
  # - '--no-tcp'
  # - '--no-udp'

# Options for rpc.statd.
#   Should rpc.statd listen on a specific port? This is especially useful
#   when you have a port-based firewall. To use a fixed port, set this
#   this variable to a statd argument like: "--port 4000 --outgoing-port 4001".
#   For more information, see rpc.statd(8) or http://wiki.debian.org/SecuringNFS
nfs_server_statdopts: []
  # - '--port 4000'
  # - '--outgoing-port 4001'
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: nfs_servers
  vars:
  roles:
    - role: ansible-nfs-server
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
