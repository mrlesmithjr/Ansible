Role Name
=========

Common base role for all hosts. Should be ran after mrlesmithjr.bootstrap role.
(Configure update dhcp client,update dns servers,configure lvm)

Requirements
------------

If creating, resizing or creating LVM volumes/volume groups ensure that you
define the correct current disk and the new disk(s) added. If you choose to use
apt-cacher ensure that you already have a server built and configured correctly
for apt-caching.

Role Variables
--------------

```
---
# defaults file for ansible-base
base_dns_nameservers: # Define DNS servers to update to if update_dns_nameservers = true
  - '8.8.8.8'
  - '8.8.4.4'
# Defines if /etc/network/interfaces dns-nameservers is present or not...Only used when update_dns_nameservers=true
base_dns_nameservers_state: 'present'
base_dns_search: 'example.org' # Defines dns-search for /etc/network/interfaces
# Defines if /etc/network/interfaces dns-search is present or not...Only used if base_update_dns_search=true
base_dns_search_state: 'present'
base_force_apt_update: false # Defines if apt-get udpate should be forced
base_rundeck_generate_resources_xml: false # Defines if rundeck CI resources.xml should be generated if using rundeck...
base_rundeck_resources_xml_file: 'resources.xml' # Defines the name of the resources file to be created on rundeck server
# Defines defaults location on rundeck server to store the new resources.xml file
base_rundeck_resources_xml_location: '/var/lib/rundeck/var'
# Define server that is running rundeck CI if used...define here or globally in group_vars/all/servers
base_rundeck_server: []
base_ssh_manage_ssh_known_hosts: false # Define if hosts ssh_known_hosts should be managed
# Defines if dhcp client config should be updated...define here or globally in group_vars/all/configs
base_update_dhcpclient_conf: false
# Defines if dns servers should be updated...define here or globally in group_vars/all/configs
base_update_dns_nameservers: false
# Defines if dns search domain should be updated...define here or globally in group_vars/all/configs
base_update_dns_search: false
```

Dependencies
------------

None

Example Playbook
----------------

#### Galaxy
-----------
    - hosts: servers
      roles:
         - mrlesmithjr.base
#### GitHub
-----------
    - hosts: servers
      roles:
        - ansible-base

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
