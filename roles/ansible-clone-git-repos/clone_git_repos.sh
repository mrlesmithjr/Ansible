#!/bin/bash
ansible-playbook -i "localhost," -c local tasks/query_git_repos.yml --ask-sudo-pass
ansible-playbook -i "localhost," -c local tasks/clone_git_repos.yml
