#! /usr/bin/env bash

# Install and force overwrite of roles to test with
# These roles are also added to the .gitignore file in order to not include the
# roles in this repo. This will ensure that the latest roles are always pulled
# down.
ansible-galaxy install -r requirements.yml -p ./roles -f
