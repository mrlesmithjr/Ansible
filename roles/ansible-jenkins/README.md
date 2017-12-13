<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [ansible-jenkins](#ansible-jenkins)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [Vagrant Usage](#vagrant-usage)
        -   [Spinning up Vagrant test environment](#spinning-up-vagrant-test-environment)
        -   [Tearing down Vagrant test environment](#tearing-down-vagrant-test-environment)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-jenkins

An [Ansible](https://www.ansible.com) Role to Install/Configure [Jenkins CI](https://jenkins-ci.org/)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-jenkins

# Defines if jenkins will be configured from templates or left as default install
config_jenkins: false

# Defines if jenkins user should have sudo rights
# (Useful for running Ansible tasks from CLI)
enable_jenkins_sudo: false

# Defines if ansible tower cli should be installed
install_tower_cli: false

# Notification e-mails from Jenkins to project owners will be sent with this
# address in the from header.
jenkins_admin_email: 'admin@{{ pri_domain_name }}'

jenkins_ansible_info:
  name: 'Default'
  home: '/usr/local/bin'
jenkins_apt_repo: 'deb http://pkg.jenkins-ci.org/debian binary/'

# Whether to enable the historical Jenkins CLI mode over remoting
# (-remoting option in the client). While this may be necessary to support
# certain commands or command options, it is considered intrinsically insecure.
# (-http mode is always available, and -ssh mode is available whenever the SSH
# service is enabled.)
jenkins_cli_mode_over_remoting: false

jenkins_cli_path: '{{ jenkins_home_dir }}/jenkins-cli.jar'

jenkins_config_info:
  # AuthorizationStrategy$Unsecured or FullControlOnceLoggedInAuthorizationStrategy
  auth_strategy: 'FullControlOnceLoggedInAuthorizationStrategy'
  disable_remember_me: false
  # Defines if setup wizard is disabled
  disable_setup_wizard: false
  num_executors: 2
  system_message: 'Welcome to the Jenkins lab'
  use_security: true

jenkins_config_files:
  - 'config.xml'
  - 'hudson.tasks.Mailer.xml'
  - 'jenkins.CLI.xml'
  - 'jenkins.model.JenkinsLocationConfiguration.xml'
  - 'org.jenkinsci.plugins.ansible.AnsibleInstallation.xml'

jenkins_debian_pre_req_packages:
  - 'default-jdk'
  - 'default-jre-headless'
  - 'git'
  - 'jenkins'
  - 'python-pip'
  - 'python-setuptools'

jenkins_email_info:
  default_suffix: '@{{ pri_domain_name }}'
  reply_to_address: 'jenkins@{{ pri_domain_name }}'
  smtp_host: 'smtp.{{ pri_domain_name }}'
  use_ssl: false
  smtp_port: 25

# specify the HTTP address of the Jenkins installation, such as
# http://yourhost.yourdomain/jenkins/. This value is used to let Jenkins know
# how to refer to itself, ie. to display images or to create links in emails.
jenkins_fqdn: 'http://{{ ansible_hostname }}.{{ pri_domain_name }}:{{ jenkins_port }}'

jenkins_home_dir: '/var/lib/jenkins'

jenkins_ldap_info:
  active_directory: true
  enabled: false
  server: '192.168.202.200'
  port: 389
  root_dn: 'DC=example,DC=org'
  user_search_base: 'CN=Users'
  manager_dn: 'CN=gitlab,CN=Users,DC=example,DC=org'
  # This will be encrypted when saved from WebUI
  manager_password: 'P@55w0rd'
  disable_email_address_resolver: false

# Defines if plugins will be managed using Ansible...
jenkins_manage_plugins: false

# Defines plugins to install if jenkins_manage_plugins: true
jenkins_plugins: []
  # - 'active-directory'
  # - 'ansible'
  # - 'build-pipeline-plugin'
  # - 'git'
  # - 'gitlab-plugin'
  # - 'job-dsl'
  # - 'ldap'
  # - 'logstash'
  # - 'PowerShell'
  # - 'rundeck'
  # - 'ssh'
  # - 'travis-yml'
  # - 'vagrant'
  # - 'vmware-vrealize-automation-plugin'
  # - 'vmware-vrealize-codestream'
  # - 'vsphere-cloud'
  # - 'workflow-aggregator'

jenkins_port: 8080

jenkins_redhat_pre_req_packages:
  - 'git'
  - 'java-1.7.0-openjdk'
  - 'python-pip'
  - 'python-setuptools'

jenkins_repo_key: 'http://pkg.jenkins-ci.org/{{ ansible_os_family|lower }}/jenkins-ci.org.key'

pri_domain_name: 'example.org'
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-jenkins
  tasks:
```

## Vagrant Usage

Included is a [Vagrant](https://www.vagrantup.com) test environment to easily
spinup. This environment is very useful for quickly spinning up a usable
[Jenkins CI](https://jenkins-ci.org/) platform. It is also very useful for
learning how to provision a [Jenkins CI](https://jenkins-ci.org/) platform using
[Ansible](https://www.ansible.com).

### Spinning up Vagrant test environment

To spin up this test environment simply execute:

```bash
cd Vagrant
vagrant up
```

Once the provisioning is complete you can then connect to the
[Jenkins WebUI](http://192.168.250.10:8080) using your browser of choice and
begin doing some cool stuff.

> NOTE: This setup is an insecure setup without any authentication enabled
> and it should be treated as purely a playground.

### Tearing down Vagrant test environment

Once you are done using this test environment and are ready to tear it all down
simply execute:

```bash
cd Vagrant
./cleanup.sh
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
