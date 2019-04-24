<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-logstash](#ansible-logstash)
  - [Build Status](#build-status)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-logstash

An [Ansible](https://www.ansible.com) role that Installs/configures [Logstash](https://www.elastic.co/products/logstash)

## Build Status

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-logstash.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-logstash)

## Requirements

Default config if `config_logstash=true` is to open `tcp/udp 10514` because
ports \< 1024 require root access. Configure clients to send to `udp/tcp 10514`.
You can configure rsyslog to listen on `tcp/udp 514` and redirect rsyslog
to send to localhost on `tcp/udp 10514` to accomodate clients which cannot
send to a different port. See example below:

`/etc/rsyslog.d/50-default.conf`

`tcp`:

```bash
*.* @@localhost:10514
```

`udp`:

```bash
*.* @localhost:10514
```

## Role Variables

[default vars](./defaults/main.yml)

Use your own outputs:

Example:

```yaml
logstash_custom_outputs:
  - output: "gelf"
    lines:
      - 'host => "localhost"'
      - 'port => "12201"'
```

Additional variables for customized configs:

```yaml
logstash_custom_inputs:
  - input: someinput
    lines:
      - 'somekey => "value"'

logstash_custom_filters:
  - lines:
      - 'somekey => "value"'

logstash_custom_outputs:
  - output: someoutput
    lines:
      - 'somekey => "value"'
```

## Dependencies

None

## Example Playbook

[Example Playbook](./playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
