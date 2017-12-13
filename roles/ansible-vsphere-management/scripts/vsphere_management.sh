#! /usr/bin/env bash

# Stop script on error in order to troubleshoot issues
set -e

####
# Beginning of script execution path detection
####
# SCRIPT_NAME=$0
SCRIPT_FULL_PATH=$(dirname "$0")
####
# End of script execution path detection
####

####
# Beginning of variable definitions
####
# Define the directory to your Ansible inventory
ANSIBLE_INVENTORY_DIR="$SCRIPT_FULL_PATH/../inventory"

# Define the number of Ansible forks
ANSIBLE_NUMBER_OF_FORKS=5

# Define command or path to ansible-playbook command
ANSIBLE_PLAYBOOK_COMMAND=$(which ansible-playbook)

# Define the directory to your Ansible playbooks
ANSIBLE_PLAYBOOKS_DIR="$SCRIPT_FULL_PATH/../playbooks"

# Define the directory to your Ansible roles
ANSIBLE_ROLES_DIR="$SCRIPT_FULL_PATH/../roles"

# Define the directory to store logs in
LOG_DIR="$SCRIPT_FULL_PATH/../logs"

# Define command or path to terraform command
TERRAFORM_COMMAND=$(which terraform)

# Define the directory to Terraform
TERRAFORM_DIR="$SCRIPT_FULL_PATH/../../terraform"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Defines the Vagrant folder for deployment_host_spinup()
# The Windows 2016 Vagrant environment is included which is what the default
# deployment host has been for all of the development of this project.
VAGRANT_FOLDER="$SCRIPT_FULL_PATH/../Vagrant"
####
# End of variable definitions
####

export ANSIBLE_FORKS=$ANSIBLE_NUMBER_OF_FORKS
export ANSIBLE_INVENTORY=$ANSIBLE_INVENTORY_DIR
export ANSIBLE_LOG_PATH=$LOG_DIR/ansible.log
export ANSIBLE_ROLES_PATH=$ANSIBLE_ROLES_DIR

####
## Beginning of vSphere functions
####

_ansible_playbook_task()
{
  $ANSIBLE_PLAYBOOK_COMMAND $ANSIBLE_PLAYBOOKS_DIR/$_ANSIBLE_PLAYBOOK "$@"
}

_reboot()
{
  _ANSIBLE_PLAYBOOK="reboot.yml"
  _ansible_playbook_task "$@"
}

_vsphere_ddi()
{
  _ANSIBLE_PLAYBOOK="vsphere_ddi.yml"
  _ansible_playbook_task "$@"
}

_vsphere_dnsdist()
{
  _ANSIBLE_PLAYBOOK="vsphere_dnsdist.yml"
  _ansible_playbook_task "$@"
}

_vsphere_lb()
{
  _ANSIBLE_PLAYBOOK="vsphere_lb.yml"
  _ansible_playbook_task "$@"
}

_vsphere_management(){
  _ANSIBLE_PLAYBOOK="vsphere_management.yml"
  _ansible_playbook_task "$@"
}

_vsphere_samba()
{
  _ANSIBLE_PLAYBOOK="vsphere_samba.yml"
  _ansible_playbook_task "$@"
}

cleanup()
{
  CLEANUP_FILES=(
    ".galaxy_install_info" \
    "*.retry" \
    "generated_inventory.inv" \
    "ssh_keys_distribution.yml" \
    "vsphere_bootstrap_vms.inv" \
    "vsphere_bootstrap_vms.json" \
    "vsphere_ddi_vms.inv" \
    "vsphere_ddi_vms.json" \
    "vsphere_destroy_vms.inv" \
    "vsphere_dhcp_vms.inv" \
    "vsphere_dnsdist_vms.inv" \
    "vsphere_dnsdist_vms.json" \
    "vsphere_hosts.inv" \
    "vsphere_lb_vms.inv" \
    "vsphere_lb_vms.json" \
    "vsphere_samba_vms.inv" \
    "vsphere_samba_vms.json" \
    "vsphere_vcenter.inv"
  )
  for cleanup in "${CLEANUP_FILES[@]}"
  do
    find $SCRIPT_FULL_PATH/.. -type f -name $cleanup -exec rm -f {} \;
  done
  # Cleanup host_vars generated
  find $ANSIBLE_INVENTORY_DIR/host_vars/ -type f -name generated_details.yml -exec rm -f {} \;
}

deploy_all()
{
  vsphere_vcenter_check
  vsphere_management
  vsphere_vms
  vsphere_dnsdist_vms
  vsphere_samba_phase_1
  vsphere_ddi_vms
  vsphere_lb_vms
  vsphere_dns
  vsphere_pdns
  vsphere_post_deployment_reboot
  vsphere_ssh_key_distribution
  vsphere_samba_phase_2
  vsphere_post_samba_deployment_reboot
  vsphere_samba_sysvol_replication
  vsphere_ad_domain
  vsphere_vcsa
  vsphere_vcenter
  # vsphere_vcsa_ad
  vsphere_management
  exit 0
}

deployment_host_halt()
{
  cd $VAGRANT_FOLDER
  vagrant halt
  cd -
}

deployment_host_spinup()
{
  cd $VAGRANT_FOLDER
  vagrant up
  cd -
}

deployment_host_teardown()
{
  cd $VAGRANT_FOLDER
  scripts/cleanup.sh
  cd -
}

display_usage() {
  echo "vSphere Management Script"
  echo -e "\nThis script is for managing your vSphere environment in a holistic fashion.\n"
  echo -e "Twitter:\thttps://www.twitter.com/mrlesmithjr"
  echo -e "Blog:\t\thttp://www.everythingshouldbevirtual.com"
  echo -e "Blog:\t\thttp://mrlesmithjr.com"
  echo -e "Email:\t\tmrlesmithjr@gmail.com"
  echo -e "\nThis script requires one of the following arguments to be passed in order to perform a task."
  echo -e "\nUsage:\n\nvsphere_management.sh [arguments] \n"
  echo -e "\narguments:"
  echo -e "\tcleanup\t\t\t\t\tCleans up generated inventory, JSON data, and SSH key data"
  echo -e "\tdeploy_all\t\t\t\tDeploys whole environment"
  echo -e "\tdeployment_host_halt\t\t\tHalts Vagrant Deployment Host"
  echo -e "\tdeployment_host_spinup\t\t\tSpins up Vagrant Deployment Host and preps environment"
  echo -e "\tdeployment_host_teardown\t\tTears down Vagrant Deployment Host"
  echo -e "\tvsphere_ad_domain\t\t\tManages vSphere hosts AD membership"
  echo -e "\tvsphere_bootstrap_vms\t\t\tManages Bootstrap VMs"
  echo -e "\tvsphere_ddi_vms\t\t\t\tManages DDI VMs"
  echo -e "\tvsphere_deploy_rancher\t\t\tDeploys Rancher HA Environment (Uses Terraform)"
  echo -e "\tvsphere_deploy_rancher_stacks\t\tDeploys Rancher Stacks (PDNS, ELK, and Prometheus)"
  echo -e "\tvsphere_destroy_vms\t\t\tDestroys ALL Core VM Service VMs (USE WITH CAUTION)"
  echo -e "\tvsphere_disable_ssh\t\t\tDisables vSphere hosts SSH"
  echo -e "\tvsphere_dns\t\t\t\tManages vSphere hosts DNS settings"
  echo -e "\tvsphere_dnsdist_vms\t\t\tManages DNSDist VMs"
  echo -e "\tvsphere_enable_ssh\t\t\tEnables vSphere hosts SSH"
  echo -e "\tvsphere_generate_host_vars\t\tGenerates host_vars for Core VMs"
  echo -e "\tvsphere_lb_vms\t\t\t\tManages Load Balancer VMs"
  echo -e "\tvsphere_maintenance_mode\t\tManages vSphere hosts maintenance mode"
  echo -e "\tvsphere_management\t\t\tManages ALL vSphere host settings"
  echo -e "\tvsphere_network\t\t\t\tManages vSphere hosts network settings"
  echo -e "\tvsphere_pdns\t\t\t\tManages PowerDNS zones, records, and etc."
  echo -e "\tvsphere_post_deployment_reboot\t\tPerforms a post deployment reboot (Only if not already performed)"
  echo -e "\tvsphere_post_samba_deployment_reboot\tPerforms a post Samba deployment reboot (Only if not already performed)"
  echo -e "\tvsphere_samba_phase_1\t\t\tManages Samba VMs Stage 1 tasks (Does not install Samba)"
  echo -e "\tvsphere_samba_phase_2\t\t\tManages Samba VMs Stage 2 tasks (Installs Samba and sets up AD)"
  echo -e "\tvsphere_samba_sysvol_replication\tManages Samba VMs AD SysVol Replication"
  echo -e "\tvsphere_samba_vms\t\t\tManages Samba VMs (Does not perform Phase 1, 2, or SysVol Replication)"
  echo -e "\tvsphere_ssh_key_distribution\t\tDistributes SSH Keys between VMs (Currently only Samba VMs)"
  echo -e "\tvsphere_terraform_apply\t\t\tApplies the defined Terraform plan to reach the desired state of the configuration"
  echo -e "\tvsphere_terraform_deploy\t\tAll-in-one (init, plan, and apply)"
  echo -e "\tvsphere_terraform_destroy\t\tDestroys the Terraform infrastructure"
  echo -e "\tvsphere_terraform_init\t\t\tInitializes the Terraform working directory"
  echo -e "\tvsphere_terraform_inventory\t\tManages VMs Inventory Provisioned Using Terraform And Updates PDNS"
  echo -e "\tvsphere_terraform_plan\t\t\tShows the Terraform plan and shows what changes will be made"
  echo -e "\tvsphere_udpates\t\t\t\tUpdates vSphere Hosts (Must be in maintenance mode)"
  echo -e "\tvsphere_vcsa\t\t\t\tManages the vSphere VCSA Appliance"
  echo -e "\tvsphere_vcsa_ad\t\t\t\tManages VCSA Domain Membership"
  echo -e "\tvsphere_vcenter\t\t\t\tManages vCenter"
  echo -e "\tvsphere_vcenter_check\t\t\tChecks if vCenter exists or not"
  echo -e "\tvsphere_vms\t\t\t\tManages ALL VMs (Does not perform any post provisioning tasks)"
  echo -e "\tvsphere_vms_info\t\t\tCollects info for ALL VMs and updates inventory and etc."
  echo -e "\n\nAll arguments support additional Ansible command line arguments to be passed. However, only the following"
  echo -e "support passing a --limit most of the tasks run against the power_cli_host so the task will be"
  echo -e "skipped as no hosts will be found that match."
  echo -e "\nUsage:\n\nvsphere_management.sh [arguments] [--argument]\n"
  echo -e "\nExample:\n\tvsphere_management.sh vsphere_maintenance_mode --extra-vars '{\"vsphere_enable_software_iscsi\": True}'"
  echo -e "\nadditional arguments which support --limit to be passed:\n"
  echo -e "\t\tvsphere_post_deployment_reboot"
  echo -e "\t\tvsphere_post_samba_deployment_reboot"
  echo -e "\t\tvsphere_samba_phase_1"
  echo -e "\t\tvsphere_samba_phase_2"
  echo -e "\t\tvsphere_samba_sysvol_replication"
  echo -e "\t\tvsphere_ssh_key_distribution"
  echo -e "\nExample:\n\tvsphere_management.sh vsphere_post_deployment_reboot --limit node0.vagrant.local\n"
}

generate_inventory()
{
  _ANSIBLE_PLAYBOOK="generate_inventory.yml"
  _ansible_playbook_task "$@"
}

logging()
{
  if [ ! -d $LOG_DIR ]; then
    mkdir $LOG_DIR
  else [ -d $LOG_DIR ]
    echo "$LOG_DIR already exists"
  fi

  if [ -f $LOG_DIR/ansible.log ]; then
    mv $LOG_DIR/ansible.log $LOG_DIR/ansible.log.$TIMESTAMP
  fi
}

vsphere_ad_domain()
{
  _vsphere_management --tags vsphere_ad_domain "$@"
}

vsphere_bootstrap_vms()
{
  vsphere_destroy_vms_check
  _vsphere_management --tags vsphere_bootstrap_vms
  # _vsphere_management --tags vsphere_bootstrap_vms_info
}

vsphere_ddi_vms()
{
  vsphere_destroy_vms_check
  _vsphere_management --tags vsphere_ddi_vms
  # _vsphere_management --tags vsphere_ddi_vms_info
  _vsphere_ddi
}

vsphere_deploy_rancher()
{
  vsphere_terraform_deploy
  _ANSIBLE_PLAYBOOK="rancher.yml"
  _ansible_playbook_task "$@"
}

vsphere_deploy_rancher_stacks()
{
  _ANSIBLE_PLAYBOOK="rancher_stacks.yml"
  _ansible_playbook_task "$@"
}

vsphere_destroy_vms()
{
  clear
  echo -e "\nCAUTION:\tYou are about to DESTROY Core Services VMs!"
  echo -e "\t\tOnly VMs defined as deploy: false will be affected.....\n"
  read -p "You are about to DESTROY Core Services VMs!! Continue? (y/n) " -n 1 -r
  echo    # (optional) move to a new line
  if [[ ! $REPLY =~ ^[Yy]$ ]]
  then
    exit 1
  fi
  vsphere_destroy_vms_check
  # vsphere_ad_domain --extra-vars '{"vsphere_hosts_join_domain": False}'
  _vsphere_management --tags vsphere_destroy_vms --extra-vars '{"vsphere_destroy_vms": True}'
  vsphere_vms_info
}

vsphere_destroy_vms_check()
{
  _vsphere_management --tags vsphere_destroy_vms_check
}

vsphere_dns()
{
  _vsphere_management --tags vsphere_dns
}

vsphere_dnsdist_vms()
{
  vsphere_destroy_vms_check
  _vsphere_management --tags vsphere_dnsdist_vms
  # _vsphere_management --tags vsphere_dnsdist_vms_info
  _vsphere_dnsdist
}

vsphere_disable_ssh()
{
  _vsphere_management --tags vsphere_ssh --extra-vars '{"vsphere_hosts_enable_ssh": False}'
}

vsphere_enable_ssh()
{
  _vsphere_management --tags vsphere_ssh --extra-vars '{"vsphere_hosts_enable_ssh": True}'
}

vsphere_generate_host_vars()
{
  _vsphere_management --tags vsphere_generate_host_vars
}

vsphere_lb_vms()
{
  vsphere_destroy_vms_check
  _vsphere_management --tags vsphere_lb_vms
  # _vsphere_management --tags vsphere_lb_vms_info
  _vsphere_lb
}

vsphere_maintenance_mode()
{
  _vsphere_management --tags vsphere_maintenance_mode
}

vsphere_management()
{
  _vsphere_management --tags vsphere_management
}

vsphere_network()
{
  _vsphere_management --tags vsphere_network
}

vsphere_pdns()
{
  _ANSIBLE_PLAYBOOK="pdns.yml"
  _ansible_playbook_task "$@"
}

vsphere_post_deployment_reboot()
{
  _reboot --tags post_deployment_reboot "$@"
}

vsphere_post_samba_deployment_reboot()
{
  # We need to reboot the Samba hosts after building AD to ensure everything is up clean and working
  _reboot --tags post_samba_deployment_reboot "$@"
}

vsphere_samba_phase_1()
{
  # This phase does not install Samba or build domain...
  _vsphere_samba --tags samba_phase_1 "$@"
}

vsphere_samba_phase_2()
{
  # This phase will actually install Samba and build domain.
  # This needs to occur after reboot to ensure interfaces, dns, and everything
  # else in environment is up and functional.
  _vsphere_samba --tags samba_phase_2 "$@"
}

vsphere_samba_sysvol_replication()
{
  _vsphere_samba --tags samba_sysvol_replication "$@"
}

vsphere_samba_vms()
{
  vsphere_destroy_vms_check
  _vsphere_management --tags vsphere_samba_vms
  # _vsphere_management --tags vsphere_samba_vms_info
}

vsphere_ssh_key_distribution()
{
  _ANSIBLE_PLAYBOOK="ssh_key_distribution.yml"
  _ansible_playbook_task "$@"
}

vsphere_terraform_apply()
{
  _ANSIBLE_PLAYBOOK="terraform.yml"
  _ansible_playbook_task "$@" --extra-vars="terraform_apply=True" --tags terraform_apply
  vsphere_pdns
}

vsphere_terraform_deploy()
{
  vsphere_terraform_init
  vsphere_terraform_plan
  vsphere_terraform_apply
  vsphere_pdns
}

vsphere_terraform_destroy()
{
  _ANSIBLE_PLAYBOOK="terraform.yml"
  _ansible_playbook_task "$@" --extra-vars="terraform_destroy=True" --tags terraform_destroy
  vsphere_pdns
}

vsphere_terraform_init()
{
  _ANSIBLE_PLAYBOOK="terraform.yml"
  _ansible_playbook_task "$@" --tags terraform_init
}

vsphere_terraform_inventory()
{
  _ANSIBLE_PLAYBOOK="terraform.yml"
  _ansible_playbook_task "$@" --tags terraform_inventory
  vsphere_pdns
}

vsphere_terraform_plan()
{
  _ANSIBLE_PLAYBOOK="terraform.yml"
  _ansible_playbook_task "$@" --tags terraform_plan
}

vsphere_udpates()
{
  _vsphere_management --tags vsphere_udpates
}

vsphere_vcenter()
{
  _vsphere_management --tags vsphere_vcenter
}

vsphere_vcsa()
{
  vsphere_pdns
  _vsphere_management --tags vsphere_vcsa
}

vsphere_vcsa_ad()
{
  _ANSIBLE_PLAYBOOK="vcsa.yml"
  _ansible_playbook_task "$@"
}

vsphere_vcenter_check()
{
  _vsphere_management --tags vsphere_vcenter_check
}

vsphere_vms()
{
  # vsphere_vms_info
  _vsphere_management --tags vsphere_vms
}

vsphere_vms_info()
{
  vsphere_destroy_vms_check
  _vsphere_management --tags vsphere_vms_info
  # _vsphere_dnsdist --tags vsphere_dnsdist_vms_info
  # _vsphere_samba --tags vsphere_samba_vms_info
  # _vsphere_ddi --tags vsphere_ddi_vms_info
  # _vsphere_lb --tags vsphere_lb_vms_info
}
####
## End of vSphere functions ####
####


####
# Beginning of script execution
####
if [[ "$1" == "--help" ]]
then
  display_usage
  exit 0
elif [[ $# -eq 0 ]]
then
  echo -e "This script REQUIRES an argument to be passed to perform certain tasks!\n"
  echo -e "To view help:\n\n\tvsphere_management.sh --help\n"
  exit 0
else
  logging
  "$@"
  exit 0
fi
####
# End of script execution
####
