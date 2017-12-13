<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-gitlab-runner](#ansible-gitlab-runner)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

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

```yaml
---
# defaults file for ansible-gitlab-runner
gitlab_runner_check_interval: 0
gitlab_runner_concurrent_jobs: 1

gitlab_runner_config:
  url: https://gitlab.com/ci
  # runner token needs to be replaced
  token: TOKEN
  executor: shell

gitlab_runner_debian_package:
  key: '{{ gitlab_runner_uri }}/gpgkey'
  package: '{{ gitlab_runner_uri }}/packages/{{ ansible_distribution|lower }}/{{ ansible_distribution_release|lower }}/gitlab-ci-multi-runner_{{ gitlab_runner_version }}_amd64.deb'
  repos:
    - 'deb {{ gitlab_runner_uri }}/{{ ansible_distribution|lower }}/ {{ ansible_distribution_release|lower }} main'
    - 'deb-src {{ gitlab_runner_uri }}/{{ ansible_distribution|lower }}/ {{ ansible_distribution_release|lower }} main'

gitlab_runner_uri: https://packages.gitlab.com/runner/gitlab-ci-multi-runner

gitlab_runner_version: 9.5.0
```

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

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
