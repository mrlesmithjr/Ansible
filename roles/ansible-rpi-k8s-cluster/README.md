<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**  _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [ansible-k8s](#ansible-k8s)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [Vagrant](#vagrant)
    -   [Additional Info](#additional-info)
        -   [Reset `K8s` cluster](#reset-k8s-cluster)
        -   [Get a list of pods and information on them](#get-a-list-of-pods-and-information-on-them)
        -   [Kubernetes-Dashboard](#kubernetes-dashboard)
        -   [Find the port to connect to](#find-the-port-to-connect-to)
        -   [Inspect the service](#inspect-the-service)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-k8s

An [Ansible](https://www.ansible.com) role to deploy a
[Kubernetes](https://kubernetes.io) - K8s Cluster

-   [Weave-Net](https://www.weave.works/docs/net/latest/kube-addon/) is used for
    the network overlay currently

## Requirements

Install additional required [Ansible](https://www.ansible.com) roles:

```bash
sudo ansible-galaxy install -r requirements.yml
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

None

## Example Playbook

```yaml
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

## Vagrant

-   Requirements
    -   [Ansible](https://www.ansible.com)
    -   [Vagrant](https://www.vagrantup.com/)
    -   [Virtualbox](https://www.virtualbox.org/)

Included in the `Vagrant` folder is a testing environment with `3` nodes.

-   `node0` - K8s Cluster Master (`192.168.250.10`)
-   `node1` - K8s Cluster Member (`192.168.250.11`)
-   `node2` - K8s Cluster Member (`192.168.250.12`)

You can easily spin this up for learning purposes:

```bash
cd Vagrant/
vagrant up
```

Once the environment spins up you will see the following:

```bash
TASK [ansible-k8s : cluster_summary | Displaying Cluster Nodes] ****************
skipping: [node1]
ok: [node0] => {
    "_k8s_cluster_nodes['stdout_lines']": [
        "NAME      STATUS     AGE       VERSION",
        "node0     Ready      1m        v1.6.1",
        "node1     NotReady   4s        v1.6.1",
        "node2     NotReady   6s        v1.6.1"
    ],
    "changed": false
}
skipping: [node2]
```

Do not worry about the above as the additional nodes did not completely join
the cluster before the provisioning completed. You can quickly validate that
the additional nodes are up and `Ready` by running:

```bash
ansible-playbook -i hosts playbook.yml --tags k8s_cluster_nodes
```

The above `NotReady` should no longer be an issue as we now wait for all nodes
in the cluster to become `Ready`. However, there may be an instance where this
may not work as expected.

```bash
TASK [ansible-k8s : cluster_summary | Displaying Cluster Nodes] ******************************************************************************************************************
skipping: [node1]
skipping: [node2]
ok: [node0] => {
    "_k8s_cluster_nodes['stdout_lines']": [
        "NAME      STATUS    ROLES     AGE       VERSION",
        "node0     Ready     master    3m        v1.9.0",
        "node1     Ready     <none>    2m        v1.9.0",
        "node2     Ready     <none>    2m        v1.9.0"
    ]
}
```

Once the cluster is up `ssh` to `node0` and begin playing:

```bash
vagrant ssh node0
```

When you are all done using the environment easily tear it down:

```bash
./cleanup.sh

==> node2: Forcing shutdown of VM...
==> node2: Destroying VM and associated drives...
==> node1: Forcing shutdown of VM...
==> node1: Destroying VM and associated drives...
==> node0: Forcing shutdown of VM...
==> node0: Destroying VM and associated drives...
```

## Additional Info

### Reset `K8s` cluster

```bash
ansible-playbook -i hosts playbook.yml --tags k8s_reset -e "k8s_reset_cluster=true"
```

### Get a list of pods and information on them

```bash
ansible-playbook -i hosts playbook.yml --tags k8s_pods
```

```json
{
        "containers": [
            {
                "hostIP": "192.168.250.10",
                "image": "gcr.io/google_containers/etcd-amd64:3.1.10",
                "name": "etcd",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "192.168.250.10",
                "resources": {}
            },
            {
                "hostIP": "192.168.250.10",
                "image": "gcr.io/google_containers/kube-apiserver-amd64:v1.9.0",
                "name": "kube-apiserver",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "192.168.250.10",
                "resources": {
                    "requests": {
                        "cpu": "250m"
                    }
                }
            },
            {
                "hostIP": "192.168.250.10",
                "image": "gcr.io/google_containers/kube-controller-manager-amd64:v1.9.0",
                "name": "kube-controller-manager",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "192.168.250.10",
                "resources": {
                    "requests": {
                        "cpu": "200m"
                    }
                }
            },
            {
                "hostIP": "192.168.250.10",
                "image": "gcr.io/google_containers/k8s-dns-kube-dns-amd64:1.14.7",
                "name": "kubedns",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "10.32.0.2",
                "resources": {
                    "limits": {
                        "memory": "170Mi"
                    },
                    "requests": {
                        "cpu": "100m",
                        "memory": "70Mi"
                    }
                }
            },
            {
                "hostIP": "192.168.250.12",
                "image": "gcr.io/google_containers/kube-proxy-amd64:v1.9.0",
                "name": "kube-proxy",
                "nodeName": "node2",
                "phase": "Running",
                "podIP": "192.168.250.12",
                "resources": {}
            },
            {
                "hostIP": "192.168.250.11",
                "image": "gcr.io/google_containers/kube-proxy-amd64:v1.9.0",
                "name": "kube-proxy",
                "nodeName": "node1",
                "phase": "Running",
                "podIP": "192.168.250.11",
                "resources": {}
            },
            {
                "hostIP": "192.168.250.10",
                "image": "gcr.io/google_containers/kube-proxy-amd64:v1.9.0",
                "name": "kube-proxy",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "192.168.250.10",
                "resources": {}
            },
            {
                "hostIP": "192.168.250.10",
                "image": "gcr.io/google_containers/kube-scheduler-amd64:v1.9.0",
                "name": "kube-scheduler",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "192.168.250.10",
                "resources": {
                    "requests": {
                        "cpu": "100m"
                    }
                }
            },
            {
                "hostIP": "192.168.250.12",
                "image": "k8s.gcr.io/kubernetes-dashboard-amd64:v1.8.1",
                "name": "kubernetes-dashboard",
                "nodeName": "node2",
                "phase": "Running",
                "podIP": "10.36.0.1",
                "resources": {}
            },
            {
                "hostIP": "192.168.250.10",
                "image": "weaveworks/weave-kube:2.1.3",
                "name": "weave",
                "nodeName": "node0",
                "phase": "Running",
                "podIP": "192.168.250.10",
                "resources": {
                    "requests": {
                        "cpu": "10m"
                    }
                }
            },
            {
                "hostIP": "192.168.250.11",
                "image": "weaveworks/weave-kube:2.1.3",
                "name": "weave",
                "nodeName": "node1",
                "phase": "Running",
                "podIP": "192.168.250.11",
                "resources": {
                    "requests": {
                        "cpu": "10m"
                    }
                }
            },
            {
                "hostIP": "192.168.250.12",
                "image": "weaveworks/weave-kube:2.1.3",
                "name": "weave",
                "nodeName": "node2",
                "phase": "Running",
                "podIP": "192.168.250.12",
                "resources": {
                    "requests": {
                        "cpu": "10m"
                    }
                }
            }
        ]
    }
}
```

### [Kubernetes-Dashboard](https://github.com/kubernetes/dashboard)

The [Kubernetes-Dashboard](https://github.com/kubernetes/dashboard) is installed
during the install and available for usage. In order to find out where/how to
connect to the dashboard seems to involve the following.

### Find the port to connect to

```bash
vagrant ssh node0

kubectl get services --all-namespaces
...
NAMESPACE     NAME                   TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)         AGE
default       kubernetes             ClusterIP   10.96.0.1     <none>        443/TCP         6m
kube-system   kube-dns               ClusterIP   10.96.0.10    <none>        53/UDP,53/TCP   6m
kube-system   kubernetes-dashboard   ClusterIP   10.97.72.90   <none>        443/TCP         4m
```

We can see the port is `80:32285` from above.

> NOTE: The above only works for later versions of the dashboard. Reference the
> [Accessing-Dashboard#nodeport](https://github.com/kubernetes/dashboard/wiki/Accessing-Dashboard---1.7.X-and-above#nodeport) for more info on doing this as of later versions.
>
> INFO: This way of accessing Dashboard is only recommended for development environments in a single node setup.

### Inspect the service

```bash
kubectl describe services kubernetes-dashboard --namespace=kube-system
...
Name:              kubernetes-dashboard
Namespace:         kube-system
Labels:            k8s-app=kubernetes-dashboard
Annotations:       kubectl.kubernetes.io/last-applied-configuration={"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"k8s-app":"kubernetes-dashboard"},"name":"kubernetes-dashboard","namespace":...
Selector:          k8s-app=kubernetes-dashboard
Type:              ClusterIP
IP:                10.97.72.90
Port:              <unset>  443/TCP
TargetPort:        8443/TCP
Endpoints:         10.36.0.1:8443
Session Affinity:  None
Events:            <none>
```

You can then connect to [Dashboard](https://192.168.250.10:32285) for this example.

> NOTE: In order to login using a token reference the following [link](https://github.com/kubernetes/dashboard/wiki/Access-control#bearer-token)
>
> NOTE: To login with admin privileges reference the following [link](https://github.com/kubernetes/dashboard/wiki/Access-control#admin-privileges)

The `32285` port changes every new deployment of the dashboard so you will
need to discover what that new port is. Or you can run the following to report
on the usable link:

```bash
ansible-playbook -i hosts playbook.yml --tags k8s_get_dashboard
```

Which will result in the following after the play finishes:

```bash
TASK [ansible-k8s : reports | Dashboard] ***************************************
skipping: [node1]
skipping: [node2]
ok: [node0] => {
    "msg": "Kubernetes Dashboard Can be reached at: http://192.168.250.10:30467\n"
}
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
