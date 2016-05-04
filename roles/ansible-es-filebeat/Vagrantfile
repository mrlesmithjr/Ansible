# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "es" do |es|
    es.vm.box = "mrlesmithjr/trusty64"
    es.vm.hostname = "es"

    es.vm.network :private_network, ip: "192.168.202.202"
    es.vm.network :forwarded_port, guest: 5601, host: 5601
    es.vm.network :forwarded_port, guest: 9200, host: 9200

    es.vm.provider "virtualbox" do |vb|
     vb.memory = "2048"
    end
    es.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/playbook.yml --limit "es"'
  end
  config.vm.define "logstash" do |logstash|
    logstash.vm.box = "mrlesmithjr/trusty64"
    logstash.vm.hostname = "logstash"

    logstash.vm.network :private_network, ip: "192.168.202.203"

    logstash.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
    end
    logstash.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/playbook.yml --limit "logstash"'
  end
  config.vm.define "filebeat" do |filebeat|
    filebeat.vm.box = "mrlesmithjr/trusty64"
    filebeat.vm.hostname = "filebeat"

    filebeat.vm.network :private_network, ip: "192.168.202.201"

    filebeat.vm.provider "virtualbox" do |vb|
     vb.memory = "512"
    end
    filebeat.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/playbook.yml --limit "filebeat"'
  end
  config.vm.provision :shell, path: "provision.sh"
end
