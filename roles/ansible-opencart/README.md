<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-opencart](#ansible-opencart)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-opencart

An [Ansible](https://www.ansible.com) role to install/configure [OpenCart](https://www.opencart.com/)

## Requirements

Install additional Ansible [required](requirements.yml) roles.

```bash
ansible-galaxy install -r requirements.yml
```

### Ubuntu Trusty

In order to successfully install using the example [playbook](playbook.yml) you
will need to comment out the `php{{ php_version_debian }}-zip` as this package is missing:

```yaml
php_debian_packages:
  - "libapache2-mod-php{{ php_version_debian }}"
  - "php{{ php_version_debian }}"
  - "php{{ php_version_debian }}-cli"
  - "php{{ php_version_debian }}-cgi"
  - "php{{ php_version_debian }}-curl"
  - "php{{ php_version_debian }}-gd"
  - "php{{ php_version_debian }}-json"
  - "php{{ php_version_debian }}-ldap"
  - "php{{ php_version_debian }}-mcrypt"
  - "php{{ php_version_debian }}-mysql"
#  - "php{{ php_version_debian }}-zip"
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

Reference [Requirements](#requirements)

## Example Playbook

[playbook.yml](playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
