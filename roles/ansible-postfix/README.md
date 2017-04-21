Role Name
=========

An [Ansible] role to install/configure [Postfix]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-postfix.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-postfix)

Requirements
------------

None
Role Variables
--------------

```
---
# defaults file for ansible-postfix

# Defines if postfix should be configured
configure_postfix: false

# Defines if outgoing email domain should be changed
enable_postfix_domain_rewrite: false

# Defines if a relay host should be used
enable_postfix_relayhost: false
postfix_conf_dir: '/etc/postfix'

# Defines which networks are allowed to relay through postfix server
# this is defined for all nodes which have roles/postfix applied
postfix_mynetworks:
  - '127.0.0.0/8'
#  - '10.0.101.0/24'
#  - '172.16.0.0/16'
#  - '192.168.0.0/16'

# Define smtp relay server
postfix_relayhost: '[smtp.example.org]'

# Defines what domain all outgoing email should be set to for @domain.example
postfix_rewrite_domain: 'example.org'

# Defines if tls should be used or not
postfix_use_tls: true

postfix_tls_cert_file: '/etc/ssl/certs/ssl-cert-snakeoil.pem'

postfix_tls_cert_key: '/etc/ssl/private/ssl-cert-snakeoil.key'
enable_sender_canonical: false
postfix_sender_canonical_maps:
  - "/^(.*@)example.com$/     ${1}example.co.uk"

# Can be set to 'hash' or 'regexp' filetype
postfix_domain_rewrite_filetype: 'hash'

# set which template to use for generic maps file
postfix_generic_template: 'generic.j2'
postfix_altgeneric_maps:
  - "/^(.*@)something.com$/     ${1}somethingelse.co.uk"
enable_postifx_dkim: false

# Support the setting of the helo name
enable_smtp_helo_name: false
postfix_smtp_helo_name: '{{ ansible_fqdn }}'
enable_always_add_missing_headers: false
```

Dependencies
------------

None

Example Playbook
----------------

```
---
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-postfix
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[Postfix]: <http://www.postfix.org/>
