# Role Name
Ansible role to install HAProxy
## Requirements

## Role Variables

## Dependencies
To sync_haproxy GlusterFS must be installed...Add GlusterFS role to Playbook.

## Example Playbook
- hosts: haproxy-nodes
  sudo: yes
  role:
    - haproxy

- hosts: gluster-haproxy-nodes
  sudo: yes
  vars:
    - config_haproxy: true
    - sync_haproxy: true
  roles:
    - glusterfs
    - haproxy
## License
GNU General Public License Version 2

## Author Information
Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
