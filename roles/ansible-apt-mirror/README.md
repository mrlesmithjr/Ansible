Role Name
=========

Installs and configures apt-mirror (Local APT Repository). Also configures clients if extra-var passed.

Requirements
------------

Lot's of disk space required for repos...At time of putting this together Ubuntu Trusty w/defaults in this role requires 139GB+

Install Ansible role requirements
````
sudo ansible-galaxy install -r requirements.yml -f
````

Vagrant
-------
Spin up Environment under Vagrant to test.
````
vagrant up
````

Docker
------
Spin up Docker container (apt mirror repos not populated...will update on cron schedule)
````
docker run -d -p 80:80 --name apt-mirror mrlesmithjr/apt-mirror
````
To immediately update cache (Will take a long time...so do not cancel)
````
docker exec -it apt-mirror apt-mirror
````

Role Variables
--------------
````
---
# defaults file for ansible-apt-mirror
apache2_default_root: /var/www/html
apt_mirror_apache_links:  #defines the uri of each repository used in apt_mirror_repos..ex. http://{{ apt_mirror_ubuntu_mirror }} will be archive.ubuntu.com/ubuntu
  - uri: '{{ apt_mirror_ubuntu_mirror }}'
    distro: ubuntu  #defines name of symlink..ensure to change apt_mirror_client_repos to match
apt_mirror_client: false  #defines if running this role against a client...define this as an extra-var...example in README.md or in group_vars/all
apt_mirror_client_repos:
  - 'deb http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }} main restricted universe multiverse'
  - 'deb http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-security main restricted universe multiverse'
  - 'deb http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-updates main restricted universe multiverse'
#  - 'deb http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-proposed main restricted universe multiverse'
#  - 'deb http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-backports main restricted universe multiverse'
  - 'deb-src http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }} main restricted universe multiverse'
  - 'deb-src http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-security main restricted universe multiverse'
  - 'deb-src http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-updates main restricted universe multiverse'
#  - 'deb-src http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-proposed main restricted universe multiverse'
#  - 'deb-src http://{{ apt_mirror_server }}/ubuntu {{ ansible_distribution_release }}-backports main restricted universe multiverse'
apt_mirror_dir: /var/spool/apt-mirror  #define directory to use as repo...default is /var/spool/apt-mirror
apt_mirror_limit_rate: 125  #defines download rate limit in KiloBytes/thread...ex. 1Mb=125Kb..so enter 125
apt_mirror_nthreads: 10  #defines the number of threads
apt_mirror_populate_repos: true  #defines if repos should be populated during install..can set to false and allow cron job to populate.
apt_mirror_repos:  #define list of repos to add
## Ubuntu Trusty (14.04)
  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} trusty main restricted universe multiverse'
  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} trusty-security main restricted universe multiverse'
  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} trusty-updates main restricted universe multiverse'
#  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} trusty-proposed main restricted universe multiverse'
#  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} trusty-backports main restricted universe multiverse'
  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} trusty main restricted universe multiverse'
  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} trusty-security main restricted universe multiverse'
  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} trusty-updates main restricted universe multiverse'
#  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} trusty-proposed main restricted universe multiverse'
#  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} trusty-backports main restricted universe multiverse'
  - 'deb-src http://{{ apt_mirror_ubuntu_mirror }} trusty main restricted universe multiverse'
  - 'deb-src http://{{ apt_mirror_ubuntu_mirror }} trusty-security main restricted universe multiverse'
  - 'deb-src http://{{ apt_mirror_ubuntu_mirror }} trusty-updates main restricted universe multiverse'
#  - 'deb-src http://{{ apt_mirror_ubuntu_mirror }} trusty-proposed main restricted universe multiverse'
#  - 'deb-src http://{{ apt_mirror_ubuntu_mirror }} trusty-backports main restricted universe multiverse'
  - 'deb http://{{ apt_mirror_ubuntu_mirror }} trusty main/debian-installer multiverse/debian-installer restricted/debian-installer universe/debian-installer'
## Ubuntu Precise (12.04)
#  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} precise main restricted universe multiverse'
#  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} precise-security main restricted universe multiverse'
#  - 'deb-amd64 http://{{ apt_mirror_ubuntu_mirror }} precise-updates main restricted universe multiverse'
#  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} precise main restricted universe multiverse'
#  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} precise-security main restricted universe multiverse'
#  - 'deb-i386 http://{{ apt_mirror_ubuntu_mirror }} precise-updates main restricted universe multiverse'
apt_mirror_schedule:
  - name: 'apt-mirror updates'
    special_time: daily  #defines easy schedule....can be hourly, daily, weekly, monthly, annually, yearly or reboot..comment out if setting specific times
#    minute: 0
#    hour: *
#    day: *
#    month: *
#    weekday: *
    job: '/usr/bin/apt-mirror > /var/spool/apt-mirror/var/cron.log'
    cron_file: apt-mirror
apt_mirror_schedule_updates: true  #defines if repos should be updates on a schedule...defined in apt_mirror_schedule
apt_mirror_server: 'apt-mirror.{{ pri_domain_name }}'  #defines server clients point to...either FQDN/hostname/IP
apt_mirror_ubuntu_mirror: mirror.pnl.gov/ubuntu/  #define ubuntu mirror to use for ubuntu repos
enable_apt_mirror: false  #defines if apt_mirror is being used...if not client will be reset...
enable_apt_mirror_limit_rate: false  #defines if you would like to enable bandwidth limits defined in apt_mirror_limit_rate
pri_domain_name: example.org
````

Dependencies
------------

ansible-apache2 and mrlesmithjr.apache2 (Installed as part of requirements.yml)

Example Playbook
----------------

###### Galaxy
    - hosts: servers
      roles:
         - role: mrlesmithjr.apache2
         - role: mrlesmithjr.apt-mirror

     - hosts: clients
       roles:
         - { role: mrlesmithjr.apt-mirror, apt_mirror_client: true }

###### GitHub
    - hosts: servers
      roles:
        - role: ansible-apache2
        - role: ansible-apt-mirror

    - hosts: clients
      roles:
        - { role: ansible-apt-mirror, apt_mirror_client: true }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
