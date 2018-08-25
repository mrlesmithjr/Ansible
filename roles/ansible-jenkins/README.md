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

[defaults/main.yml](defaults/main.yml)

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
