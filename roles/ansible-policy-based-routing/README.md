Role Name
=========

An [Ansible] role to manage policy based routing

Requirements
------------

None

Role Variables
--------------
```
---
# defaults file for ansible-policy-based-routing
policy_based_routing_enable_ip_forwarding: false
policy_based_routing_rules:
  - rule: '20'
    table: 'management1'
    source: '192.168.1.0/24'
    gateway: '10.0.2.2'
    state: "absent"
    persistent: true
  - rule: '30'
    table: 'management2'
    source: '192.168.250.0/24'
    # destination: '10.0.0.5'
    gateway: '192.168.250.1'
    state: "absent"
    persistent: true
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-policy-based-routing
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- [@mrlesmithjr]
- [EverythingShouldBeVirtual]
- mrlesmithjr [at] gmail.com

[@mrlesmithjr]: <https://www.twitter.com/mrlesmithjr>
[EverythingShouldBeVirtual]: <http://www.everythingshouldbevirtual.com>

[Ansible]: <https://www.ansible.com>
