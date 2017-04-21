FROM ubuntu:14.04

MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>

#Update apt-cache
RUN apt-get update

#Install pre-reqs for Ansible
RUN apt-get -y install git software-properties-common

#Adding Ansible ppa
RUN apt-add-repository ppa:ansible/ansible

#Update apt-cache
RUN apt-get update

#Install Ansible
RUN apt-get -y install ansible

#Create directory to copy Ansible files to
RUN mkdir -p /opt/ansible_tasks

#Copy Ansible playbooks
COPY playbook.yml requirements.yml /opt/ansible_tasks/

#Install Ansible role(s)
RUN ansible-galaxy install -r /opt/ansible_tasks/requirements.yml

#Run Ansible playbook
RUN ansible-playbook -i "localhost," -c local /opt/ansible_tasks/playbook.yml

#Clean-up packages
RUN apt-get -y clean && \
    apt-get -y autoremove

#Clean-up temp files
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Expose ports
EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
