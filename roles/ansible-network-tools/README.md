<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-network-tools](#ansible-network-tools)
  - [Role info](#role-info)
  - [Role purpose](#role-purpose)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-network-tools

## Role info

An [Ansible](https://www.ansible.com) role to install various network related
tools.

## Role purpose

The purpose of this role is to install various network related tools which can
be used for performing various tasks such as below:

-   ARP discovery
-   Bandwidth monitoring
-   LLDP neighbor info
-   Packet inspection
    -   Captures
    -   Dumps
-   Port scanning
-   Route tracing

## Requirements

None

## Role Variables

```yaml
---
# defaults file for ansible-network-tools
network_tools_debian:
  - 'arp-scan'
  - 'arping'
  - 'arptables'
  - 'bmon'
  - 'dnsutils'
  - 'ifstat'
  - 'iftop'
  - 'iperf'
  - 'iproute'
  - 'lldpd'
  - 'lsof'
  - 'nbtscan'
  - 'netcat'
  - 'netdiscover'
  - 'netdiag'
  - 'nethogs'
  - 'netperf'
  - 'netsniff-ng'
  - 'nfdump'
  - 'ngrep'
  - 'nload'
  - 'nmap'
  - 'socat'
  - 'tcpdump'
  - 'tcpflow'
  - 'tcpstat'
  - 'tcptrace'
  - 'tcptrack'
  - 'telnet'
  - 'traceroute'

network_tools_redhat:
  - 'arp-scan'
  - 'arptables'
  - 'bind-utils'
  - 'bmon'
  - 'iftop'
  - 'iperf'
  - 'iproute'
  - 'iptraf'
  - 'iputils'
  - 'lldpd'
  - 'lsof'
  - 'nethogs'
  - 'netsniff-ng'
  - 'nfdump'
  - 'ngrep'
  - 'nload'
  - 'nmap'
  - 'nmap-ncat'
  - 'socat'
  - 'tcpdump'
  - 'tcpflow'
  - 'telnet'
  - 'traceroute'
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  vars:
  roles:
    - role: ansible-network-tools
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
