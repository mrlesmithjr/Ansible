Role Name
=========

Installs and configures lighttpd web server (https://www.lighttpd.net/)  

Requirements
------------

None  

Role Variables
--------------

````
---
# defaults file for ansible-lighttpd
config_lighttpd: true
lighttpd_config_file: '/etc/lighttpd/lighttpd.conf'
lighttpd_debian_info:  #defines Debian configuration vars
  compress_filetype:
    - 'application/javascript'
    - 'text/css'
    - 'text/html'
    - 'text/plain'
  default_root: '/var/www'
  include_shell:
    - '/usr/share/lighttpd/create-mime.assign.pl'
    - '/usr/share/lighttpd/include-conf-enabled.pl'
  index_filenames:
    - 'index.php'
    - 'index.html'
    - 'index.lighttpd.html'
  max_fds: 2048  #max file descriptors (1024 is default)..this setting also sets max-connections to max_fds/2
  server_modules:
    - 'mod_access'
    - 'mod_alias'
    - 'mod_compress'
    - 'mod_redirect'
  #  - mod_rewrite
  static_file_exclude_extensions:
    - '.php'
    - '.pl'
    - '.fcgi'
  url_access_deny:
    - '~'
    - '.inc'
lighttpd_enable_php5: true
lighttpd_enable_php5_xcache: true
lighttpd_redhat_info:
  include:
    - 'modules.conf'
    - 'conf.d/access_log.conf'
    - 'conf.d/debug.conf'
    - 'conf.d/mime.conf'
    - 'conf.d/dirlisting.conf'
  index_filenames:
    - 'index.xhtml'
    - 'index.html'
    - 'index.htm'
    - 'default.htm'
    - 'index.php'
  max_fds: 2048  #max file descriptors (1024 is default)..this setting also sets max-connections to max_fds/2
  server_root: '/srv/www'
  static_file_exclude_extensions:
    - '.php'
    - '.pl'
    - '.fcgi'
    - '.scgi'
  url_access_deny:
    - '~'
    - '.inc'
lighttpd_server_bind_address: '0.0.0.0'
lighttpd_server_port: 80
````

Dependencies
------------

None  

Example Playbook
----------------

````
- hosts: test-nodes
  become: true
  vars:
    - pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-lighttpd
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
