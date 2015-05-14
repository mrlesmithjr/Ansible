# Ansible
I will be sharing some of my Ansible roles and playbooks here going forward.
Projects - What I use for deployments using vm_provisioning scripts and playbooks. These projects use the roles folder for installs.
roles - individual specific role based playbooks
vm_provisioning - scripts and playbooks for provisioning vms on vSphere via Ansible

# Bootstrap role
You need to generate and copy a SSH public key to place in roles/bootstrap/files to upload to your servers.
Generate SSH key using 'ssh-keygen' and copy and rename id_rsa.pub to roles/bootstrap/files
