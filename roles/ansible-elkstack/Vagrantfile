# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "elk-broker" do |elkbroker|
    elkbroker.vm.box = "mrlesmithjr/trusty64"
    elkbroker.vm.hostname = "elk-broker"

    elkbroker.vm.network :private_network, ip: "192.168.202.200"
    elkbroker.vm.network :forwarded_port, guest: 5601, host: 5601
    elkbroker.vm.network :forwarded_port, guest: 6379, host: 6379

    elkbroker.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
    elkbroker.vm.provision :shell, path: "provision.sh", keep_color: "true"
    elkbroker.vm.provision :shell, inline: 'ansible-galaxy install -r /vagrant/requirements.yml -f'
    elkbroker.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack-core.yml --limit "elk-broker-nodes"'
    elkbroker.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack.yml --limit "elk-broker-nodes"'
  end
  config.vm.define "elk-es" do |elkes|
    elkes.vm.box = "mrlesmithjr/trusty64"
    elkes.vm.hostname = "elk-es"

    elkes.vm.network :private_network, ip: "192.168.202.201"
    elkes.vm.network :forwarded_port, guest: 9200, host: 9200

    elkes.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
    elkes.vm.provision :shell, path: "provision.sh", keep_color: "true"
    elkes.vm.provision :shell, inline: 'ansible-galaxy install -r /vagrant/requirements.yml -f'
    elkes.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack-core.yml --limit "elk-es-nodes"'
    elkes.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack.yml --limit "elk-es-nodes"'
  end
  config.vm.define "elk-pre-processor" do |elkpreprocessor|
    elkpreprocessor.vm.box = "mrlesmithjr/trusty64"
    elkpreprocessor.vm.hostname = "elk-pre-processor"

    elkpreprocessor.vm.network :private_network, ip: "192.168.202.202"
    elkpreprocessor.vm.network :forwarded_port, guest: 3515, host: 3515
    elkpreprocessor.vm.network :forwarded_port, guest: 10514, host: 10514


    elkpreprocessor.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
    elkpreprocessor.vm.provision :shell, path: "provision.sh", keep_color: "true"
    elkpreprocessor.vm.provision :shell, inline: 'ansible-galaxy install -r /vagrant/requirements.yml -f'
    elkpreprocessor.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack-core.yml --limit "elk-pre-processor-nodes"'
    elkpreprocessor.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack.yml --limit "elk-pre-processor-nodes"'
  end
  config.vm.define "elk-processor" do |elkprocessor|
    elkprocessor.vm.box = "mrlesmithjr/trusty64"
    elkprocessor.vm.hostname = "elk-processor"

    elkprocessor.vm.network :private_network, ip: "192.168.202.203"

    elkprocessor.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
    elkprocessor.vm.provision :shell, path: "provision.sh", keep_color: "true"
    elkprocessor.vm.provision :shell, inline: 'ansible-galaxy install -r /vagrant/requirements.yml -f'
    elkprocessor.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack-core.yml --limit "elk-processor-nodes"'
    elkprocessor.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/elkstack.yml --limit "elk-processor-nodes"'
  end
end
