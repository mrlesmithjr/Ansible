Role Name
=========

Installs and configures Gerrit Code Review...https://www.gerritcodereview.com/

Requirements
------------
Install all Ansible role requirements.
```
sudo ansible-galaxy install -r requirements.yml -f
```

Vagrant
-------
Spin up Environment under Vagrant to test.
```
vagrant up
```

Usage
-----

###### Non-Vagrant
Login to WebUI using defined owncloud_admin_user and owncloud_admin_pass vars (http://iporhostname:8080)

###### Vagrant
Login to WebUI using defined owncloud_admin_user and owncloud_admin_pass vars (http://127.0.0.1:8080)


Role Variables
--------------

```
---
# defaults file for ansible-gerrit
gerrit_account_info:
  name: gerrit  #defines username
  comment: Gerrit User  #defines username comment
  home: '{{ gerrit_site_dir }}'  #defines username home directory
  group: gerrit  #defines usernames groupname
gerrit_allow_remote_admin: false  #defines if gerrit should allow remote admin capabilities
gerrit_auth_type: OPENID  #defines authorization type...OPENID, LDAP, LDAP_BIND...
gerrit_canonical_web_url: http://{{ ansible_hostname }}.{{ pri_domain_name }}:{{ gerrit_http_listen_port }}/
gerrit_db_info:
  - host: localhost
    type: h2
    db: db/ReviewDB
    user: gerrit
    pass: gerrit
#  - host: localhost
#    type: mysql
#    db: reviewdb
#    user: gerrit
#    pass: gerrit
gerrit_dl_info:
  - url: https://gerrit-releases.storage.googleapis.com
    filename: 'gerrit-{{ gerrit_version }}.war'
    sha256sum: cb1794ccdf22da4e0ba5a431b832578017bbe53152ce028f46d2ebbb611705aa
gerrit_gitweb_integration: false  #defines is gerrit should be integrated with gitweb...gitweb is not controlled via gerrit using this method...
gerrit_http_listen_port: 8080
#gerrit_init: "java -jar {{ gerrit_install_dir }}/gerrit.war init --batch --no-auto-start -d {{ gerrit_site_dir }}"  #define this instead of the below to not setup plugins.
gerrit_init: "java -jar {{ gerrit_install_dir }}/gerrit.war init --batch --no-auto-start -d {{ gerrit_site_dir }} --install-plugin reviewnotes --install-plugin replication --install-plugin download-commands --install-plugin singleusergroup --install-plugin commit-message-length-validator"
gerrit_install_dir: /opt/gerrit
gerrit_install_plugins: false  #setting to false for now until plugin install method works...
gerrit_java_home: /usr/lib/jvm/java-7-openjdk-amd64/jre
gerrit_ldap_info:
  - server: 'ldap://dc01.{{ pri_domain_name }}'
    accountbase: 'DC=example,DC=org'
    accountpattern: '(&(objectClass=person)(userPrincipalName=${username}))'
    accountscope: 'sub'
    groupbase: 'DC=example,DC=org'
    accountfullname: 'displayName'
    accountmemberfield: 'memberOf'
    accountemailaddress: 'mail'
    accountsshusername: '${sAMAccountName.toLowerCase}'
    referral: 'follow'
gerrit_mysql_connector_file: mysql-connector-java-5.1.21.jar
gerrit_mysql_connector_url: http://repo2.maven.org/maven2/mysql/mysql-connector-java/5.1.21
gerrit_plugins:
  - url: https://storage.cloud.google.com/gerritcodereview-plugins/plugins/master/commit-message-length-validator
    name: commit-message-length-validator.jar
  - url: https://storage.cloud.google.com/gerritcodereview-plugins/plugins/master/download-commands
    name: download-commands.jar
  - url: https://gerrit-ci.gerritforge.com/job/plugin-github-mvn-stable-2.11/lastSuccessfulBuild/artifact/github-oauth/target
    name: github-oauth-2.11.jar
  - url: https://gerrit-ci.gerritforge.com/job/plugin-github-mvn-stable-2.11/lastSuccessfulBuild/artifact/github-plugin/target
    name: github-plugin-2.11.jar
  - url: https://storage.cloud.google.com/gerritcodereview-plugins/plugins/master/replication
    name: replication.jar
  - url: https://storage.cloud.google.com/gerritcodereview-plugins/plugins/master/reviewnotes
    name: reviewnotes.jar
  - url: https://storage.cloud.google.com/gerritcodereview-plugins/plugins/master/singleusergroup
    name: singleusergroup.jar
gerrit_replication_enabled: false  #defines if replication should be enabled or not
gerrit_replication_info:
  authgroup: 'Gitlab Replication'  #define the gerrit group to execute replication as..This group needs to be created in gerrit as well. and perms defined as below.
  name: 'gitlab'  #define name to assign to replication definition
  owner: 'infra'  #define username or groupname...if collaborating use groupname
  ssh_config_info:  #defines configuration of ~/.ssh/config....THIS WILL OVERWRITE WHAT IS THERE
    - host: 'gitlab.{{ pri_domain_name }}'
      user: '{{ gerrit_account_info.name }}'
      identityfile: '{{ gerrit_site_dir }}/.ssh/id_rsa'
      stricthostkeychecking: false
  threads: '3'  #defines the number of threads to allocate to replication
  timeout: '30'  #define the replication timeout
  url: 'git@gitlab.{{ pri_domain_name }}'  #define remote url
       ##Gitlab Replication allowed read to refs/* in in Project nameofproject (ex. test-replication)
       ##Gitlab Replication denied read to refs/* in all projects
       ##Group Name: Gitlab Replication
gerrit_service_name: gerrit
gerrit_site_dir: /var/gerrit
gerrit_smtp_server: 'smtp.{{ pri_domain_name }}'
gerrit_sshd_listen_port: 29418
gerrit_vagrant_install: false  #defines if deploying within a Vagrant environment
gerrit_version: 2.13.7
gitweb_cgi_path: /usr/share/gitweb/gitweb.cgi
pri_domain_name: example.org
```

Dependencies
------------

None

Example Playbook
----------------
```
---
- name: Installs Gerrit Code Review
  hosts: gerrit-servers
  sudo: true
  vars:
    - gerrit_db_info:
#        - host: localhost
#          type: h2
#          db: db/ReviewDB
#          user: gerrit
#          pass: gerrit
        - host: localhost
          type: mysql
          db: reviewdb
          user: gerrit
          pass: gerrit
    - install_mysql: true
  roles:
    - ansible-apache2
    - { role: ansible-mariadb-mysql, when: install_mysql is defined and install_mysql }
    - ansible-gerrit
  tasks:
```

Notes
-----
Portions of this role have been borrowed from https://github.com/kbrebanov/ansible-gerrit

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
