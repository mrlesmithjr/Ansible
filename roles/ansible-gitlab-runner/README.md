<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [ansible-gitlab-runner](#ansible-gitlab-runner)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-gitlab-runner

An [Ansible](https://www.ansible.com) role to install/configure [GitLab Runner](https://docs.gitlab.com/runner/)

## Requirements

Replace GitLab token in `defaults/main.yml`

```yaml
gitlab_runner_config:
  url: https://gitlab.com/ci
  # runner token needs to be replaced
  token: TOKEN
  executor: shell
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: gitlab_runner
  vars:
  roles:
    - role: ansible-gitlab-runner
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
