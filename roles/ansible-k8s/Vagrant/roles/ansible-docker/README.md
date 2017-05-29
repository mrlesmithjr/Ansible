Role Name
=========

An [Ansible] role to install/configure [Docker]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-docker.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-docker)

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-docker

# Ensure this exists if setting docker to alternate data directory
# We do not create this to ensure any add'l mounts do not overlay this path
# Service may fail to start if not.
docker_alt_data_dir: '/mnt/docker'

# Defines if docker should be configured to store data in alternate location
# ensure to enable -g option in docker_opts if true
docker_config_alt_data_dir: false

# Defines if docker service should be configured
docker_config_service: false

# Defines if users defined in docker_users should be added to docker group
docker_config_users: false

# Defines docker images to be installed
docker_images:
    # Defines image name
    # ex. docker hub image name
  - name: 'centos'
    # Defines state of image
    # present|absent
    state: 'present'
#  - name: 'elasticsearch'
#    state: 'present'
#  - name: 'fedora'
#    state: 'present'
  - name: 'ubuntu'
    state: 'present'

# Defines if images defined in docker_images are managed
docker_manage_images: false

# Defines docker service options to be configured in /etc/docker/daemon.json
# https://docs.docker.com/engine/reference/commandline/dockerd//
docker_opts: []
# Only define bridge or bridge_ip if you want to use either one of these
# They cannot be used together
  # bridge: 'docker0'
  # bridge_ip: '172.17.0.1/8'
  # dns:
  #   - '8.8.8.8'
  #   - '8.8.4.4'
  # dns_search:
  #   - 'etsbv.internal'
  #   - 'etsbv.test'
  # insecure_registries:
  #   - 'gitlab.etsbv.internal:5000'
  # ip: '0.0.0.0'
  # ip_forward: true
  # ip_masq: true
  # iptables: true
  # labels:
  #   - key: 'environment'
  #     value: 'test'
  #   - key: 'datacenter'
  #     value: 'atlanta'
  # log_driver: 'json-file'
  # log_level: 'info'
  # max_concurrent_downloads: '3'
  # max_concurrent_uploads: '5'
  # aufs, devicemapper, btrfs, zfs, overlay and overlay2
  # storage_driver: 'aufs'
  # tls: false

# Defines if docker memory limits should be added to grub boot loader
docker_set_grub_memory_limit: true

# Defines docker ubuntu repo info for installing from
docker_ubuntu_repo_info:
  id: '58118E89F3A912897C070ADBF76221572C52609D'
  keyserver: 'hkp://p80.pool.sks-keyservers.net:80'
  repo: 'deb https://apt.dockerproject.org/repo {{ ansible_distribution | lower }}-{{ ansible_distribution_release }} main'

# Defines users to be added to docker group to allow non sudo access to docker
docker_users:
  - 'vagrant'

# Define Docker version to install
docker_version: '17.04.0'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: docker_hosts
  become: true
  vars:
  roles:
    - role: ansible-docker
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[Docker]: <https://www.docker.com>
