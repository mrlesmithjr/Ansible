# ansible-virtualbox

An [Ansible](https://www.ansible.com) role to install [Virtualbox](https://www.virtualbox.org/)

<!-- TOC -->

- [ansible-virtualbox](#ansible-virtualbox)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- /TOC -->

## Requirements

For Archlinux the current method to install Oracle Extensions is to run the
following manually (for now):

```bash
pamac build virtualbox-ext-oracle
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: all
  vars:
  roles:
    - role: ansible-virtualbox
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- mrlesmithjr [at] gmail.com
