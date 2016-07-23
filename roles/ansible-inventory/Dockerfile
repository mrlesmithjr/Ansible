FROM ubuntu:14.04

MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>

COPY ansible_tasks /opt/ansible_tasks

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install git software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get -y install ansible && \
    ansible-galaxy install -r /opt/ansible_tasks/requirements.yml && \
    ansible-playbook -i "localhost," -c local /opt/ansible_tasks/playbook.yml && \
    apt-get -y purge software-properties-common && \
    apt-get -y clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Expose port(s)
EXPOSE 3306

#Process start-up
CMD ["/usr/bin/mysqld_safe"]
