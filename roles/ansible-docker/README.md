Role Name
=========

Installs and configures Docker. Also adds ability to manage Docker images.

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-docker

# Ensure this exists if setting docker to alternate data directory...We do not create this to ensure any add'l mounts do not overlay this path..Service may fail to start if not.
docker_alt_data_dir: '/mnt/docker'
# Defines if docker should be configured to store data in alternate location..ensure to enable -g option in docker_opts if true
docker_config_alt_data_dir: false
docker_config_service: false  # Defines if docker service should be configured
docker_images:  #defines docker images to be installed
  - image: 'centos'  #defines image name...ex. docker hub image name
    state: 'present'  #defines state of container....present, started, reloaded, restarted, stopped, killed or absent
#  - image: 'elasticsearch'
#    state: 'present'
#  - image: 'fedora'
#    state: 'present'
  - image: 'ubuntu'
    state: 'present'
docker_manage_images: false  #defines if images defined in docker_images are managed
docker_opts:  #defines docker service options to be configured
  - '-H fd://'
  # - '--dns {{ docker_pri_dns }}'
  # - '--dns {{ docker_sec_dns }}'
  # - '-g {{ docker_alt_data_dir }}'  #example to change location of where Docker will store data...to change - change docker_data_dir var above.
docker_pri_dns: '8.8.8.8'  #defines primary dns server for your site
docker_sec_dns: '8.8.4.4'  #defines secondary dns server for your site
docker_set_grub_memory_limit: true  #defines if docker memory limits should be added to grub boot loader
docker_ubuntu_repo_info:  #defines docker ubuntu repo info for installing from
  id: '58118E89F3A912897C070ADBF76221572C52609D'
  keyserver: 'hkp://p80.pool.sks-keyservers.net:80'
  repo: 'deb https://apt.dockerproject.org/repo {{ ansible_distribution | lower }}-{{ ansible_distribution_release }} main'
docker_users:  #defines users to be added to docker group to allow non sudo access to docker
  - 'vagrant'
```

Dependencies
------------

#### Galaxy
-----------
mrlesmithjr.ufw

#### GitHub
-----------
ansible-ufw

Example Playbook
----------------

#### Galaxy
-----------
    - hosts: servers
      vars:
        - configure_firewall: true
        - ufw_policies:  #defines default policy for incoming, outgoing and routed (forwarded) traffic...allow, deny or reject
            - direction: incoming
              policy: deny
            - direction: outgoing
              policy: allow
            - direction: routed
              policy: allow
        - ufw_rules:
            - rule: limit
              proto: tcp
              to_port: 22
            - rule: allow
              proto: tcp
              to_port: 2375
      roles:
        - role: mrlesmithjr.docker
        - role: mrlesmithjr.ufw
          when: configure_firewall is defined and configure_firewall

#### GitHub
-----------
    - hosts: servers
      vars:
        - configure_firewall: true
        - ufw_policies:  #defines default policy for incoming, outgoing and routed (forwarded) traffic...allow, deny or reject
            - direction: incoming
              policy: deny
            - direction: outgoing
              policy: allow
            - direction: routed
              policy: allow
        - ufw_rules:
            - rule: limit
              proto: tcp
              to_port: 22
            - rule: allow
              proto: tcp
              to_port: 2375
      roles:
        - role: ansible-docker
        - role: ansible-ufw
          when: configure_firewall is defined and configure_firewall        

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
