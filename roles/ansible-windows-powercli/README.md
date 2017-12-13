<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-windows-powercli](#ansible-windows-powercli)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-windows-powercli

An [Ansible](https://www.ansible.com) role to install [VMware PowerCLI](https://blogs.vmware.com/PowerCLI/2017/05/powercli-6-5-1-install-walkthrough.html) on `Windows`.

## Requirements

## Role Variables

```yaml
---
# defaults file for ansible-windows-powercli

window_powercli_customer_experience_improvement_program: false

windows_powercli_disable_invalid_cert_warning: true
```

## Dependencies

## Example Playbook

```yaml
---
- hosts: test_nodes
  vars:
    pri_domain_name: test.vagrant.local
  roles:
    - role: ansible-windows-powercli
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
