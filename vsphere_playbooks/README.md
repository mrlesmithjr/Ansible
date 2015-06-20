#vSphere Playbooks
###vsphere_dynamic_invetory.yml
######Creates a dynamic inventory hosts file from vCenter
###gather_vm_details.yml
######Builds out host_vars/inventory_hostname w/ansible_ssh_host var set
######(will not overwrite existing contents)
######Also updates and imports ssh_keys for hosts discovered
## Requirements
Requires python module pysphere to be installed
````
pip install -U pysphere
````
##Variables
###vsphere_dynamic_invetory.yml
````
ansible_root: ~/ansible  #defines where your ansible_root folder resides
host_vars_dir: '{{ ansible_root }}/host_vars'  #defines where your ansible host_vars folder resides
pysphere_script_home: library
vsphere_dynamic_inventory: vsphere_inventory
# - vcenter_hostname: ''  #defined in group_vars/all/configs or define here
# - vcenter_pass: ''  #defined in group_vars/all/accounts or define here
# - vcenter_user: ''  #defined in group_vars/all/accounts or define here
````
###gather_vm_details.yml
````
ansible_root: ~/ansible  #defines where your ansible_root folder resides
cleanup_temp: true  #defines cleaning up temp files/folders used in tasks....
gather_dir: ~/gather_info  #defines where to temporarily store gather information
host_vars_dir: '{{ ansible_root }}/host_vars'  #defines where your ansible host_vars folder resides
pysphere_script_home: library  #defines script folder location for python modules used
ssh_known_hosts_command: ssh-keyscan
ssh_known_hosts_dir: ~/.ssh  #define the location of where you want to store your ssh_keys
ssh_known_hosts_file: known_hosts  #defines the file of where you want to store your ssh_keys
# - vcenter_hostname: ''  #defined in group_vars/all/configs or define here
# - vcenter_pass: ''  #defined in group_vars/all/accounts or define here
# - vcenter_user: ''  #defined in group_vars/all/accounts or define here
tasks:
````
##Dependencies
None
##Example Playbook run
````
ansible-playbook vsphere_playbooks/vsphere_dynamic_inventory.yml
ansible-playbook -i vsphere_inventory vsphere_playbooks/gather_vm_details.yml
````
##License
GNU General Public License Version 2
##Author Information
Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
