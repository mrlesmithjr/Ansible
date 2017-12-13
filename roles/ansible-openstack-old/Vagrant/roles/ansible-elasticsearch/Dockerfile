FROM ubuntu:14.04

MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>

#Update apt-cache
RUN apt-get update

#Install pre-reqs for Ansible
RUN apt-get -y install curl git software-properties-common

#Adding Ansible ppa
RUN apt-add-repository ppa:ansible/ansible

#Update apt-cache
RUN apt-get update

#Install Ansible
RUN apt-get -y install ansible

# Install gosu
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN arch="$(dpkg --print-architecture)" \
	&& set -x \
	&& curl -o /usr/local/bin/gosu -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \
	&& curl -o /usr/local/bin/gosu.asc -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

# Create Ansible Folder
RUN mkdir -p /opt/ansible_tasks

# Copy Ansible playbooks
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

ENV PATH /usr/share/elasticsearch/bin:$PATH

# Mountable data directories.
VOLUME /usr/share/elasticsearch/data

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

# Expose ports
EXPOSE 9200 9300

CMD ["elasticsearch"]
