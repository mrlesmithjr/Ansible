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

stackstorm_actionrunner:
  logging: '/etc/st2/logging.actionrunner.conf'
  virtualenv_opts: '--always-copy'

# Define Stackstorm API info
stackstorm_api:
  host: '0.0.0.0'
  logging: '/etc/st2/logging.api.conf'
  mask_secrets: true
  port: '9101'

stackstorm_auth:
  api_url: ''
  debug: false
  enable: false
  host: '0.0.0.0'
  logging: '/etc/st2/logging.auth.conf'
  mode: 'standalone'
  port: '9100'
  use_ssl: false

stackstorm_config_stackstorm: true

# Defines MongoDB settings
stackstorm_database:
  db: 'st2'
  # Supports MongoDB Replica Sets
  # host = mongodb://<#MDB_NODE_1>,<#MDB_NODE_2>,<#MDB_NODE_3>/?replicaSet=<#MDB_REPLICA_SET_NAME>
  host: '127.0.0.1'
  port: '27017'
  # username: ''
  # password: ''

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

stackstorm_exporter:
  logging: '/etc/st2/logging.exporter.conf'

stackstorm_garbagecollector:
  logging: '/etc/st2/logging.garbagecollector.conf'

# Defines if packs defined should be installed
stackstorm_install_packs: true

stackstorm_log:
  excludes:
    - 'requests'
    - 'paramiko'
  mask_secrets: true
  redirect_stderr: false

# Define RabbitMQ host/login
stackstorm_messaging:
  cluster: false
  # cluster_hosts: '{{ groups[rabbitmq_cluster] }}'
  host: '127.0.0.1'
  password: 'guest'
  port: '5672'
  username: 'guest'

stackstorm_notifier:
  logging: '/etc/st2/logging.notifier.conf'

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

stackstorm_resultstracker:
  logging: '/etc/st2/logging.resultstracker.conf'

stackstorm_rulesengine:
  logging: '/etc/st2/logging.rulesengine.conf'

stackstorm_sensor_container:
  logging: '/etc/st2/logging.sensorcontainer.conf'

stackstorm_ssh_info:
  key_file: '/home/stanley/.ssh/stanley_rsa'
  user: '{{ stackstorm_user }}'

stackstorm_ssl_info:
  cert_days: 3650
  cert_dir: '/etc/ssl/st2'
  cert_info: '/C=US/ST=California/L=Palo Alto/O=StackStorm/OU=Information Technology/CN={{ ansible_hostname }}'

stackstorm_stream:
  logging: '/etc/st2/logging.stream.conf'

stackstorm_syslog:
  host: '127.0.0.1'
  port: '514'
  facility: 'local7'
  protocol: 'udp'

stackstorm_system:
  base_path: '/opt/stackstorm'

stackstorm_user: 'stanley'

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

```
---
- hosts: all
  become: true
  vars:
    etc_hosts_add_all_hosts: true
    pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-etc-hosts

- hosts: stackstorm_server
  become: true
  vars:
    pri_domain_name: 'test.vagrant.local'
    stackstorm_install_packs: true
  roles:
    - role: ansible-mongodb
    - role: ansible-nginx
    - role: ansible-postgresql
    - role: ansible-rabbitmq
    - role: ansible-nodejs
    - role: ansible-stackstorm
  tasks:

- hosts: stackstorm_client
  become: true
  vars:
    create_users:
      - user: '{{ stackstorm_user }}'
        comment: 'Stackstorm SSH User'
        generate_keys: true
        # P@55w0rd
        pass: '$6$8tMUxKP33/$Fb/hZBaYvyzGubO9nrlRJMjUnt3aajXZwxCifH9NYqrhjMlC9COWmNNFiMpnyNGsgmDeNCCn2wKNh0G1E1BBV0'
        preseed_user: false
        state: 'present'
        sudo: true
        system_account: false
    enable_manage_ssh_keys: true
    manage_ssh_keys:
      - remote_user: '{{ stackstorm_user }}'
        state: present
        keys:
          - ./{{ stackstorm_user }}@node0.pub
    pri_domain_name: 'test.vagrant.local'
    stackstorm_user: 'stanley'
  roles:
    - role: ansible-users
      tags:
        - "stackstorm-ssh-keys"
        - "stackstorm-user"
    - role: ansible-manage-ssh-keys
      tags:
        - "stackstorm-ssh-keys"
        - "stackstorm-user"
  tasks:
```

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
