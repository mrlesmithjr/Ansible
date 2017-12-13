<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-windows-docker](#ansible-windows-docker)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-windows-docker

An [Ansible](https://www.ansible.com) role to install [Docker](https://www.docker.com) on [Windows - 2016](https://www.microsoft.com/en-us/cloud-platform/windows-server)

## Requirements

## Role Variables

## Dependencies

## Example Playbook

```yaml
---
- hosts: windows_docker_hosts
  roles:
    - role: ansible-windows-docker
      when: ansible_os_family == "Windows"
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
