#FROM mrlesmithjr/ansible:ubuntu-12.04
#FROM mrlesmithjr/ansible:ubuntu-14.04
FROM mrlesmithjr/ubuntu-ansible

MAINTAINER mrlesmithjr@gmail.com

#Installs git
RUN apt-get update && apt-get install -y git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

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
RUN mkdir -p /opt/ansible-playbooks/roles

# Clone GitHub Repo
RUN git clone --depth=50 --branch=2.1 https://github.com/mrlesmithjr/ansible-logstash.git /opt/ansible-playbooks/roles/ansible-logstash \
   && git clone --depth=50 --branch=2.1 https://github.com/mrlesmithjr/ansible-elk-pre-processor.git /opt/ansible-playbooks/roles/ansible-elk-pre-processor

# Copy Ansible playbooks
COPY playbook.yml /opt/ansible-playbooks/

# Run Ansible playbook to install logstash
RUN ansible-playbook -i "localhost," -c local /opt/ansible-playbooks/playbook.yml

# Clean up APT
RUN apt-get clean

ENV PATH /opt/logstash/bin:$PATH

COPY docker-entrypoint.sh /

EXPOSE 514 514/udp 1514 1515 1517 3515 3525 10514

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["logstash", "agent", "-f", "/etc/logstash/conf.d/"]
