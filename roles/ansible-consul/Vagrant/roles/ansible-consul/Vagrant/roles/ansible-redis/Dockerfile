FROM debian:jessie

MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>

#Copy Ansible tasks
COPY ansible_tasks /opt/ansible_tasks

#Update apt-cache, install Ansible and install Ansible roles
RUN apt-get update && \
    apt-get -y install build-essential git libssl-dev libffi-dev python-dev python-setuptools && \
    easy_install pip && \
    pip install --upgrade setuptools && \
    pip install ansible && \
    ansible-galaxy install -r /opt/ansible_tasks/requirements.yml && \
    ansible-playbook -i "localhost," -c local /opt/ansible_tasks/playbook.yml && \
    apt-get -y purge build-essential libssl-dev libffi-dev python-dev python-setuptools && \
    apt-get -y clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Expose ports
EXPOSE 6379

ENTRYPOINT  ["/usr/bin/redis-server"]
