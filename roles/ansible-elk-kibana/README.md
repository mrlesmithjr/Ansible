Role Name
=========

An [Ansible] role to install and configure Kibana for ELK Stack

Requirements
------------

None

Role Variables
--------------

```
---
# defaults file for ansible-elk-kibana

kibana_bin_dir: '/usr/share/kibana/bin'

# Defines if Kibana should be configured
kibana_config: true
kibana_dir: '/etc/kibana'
kibana_debian_repo_info:
  key: 'https://artifacts.elastic.co/GPG-KEY-elasticsearch'
  repo: 'deb https://artifacts.elastic.co/packages/{{ kibana_major_version }}/apt stable main'

# The default application to load.
kibana_default_app: 'discover'

# Defines the port of the kibana_elasticsearch_url host
kibana_elasticsearch_port: '9200'

# When this setting's value is true Kibana uses the hostname specified in the server.host
# setting. When the value of this setting is false, Kibana uses the hostname of the host
# that connects to this Kibana instance.
kibana_elasticsearch_preservehost: true

# Defines where to connect to elasticsearch for kibana
# default is localhost
# change to fit environment requirements
kibana_elasticsearch_url: 'localhost'

# Defines if babelcache permissions need to be fixed
# not always needed.
kibana_fix_babelcache_perms: false

# Defines Kibana host
# should remain as 0.0.0.0 unless other requirements are required
# research before changing
kibana_host: '0.0.0.0'

# Kibana uses an index in Elasticsearch to store saved searches, visualizations and
# dashboards. Kibana creates a new index if the index doesn't already exist.
kibana_index: '.kibana'

kibana_manage_plugins: true

# Define Kibana Major Release
kibana_major_version: '5.x'

# The maximum payload size in bytes for incoming server requests.
kibana_maxpayloadbytes: '1048576'

# Define Kibana Minor Release
kibana_minor_version: '5.2.2'

# Define Kibana plugins
kibana_plugins:
  - name: 'x-pack'
    state: "absent"

kibana_plugins_bin: '{{ kibana_bin_dir }}/kibana-plugin'
kibana_plugins_dir: '/usr/share/kibana/plugins/'

# Define Kibana listen port
kibana_port: '5601'

# Defines if legacy install should be removed
# This will cleanup previous non package installs that used this role previously
kibana_remove_legacy_install: true

# Kibana x-pack plugin settings
kibana_xpack_graph_enabled: true
kibana_xpack_monitoring_enabled: true
kibana_xpack_reporting_enabled: true

# https://github.com/elastic/kibana/issues/9369
kibana_xpack_security_enabled: false

kibana_xpack_watcher_enabled: true
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: kibana_hosts
  become: true
  vars:
  roles:
    - role: ansible-elk-kibana
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

[Kibana]: <https://www.elastic.co/products/kibana>
