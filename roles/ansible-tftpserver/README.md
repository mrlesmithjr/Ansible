Role Name
=========

Builds out a fully functional PXE/TFTP Server for OS deployments.. (Ubuntu included using Netboot) Pre-Seed file template included and ESXi scripted install ready.

Requirements
------------

If ESXi scripted installs are needed you MUST upload the appropriate ISO's to /var/lib/tftpboot/images and configure the following vars in either the /etc/ansible/roles/mrlesmithjr.tftpserver/defaults/main.yml or add them to group_vars/tftpserver-nodes.yml (or whatever your Ansible group is called in your Ansible inventory hosts).
````
vmware_iso_images:
  - file: VMware-VMvisor-Installer-6.0.0.update01-3029758.x86_64.iso
    folder: ESXi/6.0U1
````

The best way to use this role is to install from Ansible Galaxy.
````
ansible-galaxy install mrlesmithjr.tftpserver
````

Role Variables
--------------
group_vars/all
````
# To generate passwords use (replace P@55w0rd with new password).... echo "P@55w0rd" | mkpasswd -s -m sha-512
root_password:  #define root password for hosts....define here or in group_vars/all
````

group_vars/tftpserver.yml
````
config_dnsmasq: true
config_interfaces: false
enable_apt_caching: false
enable_dhcp: false
enable_tftp: true
esxi_addl_settings:  #define additional esxli commands to run in order to configure each host
  - desc: 'Set default domain lookup name'
    command: 'esxcli network ip dns search add --domain={{ pri_domain_name }}'
  - desc: 'Add vmnic3 to vSwitch0'
    command: 'esxcli network vswitch standard uplink add --uplink-name vmnic3 --vswitch-name vSwitch0'
  - desc: 'SATP configurations'
    commands:
      - 'esxcli storage nmp satp set --satp VMW_SATP_SVC --default-psp VMW_PSP_RR'
      - 'esxcli storage nmp satp set --satp VMW_SATP_DEFAULT_AA --default-psp VMW_PSP_RR'
esxi_enable_snmp: true
esxi_enable_ssh_and_shell: true
esxi_install_vibs: true
tftp_boot_menu:  #menu_default has been disabled to allow boot from local HD by default
  - label: local
    menu_label: '^Boot from hard drive'
    menu_default: false
    localboot: true
  - label: install
    menu_label: Install
    menu_default: false
    kernel: ubuntu-installer/amd64/linux
    append: 'vga=788 initrd=ubuntu-installer/amd64/initrd.gz -- quiet'
  - label: cli
    menu_label: 'Command-line install'
    menu_default: false
    kernel: ubuntu-installer/amd64/linux
    append: 'tasks=standard pkgsel/language-pack-patterns= pkgsel/install-language-support=false vga=788 initrd=ubuntu-installer/amd64/initrd.gz -- quiet'
  - label: 'auto-install Ubuntu Netboot (Latest)'
    menu_label: 'Automated install Ubuntu (Latest)'
    menu_default: true
    kernel: ubuntu-installer/amd64/linux
    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto url=tftp://{{ tftp_bind_address }}/preseed.cfg'
  - label: 'CentOS 7 (Manual)'
    menu_label: 'CentOS 7 (Manual)'
    menu_default: false
    kernel: images/CentOS/7/images/pxeboot/vmlinuz
    append: 'auto=true priority=critical vga=normal initrd=tftp://{{ tftp_bind_address }}/images/CentOS/7/images/pxeboot/initrd.img ip=dhcp inst.repo=http://{{ tftp_bind_address }}/images/CentOS/7'
  - label: 'Ubuntu 12.04.5 (Manual)'
    menu_label: 'Install Ubuntu 12.04.5 (Manual)'
    menu_default: false
    kernel: images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/linux
    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto'
  - label: 'Ubuntu 12.04.5 (Pre-Seed)'
    menu_label: 'Install Ubuntu 12.04.5 (Pre-Seed)'
    menu_default: false
    kernel: images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/linux
    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto url=tftp://{{ tftp_bind_address }}/preseed.cfg'
  - label: 'Ubuntu 14.04.3 (Manual)'
    menu_label: 'Install Ubuntu 14.04.3 (Manual)'
    menu_default: false
    kernel: images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/linux
    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto'
  - label: 'Ubuntu 14.04.3 (Pre-Seed)'
    menu_label: 'Install Ubuntu 14.04.3 (Pre-Seed)'
    menu_default: false
    kernel: images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/linux
    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto url=tftp://{{ tftp_bind_address }}/preseed.cfg'
  - label: 'ESXi 6.0 U1 (scripted install)'
    menu_label: 'ESXi 6.0 U1 Installer'
    menu_default: false
    kernel: images/ESXi/6.0/mboot.c32
    append: '-c images/ESXi/6.0/boot.cfg ks=http://{{ ansible_fqdn }}/KS/ESX_KS.CFG'
tftp_build_images: true  #defines if images folder(s) and isos should be added
tftp_iso_images:
  - url: http://www.gtlib.gatech.edu/pub/centos/7/isos/x86_64
    file: CentOS-7-x86_64-Minimal-1503-01.iso
    folder: CentOS/7
  - url: http://mirror.pnl.gov/releases/12.04
    file: ubuntu-12.04.5-server-amd64.iso
    folder: Ubuntu/12.04
  - url: http://mirror.pnl.gov/releases/14.04
    file: ubuntu-14.04.3-server-amd64.iso
    folder: Ubuntu/14.04
vmware_iso_images:
  - file: VMware-VMvisor-Installer-6.0.0.update01-3029758.x86_64.iso
    folder: ESXi/6.0U1
````

defaults/main.yml
````
---
# defaults file for ansible-tftpserver
apache_root: /var/www/html
apache_tftp_links:
  - ESXi_VIBS
  - ESXi_boot
  - images
  - KS
apt_cacher_server: '{{ ansible_hostname }}'
apt_mirror_dir: /ubuntu  #defines the mirror directory of webserver if using local apt repo mirror (apt-mirror) server.
apt_mirror_server: 'apt-mirror.{{pri_domain_name }}'  #define your local apt repo mirror (apt-mirror) server if you are using one.
config_tftp: true  #defines if tftp services should be configured
# To generate passwords use (replace P@55w0rd with new password).... echo "P@55w0rd" | mkpasswd -s -m sha-512
#create_users:  #defines user accounts to setup on hosts....define here or in group_vars/all
#  - user: demo_user  #define username
#    authorized_keys: ''
#    comment: 'Demo user'  #define a comment to associate with the account
#    generate_keys: false  #generate ssh keys...true|false
#    home: ''  #define a different home directory... ''=/home/username
#    pass: demo_password  #define password for account
#    setup: false  #true=creates account|false=removes account if exists...true|false
#    shell: ''  #define a different shell for the user
#    preseed_user: false  #defines if user should be setup as default user during preseed auto-install...Only 1 user can be added.
#    sudo: false  #define if user should have sudo access...true|false
#    system_account: false  #define if account is a system account...true|falseinstall_fail2ban: false
domain_name: '{{ pri_domain_name }}'  #defined here or in group_vars/all/network
enable_apt_caching: false  #defines if apt-cacher-ng is setup and added to preseed.cfg
enable_apt_mirror: false  #defines if using a local mirror (apt-mirror) and configures preseed.cfg as such. Do not use both apt_caching and apt_mirror...
esxi_addl_settings:  #define additional esxli commands to run in order to configure each host
  - desc: 'Set default domain lookup name'
    command: 'esxcli network ip dns search add --domain={{ pri_domain_name }}'
#  - desc: 'Add vmnic3 to vSwitch0'
#    command: 'esxcli network vswitch standard uplink add --uplink-name vmnic3 --vswitch-name vSwitch0'
#  - desc: 'SATP configurations'
#    commands:
#      - 'esxcli storage nmp satp set --satp VMW_SATP_SVC --default-psp VMW_PSP_RR'
#      - 'esxcli storage nmp satp set --satp VMW_SATP_DEFAULT_AA --default-psp VMW_PSP_RR'
esxi_create_host_kickstart_configs: false  #defines if individual kickstart configs should be created
esxi_enable_snmp: false
esxi_enable_ssh_and_shell: false  #defines if SSH and ESXi shell are to be enabled
esxi_exit_maint_mode: false  #defines if during TFTP/PXE load of ESXi hosts maintenance mode should be exited.
esxi_global_network_options:
  - bootproto: dhcp
    create_default_portgroup: false
    interface: vmnic0
#esxi_hosts:
#  - name: esxi01
#    bootproto: dhcp
#    create_default_portgroup: false
#    interface: vmnic0
#  - name: esxi02
#    bootproto: static
#    create_default_portgroup: false
#    interface: vmnic0
#    ip: 10.0.106.22
#    netmask: 255.255.255.0
#    gateway: 10.0.106.1
#    nameservers: '{{ pri_dns }},{{ sec_dns }}'
esxi_install_disk_options: install --firstdisk --overwritevmfs  #example options are... install --firstdisk=usb --overwritevmfs --novmfsondisk ... or ... install --firstdisk --overwritevmfs
esxi_install_vibs: false
esxi_root_pw: vmware1  #define here or in group_vars/all/accounts (preferred)
esxi_root_pw_encrypted: false  #defines if esxi_root_pw has been set to an already encrypted password
esxi_snmp_options:
  - community: PUBLIC
    allowed_from: 10.0.0.0/24
esxi_vibs:
  - 'http://{{ ansible_fqdn }}/ESXi_VIBS/Dell/cross_oem-dell-openmanage-esxi_7.3.0.2.ESXi550-0000.vib'
  - 'http://{{ ansible_fqdn }}/ESXi_VIBS/Dell/cross_oem-dell-iSM-esxi_1.0.ESXi550-0000.vib'
  - 'http://{{ ansible_fqdn }}/ESXi_VIBS/PernixData/PernixData_bootbank_pernixcore-vSphere5.5.0_1.5.0.2-25498.vib'
netboot_url: http://archive.ubuntu.com/ubuntu/dists/trusty-updates/main/installer-amd64/current/images/netboot/
netboot_file: netboot.tar.gz
#pri_dns: 10.0.101.11  #define primary dns server here or in group_vars/all/servers
pre_seed_expert_recipe_partitioning: false  #defines if custom partitioning is required
pre_seed_expert_recipe_partitions:  #define the partitions to create during pre-seed
  - name: boot
    mountpoint: /boot
    bootable: true
    filesystem: ext4
###    lv_name: boot  #This is an example only for /boot  do not assign an lv_name for boot.../boot will not be part of LVM.
    max_size: 1000
    method: format
    min_size: 500
    priority: 50
    use_filesystem: true
  - name: swap
#    mountpoint:  #not needed for swap
#    bootable: false  #not needed for swap.
    filesystem: linux-swap
    lv_name: swap  #defines the LVM name to use if pre_seed_partitioning_method: lvm and pre_seed_expert_recipe_partitioning: true
    max_size: 2048
    method: swap
    min_size: 500
    priority: 512
#    use_filesystem: true
  - name: root
    mountpoint: /
#    bootable: false  #not needed for root
    filesystem: ext4
    lv_name: root  #defines the LVM name to use if pre_seed_partitioning_method: lvm and pre_seed_expert_recipe_partitioning: true
    max_size: 10000
    method: format
    min_size: 5000
    priority: 10000
    use_filesystem: true
pre_seed_packages:  #define packages to install during pre-seed installation(s)
  - openssh-server
  - open-vm-tools
pre_seed_partition_disk: /dev/sda  #defines disk to install to during pre-seed TFTP/PXE install
pre_seed_partitioning_method: lvm   #defines partitioning method....lvm, regular or crypto
pri_domain_name: example.org  #define here or globally in group_vars/all
#sec_dns: 10.0.101.12  #define secondary dns server here or in group_vars/all/servers
primary_gfs_server: ''  #define if using GlusterFS
secondary_gfs_server: ''  #define if using GlusterFS
sync_tftp: false  #defines if setting up multiple servers are to be configured for GlusterFS
# To generate passwords use (replace P@55w0rd with new password).... echo "P@55w0rd" | mkpasswd -s -m sha-512
root_password: [] #define root password for hosts....define here or in group_vars/all
tftpboot_backup_dir: ''  #define if using GlusterFS
tftpboot_home: ''  #define if using GlusterFS
tftpboot_mnt: ''  #define if using GlusterFS
tftp_bind_address: '{{ ansible_default_ipv4.address }}'
tftp_boot_menu:  #menu_default has been disabled to allow boot from local HD by default
  - label: local
    menu_label: '^Boot from hard drive'
    menu_default: true
    localboot: true
#  - label: install
#    menu_label: Install
#    menu_default: false
#    kernel: ubuntu-installer/amd64/linux
#    append: 'vga=788 initrd=ubuntu-installer/amd64/initrd.gz -- quiet'
#  - label: cli
#    menu_label: 'Command-line install'
#    menu_default: false
#    kernel: ubuntu-installer/amd64/linux
#    append: 'tasks=standard pkgsel/language-pack-patterns= pkgsel/install-language-support=false vga=788 initrd=ubuntu-installer/amd64/initrd.gz -- quiet'
  - label: 'auto-install Ubuntu Netboot (Latest)'
    menu_label: 'Automated install Ubuntu (Latest)'
    menu_default: false
    kernel: ubuntu-installer/amd64/linux
    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto url=tftp://{{ tftp_bind_address }}/preseed.cfg'
#  - label: 'CentOS 7 (Manual)'
#    menu_label: 'CentOS 7 (Manual)'
#    menu_default: false
#    kernel: images/CentOS/7/images/pxeboot/vmlinuz
#    append: 'auto=true priority=critical vga=normal initrd=tftp://{{ tftp_bind_address }}/images/CentOS/7/images/pxeboot/initrd.img ip=dhcp inst.repo=http://{{ tftp_bind_address }}/images/CentOS/7'
#  - label: 'Ubuntu 12.04.5 (Manual)'
#    menu_label: 'Install Ubuntu 12.04.5 (Manual)'
#    menu_default: false
#    kernel: images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/linux
#    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto live-installer/net-image=http://{{ tftp_bind_address }}/images/Ubuntu/12.04/install/filesystem.squashfs'
#  - label: 'Ubuntu 12.04.5 (Pre-Seed)'
#    menu_label: 'Install Ubuntu 12.04.5 (Pre-Seed)'
#    menu_default: false
#    kernel: images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/linux
#    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/12.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto url=tftp://{{ tftp_bind_address }}/ubuntu_12.04_preseed.cfg live-installer/net-image=http://{{ tftp_bind_address }}/images/Ubuntu/12.04/install/filesystem.squashfs'
#  - label: 'Ubuntu 14.04.2 (Manual)'
#    menu_label: 'Install Ubuntu 14.04.2 (Manual)'
#    menu_default: false
#    kernel: images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/linux
#    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto live-installer/net-image=http://{{ tftp_bind_address }}/images/Ubuntu/14.04/install/filesystem.squashfs'
#  - label: 'Ubuntu 14.04.2 (Pre-Seed)'
#    menu_label: 'Install Ubuntu 14.04.2 (Pre-Seed)'
#    menu_default: false
#    kernel: images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/linux
#    append: 'auto=true priority=critical vga=788 initrd=tftp://{{ tftp_bind_address }}/images/Ubuntu/14.04/install/netboot/ubuntu-installer/amd64/initrd.gz locale=en_US.UTF-8 kbd-chooser/method=us netcfg/choose_interface=auto url=tftp://{{ tftp_bind_address }}/ubuntu_14.04_preseed.cfg live-installer/net-image=http://{{ tftp_bind_address }}/images/Ubuntu/14.04/install/filesystem.squashfs'
tftp_build_images: false  #defines if images folder(s) and isos should be added
tftp_images_folders:
  - CentOS/7
  - ESXi/5.1
  - ESXi/5.1U1
  - ESXi/5.1U2
  - ESXi/5.5
  - ESXi/5.5U1
  - ESXi/5.5U2
  - ESXi/5.5U3
  - ESXi/6.0
  - ESXi/6.0U1
  - Ubuntu/12.04
  - Ubuntu/14.04
tftp_poweroff_after_install: false  #defines if host should be shutdown after installing...good for mass PXE deployments when the option to do a one-time boot to PXE is not an option.
tftpboot_dir: /var/lib/tftpboot
tftp_iso_images: []
#  - url: http://www.gtlib.gatech.edu/pub/centos/7/isos/x86_64
#    file: CentOS-7-x86_64-Minimal-1503-01.iso
#    folder: CentOS/7
#  - url: http://mirror.pnl.gov/releases/12.04
#    file: ubuntu-12.04.5-server-amd64.iso
#    folder: Ubuntu/12.04
#  - url: http://mirror.pnl.gov/releases/14.04
#    file: ubuntu-14.04.2-server-amd64.iso
#    folder: Ubuntu/14.04
#vmware_iso_images:
#  - file: VMware-VMvisor-Installer-6.0.0.update01-3029758.x86_64.iso
#    folder: ESXi/6.0U1
tftp_preseed_create_users: false  #defines if Users should be created as part of preseed....define these in create_users
tftp_preseed_files:
  - preseed
  - ubuntu_12.04_preseed
  - ubuntu_14.04_preseed
  - ubuntu_16.04_preseed
tftp_preseed_users_encrypted_pw: true  #defines if users accounts are encrypted....this should be yes..but ensure that password under create_users is MD5 hash.
````

Dependencies
------------

````
- { role: mrlesmithjr.apache2 }
- { role: mrlesmithjr.apt-cacher-ng, when: enable_apt_caching is defined and enable_apt_caching }
- { role: mrlesmithjr.config-interfaces, when: config_interfaces is defined and config_interfaces }
- { role: mrlesmithjr.dnsmasq }
- { role: mrlesmithjr.isc-dhcp, when: enable_dhcp is defined and enable_dhcp }
````

Example Playbook
----------------

---
- hosts: tftpserver-nodes
  remote_user: remote
  sudo: true
  roles:
    - { role: mrlesmithjr.apache2 }
    - { role: mrlesmithjr.apt-cacher-ng, when: enable_apt_caching is defined and enable_apt_caching }
    - { role: mrlesmithjr.config-interfaces, when: config_interfaces is defined and config_interfaces }
    - { role: mrlesmithjr.dnsmasq }
    - { role: mrlesmithjr.isc-dhcp, when: enable_dhcp is defined and enable_dhcp }
    - mrlesmithjr.tftpserver


License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
