# ansible-wordpress

An [Ansible](https://www.ansible.com) role to install/configure [Wordpress](https://wordpress.org)

## Requirements

Install Ansible required roles from `requirements.yml`:

```bash
ansible-galaxy install -r requirements.yml
```

## Role Variables

```yaml
---
# defaults file for ansible-wordpress
wordpress_db: wordpress
wordpress_db_user: wordpress
wordpress_db_password: wordpress
wordpress_db_host: localhost
wordpress_db_table_prefix: wp_
wordpress_dl_file: "wordpress-{{ wordpress_version }}.tar.gz"
wordpress_dl_uri: https://wordpress.org
wordpress_dl: "{{ wordpress_dl_uri }}/{{ wordpress_dl_file }}"
wordpress_version: 4.8.3
```

## Dependencies

Rererence [Requirements](#requirements)

## Example Playbook

[Example playbook](./playbook.yml)

## License

MIT

## Author Information

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](https://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
