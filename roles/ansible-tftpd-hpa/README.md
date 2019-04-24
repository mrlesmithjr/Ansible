# ansible-tftpd-hpa

An [Ansible](https://www.ansible.com) role to install/configure `tftpd-hpa`.

## Requirements

None

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: tftp_servers
  become: true
  vars:
  roles:
    - role: ansible-tftpd-hpa
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)