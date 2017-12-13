# ansible-es-packetbeat

An [Ansible](https://www.ansible.com) role to install/configure [Packetbeat](https://www.elastic.co/products/beats/packetbeat)

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
- hosts: packetbeat_clients
  become: true
  vars:
  roles:
    - role: ansible-es-packetbeat
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   mrlesmithjr [at] gmail.com
