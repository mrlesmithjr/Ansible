<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-virtualbox](#ansible-virtualbox)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-virtualbox

An [Ansible](https://www.ansible.com) role to install [Virtualbox](https://www.virtualbox.org/)

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-virtualbox

virtualbox_build_ver: 115126
virtualbox_debian_package: 'virtualbox-{{ virtualbox_major_ver }}_{{ virtualbox_minor_ver }}-{{ virtualbox_build_ver }}~{{ ansible_distribution }}~{{ ansible_distribution_release|lower }}_amd64.deb'

virtualbox_dl_url: 'http://download.virtualbox.org/virtualbox/{{ virtualbox_minor_ver }}'

virtualbox_ext_pack: 'Oracle_VM_VirtualBox_Extension_Pack-{{ virtualbox_minor_ver }}-{{ virtualbox_build_ver }}.vbox-extpack'
virtualbox_ext_pack_license_agreement: '715c7246dc0f779ceab39446812362b2f9bf64a55ed5d3a905f053cfab36da9e'
virtualbox_major_ver: 5.1
virtualbox_minor_ver: 5.1.22
```

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

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
