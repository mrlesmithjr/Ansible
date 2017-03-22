Role Name
=========

An [Ansible] role to install/configure [StackStorm] Community Edition

[StackStorm] is an event-driven automation platform that ties
together every component of your environment.

Requirements
------------

Install [Ansible] required roles...  
```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------

```
---
# defaults file for ansible-stackstorm
stackstorm_db_info:
  user: 'mistral'
  password: 'StackStorm'
  db: 'mistral'
stackstorm_debian_packages:
  - 'apache2-utils'
  - 'python-passlib'
  - 'st2'
  - 'st2chatops'
  - 'st2mistral'
  - 'st2web'
stackstorm_debian_repo_info:
  repo_key: 'https://packagecloud.io/StackStorm/staging-stable/gpgkey'
  repos:
    - 'deb https://packagecloud.io/StackStorm/staging-stable/{{ ansible_distribution|lower }}/ {{ ansible_distribution_release|lower }} main'
    - 'deb-src https://packagecloud.io/StackStorm/staging-stable/{{ ansible_distribution|lower }}/ {{ ansible_distribution_release|lower }} main'

# Defines if packs defined should be installed
stackstorm_install_packs: true

stackstorm_packs:
    # st2 content pack containing ansible integrations
  - name: 'ansible'
    installed: true
    # st2 content pack containing docker integrations
  - name: 'docker'
    installed: true
    # st2 elasticsearch integration pack
  - name: 'elasticsearch'
    installed: false
    # st2 content pack containing github integrations
  - name: 'github'
    installed: true
    # Jenkins CI Integration Pack
  - name: 'jenkins'
    installed: false
    # A StackStorm pack for working with network devices using the NAPALM library
  - name: 'napalm'
    installed: true
    # StackStorm integration with Nest Thermostats
  - name: 'nest'
    installed: false
    # A pack containing useful networking utils for use in workflows.
  - name: 'networking_utils'
    installed: true
    # st2 content pack containing sensu integrations
  - name: 'sensu'
    installed: false
    # st2 content pack containing slack integrations
  - name: 'slack'
    installed: false
    # st2 content pack containing urban dictionary integrations
  - name: 'urbandict'
    installed: false
stackstorm_ssh_info:
  user: 'stanley'
stackstorm_ssl_info:
  cert_days: 3650
  cert_dir: '/etc/ssl/st2'
  cert_info: '/C=US/ST=California/L=Palo Alto/O=StackStorm/OU=Information Technology/CN={{ ansible_hostname }}'
stackstorm_webui_login_info:
  password: 'Ch@ngeMe'
  password_file: '/etc/st2/htpasswd'
  user: 'st2admin'
```

Dependencies
------------

None

Example Playbook
----------------

[Vagrant]
-------
Spin up [StackStorm] using [Vagrant].
```
cd Vagrant
vagrant up
```
You should now be able to connect to https://192.168.250.10

Login using: `st2admin\Ch@ngeMe`

When you are all done testing using [Vagrant] you can easily tear down and
cleanup:
```
./cleanup.sh
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
[StackStorm]: <https://stackstorm.com/>
[Vagrant]: <https://www.vagrantup.com/>
