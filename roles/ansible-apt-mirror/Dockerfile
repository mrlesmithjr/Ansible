#Builds Ubuntu Apt-Mirror (APT REPO) image

FROM mrlesmithjr/ubuntu-ansible

MAINTAINER mrlesmithjr@gmail.com

#Install packages
RUN apt-get update && \
    apt-get install -y git

#Create Ansible Folder
RUN mkdir -p /opt/ansible-playbooks/roles

#Clone GitHub Repo
RUN git clone https://github.com/mrlesmithjr/ansible-apache2.git /opt/ansible-playbooks/roles/ansible-apache2 && \
    git clone https://github.com/mrlesmithjr/ansible-apt-mirror.git /opt/ansible-playbooks/roles/ansible-apt-mirror

#Copy Ansible playbooks
COPY playbook.yml /opt/ansible-playbooks/

#Run Ansible playbook
RUN ansible-playbook -i "localhost," -c local /opt/ansible-playbooks/playbook.yml

# Cleanup
RUN apt-get clean -y && \
    apt-get autoremove -y

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Expose ports
EXPOSE 80

ENTRYPOINT ["apache2ctl"]

CMD ["-D", "FOREGROUND"]
