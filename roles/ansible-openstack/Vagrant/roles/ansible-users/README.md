Role Name
=========

Manages local users on systems.

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-users
create_local_users: true  #defines creating local user accounts on hosts
create_users:  #defines user accounts to setup on hosts....define here or in group_vars/all
  - user: demo_user  #define username
    comment: 'Demo user'  #define a comment to associate with the account
    generate_keys: true  #generate ssh keys...( true|false )
#    home: ''  #define a different home directory... ''=/home/username
    pass: demo_password  #define password for account
#    shell: ''  #define a different shell for the user
    preseed_user: false  #defines if user should be setup as default user during preseed auto-install...Only 1 user can be added...used in tftpserver Ansible role (mrlesmithjr.tftpserver or ansible-tftpserver)
    state: absent  #defines whether account exists or not ( absent|present )
    sudo: false  #define if user should have sudo access...( true|false )
    system_account: false  #define if account is a system account...( true|false )
````

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.users }

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
