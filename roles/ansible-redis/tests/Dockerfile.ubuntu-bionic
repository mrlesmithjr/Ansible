FROM ubuntu:bionic

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev \
    libssl-dev python-dev python-minimal python-pip python-setuptools \
    python-virtualenv systemd

RUN pip install ansible
