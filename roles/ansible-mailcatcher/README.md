Role Name
=========

Installs and configures mailcatcher (https://mailcatcher.me/)

- MailCatcher runs a super simple SMTP server which catches any message sent to it to display in a web interface. Run mailcatcher, set your favourite app to deliver to smtp://127.0.0.1:1025 instead of your default SMTP server, then check out http://127.0.0.1:1080 to see the mail that's arrived so far.

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-mailcatcher
mailcatcher_debian_packages:
  - 'build-essential'
  - 'libsqlite3-dev'
  - 'ruby'
  - 'ruby-dev'
  - 'software-properties-common'
mailcatcher_http_listen_address: '0.0.0.0'
mailcatcher_http_port: '1080'
mailcatcher_listen_address: '0.0.0.0'
mailcatcher_ruby_version: '2.3'
mailcatcher_smtp_listen_address: '0.0.0.0'
mailcatcher_smtp_port: '1025'
mailcatcher_ubuntu_packages:
  - 'build-essential'
  - 'libsqlite3-dev'
  - 'ruby{{ mailcatcher_ruby_version }}'
  - 'ruby{{ mailcatcher_ruby_version }}-dev'
  - 'software-properties-common'
````

Dependencies
------------

None

Example Playbook
----------------

````
- hosts: all
  become: true
  vars:
  roles:
    - role: ansible-mailcatcher
  tasks:
````

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
