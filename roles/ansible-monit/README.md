# Role Name

An [Ansible](https://www.ansible.com) role to install/configure [monit](https://mmonit.com/monit/)

## Requirements

None.

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None.

## Example Playbook

```yaml
---
- hosts: test-nodes
  vars:
    config_monit: true
    monit_enable_web_server: true
    monit_monitor_services:
      - name: 'cron'
        monitored: true
        pidfile: '/var/run/crond.pid'
        start_program: '/usr/sbin/service cron start'
        stop_program: '/usr/sbin/service cron stop'
      - name: 'docker'
        monitored: true
        pidfile: '/var/run/docker.pid'
        start_program: '/usr/sbin/service docker start'
        stop_program: '/usr/sbin/service docker stop'
      - name: 'ntp'
        action: 'restart'
        failed_host: 127.0.0.1
        failed_host_port: 123
        failed_host_type:
          - 'udp'
        monitored: true
        pidfile: '/var/run/ntpd.pid'
        start_program: '/usr/sbin/service ntp start'
        stop_program: '/usr/sbin/service ntp stop'
      - name: 'rsyslogd'
        monitored: true
        pidfile: '/var/run/rsyslogd.pid'
        start_program: '/usr/sbin/service rsyslog start'
        stop_program: '/usr/sbin/service rsyslog stop'
      - name: 'sshd'
        failed_host: 127.0.0.1
        failed_host_port: 22
        monitored: true
        pidfile: '/var/run/sshd.pid'
        start_program: '/usr/sbin/service ssh start'
        stop_program: '/usr/sbin/service ssh stop'
    monit_web_server_allow_list:
      - 192.168.0.0/16
      - localhost
    monit_web_server_local_only: false
    pri_domain_name: 'test.vagrant.local'
  roles:
    - name: Install/Configure Monitoring Of Services
      role: ansible-monit
    - name: Install Docker
      role: ansible-docker
  tasks:
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
