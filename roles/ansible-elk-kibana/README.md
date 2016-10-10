Role Name
=========

Installs and configures Kibana for ELK Stack https://www.elastic.co/products/kibana

Requirements
------------

Requires Elasticsearch 2.2+

If setting up a scaled out HA ELK deployment ensure that your kibana node is either running elasticsearch or change the variable for kibana_elasticsearch_url in defaults/main.yml ...Another option (recommended) is to define this variable in your group_vars/group for your ELK group for consistency.

Role Variables
--------------

````
---
# defaults file for ansible-elk-kibana
config_kibana: true  #Defines if Kibana should be configured
kibana_dir: '/opt/kibana'
kibana_debian_repo_info:
  key: 'https://packages.elastic.co/GPG-KEY-elasticsearch'
  repo: 'deb http://packages.elastic.co/kibana/{{ kibana_major_version }}/debian stable main'
kibana_docker_elasticsearch_container_name: elasticsearch  #defines the Docker container name to link to for elasticsearch
kibana_docker_install: false  #defines if Kibana is being installed as a Docker container
kibana_elasticsearch_url: localhost  #defines where to connect to elasticsearch for kibana...default is localhost...change to fit environment requirements...define here or in group_vars/group
kibana_fix_babelcache_perms: false   #defines if babelcache permissions need to be fixed...not always needed.
kibana_host: 0.0.0.0  #defines Kibana host...should remain as 0.0.0.0 unless other requirements are required...research before changing
kibana_port: 5601
kibana_major_version: '4.6'
kibana_version: '4.6.1'
remove_legacy_kibana_install: true

## Below are legacy settings prior to package installer method...will be removed..
# kibana_dl_dir: /opt
# kibana_dl_file: "kibana-{{ kibana_version }}-linux-x86_64"
# kibana_dl_url: "https://download.elastic.co/kibana/kibana"
# kibana_index: .kibana
# kibana_log: /var/log/kibana.log
# kibana_log_rotate_count: 5
# kibana_log_rotate_interval: daily
````

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mrlesmithjr.elk-kibana }

Docker Info
-----------

In order to run as a Docker container you will need to link to an elasticsearch container by default called elasticsearch.
Ex.
````
docker run -d --name elasticsearch -p 9200:9200 mrlesmithjr/elasticsearch
docker run -d --name kibana -p 5601:5601 --link elasticsearch mrlesmithjr/elk-kibana
````
You can change the name of the elasticsearch url after the container is spun up if desired. By executing the following:
````
docker exec -it kibana-test ansible-playbook -i "localhost," -c local /opt/ansible-playbooks/playbook.yml --extra-vars="kibana_docker_elasticsearch_container_name=10.0.101.60" && docker restart kibana-test
````
The above will change the configuration for Kibana and point to the new location after the container is restarted.

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
