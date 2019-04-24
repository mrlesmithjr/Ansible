FROM fedora:24
ENV container=docker

RUN dnf -y install gmp-devel libffi-devel openssl-devel python-crypto \
    python-devel python-dnf python-pip python-setuptools python-virtualenv \
    redhat-rpm-config systemd && \
    dnf -y group install "C Development Tools and Libraries"

# Install systemd -- See https://hub.docker.com/_/centos/
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /lib/systemd/system/multi-user.target.wants/*;\
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;\
    rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN pip install enum34 ipaddress wheel && \
    pip install ansible ansible-lint

COPY .ansible-lint /

VOLUME ["/sys/fs/cgroup"]

CMD ["/usr/sbin/init"]
