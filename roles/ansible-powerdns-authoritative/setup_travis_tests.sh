#!/usr/bin/env bash

TAR_FILE="v1.6.1.tar.gz"

# Prompt for Ansible role name
read -p "Enter the Ansible role name: " input

# Update .travis.yml with Ansible role name
sed -i '' "s/replace_role/${input}/g" ".travis.yml"

# Update tests/test.yml with Ansible role name
sed -i '' "s/replace_role/${input}/g" "tests/test.yml"

# Cleanup
if [ -f $TAR_FILE ]; then
    rm $TAR_FILE
fi
