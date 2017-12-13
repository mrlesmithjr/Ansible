#! /usr/bin/env bash

set -e
# set -x

red="\033[0;31m"
reset="\033[0m"

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

UNIT_TEST_LOGFILE="logs/unit-test.log.$timestamp"

# Check provisioning settings and fail if not set to provision
for i in $(cat nodes.yml| grep 'provision: '| awk '{print $2}'); do
  if ! $i; then
    printf "You must set ${red}'provision: true' ${reset}in nodes.yml\n"
    printf "in order to do execute a proper unit test."
    exit
  fi
done

if [ ! -d logs ]; then
  mkdir logs 2>&1 | tee $UNIT_TEST_LOGFILE
fi

# Check ansible version
ansible --version 2>&1 | tee -a $UNIT_TEST_LOGFILE

ansible-lint playbook.yml 2>&1 | tee -a $UNIT_TEST_LOGFILE

# Basic Ansible syntax check
ansible-playbook playbook.yml --syntax-check 2>&1 | tee -a $UNIT_TEST_LOGFILE

# Spin up environment
vagrant up 2>&1 | tee -a $UNIT_TEST_LOGFILE

# Execute Ansible playbook again and check for idempotence
ansible-playbook -i hosts playbook.yml \
| (grep -q 'changed=0.*failed=0' && (echo 'Idempotence test: pass' && exit 0) \
|| (echo 'Idempotence test: fail' && exit 1)) 2>&1 | tee -a $UNIT_TEST_LOGFILE

# Clean up Vagrant environment
./cleanup.sh 2>&1 | tee -a $UNIT_TEST_LOGFILE
