# Build Inventories
#####Adds ability to create host_vars, group_vars and add variables to each using vars files
#####Adds ability to create host inventory and update host_vars ansible_ssh_host to current IP address discovered from vCenter
## Requirements
None
## Variables Examples
vars/host_vars
````
---
hosts:
  - name: ans-test-1
    create: true
    groups:
      - ubuntu-servers
      - ansible-test-servers
    vars:
      - name: build_from_template
        value: false
        set: true
      - name: cpu_hotadd
        value: false
        set: true
      - name: cpucount
        value: 1
        set: true
      - name: datastore
        value: 'Tier-3 (NAS01)'
        set: true
      - name: disk1
        value: 36
        set: true
      - name: mem_hotadd
        value: false
        set: true
      - name: memory
        value: 512
        set: true
      - name: multi
        value: false
        set: true
      - name: network
        value: 'vSS-Green-Servers-VLA
````
## Dependencies
None
## Example Playbook
````
````
## License
GNU General Public License Version 2

## Author Information
Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
