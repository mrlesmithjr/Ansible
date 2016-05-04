Role Name
=========

Installs and configures UFW (Uncomplicated Firewall) on Debian systems.

Requirements
------------

None

Role Variables
--------------

````
---
# defaults file for ansible-ufw
ufw_rules:  #defines rules to be configured...commented out lines are not required and will be defined with defaults as part of the task
  - rule: limit  #defines rule type...allow, deny, reject or limit (limit: ufw supports connection rate limiting, which is useful for protecting against brute-force login attacks)
#    delete: 'no'  #defines if rule should be deleted...yes or no
#    direction: in  #defines direction of traffic to apply rule against...in, out, incoming, outgoing or routed
#    from_ip: 1.2.3.4 #defines address to allow connections from
#    from_port: 12345  #defines from port for connection if desired
#    interface: eth0  #defines interface to allow connections on if desired
#    log: 'yes'  #defines if connections should be logged which match this rule
    proto: tcp  #defines protocol...any, tcp, udp, ipv6, esp or ah
#    to_ip: 1.2.3.4  #defines address to allow connections to
    to_port: 22  #defines port to allow connections to
ufw_logging: 'on'  #defines UFW logging...on, off, low, medium, high or full
ufw_policies:  #defines default policy for incoming, outgoing and routed (forwarded) traffic...allow, deny or reject
  - direction: incoming
    policy: deny
  - direction: outgoing
    policy: allow
  - direction: routed
    policy: deny
ufw_state: enabled  #defines UFW firewall state...enabled, disabled, reloaded or reset
````

Dependencies
------------

None

Example Playbook
----------------

#### Galaxy
-----------
    - hosts: servers
      vars:
        - ufw_rules:
            - rule: limit
              proto: tcp
              to_port: 22
            - rule: allow
              proto: tcp
              to_port: 80
            - rule: allow
              proto: tcp
              to_port: 443
      roles:
         - role: mrlesmithjr.ufw
#### GitHub
-----------
    - hosts: servers
      vars:
        - ufw_rules:
            - rule: limit
              proto: tcp
              to_port: 22
            - rule: allow
              proto: tcp
              to_port: 80
            - rule: allow
              proto: tcp
              to_port: 443
      roles:
        - role: ansible-ufw

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
