Role Name
=========

Installs postfix http://www.postfix.org/

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

````
# defaults file for ansible-postfix
configure_postfix: false  #defines if postfix should be configured
enable_postfix_domain_rewrite: false  #defines if outgoing email domain should be changed
enable_postfix_relayhost: false  #defines if a relay host should be used
postfix_conf_dir: /etc/postfix
postfix_mynetworks:  #defines which networks are allowed to relay through postfix server...this is defined for all nodes which have roles/postfix applied
  - 127.0.0.0/8
#  - 10.0.101.0/24
#  - 172.16.0.0/16
#  - 192.168.0.0/16
postfix_relayhost: '[smtp.example.org]'  #define smtp relay server...define here or globally in group_vars/all
postfix_rewrite_domain: example.org  #defines what domain all outgoing email should be set to for @domain.example...should be the same as smtp_domain_name
postfix_use_tls: true  #defines if tls should be used or not

# enable 'sender_canonical_maps = regexp:/etc/postfix/sender_canonical' in main.cf
enable_sender_canonical: false
# if enable_sender_canonical == true, use mappings set in...
postfix_sender_canonical_maps:
  - "/^(.*@)example.com$/     ${1}example.co.uk"

# Can be set to 'hash' or 'regexp' filetype
postfix_domain_rewrite_filetype: hash

# set which template to use for generic maps file
# values are currently the original 'generic.j2' or
# the more flexible 'altgeneric.j2'
postfix_generic_template: generic.j2

# when using the 'altgeneric.j2' template, use mappings set in...
postfix_altgeneric_maps:
  - "/^(.*@)something.com$/     ${1}somethingelse.co.uk"

````

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrlesmithjr.postfix }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
