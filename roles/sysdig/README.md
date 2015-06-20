# Role Name
Installs sysdig role
## Requirements
None
## Role Variables
````
sysdig_repo: /etc/yum.repos.d/draios.repo
sysdig_repo_apt: /etc/apt/sources.list.d/draios.list
sysdig_repokey: https://s3.amazonaws.com/download.draios.com/DRAIOS-GPG-KEY.public
sysdig_url: http://download.draios.com/stable/rpm/draios.repo
sysdig_url_apt: http://download.draios.com/stable/deb/draios.list
````
## Dependencies
None
## Example Playbook
````
- hosts: all
  remote_user: remote
  sudo: yes
  roles:
    - sysdig
````
## License
GNU General Public License Version 2

## Author Information
Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
