Role Name
=========

An [Ansible] role to install [KVM]

Build Status
------------

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-kvm.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-kvm)

Requirements
------------

Install required [Ansible] roles:
```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------

```
---
# defaults file for ansible-kvm

# Defines if kvm/libvirt should be configured
config_kvm: false

# Defines if ssh should be configured to allow root logins
# mainly for managing KVM/Libvirt remotely using virt-manager or other.
kvm_allow_root_ssh: false

# Defines if kvm_users should be added to libvirtd for managing KVM
kvm_config_users: false

# Defines if kvm virtual networks should be configured
# if set to true ensure that your underlying bridges have been created
# using mrlesmithjr.config-interfaces role from Ansible Galaxy.
kvm_config_virtual_networks: false

kvm_debian_packages:
  - 'bridge-utils'
  - 'libvirt-bin'
  - 'lldpd'
  - 'python-libvirt'
  - 'python-lxml'
  - 'qemu-kvm'
  - 'ubuntu-vm-builder'
  - 'vlan'

# Defines if libvirt should be advertised over mDNS - Avahi
# default is false.
kvm_enable_mdns: false

kvm_enable_system_tweaks: false

# Defines if unencrypted tcp connections are desired
# default is false
kvm_enable_tcp: false

# Defines if remote tls connections are desired
# default is true.
kvm_enable_tls: true

kvm_enable_libvirtd_syslog: false

kvm_images_format_type: 'qcow2'

# Defines the path to store VM images
kvm_images_path: '/var/lib/libvirt/images'

# Defines if VMs defined in kvm_vms are managed
kvm_manage_vms: false

# I experienced an issue with bridges no longer working on Ubuntu 16.04
# for some reason. And the following settings below from the link provided
# solved this issue.
# https://wiki.libvirt.org/page/Networking#Debian.2FUbuntu_Bridging
kvm_sysctl_settings:
  - name: 'net.bridge.bridge-nf-call-ip6tables'
    value: 0
    state: "present"
  - name: 'net.bridge.bridge-nf-call-iptables'
    value: 0
    state: "present"
  - name: 'net.bridge.bridge-nf-call-arptables'
    value: 0
    state: "present"

# Defines users to add to libvirt group
kvm_users:
  - 'remote'

# Define KVM Networks to create
kvm_virtual_networks:
  - name: 'DMZ_ORANGE_VLAN100'
    mode: 'bridge'
    bridge_name: 'vmbr100'
    autostart: true
    # active, inactive, present and absent
    state: active
  - name: 'Green_Servers_VLAN101'
    mode: 'bridge'
    bridge_name: 'vmbr101'
    autostart: true
    state: active

# Define VM(s) to create
kvm_vms:
  - name: 'test_vm'
    # Define boot devices in order of preference
    boot_devices:
      - 'network'
      - 'hd'
      # - 'cdrom'
    # Define disks in MB
    disks:
        # ide, scsi, virtio, xen, usb, sata or sd
      - disk_driver: 'virtio'
        name: 'test_vm.1'
        size: '36864'
      - disk_driver: 'virtio'
        name: 'test_vm.2'
        size: '51200'
    # Define a specific host where the VM should reside..Match inventory_hostname
    # host: 'kvm01'
    # Define memory in MB
    memory: '512'
    network_interfaces:
      - source: 'default'
        network_driver: 'virtio'
        type: 'network'
      # - source: 'vmbr102'
      #   network_driver: 'virtio'
      #   type: 'bridge'
    state: 'running'
    vcpu: '1'
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: kvm_hosts
  become: true
  vars:
  roles:
    - role: ansible-kvm
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
[KVM]: <https://www.linux-kvm.org/page/Main_Page>
