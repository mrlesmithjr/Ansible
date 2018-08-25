FROM debian:jessie
ENV container=docker

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev \
    libssl-dev python-dev python-minimal python-pip python-setuptools \
    python-virtualenv

RUN pip install --upgrade pip setuptools && \
    pip install enum34 ipaddress wheel && \
    pip install ansible ansible-lint

COPY .ansible-lint /
