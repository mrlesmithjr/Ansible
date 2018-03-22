<!-- START doctoc generated TOC please keep comment here to allow auto update -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [ansible-ipset](#ansible-ipset)
    -   [Related Info](#related-info)
    -   [Using Block Lists](#using-block-lists)
        -   [Current supported block lists:](#current-supported-block-lists)
        -   [Enabling supported block lists:](#enabling-supported-block-lists)
    -   [IP Sets Rules Management](#ip-sets-rules-management)
    -   [Requirements](#requirements)
    -   [Role Variables](#role-variables)
    -   [Dependencies](#dependencies)
    -   [Example Playbook](#example-playbook)
    -   [Examples](#examples)
        -   [Example ipset list](#example-ipset-list)
        -   [Example iptables list](#example-iptables-list)
    -   [License](#license)
    -   [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# ansible-ipset

An [Ansible](https://www.ansible.com) role to install/configure [ipset](http://ipset.netfilter.org/)

> NOTE: This role will also manage [IPTables](http://netfilter.org/projects/iptables/index.html)
> rules as part of configuring ipset. Any existing IPTables rules **WILL** be
> removed.

## Related Info

We have also put together a [blog post](http://everythingshouldbevirtual.com/automation/ansible-ip-sets-and-dshield-block-list/)
which is related to this role.

## Using Block Lists

We have also included the ability to use various different IP block lists to
generate `ipset` rules and `iptables` rules. These can be easily implemented to
block traffic inbound, outbound, or both inboud/outbound.

### Current supported block lists:

-   [DShield](https://www.dshield.org/)
-   [FireHOL](http://iplists.firehol.org/)
-   [Spamhaus DROP](https://www.spamhaus.org/faq/section/DROP%20FAQ)
    -   DROP
    -   EDROP

### Enabling supported block lists:

In order to enable the supported block lists you must set the following variables
to `true` as their defaults are `false`:

```yaml
# Defines if DShield top 20 block lists should be defined from https://www.dshield.org/block.txt
ipset_enable_dshield_block_list: false

# Defines if FireHOL ip lists should be defined from http://iplists.firehol.org/
ipset_enable_firehol_block_list: false

# Defines if Spamhaus block lists should be defined from https://www.spamhaus.org/drop/
ipset_enable_spamhaus_block_list: false
```

## IP Sets Rules Management

We have added functionality to check if existing rules exist by the same name. If
they do exist, a temporary rule set is created which will then be populated. Once
the population has completed the existing rule set will be swapped with the
temporary rule set, and then the temporary rule set will be destroyed. This will
ensure that there is not a time period in which all rules are flushed and then
repopulated therefore leaving a short period of time of being out of scope.

## Requirements

The following requirements **MUST** be met on the Ansible host that is executing
this role:

-   [python-netaddr](https://pypi.python.org/pypi/netaddr)

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

## Example Playbook

[playbook.yml](./playbook.yml)

## Examples

### Example ipset list

Displaying the list of ipset rule names:

```bash
vagrant@node0:~$ sudo ipset list -n
safe_input
dshield_block_list
firehol_block_list
spamhaus_drop_block_list
spamhaus_edrop_block_list
```

Displaying the complete list of ipset rules:

> NOTE: This list is just an example and does not show all of the ipset rules
> shown above.

```bash
vagrant@node0:~$ sudo ipset list
Name: safe_input
Type: hash:net
Revision: 6
Header: family inet hashsize 1024 maxelem 1000111222
Size in memory: 448
References: 1
Members:
10.0.0.0/8

Name: dshield_block_list
Type: hash:net
Revision: 6
Header: family inet hashsize 1024 maxelem 1000111222
Size in memory: 1664
References: 4
Members:
85.93.20.0/24
5.188.203.0/24
104.236.178.0/24
77.72.85.0/24
77.72.82.0/24
181.214.87.0/24
5.188.11.0/24
46.29.162.0/24
141.212.122.0/24
80.82.77.0/24
180.97.106.0/24
185.35.62.0/24
216.158.238.0/24
5.188.86.0/24
191.101.167.0/24
93.174.93.0/24
109.248.9.0/24
5.188.10.0/24
80.82.70.0/24
196.52.43.0/24
```

### Example iptables list

```bash
vagrant@node0:~$ sudo iptables -L -v -n
Chain INPUT (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0
  824  666K ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set dshield_block_list src
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set firehol_block_list src
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set spamhaus_drop_block_list src
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set spamhaus_edrop_block_list src
    1    44 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            multiport dports 22,2202,2222 ctstate NEW match-set safe_input src
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 ACCEPT     all  --  *      lo      0.0.0.0/0            0.0.0.0/0
  733 61601 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate ESTABLISHED
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set dshield_block_list dst
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set firehol_block_list dst
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set spamhaus_drop_block_list dst
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0            match-set spamhaus_edrop_block_list dst
    0     0 ACCEPT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate NEW
   12   808 ACCEPT     udp  --  *      *       0.0.0.0/0            0.0.0.0/0            multiport dports 53,123 ctstate NEW
    0     0 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            multiport dports 22,80,443 ctstate NEW
    0     0 LOGGING-DROPPED  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain LOGGING-DROPPED (10 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            limit: avg 2/min burst 5 LOG flags 0 level 4 prefix "IPTables-Dropped: "
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   <mailto:mrlesmithjr@gmail.com>
