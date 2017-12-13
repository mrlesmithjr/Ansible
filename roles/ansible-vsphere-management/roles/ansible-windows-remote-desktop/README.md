<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-windows-remote-desktop](#ansible-windows-remote-desktop)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-windows-remote-desktop

An [Ansible](https://www.ansible.com) role to install `Remote Desktop (RDP)` on
[Windows](https://www.microsoft.com/en-us/windows)

## Requirements

## Role Variables

```yaml
---
# defaults file for ansible-windows-remote-desktop

windows_remote_desktop_enabled: true

windows_remote_desktop_firewall: []
  # - name: Remote Desktop
  #   action: allow
  #   description: Disabled Default Remote Desktop Rule
  #   direction: in
  #   enable: false
  #   force: true
  #   localport: 3389
  #   protocol: TCP
  #   state: present
  # - name: Remote Desktop - Any
  #   action: allow
  #   description: Allow Remote Desktop From Any
  #   direction: in
  #   enable: true
  #   force: true
  #   localport: 3389
  #   profile: any
  #   protocol: TCP
  #   remoteip: any
  #   state: present
  # - name: Remote Desktop - 192.168.250.0/24
  #   action: allow
  #   description: Allow Remote Desktop From 192.168.250.0/24
  #   direction: in
  #   enable: true
  #   force: true
  #   localip: '{{ ansible_ssh_host }}'
  #   localport: 3389
  #   profile: any
  #   protocol: TCP
  #   remoteip: 192.168.250.0/24
  #   state: present
```

## Dependencies

## Example Playbook

```yaml
---
- hosts: windows_hosts
  roles:
    - role: ansible-windows-remote-desktop
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
