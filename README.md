# Ansible
I will be sharing some of my Ansible roles and playbooks here going forward.
Projects - What I use for deployments using vm_provisioning scripts and playbooks. These projects use the roles folder for installs.
roles - individual specific role based playbooks
vm_provisioning - scripts and playbooks for provisioning vms on vSphere via Ansible

# Bootstrap role
You need to generate and copy a SSH public key to place in roles/bootstrap/files to upload to your servers.
Generate SSH key using 'ssh-keygen' and copy and rename id_rsa.pub to roles/bootstrap/files

# Projects
I have included a template folder within Projects. This can be used to start building out environments using Ansible roles and such.
Make the following changes within the playbooks folder for your project.
playbooks/provision.yml

  vars:
    vcenter_hostname: 'vcsa.everythingshouldbevirtual.local'
    vcenter_user: 'ansible@everythingshouldbevirtual.local'
    datacenter: 'everythingshouldbevirtual'
    esxi_host: 'esxi01.everythingshouldbevirtual.local'
    notes: 'Created by Ansible'
    vm_state: 'present'
    vm_task_action: 'none' # none|create|create_from_template|reconfigure
    cluster: 'HA-DRS-CLUSTER'
    resource_pool: '/Resources'
