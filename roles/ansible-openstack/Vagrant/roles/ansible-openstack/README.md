Role Name
=========

This role is to provision out a complete OpenStack (Kilo) deployment. Including all services, networks and tenants (Projects).

Requirements
------------

You must define an IP address and DNS FQDN to be used for Load Balancing and services to connect to. These vars are defined in openstack_services_vip and openstack_services_vip_fqdn

You also need to define Multi-Cast addresses for Pacemaker/Corosync HAProxy and Controller nodes. They MUST be different for each as we are creating separate Pacemaker clusters for HAProxy and Controller nodes. Define the Multi-Cast address in group_vars as below.

Also make sure to define one of your controller nodes as openstack_keystone_api_master...using keystone_user module does not work with run_once and causes additional controller nodes to fail when creating
keystone users, endpoints, tenants and services...

Also make sure to define one of your controller nodes as mysql_master...should be the same as the node defined as openstack_keystone_api_master...this should already be set if installing ansible-mariadb-galera-cluster role.

````
openstack_keystone_api_master: os-controller-01
````
host_vars/os-controller-01.yml
````
mysql_master: true
````
group_vars/openstack-controller-nodes/main.yml
````
corosync_mcastaddr: 239.255.42.1
````

group_vars/openstack-haproxy-nodes/main.yml
````
corosync_mcastaddr: 239.255.42.2
````

All additional Ansible requirements are included in the requirements.yml file.
````
sudo ansible-galaxy install -r requirements.yml
````

Role Variables
--------------

````
---
# defaults file for ansible-openstack
# generate passwords and keys using 'openssl rand -hex 10'
config_openstack_neutron_networks: false  #defines if networks in openstack_neutron_external_networks and openstack_neutron_tenant_networks are configured
enable_haproxy_admin_page: true
enable_haproxy_remote_syslog: true
haproxy_admin_user: admin
haproxy_admin_password: admin
haproxy_admin_port: 9090
mysql_master: false  #defines if inventory_hostname is considered mysql_master...This needs to be defined on one controller node in host_vars/os-controller-xx ..This should already be set for building Galera Cluster. **IMPORTANT***
mysql_root_password: []  #Root password for the database
openstack_admin_email: 'admin@{{ pri_domain_name }}'  #Defines admin users email
openstack_admin_pass: []  #Password of user admin
openstack_keystone_api_master: os-controller-01  #defines one of the controller nodes as a primary to create keystone users, endpoints, tenants and services...this gets around the issue of errors  since run_once does not work on keystone_user.
openstack_ceilometer_dbpass: []  #Database password for the Telemetry service
openstack_ceilometer_pass: []  #Password of Telemetry service user ceilometer
openstack_ceilometer_token_secret: []  #defines the token secret to configure Telemtry services.
openstack_ceilometer_url: 'http://{{ openstack_services_vip_fqdn }}'
openstack_ceilometer_verbose_logging: false  #Defines if ceilometer should enable verbose logging for troubleshooting
openstack_cinder_dbpass: []  #Database password for the Block Storage service
openstack_cinder_install: true  #Defines if Cinder (Block-Storage) services should be installed.
openstack_cinder_pass: []  #Password of Block Storage service user cinder
openstack_cinder_url: 'http://{{ openstack_services_vip_fqdn }}'  #http://cinder.{{ pri_domain_name }}
openstack_dash_dbpass: []  #Database password for the dashboard
openstack_debian_repository: 'deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-updates/{{ openstack_release }} main'
openstack_demo_email: 'demo@{{ pri_domain_name }}'  #Defines demo users email
openstack_demo_pass: []  #Password of user demo
openstack_enable_remote_syslog: false  #defines if all openstack services should write to syslog which allows remote syslog functionality...
openstack_glance_dbhost: "{{ openstack_services_vip_fqdn }}"  #Defines glance db host
openstack_glance_dbpass: []  #Database password for Image Service
openstack_glance_images:  #define cloud images to automatically upload to Glance
  - name: cirros
    container_format: bare
    disk_format: qcow2
    image_url: http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img
    installed: true
  - name: Fedora-22
    container_format: bare
    disk_format: qcow2
    image_url: http://repo.atlantic.net/fedora/linux/releases/22/Cloud/x86_64/Images/Fedora-Cloud-Base-22-20150521.x86_64.qcow2
    installed: true
  - name: Ubuntu-14.04
    container_format: bare
    disk_format: qcow2
    image_url: https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img
    installed: true
openstack_glance_manage_images: false  #defines if images should be managed based on openstack_glance_images....this should be ran as part of the playbook as a local task
# rather than during initial deploy as it will error our and tasks will fail due to services for keystone and glance not being restarted. But can be set to true after the stack is up!!!
openstack_glance_pass: []  #Password of Image Service user glance
openstack_glance_url: 'http://{{ openstack_services_vip_fqdn }}'  #http://glance.{{ pri_domain_name }}
openstack_glance_verbose_logging: false  #Defines if glance should enable verbose logging for troubleshooting
openstack_group_based_policy_install: false  #Defines if Group Based Policy Should be installed. https://wiki.openstack.org/wiki/GroupBasedPolicy/InstallUbuntu
openstack_haproxy_config: true  #defines if haproxy should be configured on controller nodes....can separate out but installing on controller nodes is common practice and use corosync/pacemaker to handle the VIP.
openstack_heat_dbhost: '{{ openstack_services_vip_fqdn }}'  #Defines heat db host
openstack_heat_dbpass: []  #Database password for the Orchestration service
openstack_heat_domain_pass: []  #Password for Heat domain in Identity service
openstack_heat_install: true  #Defines if Heat (Orchestration Module) is to be installed
openstack_heat_pass: []  #Password of Orchestration service user heat
openstack_heat_url: 'http://{{ openstack_services_vip_fqdn }}'  #http://heat.{{ pri_domain_name }}
openstack_heat_verbose_logging: false  #Defines if glance should enable verbose logging for troubleshooting
openstack_horizon_install: true  #Defines if Horizon Dashboard should be installed
openstack_horizon_remove_ubuntu_theme: false  #Defines if the Ubuntu Horizon theme should be removed and the original Horizon theme restored
openstack_instance_tunnel_ip: []  #Define interface address for tunnel interface....ex. {{ ansible_eth2.ipv4.address }}
openstack_keystone_dbhost: '{{ openstack_services_vip_fqdn }}'  #Defines keystone db host
openstack_keystone_dbpass: []  #Database password of Identity service
openstack_keystone_default_region: regionOne
openstack_keystone_endpoints:
  - service_name: ceilometer
    public_url: "{{ openstack_ceilometer_url }}:8777"
    internal_url: "{{ openstack_ceilometer_url }}:8777"
    admin_url: "{{ openstack_ceilometer_url }}:8777"
  - service_name: cinder
    public_url: "{{ openstack_cinder_url }}:8776/v2/%(tenant_id)s"
    internal_url: "{{ openstack_cinder_url }}:8776/v2/%(tenant_id)s"
    admin_url: "{{ openstack_cinder_url }}:8776/v2/%(tenant_id)s"
  - service_name: cinderv2
    public_url: "{{ openstack_cinder_url }}:8776/v2/%(tenant_id)s"
    internal_url: "{{ openstack_cinder_url }}:8776/v2/%(tenant_id)s"
    admin_url: "{{ openstack_cinder_url }}:8776/v2/%(tenant_id)s"
  - service_name: glance
    public_url: "{{ openstack_glance_url }}:9292"
    internal_url: "{{ openstack_glance_url }}:9292"
    admin_url: "{{ openstack_glance_url }}:9292"
  - service_name: heat
    public_url: "{{ openstack_heat_url }}:8004/v1/%(tenant_id)s"
    internal_url: "{{ openstack_heat_url }}:8004/v1/%(tenant_id)s"
    admin_url: "{{ openstack_heat_url }}:8004/v1/%(tenant_id)s"
  - service_name: heat-cfn
    public_url: "{{ openstack_heat_url }}:8000/v1"
    internal_url: "{{ openstack_heat_url }}:8000/v1"
    admin_url: "{{ openstack_heat_url }}:8000/v1"
  - service_name: keystone
    public_url: "{{ openstack_keystone_url }}:5000/v2.0"
    internal_url: "{{ openstack_keystone_url }}:5000/v2.0"
    admin_url: "{{ openstack_keystone_url }}:35357/v2.0"
  - service_name: neutron
    public_url: "{{ openstack_neutron_url }}:9696"
    internal_url: "{{ openstack_neutron_url }}:9696"
    admin_url: "{{ openstack_neutron_url }}:9696"
  - service_name: nova
    public_url: "{{ openstack_nova_url }}:8774/v2/%(tenant_id)s"
    internal_url: "{{ openstack_nova_url }}:8774/v2/%(tenant_id)s"
    admin_url: "{{ openstack_nova_url }}:8774/v2/%(tenant_id)s"
openstack_keystone_roles:  #Tenants are now Projects
  - name: admin
    user: admin
    tenant: admin
  - name: admin
    user: ceilometer
    tenant: service
  - name: admin
    user: cinder
    tenant: service
  - name: admin
    user: glance
    tenant: service
  - name: admin
    user: heat
    tenant: service
  - name: heat_stack_owner
    user: demo
    tenant: demo
  - name: heat_stack_user
    user: demoheatuser  #account to test as a Heat user vs. Heat owner...same password as demo account
    tenant: demo
  - name: admin
    user: neutron
    tenant: service
  - name: admin
    user: nova
    tenant: service
  - name: user
    user: demo
    tenant: demo
openstack_keystone_services:
  - name: ceilometer
    description: "Telemetry"
    service_type: metering
  - name: cinder
    description: "OpenStack Block Storage"
    service_type: volume
  - name: cinderv2
    description: "OpenStack Block Storage"
    service_type: volumev2
  - name: glance
    description: "OpenStack Image Service"
    service_type: image
  - name: heat
    description: "Orchestration"
    service_type: orchestration
  - name: heat-cfn
    description: "Orchestration"
    service_type: cloudformation
  - name: keystone
    description: "OpenStack Identity"
    service_type: identity
  - name: neutron
    description: "OpenStack Networking"
    service_type: network
  - name: nova
    description: "OpenStack Compute"
    service_type: compute
openstack_keystone_temp_admin_token: []  #Key for initial setup of keystone
openstack_keystone_tenants:  #Tenants are now Projects
  - name: admin
    description: "Admin Project"
  - name: demo
    description: "Demo Project"
  - name: service
    description: "Service Project"
openstack_keystone_url: 'http://{{ openstack_services_vip_fqdn }}'  #http://keystone.{{ pri_domain_name }}
openstack_keystone_users:  #Tenants are now Projects
  - name: admin
    password: "{{ openstack_admin_pass }}"
    email: "{{ openstack_admin_email }}"
    tenant: admin
  - name: ceilometer
    password: "{{ openstack_ceilometer_pass }}"
    tenant: service
  - name: cinder
    password: "{{ openstack_cinder_pass }}"
    tenant: service
  - name: demo
    password: "{{ openstack_demo_pass }}"
    email: "{{ openstack_demo_email }}"
    tenant: demo
  - name: demoheatuser  #account to test as a Heat user vs. Heat owner...same password as demo account
    password: "{{ openstack_demo_pass }}"
    email: "{{ openstack_demo_email }}"
    tenant: demo
  - name: glance
    password: "{{ openstack_glance_pass }}"
    tenant: service
  - name: heat
    password: "{{ openstack_heat_pass }}"
    tenant: service
  - name: neutron
    password: "{{ openstack_neutron_pass }}"
    tenant: service
  - name: nova
    password: "{{ openstack_nova_pass }}"
    tenant: service
openstack_keystone_verbose_logging: false  #Defines if keystone should enable verbose logging for troubleshooting
openstack_metadata_secret: []  #Defines shared metadata secret for metadata services
openstack_mongodb_admin_user: admin  #define mongodb admin user for mongodb cluster
openstack_mongodb_dbpath: /var/lib/mongodb  #defines mongodb path for database
openstack_mongodb_keyfile: /etc/mongodb-keyfile  #defines where auth keyfile is located
openstack_mongodb_master: false  #defines if host is master or slave...define false here and set to true on one host_vars/hostname
openstack_multi_controller_setup: false  #defines if more than 1 controller is being setup...for production this should be set to true with at least 3 controllers.
openstack_networking: neutron  #Defines networking to use...neutron or nova (legacy)
openstack_neutron_bridges:  #defines OVS bridges and physical interface(s)
  - bridge_name: br-ex  #defines the OVS Bridge name to create.
    physical_networks:
      - external  #defines the physical_network name which maps to the OVS bridge_name
#      - external-vlans
    ports:  #defines the physical interface port(s)
      - eth2
openstack_neutron_dbhost: '{{ openstack_services_vip_fqdn }}'  #Defines neutron db host
openstack_neutron_dbpass: []  #Database password for the Networking service
openstack_neutron_dhcp_domain: '{{ pri_domain_name }}'  #Defines the domain name assigned to tenant instances
openstack_neutron_dhcp_dnsmasq_dns_servers: '8.8.8.8,8.8.4.4'  # Comma-separated list of DNS servers which will be used by dnsmasq as forwarders.
openstack_neutron_external_networks: #Define external networking resources
  - name: external-networks  #description for networks
    login_password: "{{ openstack_admin_pass }}"
    login_username: admin
    login_tenant_name: admin
    region_name: #Name of the region
    networks:  #define networks to create
      - name: ext-net #Name to be assigned to the nework
        admin_state_up: true #Whether the state should be marked as up or down
        provider_network_type: flat #The type of the network to be created, flat, gre, vxlan, vlan, local
        provider_physical_network: external #The physical network which would realize the virtual network for flat and vlan networks. Defined in openstack_neutron_bridges.
        provider_segmentation_id: #The id that has to be assigned to the network, in case of vlan networks that would be vlan id, for gre the tunnel id and for vxlan the VNI
        router_external: true #If 'yes', specifies that the virtual network is a external network (public)
        shared: false #Whether this network is shared or not
        state: present #Indicate desired state of the resource
    router_interfaces:
      - router_name: external-router #Name of the router to which the subnet's interface should be attached
        subnet_name: ext-subnet #Name of the subnet to whose interface should be attached to the router
        state: present #Indicate desired state of the resource
    routers: #Defines routers to create
      - name: external-router #Name to be give to the router
        admin_state_up: true #desired admin state of the created router
        state: present #Indicate desired state of the resource
    subnets:  #define subnets to create by using networks created above
      - name: ext-subnet
        allocation_pool_end: 192.168.114.224 #From the subnet pool the last IP that should be assigned to the virtual machines
        allocation_pool_start: 192.168.114.128 #From the subnet pool the starting address from which the IP should be allocated
        cidr: 192.168.114.0/24 #The CIDR representation of the subnet that should be assigned to the subnet
        dns_nameservers: 8.8.8.8,8.8.4.4 #DNS nameservers for this subnet, comma-separated
        enable_dhcp: false #Whether DHCP should be enabled for this subnet
        gateway_ip: 192.168.114.1 #The ip that would be assigned to the gateway for this subnet
        ip_version: 4 #The IP version of the subnet 4 or 6
        network_name: ext-net  #Name of the network to which the subnet should be attached
        no_gateway: false #If "true", no gateway will be created for this subnet
        state: present #Indicate desired state of the resource
openstack_neutron_flat_networks:  #defines the physical_network(s) defined in openstack_neutron_bridges to use as external uplinks for flat networking.
#  - external
  - "*"  #defines allow all
openstack_neutron_mechanism_drivers:  #defines the networking mechanism driver entrypoints to load....openvswitch, arista, cisco, brocade, linuxbridge, and etc....
  - openvswitch
  - l2population
#  - cisco
openstack_neutron_pass: []  #Password of Networking service user neutron
openstack_neutron_tenant_network_types:  #defines tenant network type(s) for tenant networks..local,vlan,gre,vxlan
  - gre
openstack_neutron_tenant_networks:
    - name: demo-networks
      login_password: "{{ openstack_demo_pass }}"
      login_username: demo
      login_tenant_name: demo
      region_name: #Name of the region
      networks:  #define networks to create
        - name: demo-net-1 #Name to be assigned to the nework
          admin_state_up: true #Whether the state should be marked as up or down
          provider_network_type: flat #The type of the network to be created, flat, gre, vxlan, vlan, local
          shared: false #Whether this network is shared or not
          state: present #Indicate desired state of the resource
        - name: demo-net-2 #Name to be assigned to the nework
          admin_state_up: true #Whether the state should be marked as up or down
          provider_network_type: flat #The type of the network to be created, flat, gre, vxlan, vlan, local
          shared: false #Whether this network is shared or not
          state: present #Indicate desired state of the resource
      router_interfaces:
        - router_name: demo-router #Name of the router to which the subnet's interface should be attached
          subnet_name: demo-subnet-1 #Name of the subnet to whose interface should be attached to the router
          state: present #Indicate desired state of the resource
        - router_name: demo-router #Name of the router to which the subnet's interface should be attached
          subnet_name: demo-subnet-2 #Name of the subnet to whose interface should be attached to the router
          state: present #Indicate desired state of the resource
      routers: #Defines routers to create
        - name: demo-router #Name to be give to the router
          admin_state_up: true #desired admin state of the created router
          state: present #Indicate desired state of the resource
      subnets:  #define subnets to create by using networks created above
        - name: demo-subnet-1
          allocation_pool_end: 192.168.10.50 #From the subnet pool the last IP that should be assigned to the virtual machines
          allocation_pool_start: 192.168.10.25 #From the subnet pool the starting address from which the IP should be allocated
          cidr: 192.168.10.0/24 #The CIDR representation of the subnet that should be assigned to the subnet
          dns_nameservers: 8.8.8.8,8.8.4.4 #DNS nameservers for this subnet, comma-separated
          enable_dhcp: true #Whether DHCP should be enabled for this subnet
          gateway_ip: 192.168.10.1 #The ip that would be assigned to the gateway for this subnet
          ip_version: 4 #The IP version of the subnet 4 or 6
          network_name: demo-net-1  #Name of the network to which the subnet should be attached
          no_gateway: false #If "true", no gateway will be created for this subnet
          state: present #Indicate desired state of the resource
        - name: demo-subnet-2
          allocation_pool_end: 192.168.11.50 #From the subnet pool the last IP that should be assigned to the virtual machines
          allocation_pool_start: 192.168.11.25 #From the subnet pool the starting address from which the IP should be allocated
          cidr: 192.168.11.0/24 #The CIDR representation of the subnet that should be assigned to the subnet
          dns_nameservers: 8.8.8.8,8.8.4.4 #DNS nameservers for this subnet, comma-separated
          enable_dhcp: true #Whether DHCP should be enabled for this subnet
          gateway_ip: 192.168.11.1 #The ip that would be assigned to the gateway for this subnet
          ip_version: 4 #The IP version of the subnet 4 or 6
          network_name: demo-net-2  #Name of the network to which the subnet should be attached
          no_gateway: false #If "true", no gateway will be created for this subnet
          state: present #Indicate desired state of the resource
openstack_neutron_tunnel_types:  #defines the tunnel types to use for agent communications....gre, vxlan, etc.
  - gre
openstack_neutron_type_drivers:  #local, flat, vlan, gre, vxlan
  - flat
  - gre
  - vlan
  - vxlan
openstack_neutron_url: 'http://{{ openstack_services_vip_fqdn }}'
openstack_neutron_verbose_logging: false  #Defines if neutron should enable verbose logging for troubleshooting
openstack_neutron_vlans:  #define vlans to be configured as external networks....ex. 101, or for a group 101:110
  - physical_network: external
    vlans:
      - range: 114:114
openstack_nova_dbhost: '{{ openstack_services_vip_fqdn }}'  #Defines nova db host
openstack_nova_dbpass: []  #Database password for Compute service
openstack_nova_my_ip: '{{ ansible_eth0.ipv4.address }}' #defines the my_ip variable in nova
openstack_nova_pass: []  #Password of Compute service user nova
openstack_nova_url: 'http://{{ openstack_services_vip_fqdn }}'  #http://nova.{{ pri_domain_name }}
openstack_nova_virt_type: kvm  #Nova virtualization Type, set to KVM if supported and QEMU if not
openstack_rabbit_host: '{{ openstack_services_vip_fqdn }}'  #Defines RabbitMQ host
openstack_rabbit_pass: []  #Password of user of RabbitMQ
openstack_rabbit_user: openstack  #User of RabbitMQ
openstack_release: kilo  #Defines openstack release to install
openstack_services_vip: 10.0.101.61  #Define IP to configure LB VIP
openstack_services_vip_fqdn: 'openstack.{{ pri_domain_name }}'  #Define FQDN for the openstack_services_vip...This should be used for all services to connect to.
openstack_services_vip_cidr: 24
openstack_services_vip_int: eth0  #defines the interface to configure Pacemaker to listen on
openstack_telementry_install: true  #defines if Telemetry (Ceilometer) should be installed.
openstack_trove_dbpass: []  #Database password of Database service
openstack_trove_pass: []  #Password of Database Service user trove
pri_domain_name: example.org  #Defines primary domain name of site.
syslog_servers:
  - name: 'logstash.{{ pri_domain_name }}'
    proto: tcp
    port: 514
````

Dependencies
------------

None

Example Playbook
----------------
````
---
# Bootstrap Hosts
- name: Bootstrapping Hosts
  hosts: openstack-nodes
  any_errors_fatal: true  #Added this to ensure plays will stop completely in case of failure. We want to do this in order to not cause issues in remaining plays.
  sudo: true
  vars:
  roles:
    - role: ansible-bootstrap
      tags:
        - bootstrap
    - role: ansible-users
      tags:
        - bootstrap
    - role: ansible-manage-ssh-keys
      tags:
        - bootstrap

- name: Ensure Hostnames are correct and reboot if needed
  hosts: openstack-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-change-hostname

- name: Setting Up Base Apps
  hosts: openstack-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-base
    - role: ansible-config-interfaces
    - role: ansible-ntp
    - role: ansible-rsyslog
    - role: ansible-postfix
    - role: ansible-snmpd
    - role: ansible-timezone

- name: Setting up (openstack-haproxy-nodes)
  hosts: openstack-haproxy-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-haproxy
    - role: ansible-pacemaker
      when: (openstack_multi_controller_setup is defined and openstack_multi_controller_setup)

- name: Setting up (openstack-controller-nodes)
  hosts: openstack-controller-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-apache2
    - role: ansible-mariadb-mysql
      when: (openstack_multi_controller_setup is defined and not openstack_multi_controller_setup)
    - role: ansible-mariadb-galera-cluster
      when: (openstack_multi_controller_setup is defined and openstack_multi_controller_setup)
    - role: ansible-memcached
    - role: ansible-rabbitmq
    - role: ansible-pacemaker
      when: (openstack_multi_controller_setup is defined and openstack_multi_controller_setup)

- name: Setting up (openstack-compute-nodes)
  hosts: openstack-compute-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-manage-lvm

- name: Setting up (openstack-storage-nodes)
  hosts: openstack-storage-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-manage-lvm

- name: Builds OpenStack Environment
  hosts: openstack-nodes
  any_errors_fatal: true
  sudo: true
  vars:
  roles:
    - role: ansible-openstack
  tags:
    - openstack
  tasks:

####################
- name: Local Tasks
  hosts: localhost
  connection: local
  sudo: false
  vars:
  tasks:
    - name: creating client script(s)  #creating this to source in order to create heat domain
      template:
        src: "templates/{{ item }}-openrc.sh.j2"
        dest: "./{{ item }}-openrc.sh"
        mode: 0700
      tags:
        - create-openstack-client-scripts
      with_items:
        - admin
        - demo

################################
- name: manage glance images
  hosts: localhost
  connection: local
  sudo: false
  vars:
    - openstack_glance_images:  #define cloud images to automatically upload to Glance
        - name: cirros
          container_format: bare
          disk_format: qcow2
          image_url: http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img
          installed: true
        - name: Fedora-22
          container_format: bare
          disk_format: qcow2
          image_url: http://repo.atlantic.net/fedora/linux/releases/22/Cloud/x86_64/Images/Fedora-Cloud-Base-22-20150521.x86_64.qcow2
          installed: true
        - name: Ubuntu-14.04
          container_format: bare
          disk_format: qcow2
          image_url: https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img
          installed: true
    - openstack_glance_manage_images: true
  tasks:
    - name: uploading glance images
      glance_image:
        auth_url: "{{ openstack_keystone_auth_url }}"  #defined in group_vars/all/openstack_auth_urls.yml
        login_username: admin
        login_password: "{{ openstack_admin_pass }}"  #defined in group_vars/all/accounts.yml
        login_tenant_name: admin
        name: "{{ item.name }}"
        container_format: "{{ item.container_format }}"
        disk_format: "{{ item.disk_format }}"
        state: present
        copy_from: "{{ item.image_url }}"
      tags:
        - manage_glance_images
      with_items: openstack_glance_images
      when: (openstack_glance_manage_images is defined and openstack_glance_manage_images) and (item.installed is defined and item.installed)

    - name: manage_glance_images | removing glance images
      glance_image:
        auth_url: "{{ openstack_keystone_auth_url }}"   #defined in group_vars/all/openstack_auth_urls.yml
        login_username: admin
        login_password: "{{ openstack_admin_pass }}"  #defined in group_vars/all/accounts.yml
        login_tenant_name: admin
        name: "{{ item.name }}"
        state: absent
      tags:
        - manage_glance_images
      with_items: openstack_glance_images
      when: (openstack_glance_manage_images is defined and openstack_glance_manage_images) and (item.installed is defined and not item.installed)
````
group_vars/all/accounts.yml
````
---
# generate passwords and keys using 'openssl rand -hex 10'
mysql_root_password: 61fea78e16dd73bd757a  #Root password for the database
openstack_admin_pass: 29b1416692cb38014ea0  #Password of user admin
openstack_ceilometer_dbpass: 85c4ac62a58c0a25a922  #Database password for the Telemetry service
openstack_ceilometer_pass: c3e1b1db22e9b33cd7f4  #Password of Telemetry service user ceilometer
openstack_cinder_dbpass: bcb4f4279d699c12c6ea  #Database password for the Block Storage service
openstack_cinder_pass: d9eb36abbb2e88356208  #Password of Block Storage service user cinder
openstack_dash_dbpass: cb77b8806e4dc8693d8e  #Database password for the dashboard
openstack_demo_pass: 54a27efd264beeb7843d  #Password of user demo
openstack_glance_dbpass: 295062a986b8deded530  #Database password for Image Service
openstack_glance_pass: 60278dafa015c0cc3943  #Password of Image Service user glance
openstack_heat_dbpass: d69d8f9bd2a70f0f1f5b  #Database password for the Orchestration service
openstack_heat_domain_pass: 72a9474bf295fe4315bd  #Password for Heat domain in Identity service
openstack_heat_pass: 9fd0ae5b48837ad34b31  #Password of Orchestration service user heat
openstack_keystone_dbpass: 8ed178efd2bef6fcabe3  #Database password of Identity service
openstack_keystone_temp_admin_token: 52f5e14ad1a9f7d54e1d  #Key for initial setup of keystone
openstack_metadata_secret: 91c94f7734057cb3db6a  #defines shared metadata secret for metadata services
openstack_neutron_dbpass: 7bff44471bdce25d55af  #Database password for the Networking service
openstack_neutron_pass: 19440ed58e9ba153bbb5  #Password of Networking service user neutron
openstack_nova_dbpass: b544e0b6881f33c82dc8  #Database password for Compute service
openstack_nova_pass: 34e5f8990ef84cc69f91  #Password of Compute service user nova
openstack_rabbit_pass: 6bd8dbb369181e89bf3a  #Password of user guest of RabbitMQ
openstack_trove_dbpass: c6c2792fa14319dbe9da  #Database password of Database service
openstack_trove_pass: 892ba2ff14319c299b54  #Password of Database Service user trove
````
group_vars/all/main.yml
````
---
pri_domain_name: example.org  #defines primary domain name of site.
update_etc_hosts: true
````
group_vars/openstack-compute-nodes/main.yml
````
---
config_network_interfaces: true
network_interfaces:  #define interfaces and settings. (Define separately for each node in host_vars) - Anything not defined can be added to addl_settings.
  - name: eth0
    configure: true
    comment: management interface
    method: dhcp
    address:
    netmask:
    netmask_cidr:
    gateway:
#    addl_settings:
#      - bond_master bond0
  - name: eth1
    configure: true
    comment: tunnel interface
    method: static
    address: '{{ openstack_instance_tunnel_ip }}'
    netmask: 255.255.255.0
    netmask_cidr: 24
    gateway:
#    addl_settings:
#      - bond_master bond0
````
group_vars/openstack-controller-nodes/main.yml
````
---
config_rabbitmq_ha: true
corosync_mcastaddr: 239.255.42.2
enable_rabbitmq_clustering: true
galera_cluster_name: openstack # Define the name of the cluster...define here or in group_vars/group
galera_cluster_nodes: '10.0.101.139,10.0.101.137,10.0.101.180' # Define the IP addresses of the nodes which will be part of the cluster...define here or in group_vars/group
rabbitmq_config:
  - queue_name: '^(?!amq\.).*'
    durable: true
    tags: 'ha-mode=all,ha-sync-mode=automatic'
````
group_vars/openstack-haproxy-nodes/main.yml
````
---
corosync_mcastaddr: 239.255.42.1
````
group_vars/openstack-network-nodes/main.yml
````
---
config_network_interfaces: true
network_interfaces:  #define interfaces and settings. (Define separately for each node in host_vars) - Anything not defined can be added to addl_settings.
  - name: eth0
    configure: true
    comment: management interface
    method: dhcp
    address:
    netmask:
    netmask_cidr:
    gateway:
#    addl_settings:
#      - bond_master bond0
  - name: eth1
    configure: true
    comment: tunnel interface
    method: static
    address: '{{ openstack_instance_tunnel_ip }}'
    netmask: 255.255.255.0
    netmask_cidr: 24
    gateway:
#    addl_settings:
#      - bond_master bond0
  - name: eth2
    configure: true
    comment: tunnel interface
    method: manual
    address: 0.0.0.0
    netmask: 255.255.255.0
    netmask_cidr: 24
    gateway:
    addl_settings:
      - up ip link set $IFACE promisc on
      - down ip link set $IFACE promisc off
      - down ifconfig $IFACE down
````
group_vars/openstack-nodes/main.yml
````
---
config_openstack_neutron_networks: true
corosync_bindnet_addr: "{{ ansible_eth0.ipv4.network }}"  #defines the interface to use for syncing cluster..this is a /24 address...ie...
corosync_expected_votes: 1  #defines the number of nodes to be functional in order to avoid split-brain scenarios...ex. 2-nodes = 1, 3-nodes = 2
mysql_allow_remote_connections: true  #defines if mysql should listen on loopback (default) or allow remove connections
openstack_enable_remote_syslog: true  #defines if all openstack services should write to syslog which allows remote syslog functionality...
openstack_glance_verbose_logging: true  #defines if glance should enable verbose logging for troubleshooting
openstack_haproxy_install: true  #defines if haproxy should be installed on controller nodes....can separate out but installing on controller nodes is common practice and use corosync/pacemaker to handle the VIP.
openstack_heat_verbose_logging: true  #defines if glance should enable verbose logging for troubleshooting
openstack_horizon_remove_ubuntu_theme: true  #defines if the Ubuntu Horizon theme should be removed and the original Horizon theme restored
openstack_keystone_verbose_logging: true  #defines if keystone should enable verbose logging for troubleshooting
openstack_multi_controller_setup: true
openstack_neutron_verbose_logging: true  #defines if neutron should enable verbose logging for troubleshooting
openstack_nova_virt_type: qemu  #Nova virtualization Type, set to KVM if supported and QEMU if not
rabbitmq_master: os-controller-01
````
host_vars/os-compute-01
````
---
ansible_ssh_host: 10.0.101.143
openstack_instance_tunnel_ip: 10.0.111.31 #define interface address for tunnel interface....ex. {{ ansible_eth2.ipv4.addres }}
````
host_vars/os-compute-02
````
---
ansible_ssh_host: 10.0.101.191
openstack_instance_tunnel_ip: 10.0.111.32 #define interface address for tunnel interface....ex. {{ ansible_eth2.ipv4.addres }}
````
host_vars/os-controller-01
````
---
mysql_master: true
pacemaker_primary_server: true
````
host_vars/os-network-01
````
---
ansible_ssh_host: 10.0.101.141
openstack_instance_tunnel_ip: 10.0.111.21 #define interface address for tunnel interface....ex. {{ ansible_eth2.ipv4.addres }}
````
host_vars/os-network-02
````
---
ansible_ssh_host: 10.0.101.142
openstack_instance_tunnel_ip: 10.0.111.22 #define interface address for tunnel interface....ex. {{ ansible_eth2.ipv4.addres }}
````

Inventory Hosts
````
[openstack-nodes]
os-haproxy-[01:02]
os-controller-[01:03]
os-network-[01:02]
os-compute-[01:02]

[openstack-controller-nodes]
os-controller-[01:03]

[openstack-haproxy-nodes]
os-haproxy-[01:02]

[openstack-network-nodes]
os-network-[01:02]

[openstack-compute-nodes]
os-compute-[01:02]
````

Notes
-----

Some things to note...
In order to allow ping/ssh ingress on floating-IPs you need to create the following rules.
````
$ neutron security-group-rule-create --protocol icmp \
  --direction ingress --remote-ip-prefix 0.0.0.0/0 default

$ neutron security-group-rule-create --protocol tcp \
  --port-range-min 22 --port-range-max 22 \
  --direction ingress --remote-ip-prefix 0.0.0.0/0 default
````

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
