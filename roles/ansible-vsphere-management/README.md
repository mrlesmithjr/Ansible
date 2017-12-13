<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [ansible-vsphere-management](#ansible-vsphere-management)
  - [Requirements](#requirements)
    - [Ansible Version >= 2.4.x.x](#ansible-version--24xx)
    - [inventory/hosts.0.inv](#inventoryhosts0inv)
    - [inventory/group_vars/all/accounts.yml](#inventorygroup_varsallaccountsyml)
    - [inventory/group_vars/all/vsphere_hosts.yml](#inventorygroup_varsallvsphere_hostsyml)
    - [Windows 2012R2/2016 Host](#windows-2012r22016-host)
    - [inventory/host_vars](#inventoryhost_vars)
    - [Software iSCSI](#software-iscsi)
      - [Managing Software iSCSI Adapter](#managing-software-iscsi-adapter)
    - [VCSA ISO](#vcsa-iso)
  - [Deployment Host](#deployment-host)
    - [Spinning It Up](#spinning-it-up)
  - [Environment Deployment](#environment-deployment)
    - [Deployment Script Functions](#deployment-script-functions)
  - [Destroying Core Services VMs](#destroying-core-services-vms)
  - [Defining Environmental Variables](#defining-environmental-variables)
  - [Bootstrap VMs](#bootstrap-vms)
  - [DNSDist VMs](#dnsdist-vms)
  - [DDI VMs](#ddi-vms)
    - [Autostart DDI VMs](#autostart-ddi-vms)
    - [Defining DDI VMs](#defining-ddi-vms)
    - [Defining DNS Records](#defining-dns-records)
    - [Future DDI Functionality](#future-ddi-functionality)
  - [Samba based Active Directory](#samba-based-active-directory)
    - [Creating Samba AD Users and Groups](#creating-samba-ad-users-and-groups)
    - [vSphere Host(s)](#vsphere-hosts)
      - [Host Domain Membership](#host-domain-membership)
      - [Host User Roles Domain Permissions](#host-user-roles-domain-permissions)
  - [VCSA](#vcsa)
    - [Defining VCSA Specifics](#defining-vcsa-specifics)
      - [Default definitions](#default-definitions)
      - [Deployment definitions](#deployment-definitions)
    - [Sizing](#sizing)
  - [Terraform Infrastructure Deployment](#terraform-infrastructure-deployment)
    - [Defining Terraform Infrastructure](#defining-terraform-infrastructure)
    - [Deploying Terraform Infrastructure](#deploying-terraform-infrastructure)
  - [Role Variables](#role-variables)
  - [Dependencies](#dependencies)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-vsphere-management

The purpose of this repo is to provide the automation of `vSphere` environments
using `Ansible`. Most of the tasks in this repo will be written initially as
`win_shell` tasks which require `Powershell` and `PowerCLI`. There are many
`Ansible` modules specific to [VMware Cloud Modules](http://docs.ansible.com/ansible/latest/list_of_cloud_modules.html#vmware)
however, the majority of them are lacking functionality or simply do not work. My
goal with this is to have the ability to build from scratch a `vSphere` environment
with many different options to define the infrastructure. Another focus on using
the `win_shell` module I wanted to ensure idempotency on tasks in order to not
just throw a bunch of `Powershell` and `PowerCLI` commands around. But rather
build the logic in to only do something when something truly needs to be done. The
issue currently with this is that some if not most of the `win_shell` tasks show
as changes however, if you watch your `vSphere` host tasks you will not see things
change unless something was required to change. This repo will be continually a
work in progress so do not expect perfection.

> NOTE: As this progresses you will notice that the focus around strict policy
> enforcement is growing. The reason behind that is because the goal should be
> that mostly everything in the environment should be defined as code. If manual
> changes occur outside of the code this can lead to an unmanaged environment.
> By enforcing strict policies, we can ensure that the environment is stable.
> This is something that should exist but unfortunately most environments do not
> follow this. Which means that this strict policy enforcement may not be suitable
> for each environment. Over time the ability to enable/disable enforcement will
> grow allowing for more flexibility.

## Requirements

### Ansible Version >= 2.4.x.x

Because of the discovery required for VMs, Ansible version must be at least 2.4.x.x

### inventory/hosts.0.inv

Adjust `inventory/hosts.0.inv` to include your Windows `powecli_host`.

```yaml
[powercli_host]
node0 ansible_ssh_host=192.168.250.10
```

### inventory/group_vars/all/accounts.yml

This file is intentionally added to `.gitignore` to ensure that passwords do not
leak. We will eventually use `ansible-vault` to encrypt this file as well in
order to add additional security measures in place. You must create this file
manually and it should look similar to below:

```yaml
---
powercli_host_user_info:
  password: vagrant
  username: vagrant

samba_domain_groups:
  - name: vSphere-Admins
    members:
      - administrator
      - vSphere-Admin

samba_domain_users:
  - name: vSphere-Admin
    password: P@55w0rd

vsphere_bootstrap_user_info:
  username: ubuntu
  password: ubuntu

# roles can be NoAccess, Anonymous, View, ReadOnly, Admin
vsphere_domain_access:
  - name: "{{ vsphere_ad_netbios_name|upper }}\\vSphere-Admins"
    role: Admin

vsphere_samba_ad_password: P@55w0rd
vsphere_samba_ad_user: administrator

vsphere_user_info:
  username: root
  password: VMw@re1

vsphere_vcsa_sso_user_info:
  username: "Administrator@{{ vsphere_vcsa_sso_domain_name }}"
  password: VMw@re1!

vsphere_vcsa_user_info:
  username: root
  password: VMw@re1!
```

### inventory/group_vars/all/vsphere_hosts.yml

> NOTE: `inventory/group_vars/all/vsphere_hosts.yml` is where to add your ESXi
> hosts. `defaults/main.yml` can also be used but I recommend you don't do it
> here.

`inventory/group_vars/all/vsphere_hosts.yml` is used to dynamically generate
an Ansible group `vsphere_hosts` which is used throughout this project.
`tasks/set_facts.yml` is executed whenever is needed and will by default generate
`inventory/vsphere_hosts.inv` for Ansible inventory on your ESXi hosts. This
ensures that the first deployment, the `vsphere_hosts` group is dynamically
created and available throughout the play and subsequent plays will leverage
`inventory/vsphere_hosts.inv` for Ansible inventory of your ESXi hosts. This
alleviates the need to always update your inventory and just let the tasks update
the inventory as needed.

Make sure to update [inventory/group_vars/all/vsphere_hosts.yml](inventory/group_vars/all/vsphere_hosts.yml)

### Windows 2012R2/2016 Host

Because most of the tasks in this repo use the `win_shell` module a `Windows 2012R2/2016`
host is required. The plus side to this is that I have already created the `Ansible`
roles to properly prep this host to get up and running quickly as well as a playbook.

-   [ansible-windows-powercli](https://github.com/mrlesmithjr/ansible-windows-powercli)
-   [ansible-windows-remote-desktop](https://github.com/mrlesmithjr/ansible-windows-remote-desktop)

```yaml
---
- hosts: powercli_host
  roles:
    - role: ansible-windows-powercli
    - role: ansible-windows-remote-desktop
    - role: ansible-vsphere-management
      when: inventory_hostname == groups['powercli_host'][0]
  tasks:
    - name: Install NET-Framework-Core
      win_feature:
        name: NET-Framework-Core
        state: present

    - name: Rebooting Server
      win_reboot:
        shutdown_timeout: 3600
        reboot_timeout: 3600
      when: ansible_reboot_pending

    - name: Install vmwarevsphereclient
      win_chocolatey:
        name: vmwarevsphereclient
        state: present
```

### inventory/host_vars

> NOTE: As of current, `inventory/host_vars/*/generated_details.yml` is excluded
> in `.gitignore` to ensure that they do not cause issues for anyone. Keep this
> in mind if you decide to use `host_vars`.

Currently the only `host_vars` which are generated are for the Core Services
VMs. We are doing this to have them available to subsequent tasks and etc. which
may require them. They will be accounted for and kept current throughout the
management tasks.

### Software iSCSI

Because we iterate over `groups['vsphere_hosts']` to capture
`hostvars` variables. The following variable `vsphere_enable_software_iscsi`
needs to be defined as one of the examples below.

> NOTE: By default defining this variable only in this roles `defaults/main.yml`
> does not have any effect on whether the iSCSI Software Adapter is enabled or
> not.

`host_vars/esxi-01/iscsi.yml`

```yaml
---
vsphere_enable_software_iscsi: true
```

`group_vars/vsphere_hosts/iscsi.yml`

```yaml
---
vsphere_enable_software_iscsi: true
```

#### Managing Software iSCSI Adapter

We currently have the ability to:

-   enable/disable adapter
-   configure target portal IP addresses

### VCSA ISO

In order to deploy the `VCSA` you will need to obtain the `ISO` and extract it
to a folder on the [Deployment Host](deployment-host) and define the following
variable in `inventory/group_vars/all/environment.yml`:

```yaml
vsphere_vcsa_iso_directory: C:\vagrant\vApps\VCSA_ISO
```

> NOTE: Because we are using Vagrant for the deployment host it makes this
> relatively easy. The Vagrant folder is mounted by default so we can just extract
> to `Vagrant/vApps`. This folder is added to `.gitignore` so anything in this
> folder will not be added to the GIT repo.

## Deployment Host

Included is a `Vagrant` environment in which you can use for your deployments. It
is a working `Windows 2016` server which will be autoprovisioned on bootup. The
`Vagrantfile` is set to bring this up in headless mode but you will be able to
remote desktop to the server. The reason this is brought up in headless mode is
because it will allow the `Vagrant` environment to be spun up on a remote system.
This will provide the ability to still run `Powershell` and `PowerCLI` scripts
against it.

### Spinning It Up

```bash
cd /Vagrant
vagrant up
```

After all provisioning is complete use remote desktop and connect to `192.168.250.10`
and on the desktop double click `extend-trial.cmd` to extend the trial license,
otherwise the server will shutdown every 30 minutes or so. And then reboot.

## Environment Deployment

Currently there is a script which will provision everything after the [Deployment Host](#deployment_host) is deployed. The script is [vsphere_management.sh](scripts/vsphere_management.sh). This script will likely
include the [Deployment Host](#deployment_host) deployment at some point as well
seeing as this deployment initially includes the Windows Vagrant box to do all
of the deployments.

### Deployment Script Functions

> NOTE: We have started building in functions into the provisioning [script](scripts/vsphere_management.sh) in order to provide the functionality to call a certain set of provisioning
> tasks rather than running the whole script from beginning to end or having to
> comment out portions of the script.

The deployment script has now become the main method to deloy. We have now
included help for the script usage. Which you can use to help understand how to
use the script.

```bash
vsphere_management.sh --help
```

```raw
vSphere Management Script

This script is for managing your vSphere environment in a holistic fashion.

Twitter:	https://www.twitter.com/mrlesmithjr
Blog:		http://www.everythingshouldbevirtual.com
Blog:		http://mrlesmithjr.com
Email:		mrlesmithjr@gmail.com

This script requires one of the following arguments to be passed in order to perform a task.

Usage:

vsphere_management.sh [arguments]


arguments:
	cleanup					Cleans up generated inventory, JSON data, and SSH key data
	deploy_all				Deploys whole environment
	deployment_host_halt			Halts Vagrant Deployment Host
	deployment_host_spinup			Spins up Vagrant Deployment Host and preps environment
	deployment_host_teardown		Tears down Vagrant Deployment Host
	vsphere_ad_domain			Manages vSphere hosts AD membership
	vsphere_bootstrap_vms			Manages Bootstrap VMs
	vsphere_ddi_vms				Manages DDI VMs
	vsphere_destroy_vms			Destroys ALL Core VM Service VMs (USE WITH CAUTION)
	vsphere_disable_ssh			Disables vSphere hosts SSH
	vsphere_dns				Manages vSphere hosts DNS settings
	vsphere_dnsdist_vms			Manages DNSDist VMs
	vsphere_enable_ssh			Enables vSphere hosts SSH
	vsphere_generate_host_vars		Generates host_vars for Core VMs
	vsphere_lb_vms				Manages Load Balancer VMs
	vsphere_maintenance_mode		Manages vSphere hosts maintenance mode
	vsphere_management			Manages ALL vSphere host settings
	vsphere_network				Manages vSphere hosts network settings
	vsphere_pdns				Manages PowerDNS zones, records, and etc.
	vsphere_post_deployment_reboot		Performs a post deployment reboot (Only if not already performed)
	vsphere_post_samba_deployment_reboot	Performs a post Samba deployment reboot (Only if not already performed)
	vsphere_samba_phase_1			Manages Samba VMs Stage 1 tasks (Does not install Samba)
	vsphere_samba_phase_2			Manages Samba VMs Stage 2 tasks (Installs Samba and sets up AD)
	vsphere_samba_sysvol_replication	Manages Samba VMs AD SysVol Replication
	vsphere_samba_vms			Manages Samba VMs (Does not perform Phase 1, 2, or SysVol Replication)
	vsphere_ssh_key_distribution		Distributes SSH Keys between VMs (Currently only Samba VMs)
	vsphere_terraform_apply			Applies the defined Terraform plan to reach the desired state of the configuration
	vsphere_terraform_deploy		All-in-one (init, plan, and apply)
	vsphere_terraform_destroy		Destroys the Terraform infrastructure
	vsphere_terraform_init			Initializes the Terraform working directory
	vsphere_terraform_inventory		Manages VMs Inventory Provisioned Using Terraform And Updates PDNS
	vsphere_terraform_plan			Shows the Terraform plan and shows what changes will be made
	vsphere_udpates				Updates vSphere Hosts (Must be in maintenance mode)
	vsphere_vcsa				Manages the vSphere VCSA Appliance
	vsphere_vcsa_ad				Manages VCSA Domain Membership
	vsphere_vcenter				Manages vCenter
	vsphere_vcenter_check			Checks if vCenter exists or not
	vsphere_vms				Manages ALL VMs (Does not perform any post provisioning tasks)
	vsphere_vms_info			Collects info for ALL VMs and updates inventory and etc.


All arguments support additional Ansible command line arguments to be passed. However, only the following
support passing a --limit most of the tasks run against the power_cli_host so the task will be
skipped as no hosts will be found that match.

Usage:

vsphere_management.sh [arguments] [--argument]


Example:
	vsphere_management.sh vsphere_maintenance_mode --extra-vars '{"vsphere_enable_software_iscsi": True}'

additional arguments which support --limit to be passed:

		vsphere_post_deployment_reboot
		vsphere_post_samba_deployment_reboot
		vsphere_samba_phase_1
		vsphere_samba_phase_2
		vsphere_samba_sysvol_replication
		vsphere_ssh_key_distribution

Example:
	vsphere_management.sh vsphere_post_deployment_reboot --limit node0.vagrant.local
```

So for example, say we would like to redistribute SSH Keys. We could just run
the following:

```bash
./scripts/vsphere_management.sh vsphere_ssh_key_distribution

...
logs already exists
 [WARNING]: Found both group and host with same name: samba-dc-02.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: samba-dc-00.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: samba-dc-01.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: ddi-02.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: ddi-00.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: dnsdist-01.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: ddi-01.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: lb-01.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: dnsdist-00.lab.etsbv.internal

 [WARNING]: Found both group and host with same name: lb-00.lab.etsbv.internal


PLAY [vsphere_samba_vms] *************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************************************************************************
ok: [samba-dc-00.lab.etsbv.internal]
ok: [samba-dc-01.lab.etsbv.internal]
ok: [samba-dc-02.lab.etsbv.internal]

TASK [Generating User(s) SSH Key] ****************************************************************************************************************************************************************************************************************
ok: [samba-dc-02.lab.etsbv.internal] => (item=ubuntu)
ok: [samba-dc-01.lab.etsbv.internal] => (item=ubuntu)
ok: [samba-dc-00.lab.etsbv.internal] => (item=ubuntu)

TASK [Scan And Register SSH Host Keys (hostname)] ************************************************************************************************************************************************************************************************
ok: [samba-dc-01.lab.etsbv.internal -> localhost] => (item=samba-dc-00.lab.etsbv.internal)
ok: [samba-dc-00.lab.etsbv.internal -> localhost] => (item=samba-dc-00.lab.etsbv.internal)
ok: [samba-dc-02.lab.etsbv.internal -> localhost] => (item=samba-dc-00.lab.etsbv.internal)
ok: [samba-dc-02.lab.etsbv.internal -> localhost] => (item=samba-dc-01.lab.etsbv.internal)
ok: [samba-dc-01.lab.etsbv.internal -> localhost] => (item=samba-dc-01.lab.etsbv.internal)
ok: [samba-dc-00.lab.etsbv.internal -> localhost] => (item=samba-dc-01.lab.etsbv.internal)
ok: [samba-dc-02.lab.etsbv.internal -> localhost] => (item=samba-dc-02.lab.etsbv.internal)
ok: [samba-dc-00.lab.etsbv.internal -> localhost] => (item=samba-dc-02.lab.etsbv.internal)
ok: [samba-dc-01.lab.etsbv.internal -> localhost] => (item=samba-dc-02.lab.etsbv.internal)

TASK [Scan And Register SSH Host Keys (IP)] ******************************************************************************************************************************************************************************************************
ok: [samba-dc-01.lab.etsbv.internal -> localhost] => (item=samba-dc-00.lab.etsbv.internal)
ok: [samba-dc-00.lab.etsbv.internal -> localhost] => (item=samba-dc-00.lab.etsbv.internal)
ok: [samba-dc-02.lab.etsbv.internal -> localhost] => (item=samba-dc-00.lab.etsbv.internal)
ok: [samba-dc-01.lab.etsbv.internal -> localhost] => (item=samba-dc-01.lab.etsbv.internal)
ok: [samba-dc-02.lab.etsbv.internal -> localhost] => (item=samba-dc-01.lab.etsbv.internal)
ok: [samba-dc-00.lab.etsbv.internal -> localhost] => (item=samba-dc-01.lab.etsbv.internal)
ok: [samba-dc-01.lab.etsbv.internal -> localhost] => (item=samba-dc-02.lab.etsbv.internal)
ok: [samba-dc-00.lab.etsbv.internal -> localhost] => (item=samba-dc-02.lab.etsbv.internal)
ok: [samba-dc-02.lab.etsbv.internal -> localhost] => (item=samba-dc-02.lab.etsbv.internal)

TASK [Write SSH Host Keys] ***********************************************************************************************************************************************************************************************************************
changed: [samba-dc-00.lab.etsbv.internal]
changed: [samba-dc-01.lab.etsbv.internal]
changed: [samba-dc-02.lab.etsbv.internal]

TASK [Capturing SSH Keys] ************************************************************************************************************************************************************************************************************************
ok: [samba-dc-00.lab.etsbv.internal] => (item=ubuntu)
ok: [samba-dc-01.lab.etsbv.internal] => (item=ubuntu)
ok: [samba-dc-02.lab.etsbv.internal] => (item=ubuntu)

TASK [Generating SSH Keys] ***********************************************************************************************************************************************************************************************************************
ok: [samba-dc-00.lab.etsbv.internal -> localhost]

PLAY [vsphere_samba_vms] *************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************************************************************************
ok: [samba-dc-00.lab.etsbv.internal]
ok: [samba-dc-01.lab.etsbv.internal]
ok: [samba-dc-02.lab.etsbv.internal]

TASK [Adding SSH Keys] ***************************************************************************************************************************************************************************************************************************
skipping: [samba-dc-00.lab.etsbv.internal] => (item=({u'host': u'samba-dc-00.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCY4AUT/vi441NBib+MC8f1uaHIS+5kIfIoKQbKWvPd/WNFk/A9imz1MiN/vPpc3FFFrv7WxqkLGBcSNT21sflUfTStLkOGhhWL1IsbylRBFBw/mP7VNat+/dDNiUYiroYqGjq5HXCr1Xd6jll6BgBtune3hPQ5u/fdDXAD+XdHetErsW6zh0e7gNyL1IDZx4QRHNtS9qf0esiVLFKJpFvU3pix2PFvRw37/hVcsUUASZOpfVtXSOUEeX1Ifu6nCv+ev3WvUKqrDg81myHseNwTaeAFsv2dYBn28cE99cdl8m+AT1L7Zn1ucS7Dk6GsvWjlTRJuUv7VmWyoq5s6Otwd ansible-generated on samba-dc-00'}))
ok: [samba-dc-02.lab.etsbv.internal] => (item=({u'host': u'samba-dc-00.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCY4AUT/vi441NBib+MC8f1uaHIS+5kIfIoKQbKWvPd/WNFk/A9imz1MiN/vPpc3FFFrv7WxqkLGBcSNT21sflUfTStLkOGhhWL1IsbylRBFBw/mP7VNat+/dDNiUYiroYqGjq5HXCr1Xd6jll6BgBtune3hPQ5u/fdDXAD+XdHetErsW6zh0e7gNyL1IDZx4QRHNtS9qf0esiVLFKJpFvU3pix2PFvRw37/hVcsUUASZOpfVtXSOUEeX1Ifu6nCv+ev3WvUKqrDg81myHseNwTaeAFsv2dYBn28cE99cdl8m+AT1L7Zn1ucS7Dk6GsvWjlTRJuUv7VmWyoq5s6Otwd ansible-generated on samba-dc-00'}))
ok: [samba-dc-00.lab.etsbv.internal] => (item=({u'host': u'samba-dc-01.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDnkOKiRieDN6QKQhgpT98qROLebPtsEE9q+o0I9vrLxgjS6NRw/+s1kUmjZVZnmCe5t3z9czHeNkoPhHtsOxvBwSMlPB1+wmFbnw856p9HAV7OIFhIh3fzHeeo4kGfyRIX0NjqMBkWzEuF1AHT8ud7q0ppMv8gv53Vnr6J+YZ24nOyLNWc2k5HWmCBI32Vcti2TmSFu8GvZiPywPv0Uxi4ijEPS+taWHljBmWb7f3fEYDaQYYq20p8pCCEGiu7rVNBwvJQlUILQb/+3AKSB4mOnSrIiq516hk4szrkOkiNm9uqq0PnWdMYu9FgpHbk/EV0IwmqtZ+W93acfjeLIBaR ansible-generated on samba-dc-01'}))
ok: [samba-dc-01.lab.etsbv.internal] => (item=({u'host': u'samba-dc-00.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCY4AUT/vi441NBib+MC8f1uaHIS+5kIfIoKQbKWvPd/WNFk/A9imz1MiN/vPpc3FFFrv7WxqkLGBcSNT21sflUfTStLkOGhhWL1IsbylRBFBw/mP7VNat+/dDNiUYiroYqGjq5HXCr1Xd6jll6BgBtune3hPQ5u/fdDXAD+XdHetErsW6zh0e7gNyL1IDZx4QRHNtS9qf0esiVLFKJpFvU3pix2PFvRw37/hVcsUUASZOpfVtXSOUEeX1Ifu6nCv+ev3WvUKqrDg81myHseNwTaeAFsv2dYBn28cE99cdl8m+AT1L7Zn1ucS7Dk6GsvWjlTRJuUv7VmWyoq5s6Otwd ansible-generated on samba-dc-00'}))
skipping: [samba-dc-01.lab.etsbv.internal] => (item=({u'host': u'samba-dc-01.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDnkOKiRieDN6QKQhgpT98qROLebPtsEE9q+o0I9vrLxgjS6NRw/+s1kUmjZVZnmCe5t3z9czHeNkoPhHtsOxvBwSMlPB1+wmFbnw856p9HAV7OIFhIh3fzHeeo4kGfyRIX0NjqMBkWzEuF1AHT8ud7q0ppMv8gv53Vnr6J+YZ24nOyLNWc2k5HWmCBI32Vcti2TmSFu8GvZiPywPv0Uxi4ijEPS+taWHljBmWb7f3fEYDaQYYq20p8pCCEGiu7rVNBwvJQlUILQb/+3AKSB4mOnSrIiq516hk4szrkOkiNm9uqq0PnWdMYu9FgpHbk/EV0IwmqtZ+W93acfjeLIBaR ansible-generated on samba-dc-01'}))
ok: [samba-dc-00.lab.etsbv.internal] => (item=({u'host': u'samba-dc-02.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDUzJNOyEFMAcvij9y05dfVb3s4HMy8/8yh3XnFWuvj2ZMt1FZ5vEFeYp6B0CFlhVeF8MfkzGNPHS3QxUeCB+7bbCC5VWXu/Gc/swmXqNHnn1OV4WBddvGmF0z4jLz2EFJ+3iQAamCH5nGahw8UWC0mN+5uD7oERTtZVPDgZ1CjCFX1epcdSt+5XBfrh7uaEdRKI9IYnz1wMwKOwUUTutDj+VDMFvvaMlXGnAYUOtwKzSr7u1yIjMiCMzAxGI5Is0NvU64Pp3bciVW4G2DNmanP+8w8ebttiquHKR3KP0/BTFxIiJkSWifxkJJl4pxood7/oLiLCpipyGQ5pK0arW0L ansible-generated on samba-dc-02'}))
ok: [samba-dc-02.lab.etsbv.internal] => (item=({u'host': u'samba-dc-01.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDnkOKiRieDN6QKQhgpT98qROLebPtsEE9q+o0I9vrLxgjS6NRw/+s1kUmjZVZnmCe5t3z9czHeNkoPhHtsOxvBwSMlPB1+wmFbnw856p9HAV7OIFhIh3fzHeeo4kGfyRIX0NjqMBkWzEuF1AHT8ud7q0ppMv8gv53Vnr6J+YZ24nOyLNWc2k5HWmCBI32Vcti2TmSFu8GvZiPywPv0Uxi4ijEPS+taWHljBmWb7f3fEYDaQYYq20p8pCCEGiu7rVNBwvJQlUILQb/+3AKSB4mOnSrIiq516hk4szrkOkiNm9uqq0PnWdMYu9FgpHbk/EV0IwmqtZ+W93acfjeLIBaR ansible-generated on samba-dc-01'}))
skipping: [samba-dc-02.lab.etsbv.internal] => (item=({u'host': u'samba-dc-02.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDUzJNOyEFMAcvij9y05dfVb3s4HMy8/8yh3XnFWuvj2ZMt1FZ5vEFeYp6B0CFlhVeF8MfkzGNPHS3QxUeCB+7bbCC5VWXu/Gc/swmXqNHnn1OV4WBddvGmF0z4jLz2EFJ+3iQAamCH5nGahw8UWC0mN+5uD7oERTtZVPDgZ1CjCFX1epcdSt+5XBfrh7uaEdRKI9IYnz1wMwKOwUUTutDj+VDMFvvaMlXGnAYUOtwKzSr7u1yIjMiCMzAxGI5Is0NvU64Pp3bciVW4G2DNmanP+8w8ebttiquHKR3KP0/BTFxIiJkSWifxkJJl4pxood7/oLiLCpipyGQ5pK0arW0L ansible-generated on samba-dc-02'}))
ok: [samba-dc-01.lab.etsbv.internal] => (item=({u'host': u'samba-dc-02.lab.etsbv.internal'}, {u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDUzJNOyEFMAcvij9y05dfVb3s4HMy8/8yh3XnFWuvj2ZMt1FZ5vEFeYp6B0CFlhVeF8MfkzGNPHS3QxUeCB+7bbCC5VWXu/Gc/swmXqNHnn1OV4WBddvGmF0z4jLz2EFJ+3iQAamCH5nGahw8UWC0mN+5uD7oERTtZVPDgZ1CjCFX1epcdSt+5XBfrh7uaEdRKI9IYnz1wMwKOwUUTutDj+VDMFvvaMlXGnAYUOtwKzSr7u1yIjMiCMzAxGI5Is0NvU64Pp3bciVW4G2DNmanP+8w8ebttiquHKR3KP0/BTFxIiJkSWifxkJJl4pxood7/oLiLCpipyGQ5pK0arW0L ansible-generated on samba-dc-02'}))

PLAY RECAP ***************************************************************************************************************************************************************************************************************************************
samba-dc-00.lab.etsbv.internal : ok=9    changed=1    unreachable=0    failed=0
samba-dc-01.lab.etsbv.internal : ok=8    changed=1    unreachable=0    failed=0
samba-dc-02.lab.etsbv.internal : ok=8    changed=1    unreachable=0    failed=0
```

## Destroying Core Services VMs

> NOTE: Use with extreme caution. We can only build in so much logic to ensure that
> you do not blow all of your VMs away. However, we feel this functionality should
> be in place in order to ensure a desired state environment.

We have built in functionality to automatically destroy VMs not defined as deploy
when defining the Core Services. The following variable definitions would need to
exist in order to auto destroy VMs.

The first definition would need to be defined as `true` either in `defaults/main.yml`
or in `inventory/group_vars/all/environment.yml`.

```yaml
# Defines if VMs defined as not defined to deploy to be destroyed
# reference vsphere_vm_services_groups as well
# Good for keeping environment in a defined state
# references tasks/destroy_vms.yml
vsphere_destroy_vms: false

# Defines core VM service groups
# Also used for determining which VMs should exist or not
# Not 100% complete yet
vsphere_vm_services_groups:
  - "{{ vsphere_bootstrap_vms }}"
  - "{{ vsphere_samba_vms }}"
  - "{{ vsphere_ddi_vms }}"
  - "{{ vsphere_dnsdist_vms }}"
  - "{{ vsphere_lb_vms }}"
```

As you can see from the above that unless `vsphere_destroy_vms` is defined as
`true` then your VMs will not be auto destroyed. Also, the `vsphere_vm_services_groups`
definition is what is used as the definition of what is in scope from an auto
destroy enforcement.

However, the next measure that must be in place is the following when defining
your VM definitions. The `deploy` definition is what defines whether the VM
should exist or not.

```yaml
vsphere_bootstrap_vms:
  - vm_name: bootstrap-vm-1.{{ vsphere_pri_domain_name }}
    cpus: "{{ vsphere_bootstrap_vms_cpu }}"
    deploy: "{{ vsphere_bootstrap_vms_deploy }}"
    datastore: "{{ vsphere_vm_services_datastore }}"
    gateway: "{{ vsphere_vm_services_subnet }}.1"
    ip: "{{ vsphere_vm_services_subnet }}.101"
    memory_mb: "{{ vsphere_bootstrap_vms_memory }}"
    netmask_cidr: "{{ vsphere_vm_services_subnet_mask_cidr }}"
    network_name: "{{ vsphere_vm_services_vswitch }}"
    vapp_source_path: "{{ vsphere_linux_vapp_ovf }}"
  - vm_name: bootstrap-vm-2.{{ vsphere_pri_domain_name }}
    cpus: "{{ vsphere_bootstrap_vms_cpu }}"
    deploy: "{{ vsphere_bootstrap_vms_deploy }}"
    datastore: "{{ vsphere_vm_services_datastore }}"
    memory_mb: "{{ vsphere_bootstrap_vms_memory }}"
    network_name: "{{ vsphere_vm_services_vswitch }}"
    vapp_source_path: "{{ vsphere_linux_vapp_ovf }}"
```

Based on the above VM definitions we have also made the `deploy` a single definition
by default for each Core Service VM type. The defaults are as follows which can
be found in `inventory/group_vars/all/environment.yml`:

```yaml
vsphere_bootstrap_vms_deploy: false
vsphere_ddi_vms_deploy: true
vsphere_dnsdist_vms_deploy: true
vsphere_lb_vms_deploy: true
vsphere_samba_vms_deploy: true
```

> NOTE: You should definitely reference the section on [Defining Environmental Variables](#defining-environmental-variables)

As well as if you run the following using the `vsphere_management.sh` script:

```bash
vsphere_management.sh vsphere_destroy_vms
```

You will be prompted as below:

```bash
CAUTION:	You are about to DESTROY Core Services VMs!
		Only VMs defined as deploy: false will be affected.....

You are about to DESTROY Core Services VMs!! Continue? (y/n)
```

## Defining Environmental Variables

> NOTE: This is a work in progress

As this project proceeds the common variables will begin to be consolidated into `inventory/groups_vars/all/environment.yml`. This will allow for environmental specific variables to be defined in a central location. These will be defined and feed into additional variables. This makes management of specific environments much easier.

```yaml
---
pri_domain_name: lab.etsbv.internal

#vSphere AD Info
# Define Ansible group which contains your Samba domain controllers
# Do not change this until further refactoring occurs...this comment will be removed at that time
samba_domain_controllers_group: "{{ vsphere_samba_vms_group }}"
vsphere_ad_netbios_name: LAB-AD

#vSphere bootstrap VM info
vsphere_bootstrap_vms_cpu: 1
vsphere_bootstrap_vms_deploy: false
vsphere_bootstrap_vms_memory: 512
# Define Ansible group which contains your DDI VMs
# Do not change this until further refactoring occurs...this comment will be removed at that time
vsphere_bootstrap_vms_group: vsphere_bootstrap_vms

#vSphere DDI VM info
vsphere_ddi_vms_cpu: 1
vsphere_ddi_vms_deploy: true
vsphere_ddi_vms_memory: 2048
# Define Ansible group which contains your DDI VMs
# Do not change this until further refactoring occurs...this comment will be removed at that time
vsphere_ddi_vms_group: vsphere_ddi_vms

# Defines if VMs defined as not defined to deploy to be destroyed
# reference vsphere_vm_services_groups as well
# Good for keeping environment in a defined state
# references tasks/destroy_vms.yml
vsphere_destroy_vms: false

#vSphere DHCP VM info
# Define Ansible group which contains your DHCP VMs
# Do not change this until further refactoring occurs...this comment will be removed at that time
vsphere_dhcp_vms_group: vsphere_dhcp_vms

#vSphere DNSDist VM info
vsphere_dnsdist_vms_cpu: 1
vsphere_dnsdist_vms_deploy: true
vsphere_dnsdist_vms_memory: 1024

# Defines inventory directory
vsphere_inventory_directory: ../inventory

#vSphere LB VM info
vsphere_lb_vms_cpu: 1
vsphere_lb_vms_deploy: true
# Define Ansible group which contains your LB VMs
# Do not change this until further refactoring occurs...this comment will be removed at that time
vsphere_lb_vms_group: vsphere_lb_vms
vsphere_lb_vms_memory: 1024

#vSphere Samba VM info
vsphere_samba_vms_cpu: 1
vsphere_samba_vms_deploy: true
# Define Ansible group which contains your LB VMs
# Do not change this until further refactoring occurs...this comment will be removed at that time
vsphere_samba_vms_group: vsphere_samba_vms
vsphere_samba_vms_memory: 512

#vSphere VM Services info
# Defines the vSphere datastore to store vm core services on
vsphere_vm_services_datastore: Datastore_1
# vSphere core services for vms
vsphere_vm_services_subnet: 10.0.102
vsphere_vm_services_subnet_mask: 255.255.255.0
vsphere_vm_services_subnet_mask_cidr: 24
vsphere_vm_services_vswitch: VSS-VLAN-102
```

## Bootstrap VMs

When spinning up a new environment you may want to spin up some initial VMs for
various functions to bootstrap your environment. This will be a work in progress
until the process becomes more sreamlined. As of right now I am using an `Ubuntu`
based `OVF` template which is stored on my `Deployment Host` which is used to
deploy these bootstrap vms.

> NOTE: The `Ubuntu` based `OVF` template is **NOT** included in this repo. I am
> still evaluating a solution around this. My instinct at the moment is to use
> `Packer` to build the `OVF` but not 100% sure at this point. This seems like a
> viable solution as I could include the build template and the scripting. But time
> will tell.

## DNSDist VMs

The option to spin up [PowerDNS DNSDist](https://dnsdist.org/) is available. These
VMs provide a set of DNS servers to use in the environment which will frontend
any and all DNS servers inside/outside this environment. DNSDist provides true DNS
load balancing and rule based DNS distribution. This is especially beneficial in
those environments where outside resources need to be accessed which already have
separate DNS servers and forwarding is not warranted on the DDI VMs. In addition
in environments where Active Directory is present. DNSDist can forward those
requests appropriately. In this project we will be adding Samba based Active
Directory functionality to alleviate the need for Windows based Active Directory.
The option to use Windows based Active Directory will eventually added at some
point. The additional benefit to using DNSDist is that you can freely change out
DNS servers on the backend without impacting clients and etc.

## DDI VMs

The option to spin up a multi-node DDI cluster is available.
[DHCP](https://www.isc.org/downloads/dhcp/), [DNS](https://www.powerdns.com/),
[IPAM](https://phpipam.net/), and NTP functionality exists on these VMs if deployed.
The VMs by default should be assigned an IP address in order to bootstrap the environment
for IP services where these constructs do not exist. The idea is that you would
be deploying from scratch an environment which needs this functionality provided
in an automated fashion. When these VMs spin up everything is automated from
beginning to end including DNS record registrations. Dynamic DNS is also enabled
in order to auto register DHCP clients.

> NOTE: Currently all of these services run on the DDI nodes and may eventually
> be separated out.
>
> NOTE: The `Ubuntu` based `OVF` template is **NOT** included in this repo. I am
> still evaluating a solution around this. My instinct at the moment is to use
> `Packer` to build the `OVF` but not 100% sure at this point. This seems like a
> viable solution as I could include the build template and the scripting. But time
> will tell.

### Autostart DDI VMs

The DDI VMs are set to autostart on host bootup with priories defined. This will
likely change a bit once vCenter is in place.

### Defining DDI VMs

Below is an example of the current DDI VM definitions in `inventory/group_vars/all/vsphere_ddi.yml`:

```yaml
---
# These define the IP addresses for the DDI VMs
vsphere_ddi_vm_ips:
  - "{{ vsphere_vm_services_subnet }}.10"
  - "{{ vsphere_vm_services_subnet }}.11"
  - "{{ vsphere_vm_services_subnet }}.12"

vsphere_ddi_vms_inventory_file: ../inventory/vsphere_ddi_vms.inv

vsphere_ddi_vms:
  - vm_name: "ddi-00.{{ vsphere_pri_domain_name }}"
    cpus: 1
    deploy: true
    datastore: Datastore_1
    gateway: "{{ vsphere_vm_services_subnet }}.1"
    ip: "{{ vsphere_ddi_vm_ips[0] }}"
    memory_mb: 2048
    netmask: 255.255.255.0
    netmask_cidr: 24
    network_name: VSS-VLAN-102
    vapp_source_path: C:\vagrant\vApps\ubuntu_16.04_template.ovf
  - vm_name: "ddi-01.{{ vsphere_pri_domain_name }}"
    cpus: 1
    deploy: true
    datastore: Datastore_1
    gateway: "{{ vsphere_vm_services_subnet }}.1"
    ip: "{{ vsphere_ddi_vm_ips[1] }}"
    memory_mb: 2048
    netmask: 255.255.255.0
    netmask_cidr: 24
    network_name: VSS-VLAN-102
    vapp_source_path: C:\vagrant\vApps\ubuntu_16.04_template.ovf
  - vm_name: "ddi-02.{{ vsphere_pri_domain_name }}"
    cpus: 1
    deploy: true
    datastore: Datastore_1
    gateway: "{{ vsphere_vm_services_subnet }}.1"
    ip: "{{ vsphere_ddi_vm_ips[2] }}"
    memory_mb: 2048
    netmask: 255.255.255.0
    netmask_cidr: 24
    network_name: VSS-VLAN-102
    vapp_source_path: C:\vagrant\vApps\ubuntu_16.04_template.ovf
```

### Defining DNS Records

Below is an example of the current DNS record definitions in `inventory/group_vars/all/pdns.yml`:

> NOTE: When creating a `CNAME` record type take not of the `.` at the end of the
> `content` variable. This is **REQUIRED** to ensure Canonical naming standards
> otherwise the record creation will fail.

```yaml
pdns_records:
  - hostname: lb
    content: "{{ vsphere_lb_vips[0] }}"
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_lb_vips[0] }}"
    type: A
  - hostname: db
    content: "lb.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_lb_vips[0] }}"
    type: CNAME
  - hostname: dns_00
    content: "dnsdist_00.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_dnsdist_vm_ips[0] }}"
    type: CNAME
  - hostname: dns_01
    content: "dnsdist_01.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_dnsdist_vm_ips[1] }}"
    type: CNAME
  - hostname: ipam
    content: "lb.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_lb_vips[0] }}"
    type: CNAME
  - hostname: nas01
    content: 10.0.101.50
    domain: "{{ vsphere_pri_domain_name }}"
    ip: 10.0.101.50
    type: A
  - hostname: nas02
    content: 10.0.101.51
    domain: "{{ vsphere_pri_domain_name }}"
    ip: 10.0.101.51
    type: A
  - hostname: ntp_00
    content: "ddi_00.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_ddi_vm_ips[0] }}"
    type: CNAME
  - hostname: ntp_01
    content: "ddi_01.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_ddi_vm_ips[1] }}"
    type: CNAME
  - hostname: ntp_02
    content: "ddi_02.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_ddi_vm_ips[2] }}"
    type: CNAME
  - hostname: pdns_api
    content: "lb.{{ vsphere_pri_domain_name }}."
    domain: "{{ vsphere_pri_domain_name }}"
    ip: "{{ vsphere_lb_vips[0] }}"
    type: CNAME
```

### Future DDI Functionality

In the future the option to use `Windows` DNS and DHCP may be an option but not
in the current state.

## Samba based Active Directory

Currently we will spin up `3` Samba based Active Directory servers. One will be
the PDC and the other 2 will function as BDCs. This functionality will provide
`NT Domain` services for the environment without the requirement of running a
`Windows` based domain. We have setup `rsync` cron jobs which run on the BDCs
and their sole purpose is to sync `SysVol` information from the PDC. This will
ensure that if the PDC were to go down then all login scripts and GPO policies
are synced to the the BDCs. The caveat with this method currently is that if
any polices or scripts are defined on the BDCs they will disappear on the next
rsync cron job. This job is scheduled to run every 5 minutes.

> NOTE: When creating any login scripts or GPO policies to ensure that you have
> selected the PDC as the Domain Controller. This is the default behavior when
> launching GPO Manager, but please ensure to do this. More information can be
> found on this [here](https://wiki.samba.org/index.php/Rsync_based_SysVol_replication_workaround).

### Creating Samba AD Users and Groups

In order to create Samba AD users and groups the info below must be defined. This
is also a pre-requisite to [Host User Roles Domain Permissions](#host-user-roles-domain-permissions).

```yaml
samba_domain_groups:
  - name: vSphere-Admins
    members:
      - administrator
      - vSphere-Admin

samba_domain_users:
  - name: vSphere-Admin
    password: P@55w0rd
```

### vSphere Host(s)

#### Host Domain Membership

We have added the ability to manage hosts Active Directory Domain membership and
host role permissions. If `vsphere_hosts_join_domain: true` then the host(s) will
be added to the `vsphere_ad_dns_domain_name` Active Directory domain. If
`vsphere_hosts_join_domain: false` then any host that is a member of `vsphere_ad_dns_domain_name`
will leave the domain.

#### Host User Roles Domain Permissions

We have also added the ability to manage the hosts user roles domain permissions.
If the host is joined to the domain then any groups defined as below will be added
to the correct host role.

```yaml
# roles can be NoAccess, Anonymous, View, ReadOnly, Admin
vsphere_domain_access:
  - name: "{{ vsphere_ad_netbios_name|upper }}\\vSphere-Admins"
    role: Admin
```

## VCSA

> NOTE: The VCSA ISO nor the VCSA ISO contents are included within this repo.

### Defining VCSA Specifics

#### Default definitions

[defaults](defaults/main.yml)

#### Deployment definitions

[deployment group_vars](inventory/group_vars/all/vsphere_vcsa.yml)

### Sizing

The following information can be used to determine the sizing required for the
VCSA deployment.

```yaml
vsphere_vcsa_appliance_deployment_option: tiny
```

```json
{
    "large": {
        "cpu": 16,
        "memory": 32768,
        "host-count": 1000,
        "vm-count": 10000,
        "disk-swap": "50GB",
        "disk-core": "100GB",
        "disk-log": "25GB",
        "disk-db": "25GB",
        "disk-dblog": "10GB",
        "disk-seat": "100GB",
        "disk-netdump": "10GB",
        "disk-autodeploy": "25GB",
        "disk-invsvc": "100GB",
        "label": "Large (up to 1000 hosts, 10,000 VMs)",
        "description": "This will deploy a Large VM configured with 16 vCPUs and 32 GB of memory and requires 450 GB of disk space. This option contains vCenter Server with an embedded Platform Services Controller."
    },
    "medium": {
        "cpu": 8,
        "memory": 24576,
        "host-count": 400,
        "vm-count": 4000,
        "disk-swap": "50GB",
        "disk-core": "50GB",
        "disk-log": "25GB",
        "disk-db": "25GB",
        "disk-dblog": "10GB",
        "disk-seat": "50GB",
        "disk-netdump": "10GB",
        "disk-autodeploy": "25GB",
        "disk-invsvc": "25GB",
        "label": "Medium (up to 400 hosts, 4,000 VMs)",
        "description": "This will deploy a Medium VM configured with 8 vCPUs and 24 GB of memory and requires 300 GB of disk space. This option contains vCenter Server with an embedded Platform Services Controller."
    },
    "small": {
        "cpu": 4,
        "memory": 16384,
        "host-count": 100,
        "vm-count": 1000,
        "disk-swap": "25GB",
        "disk-core": "50GB",
        "disk-log": "10GB",
        "disk-db": "10GB",
        "disk-dblog": "5GB",
        "disk-seat": "25GB",
        "disk-netdump": "1GB",
        "disk-autodeploy": "10GB",
        "disk-invsvc": "10GB",
        "label": "Small (up to 100 hosts, 1,000 VMs)",
        "description": "This will deploy a Small VM configured with 4 vCPUs and 16 GB of memory and requires 150 GB of disk space. This option contains vCenter Server with an embedded Platform Services Controller."
    },
    "tiny": {
        "cpu": 2,
        "memory": 8192,
        "host-count": 10,
        "vm-count": 100,
        "disk-swap": "25GB",
        "disk-core": "25GB",
        "disk-log": "10GB",
        "disk-db": "10GB",
        "disk-dblog": "5GB",
        "disk-seat": "10GB",
        "disk-netdump": "1GB",
        "disk-autodeploy": "10GB",
        "disk-invsvc": "5GB",
        "label": "Tiny (up to 10 hosts, 100 VMs)",
        "description": "This will deploy a Tiny VM configured with 2 vCPUs and 8 GB of memory and requires 120 GB of disk space. This option contains vCenter Server with an embedded Platform Services Controller."
    },
    "management-large": {
        "cpu": 16,
        "memory": 32768,
        "host-count": 1000,
        "vm-count": 10000,
        "disk-swap": "50GB",
        "disk-core": "100GB",
        "disk-log": "25GB",
        "disk-db": "25GB",
        "disk-dblog": "10GB",
        "disk-seat": "100GB",
        "disk-netdump": "10GB",
        "disk-autodeploy": "25GB",
        "disk-invsvc": "100GB",
        "label": "Large (up to 1000 hosts, 10,000 VMs)",
        "description": "This will deploy a Large VM configured with 16 vCPUs and 32 GB of memory and requires 450 GB of disk space. These resources will be used by the vCenter Server services."
    },
    "management-medium": {
        "cpu": 8,
        "memory": 24576,
        "host-count": 400,
        "vm-count": 4000,
        "disk-swap": "50GB",
        "disk-core": "50GB",
        "disk-log": "25GB",
        "disk-db": "25GB",
        "disk-dblog": "10GB",
        "disk-seat": "50GB",
        "disk-netdump": "10GB",
        "disk-autodeploy": "25GB",
        "disk-invsvc": "25GB",
        "label": "Medium (up to 400 hosts, 4,000 VMs)",
        "description": "This will deploy a Medium VM configured with 8 vCPUs and 24 GB of memory and requires 300 GB of disk space. These resources will be used by the vCenter Server services."
    },
    "management-small": {
        "cpu": 4,
        "memory": 16384,
        "host-count": 100,
        "vm-count": 1000,
        "disk-swap": "25GB",
        "disk-core": "50GB",
        "disk-log": "10GB",
        "disk-db": "10GB",
        "disk-dblog": "5GB",
        "disk-seat": "25GB",
        "disk-netdump": "1GB",
        "disk-autodeploy": "10GB",
        "disk-invsvc": "10GB",
        "label": "Small (up to 100 hosts, 1,000 VMs)",
        "description": "This will deploy a Small VM configured with 4 vCPUs and 16 GB of memory and requires 150 GB of disk space. These resources will be used by the vCenter Server services."
    },
    "management-tiny": {
        "cpu": 2,
        "memory": 8192,
        "host-count": 10,
        "vm-count": 100,
        "disk-swap": "25GB",
        "disk-core": "25GB",
        "disk-log": "10GB",
        "disk-db": "10GB",
        "disk-dblog": "5GB",
        "disk-seat": "10GB",
        "disk-netdump": "1GB",
        "disk-autodeploy": "10GB",
        "disk-invsvc": "5GB",
        "label": "Tiny (up to 10 hosts, 100 VMs)",
        "description": "This will deploy a Tiny VM configured with 2 vCPUs and 8 GB of memory and requires 120 GB of disk space. These resources will be used by the vCenter Server services."
    },
    "infrastructure": {
        "cpu": 2,
        "memory": 2048,
        "disk-swap": "5GB",
        "disk-core": "5GB",
        "disk-log": "5GB",
        "disk-db": "10GB",
        "disk-dblog": "10MB",
        "disk-seat": "10MB",
        "disk-netdump": "10MB",
        "disk-autodeploy": "10MB",
        "disk-invsvc": "10MB",
        "label": "Platform Services Controller",
        "description": "This will deploy an external Platform Services Controller VM with 2 vCPU and 2GB of memory and requires 30 GB of disk space."
    }
}
```

## Terraform Infrastructure Deployment

We have included [Terraform](https://www.terraform.io/) as a deployment mechanism
to manage VMs, PDNS, and etc. as a post Core Services deployment. We feel this
is a very efficient way to handle especially the spin up and tear down of VMs.
Terraform performs much better than handing VM management using either PowerCLI or
Ansible in this environment. However this type of deployment will be post Core
Services deployment. And at this time is a manual kick off of the provisioning.
Coming soon will be a deployment option to provision a highly available container
platform.

### Defining Terraform Infrastructure

Because this is all about Infrastructure As Code. We have even implemented the
majority of the Terraform setup to be driven by Ansible. This means that we only
need to define in some variable files what we would like. For now this is only
based on VM provisioning. We use many of the already defined variables which are
part of this project to auto generate most of the Terraform configuration files.
Some examples of the variables to define our Terraform deployment include:

-   [terraform_vms.yml](inventory/group_vars/all/terraform_vms.yml)
-   [terraform_pdns_records.yml](inventory/group_vars/all/terraform_pdns_records.yml)

You will also find in the `playbooks` and `playbooks/templates` directories the
playbook and templates used to drive the auto generated Terraform configurations.

-   [terraform.yml](playbooks/terraform.yml)

As part of all of this we also auto generate an Ansible inventory file which
includes the important information for our provisioning. This file will be
created as `inventory/terraform.inv` and it will look like something like:

```raw
[rancher_lbs]
rancher-lb-02.lab.etsbv.internal
rancher-lb-01.lab.etsbv.internal

[rancher_db_cluster]
rancher-db-03.lab.etsbv.internal
rancher-db-01.lab.etsbv.internal
rancher-db-02.lab.etsbv.internal

[rancher_hosts]
rancher-04.lab.etsbv.internal
rancher-03.lab.etsbv.internal
rancher-02.lab.etsbv.internal
rancher-01.lab.etsbv.internal
rancher-06.lab.etsbv.internal
rancher-05.lab.etsbv.internal

[terraform_vms]
rancher-lb-02.lab.etsbv.internal ansible_host=10.0.102.155 mac_address=00:50:56:aa:27:44 uuid=422ac0c8-f6fc-d69c-bccf-0513d01a00af
rancher-lb-01.lab.etsbv.internal ansible_host=10.0.102.180 mac_address=00:50:56:aa:57:79 uuid=422acbbc-0ff5-d221-be27-1e7114ff9f18
rancher-db-03.lab.etsbv.internal ansible_host=10.0.102.170 mac_address=00:50:56:aa:10:65 uuid=422a9c18-aca4-747a-1613-f0a6f207576d
rancher-db-01.lab.etsbv.internal ansible_host=10.0.102.172 mac_address=00:50:56:aa:5f:49 uuid=422a7547-e367-a8b6-228e-70f85bf9eb93
rancher-db-02.lab.etsbv.internal ansible_host=10.0.102.158 mac_address=00:50:56:aa:e2:3d uuid=422a569e-65d1-52d2-ad19-d12e8886d716
rancher-04.lab.etsbv.internal ansible_host=10.0.102.175 mac_address=00:50:56:aa:bf:b2 uuid=422a22b1-0ba9-de70-cd88-abbd84ce3a39
rancher-03.lab.etsbv.internal ansible_host=10.0.102.156 mac_address=00:50:56:aa:b5:cc uuid=422a58f4-2d53-fbbe-9376-7be257a183ae
rancher-02.lab.etsbv.internal ansible_host=10.0.102.173 mac_address=00:50:56:aa:9f:c5 uuid=422ae37c-97ff-89ec-b955-9c1e965c0716
rancher-01.lab.etsbv.internal ansible_host=10.0.102.154 mac_address=00:50:56:aa:ea:c0 uuid=422a5c7d-3f8b-d34e-5b0c-952e1d35b2c2
rancher-06.lab.etsbv.internal ansible_host=10.0.102.157 mac_address=00:50:56:aa:f5:f4 uuid=422ac850-c612-7d8e-70b9-b3dd3d2e97cd
rancher-05.lab.etsbv.internal ansible_host=10.0.102.174 mac_address=00:50:56:aa:d3:d3 uuid=422ada91-826c-db95-9dbf-1bd79bddf805
```

The above inventory is created by parsing the information collected from
`terraform state pull` and then parsed using the [terraform.inv.j2](playbooks/templates/terraform.inv.j2)
Jinja2 template.

### Deploying Terraform Infrastructure

We have added to the [vsphere_management.sh](scripts/vsphere_management.sh) script
the ability to automate the Terraform deployments and teardowns. Reference the
[Deployment Script Functions](#deployment_script_functions) to learn more about this.

## Role Variables

> NOTE: Update this once more complete. Too many changes to keep accurate.

[defaults/main.yml](defaults/main.yml)

## Dependencies

In order to properly deploy a single vSphere ESXi host should be stood up and have
at least a single NIC with an IP assigned for the management network. Everything
else will be deployed.

## Example Playbook

## License

MIT

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://www.everythingshouldbevirtual.com)
-   [mrlesmithjr.com](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
