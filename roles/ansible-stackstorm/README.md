<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-stackstorm](#ansible-stackstorm)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Vagrant](#vagrant)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-stackstorm

An [Ansible](https://www.ansible.com) role to install/configure [StackStorm](https://stackstorm.com)
Community Edition

[StackStorm](https://stackstorm.com) is an event-driven automation platform that
ties together every component of your environment.

## Requirements

Install `Ansible` [required](./requirements.yml) roles...

```bash
ansible-galaxy install -r requirements.yml
```

## Role Variables

[Role Defaults](defaults/main.yml)

## Dependencies

None

## Example Playbook

[Example Playbook](./playbook.yml)

## [Vagrant](https://vagrantup.com)

Spin up `Stackstorm` using `Vagrant`:

```bash
cd Vagrant
vagrant up
```

You should now be able to connect to <https://192.168.250.10>

Login using: `st2admin\Ch@ngeMe`

When you are all done testing using `Vagrant` you can easily tear down and
cleanup:

```bash
./cleanup.sh
```

## License

MIT

## Author Information

Larry Smith Jr.

-   @mrlesmithjr
-   <http://everythingshouldbevirtual.com>
-   mrlesmithjr [at] gmail.com
