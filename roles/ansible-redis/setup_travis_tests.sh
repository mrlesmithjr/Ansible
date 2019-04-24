#!/usr/bin/env bash
TRAVIS_TEST_VER="v1.6.2"

TAR_FILE="$TRAVIS_TEST_VER.tar.gz"

# Prompt for Ansible role name
read -r -p "Enter the Ansible role name: " input

# Update .travis.yml with Ansible role name
sed -i '' "s/replace_role/${input}/g" ".travis.yml"

# Update tests/test.yml with Ansible role name
sed -i '' "s/replace_role/${input}/g" "tests/test.yml"

# Cleanup
if [ -f $TAR_FILE ]; then
    rm $TAR_FILE
fi
