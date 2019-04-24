# ansible-graylog

An [Ansible](https://www.ansible.com) role to install [Graylog](https://www.graylog.org/)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-graylog.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-graylog)

## Requirements

Install required [Ansible](https://www.ansible.com) roles:

```bash
sudo ansible-galaxy install -r requirements.yml
```

You **MUST** define the following vars:

```bash
# Generate new pw using...pwgen -N 1 -s 96
graylog_server_password_secret:

# Generate new pw using...echo -n yourpassword | shasum -a 256
graylog_server_root_password:
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

## Example Playbook

[playbook.yml](playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
