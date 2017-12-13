<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ansible-windows-iis](#ansible-windows-iis)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-windows-iis

An [Ansible](https://www.ansible.com) role to install [Windows - IIS](https://www.iis.net/)

## Requirements

## Role Variables

```yaml
---
# defaults file for ansible-windows-iis

windows_iis_role: []
  # - name: Web-Server
  #   include_management_tools: true
  #   include_sub_features: false
  #   state: absent
  #   subfeatures: []
  #     # - name: Web-Default-Doc
  #     #   state: present
  #     # - name: Web-Dir-Browsing
  #     #   state: present
  #     # - name: Web-Http-Errors
  #     #   state: present
  #     # - name: Web-Static-Content
  #     #   state: present
  #     # - name: Web-Http-Logging
  #     #   state: present
  #     # - name: Web-Stat-Compression
  #     #   state: present
  #     # - name: Web-Filtering
  #     #   state: present
  # - name: Web-Ftp-Server
  #   include_management_tools: true
  #   include_sub_features: false
  #   state: absent
  #   subfeatures: []

windows_iis_websites: []
  # - name: Default Web Site
  #   # ip: 192.168.250.10
  #   physical_path: c:\inetpub\wwwroot
  #   port: 80
  #   state: started
```

## Dependencies

## Example Playbook

```yaml
---
- hosts: windows_iis_servers
  roles:
    - role: ansible-windows-iis
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
