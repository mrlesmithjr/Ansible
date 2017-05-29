Role Name
=========

An [Ansible] role to install/configure [SSHD]
- Obviously [SSHD] is already installed if managing remotely with [Ansible].
However, using `ansible-pull` could benefit from this and/or manually running
this playbook on a system to install [SSHD]. The configuration ability is
useful in any manner.

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-sshd
# all variables with yes or no must be defined as such including wrapping them
# in '' to ensure the variable is not converted to a boolean

# Specifies what environment variables sent by the client will be copied into
# the session's environ(7)
sshd_accept_env: 'LANG LC_*'

# This keyword can be followed by a list of group name patterns, separated by
# spaces. If specified, login is allowed only for users whose primary group or
# supplementary group list matches one of the patterns. Only group names are
# valid; a numerical group ID is not recognized. By default, login is allowed
# for all groups. The allow/deny directives are processed in the following
# order: DenyUsers, AllowUsers, DenyGroups, and finally AllowGroups.
sshd_allow_groups: []
  # - 'adm'
  # - 'ssh_users'

# This keyword can be followed by a list of user name patterns, separated by
# spaces. If specified, login is allowed only for user names that match one of
# the patterns. Only user names are valid; a numerical user ID is not
# recognized. By default, login is allowed for all users. If the pattern
# takes the form USER@HOST then USER and HOST are separately checked,
# restricting logins to particular users from particular hosts. HOST criteria
# may additionally contain addresses to match in CIDR address/masklen format.
# The allow/deny directives are processed in the following order: DenyUsers,
# AllowUsers, DenyGroups, and finally AllowGroups.
sshd_allow_users: []
  # - 'vagrant'
  # - 'admin'

# Specifies whether TCP forwarding is permitted. The available options are
# yes (the default) or all to allow TCP forwarding, no to prevent all TCP
# forwarding, local to allow local (from the perspective of ssh(1)) forwarding
# only or remote to allow remote forwarding only. Note that disabling TCP
# forwarding does not improve security unless users are also denied shell
# access, as they can always install their own forwarders.
sshd_allow_tcp_forwarding: 'yes'

# Specifies the file that contains the public keys used for user authentication.
# Alternately this option may be set to none to skip checking for user keys in
# files.
# The default is “.ssh/authorized_keys .ssh/authorized_keys2”
sshd_authorized_keys_file: '%h/.ssh/authorized_keys'

# The contents of the specified file are sent to the remote user before
# authentication is allowed. If the argument is none then no banner is
# displayed. By default, no banner is displayed.
sshd_banner: []

# Specifies whether challenge-response authentication is allowed. All
# authentication styles from login.conf(5) are supported. The default is yes.
sshd_challenge_response_authentication: 'yes'

# Specifies whether compression is enabled after the user has authenticated
# successfully. The argument must be yes, delayed (a legacy synonym for yes)
# or no. The default is yes
sshd_compression: 'yes'

sshd_config: true

# This keyword can be followed by a list of group name patterns, separated by
# spaces. Login is disallowed for users whose primary group or supplementary
# group list matches one of the patterns. Only group names are valid; a
# numerical group ID is not recognized. By default, login is allowed for
# all groups. The allow/deny directives are processed in the following
# order: DenyUsers, AllowUsers, DenyGroups, and finally AllowGroups.
sshd_deny_groups: []
  # - 'badguys'

# This keyword can be followed by a list of user name patterns, separated by
# spaces. Login is disallowed for user names that match one of the patterns.
# Only user names are valid; a numerical user ID is not recognized.
# By default, login is allowed for all users. If the pattern takes the form
# USER@HOST then USER and HOST are separately checked, restricting logins to
# particular users from particular hosts. HOST criteria may additionally
# contain addresses to match in CIDR address/masklen format. The allow/deny
# directives are processed in the following order: DenyUsers, AllowUsers,
# DenyGroups, and finally AllowGroups.
sshd_deny_users: []
  # - 'baduser'

# Specifies whether user authentication based on GSSAPI is allowed.
# The default is no.
sshd_gssapi_authentication: 'no'

# Specifies whether to automatically destroy the user's credentials cache on
# logout. The default is yes.
sshd_gssapi_cleanup_credentials: 'yes'

# Specifies whether rhosts or /etc/hosts.equiv authentication together with
# successful public key client host authentication is allowed
# (host-based authentication). The default is no.
sshd_host_based_authentication: 'no'

# Specifies a file containing a private host key used by SSH.
# The defaults are /etc/ssh/ssh_host_dsa_key, /etc/ssh/ssh_host_ecdsa_key,
# /etc/ssh/ssh_host_ed25519_key and /etc/ssh/ssh_host_rsa_key.
sshd_host_keys:
  - '/etc/ssh/ssh_host_rsa_key'
  - '/etc/ssh/ssh_host_dsa_key'
  - '/etc/ssh/ssh_host_ecdsa_key'
  - '/etc/ssh/ssh_host_ed25519_key'

# Specifies that .rhosts and .shosts files will not be used in HostbasedAuthentication.
# /etc/hosts.equiv and /etc/shosts.equiv are still used. The default is yes.
sshd_ignore_rhosts: 'yes'

# Specifies whether sshd(8) should ignore the user's ~/.ssh/known_hosts during
# HostbasedAuthentication. The default is no.
sshd_ignore_user_known_hosts: 'no'

sshd_key_regeneration_interval: '3600'

# Specifies the local addresses sshd(8) should listen on
sshd_listen_addresses:
  - '0.0.0.0'
  - '::'

# Gives the verbosity level that is used when logging messages from sshd(8).
# The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1,
# DEBUG2, and DEBUG3. The default is INFO. DEBUG and DEBUG1 are equivalent.
# DEBUG2 and DEBUG3 each specify higher levels of debugging output.
# Logging with a DEBUG level violates the privacy of users and is not recommended.
sshd_log_level: 'INFO'

# The server disconnects after this time if the user has not successfully
# logged in. If the value is 0, there is no time limit.
# The default is 120 seconds.
sshd_login_grace_time: '120'

# Specifies the maximum number of concurrent unauthenticated connections to
# the SSH daemon. Additional connections will be dropped until authentication
# succeeds or the LoginGraceTime expires for a connection.
# The default is 10:30:100.
sshd_max_startups: '10:30:100'

# Specifies whether password authentication is allowed. The default is yes
sshd_password_authentication: 'yes'

# When password authentication is allowed, it specifies whether the server
# allows login to accounts with empty password strings. The default is no.
sshd_permit_empty_passwords: 'no'

# Specifies whether root can log in using ssh(1). The argument must be yes,
# prohibit-password, without-password, forced-commands-only, or no.
# The default is prohibit-password.
sshd_permit_root_login: 'no'

# Specifies the port number that sshd(8) listens on. The default is 22.
sshd_ports:
  - '22'

# Specifies whether sshd(8) should print the date and time of the last user
# login when a user logs in interactively. The default is yes.
sshd_print_lastlog: 'yes'

# Specifies whether sshd(8) should print /etc/motd when a user logs in
# interactively. (On some systems it is also printed by the shell, /etc/profile,
# or equivalent.) The default is yes.
sshd_print_motd: 'yes'

sshd_protocol: '2'

# Specifies whether public key authentication is allowed. The default is yes
sshd_pubkey_authentication: 'yes'

sshd_rhosts_rsa_authentication: 'no'
sshd_rsa_authentication: 'yes'

sshd_server_key_bits: '1024'

# Specifies whether sshd(8) should check file modes and ownership of the
# user's files and home directory before accepting login. This is normally
# desirable because novices sometimes accidentally leave their directory or
# files world-writable. The default is yes
sshd_strict_modes: 'yes'

# Configures an external subsystem (e.g. file transfer daemon). Arguments
# should be a subsystem name and a command (with optional arguments) to execute
# upon subsystem request.
# The command sftp-server implements the SFTP file transfer subsystem.
# Alternately the name internal-sftp implements an in-process SFTP server.
# This may simplify configurations using ChrootDirectory to force a different
# filesystem root on clients.
# By default no subsystems are defined.
sshd_subsystem: 'sftp /usr/lib/openssh/sftp-server'

# Gives the facility code that is used when logging messages from sshd(8).
# The possible values are: DAEMON, USER, AUTH, LOCAL0, LOCAL1, LOCAL2, LOCAL3,
# LOCAL4, LOCAL5, LOCAL6, LOCAL7. The default is AUTH.
sshd_syslog_facility: 'AUTH'

# Specifies whether the system should send TCP keepalive messages to the other
# side. If they are sent, death of the connection or crash of one of the
# machines will be properly noticed. However, this means that connections will
# die if the route is down temporarily, and some people find it annoying. On
# the other hand, if TCP keepalives are not sent, sessions may hang indefinitely
# on the server, leaving “ghost” users and consuming server resources.
# The default is yes (to send TCP keepalive messages), and the server will
# notice if the network goes down or the client host crashes. This avoids
# infinitely hanging sessions.
# To disable TCP keepalive messages, the value should be set to no.
sshd_tcp_keep_alive: 'yes'

# Specifies whether sshd(8) should look up the remote host name, and to check
# that the resolved host name for the remote IP address maps back to the very
# same IP address.
# If this option is set to no (the default) then only addresses and not host
# names may be used in ~/.ssh/authorized_keys from and sshd_config Match
# Host directives.
sshd_use_dns: 'no'

sshd_use_pam: 'yes'
sshd_use_privilege_separation: 'yes'

# Specifies the first display number available for sshd(8)'s X11 forwarding.
# This prevents sshd from interfering with real X11 servers. The default is 10.
sshd_x11_display_offset: '10'

# Specifies whether X11 forwarding is permitted. The argument must be yes or no.
# The default is no.
sshd_x11_forwarding: 'yes'
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
    - role: ansible-sshd
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
[SSHD]: <https://www.ssh.com/ssh/sshd/>
