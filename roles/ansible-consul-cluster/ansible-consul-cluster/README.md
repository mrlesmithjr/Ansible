<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [ansible-consul-cluster](#ansible-consul-cluster)
    -   [Assumptions](#assumptions)
    -   [Requirements](#requirements)
    -   [Usage](#usage)
        -   [Spinning Up VMs](#spinning-up-vms)
            -   [Updating Variables](#updating-variables)
            -   [Spinning Up and Provisioning](#spinning-up-and-provisioning)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-consul-cluster

The purpose of this repo is to provision out a 3-node Consul cluster. The
inspiration behind this repo was a ready to roll Consul backend for Terraform.

## Assumptions

The following list of assumptions are made but may be adjusted as neccessary.

1.  Functional vSphere environment including vCenter.
2.  Ubuntu (preferred) VM template available in vCenter.
3.  DHCP is available to assign IP addresses to VMs when they spin up.

> NOTE: If you need an easy way to provision vSphere templates checkout my repo
> [Packer-For-vSphere-and-More](https://github.com/mrlesmithjr/Packer-For-vSphere-and-More).

## Requirements

Create `group_vars/all/accounts.yml` with the following contents (adapt to your
environment):

```yaml
---
# Defines Linux SSH password
ansible_password: packer

# Defines Linux SSH user
ansible_user: packer

# Defines vCenter password
vcenter_password: VMw@re1!

# Defines vCenter username
vcenter_username: administrator@vsphere.local
```

> NOTE: The above file is excluded from version control to ensure that account
> info is not leaked. You can also use `ansible-vault` if needed but you will
> need to remove `accounts.yml` from `.gitignore`.

## Usage

### Spinning Up VMs

#### Updating Variables

You will first need to spin up 3 VMs for the Consul cluster. These VMs are to
be provisioned in a vSphere environment.

Modify the following to meet your environment requirements:

1.  [group_vars/all/vms.yml](group_vars/all/vms.yml)
2.  [group_vars/all/dns.yml](group_vars/all/dns.yml)
3.  [group_vars/all/vcenter.yml](group_vars/all/vcenter.yml)

You also will need to adjust the following for Consul.

`group_vars/consul_cluster/consul.yml`:

```yaml
# Generated using 'uuidgen'
# make sure to generate a new token and replace this one
consul_acl_master_token: 7A993C85-1EA6-412D-85DB-DA14EFCD03AB

# Generate using 'consul keygen'
# make sure to generate a new key and replace this
# also update key if you changed the it in your cluster via 'consul keyring',
# otherwise the role may deploy an outdated key to additional nodes which then
# can't join the cluster
consul_encryption_key: OJVXXkKdwifyqc9BrDe1VQ==
```

#### Spinning Up and Provisioning

To spin up the VMs:

[provision_vms.yml](provision_vms.yml):

```bash
ansible-playbook provisioned_vms.yml
```

After the VMs have been provisioned, `hosts.inv` will be populated to use as
Ansible inventory.

To provision the VMs:

[playbook.yml](playbook.yml):

```bash
ansible-playbook -i hosts.inv playbook.yml
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
