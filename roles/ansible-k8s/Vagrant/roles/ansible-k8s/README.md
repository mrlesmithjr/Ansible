Role Name
=========

An [Ansible] role to deploy a [Kubernetes] - K8s Cluster

Requirements
------------

Install additional required [Ansible] roles:

```
sudo ansible-galaxy install -r requirements.yml
```

Role Variables
--------------

```
---
# defaults file for ansible-k8s
#
k8s_admin_config: '/etc/kubernetes/admin.conf'

# Define Ansible group which defines the K8s Cluster
k8s_advertise_address_int: 'enp0s8'

k8s_advertise_bind_port: '6443'

k8s_cluster_group: 'k8s'

k8s_dashboard: 'https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/kubernetes-dashboard.yaml'

k8s_debian_packages:
  - 'kubelet'
  - 'kubeadm'
  - 'kubectl'
  - 'kubernetes-cni'

k8s_debian_repo_info:
  key: '{{ k8s_package_url }}/apt/doc/apt-key.gpg'
  repo: 'deb http://apt.kubernetes.io/ kubernetes-{{ ansible_distribution_release|lower }} main'

k8s_package_url: 'https://packages.cloud.google.com'

k8s_pod_network_config: 'https://git.io/weave-kube-1.6'

k8s_reset_cluster: false

k8s_token_file: '/etc/kubernetes/.k8s_token'
```

Dependencies
------------


Example Playbook
----------------

```
---
- hosts: k8s
  # become: true
  vars:
    # Define Docker version to install
    docker_version: '1.12.6'
    # Defines if all nodes in play should be added to each hosts /etc/hosts
    etc_hosts_add_all_hosts: true
    etc_hosts_pri_dns_name: '{{ pri_domain_name }}'
    # Defines if node has static IP.
    etc_hosts_static_ip: true
    # Defines if ansible_default_ipv4.address is used for defining hosts
    etc_hosts_use_default_ip_address: false
    # Defines if ansible_ssh_host is used for defining hosts
    etc_hosts_use_ansible_ssh_host: true
    pri_domain_name: 'test.vagrant.local'
  roles:
    - role: ansible-etc-hosts
    - role: ansible-change-hostname
    - role: ansible-docker
    - role: ansible-k8s
  tasks:
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[Kubernetes]: <https://kubernetes.io>
