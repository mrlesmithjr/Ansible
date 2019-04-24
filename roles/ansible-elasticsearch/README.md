<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [ansible-elasticsearch](#ansible-elasticsearch)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [Molecule Testing](#molecule-testing)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-elasticsearch

An [Ansible](https://www.ansible.com) role to install/configure [Elasticsearch](https://www.elastic.co/products/elasticsearch)

> NOTE: This role has been completely rewritten and replaces my original
> `ansible-elasticsearch` role which has been renamed to [ansible-elasticsearch-old](https://github.com/mrlesmithjr/ansible-elasticsearch-old.git).
> I decided to rewrite this role as the original had a lot of residuals from years
> of different usages. The original will remain for historical purposes.

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-elasticsearch.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-elasticsearch)

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

If you would like to add additional Elasticsearch parameters you only need to add
them to the `elasticsearch_configuration:` section. These variables are added as
YAML using the template. So there is no need to reconfigure the template either.

## Dependencies

None

## Example Playbook

[playbook.yml](playbook.yml)

## Molecule Testing

If you have [Molecule](https://github.com/metacloud/molecule) installed, you
can easily spin up a 3-node cluster for testing.

Simply run the following to spin up:

```bash
molecule converge
```

## License

MIT

## Author Information

Larry Smith Jr.

- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
