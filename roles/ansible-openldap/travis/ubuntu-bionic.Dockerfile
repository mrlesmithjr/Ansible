FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*

RUN apt-add-repository -y ppa:ansible/ansible && \
    apt-get update && apt-get install -y \
        init \
        git \
        ansible \
    && rm -rf /var/lib/apt/lists/*

RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

ENTRYPOINT ["/sbin/init"]
