<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-elk-pre-processor](#ansible-elk-pre-processor)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-elk-pre-processor

An [Ansible](https://www.ansible.com) role to configure [Logstash](https://www.elastic.co/products/logstash)
for ELKStack functionality.

> NOTE: This role is specific to setting up an ELKStack pre-processor node. This
> role does not install Logstash and assumes that it is already installed.
> Reference <https://everythingshouldbevirtual.com/ansible-highly-available-elk-stack/>
> for details.

## Requirements

Prior to using this role you will want to add your nodes to the appropriate
inventory group. You should create 2 elk-pre-processor nodes. Examples below.
`inventory`:

```bash
[elk-nodes]
elk-pre-processor-1
elk-pre-processor-2

[elk-pre-processor-nodes]
elk-pre-processor-1
elk-pre-processor-2
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

Install all required Ansible roles from `requirements.yml`:

```bash
sudo ansible-galaxy install -r requirements.yml
```

## Example Playbook

[playbook.yml](playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
