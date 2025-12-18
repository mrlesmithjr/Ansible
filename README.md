# Ansible Playbooks and Roles

A comprehensive collection of Ansible playbooks, roles, and automation examples for infrastructure management. This repository serves as a reference implementation and learning resource for Ansible automation.

## Contents

| Directory | Description |
|-----------|-------------|
| `playbooks/` | Ready-to-use playbooks for common infrastructure tasks |
| `roles/` | 200+ Ansible roles for various technologies |
| `Projects/` | Complete project examples with inventory and playbooks |
| `vsphere_playbooks/` | VMware vSphere automation playbooks |
| `vm_provisioning/` | Virtual machine provisioning templates |
| `inventory/` | Example inventory configurations |

## Quick Start

### Prerequisites

- Ansible 2.9+ (tested with Ansible Core 2.12+)
- Python 3.8+
- SSH access to target hosts

### Installation

1. Clone this repository:

```bash
git clone https://github.com/mrlesmithjr/Ansible.git
cd Ansible
```

2. Install all roles from Ansible Galaxy:

```bash
ansible-galaxy install -r requirements.yml -f -p ./roles --ignore-errors
```

3. Update your inventory file in `inventory/` or create your own.

4. Run a playbook:

```bash
ansible-playbook -i inventory/hosts playbooks/bootstrap.yml
```

## Available Playbooks

| Playbook | Description |
|----------|-------------|
| `bootstrap.yml` | Initial host configuration and setup |
| `site.yml` | Full site deployment |
| `elkstack_prod.yml` | ELK Stack deployment |
| `graylog.yml` | Graylog log management |
| `gitlab.yml` | GitLab installation |
| `sensu.yml` | Sensu monitoring |
| `squid.yml` | Squid proxy server |

## Roles

This repository references 200+ roles covering:

- **Monitoring**: Netdata, Prometheus, Grafana, Nagios, Sensu
- **Logging**: ELK Stack, Graylog, Fluentd
- **Databases**: MariaDB, PostgreSQL, MongoDB, Cassandra
- **Virtualization**: KVM, Docker, LXC
- **Networking**: FRRouting, OpenVSwitch, Netplan
- **Storage**: ZFS, LVM, GlusterFS, NFS
- **Security**: Fail2ban, UFW, Shorewall

See `requirements.yml` for the complete list.

## Updating Roles

To ensure all roles are current:

```bash
ansible-galaxy install -r requirements.yml -f -p ./roles --ignore-errors
```

## Notes

- All roles can be found in `roles/`
- The `roles.old/` folder contains archived roles for historical reference
- Individual roles are also available on [Ansible Galaxy](https://galaxy.ansible.com/mrlesmithjr)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
- [http://everythingshouldbevirtual.com](http://everythingshouldbevirtual.com)

<a href="https://www.buymeacoffee.com/mrlesmithjr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
