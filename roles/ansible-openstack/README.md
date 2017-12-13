<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [ansible-openstack](#ansible-openstack)
    -   [Release Info](#release-info)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [Requirements](#requirements-1)
        -   [Install required Ansible roles](#install-required-ansible-roles)
    -   [Vagrant Testing](#vagrant-testing)
        -   [Requirements](#requirements-2)
    -   [TODO](#todo)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-openstack

This repo will be used as the main `OpenStack` repo to pull together all required
roles, execute playbooks, define default variables, and perform `Vagrant` testing.

> NOTE: This is a work in progress so there are likely components that do not
> currently work.
> So please do not expect things to happen quickly as I am the sole person
> working on this. I attempted this several years ago with the [Kilo Release](https://github.com/mrlesmithjr/ansible-openstack-old) and never really
> liked the way it turned out so this is a complete rewrite.

## Release Info

This is currently based on the [Ocata Release](https://docs.openstack.org/ocata/)

## Requirements

## Role Variables

## Dependencies

## Example Playbook

[Example Playbook](./playbook.yml)

## Requirements

### Install required Ansible roles

From the root of this repo execute the following:

```bash
./install_required_ansible_roles.sh
```

## Vagrant Testing

### Requirements

-   Install [required Ansible roles](#requirements-install-required-ansible-roles)

## TODO

-   [ ] Create the following Ansible roles
    -   [x] Identity service(keystone)
    -   [ ] Image service(glance)
    -   [ ] Compute service(nova)
    -   [ ] Networking service(neutron)
    -   [ ] Dashboard(horizon)
    -   [ ] Block Storage service
    -   [ ] Bare Metal service(ironic)
    -   [ ] Container Infrastructure Management service(magnum)
    -   [ ] Database service(trove)
    -   [ ] DNS Service(designate)
    -   [ ] Key Manager service(barbican)
    -   [ ] Messaging service(zaqar)
    -   [ ] Object Storage services(swift)
    -   [ ] Orchestration service(heat)
    -   [ ] Shared File Systems service(manila)
    -   [ ] Telemetry Alarming services(aodh)
    -   [ ] Telemetry Data Collection service(ceilometer)
-   [ ] Implement HA
    -   [ ] HAProxy
    -   [ ] Pacemaker
    -   [ ] Identity service(keystone)
    -   [ ] Image service(glance)
    -   [ ] Compute service(nova)
    -   [ ] Networking service(neutron)
    -   [ ] Dashboard(horizon)

> NOTE: The above roles may be created but not complete. Additional work will more
> than likely need to be performed to get them to a complete functional state.

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
    [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   mrlesmithjr [at] gmail.com
