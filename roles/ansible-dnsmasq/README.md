# Role Name

An [ansible] role to install/configure [dnsmasq]

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-dnsmasq.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-dnsmasq)

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
    - role: ansible-dnsmasq
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr]
-   <http://everythingshouldbevirtual.com>
-   mrlesmithjr [at] gmail.com

[@mrlesmithjr]: https://www.twitter.com/mrlesmithjr

[ansible]: https://ansible.com

[dnsmasq]: http://www.thekelleys.org.uk/dnsmasq/doc.html
