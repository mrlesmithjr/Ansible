#Builds Ubuntu MySQL image

FROM mrlesmithjr/ubuntu-ansible:14.04

MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>

#Install packages
RUN apt-get update && \
    apt-get install -y git

COPY playbook.yml requirements.yml /opt/

RUN ansible-galaxy install -r /opt/requirements.yml -f
RUN ansible-playbook -i "localhost," -c local /opt/playbook.yml

RUN apt-get clean -y && \
    apt-get autoremove -y

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Expose ports
EXPOSE 3306

CMD ["/usr/bin/mysqld_safe"]
