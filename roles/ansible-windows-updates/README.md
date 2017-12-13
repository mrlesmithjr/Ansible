<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-windows-updates](#ansible-windows-updates)
  - [Requirements](#requirements)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-windows-updates

An [Ansible](https://www.ansible.com) role to apply [Windows](https://www.microsoft.com/en-us/windows)
updates.

## Requirements

## Role Variables

```yaml
---
# defaults file for ansible-windows-updates

# Defines categories to update
windows_updates_categories:
  # - 'Application'
  # - 'Connectors'
  - 'CriticalUpdates'
  # - 'DefinitionUpdates'
  # - 'DeveloperKits'
  # - 'FeaturePacks'
  # - 'Guidance'
  - 'SecurityUpdates'
  # - 'ServicePacks'
  # - 'Tools'
  - 'UpdateRollups'
  # - 'Updates'

# Defines whether to reboot after updates or not
windows_updates_reboot: false
```

## Dependencies

## Example Playbook

```yaml
- hosts: windows_hosts
  roles:
    - role: ansible-windows-updates
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
