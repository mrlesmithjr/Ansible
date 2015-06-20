# Role Name
Ansible role to install Keepalived
## Requirements

## Role Variables

## Dependencies
In order to sync configurations the GlusterFS role needs to be applied to host(s)

## Example Playbook
- hosts: keepalived-nodes
  sudo: yes
  role:
    - keepalived

- hosts: gluster-keepalived-nodes
  sudo: yes
  vars:
    - config_keepalived: true
    - sync_keepalived: true
  roles:
    - glusterfs
    - keepalived

## License
GNU General Public License Version 2

## Author Information
Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
