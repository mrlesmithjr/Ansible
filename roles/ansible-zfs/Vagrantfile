# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "zfs" do |zfs|
#    zfs.vm.box = "mrlesmithjr/jessie64"
    zfs.vm.box = "mrlesmithjr/trusty64"
    zfs.vm.hostname = "zfs"

    zfs.vm.network :private_network, ip: "192.168.202.201"

    zfs.vm.provider "virtualbox" do |vb|
      unless File.exist?('./secondDisk.vdi')
        vb.customize ['createhd', '--filename', './secondDisk.vdi', '--variant', 'Fixed', '--size', 10 * 1024]
      end
      unless File.exist?('./thirdDisk.vdi')
        vb.customize ['createhd', '--filename', './thirdDisk.vdi', '--variant', 'Fixed', '--size', 10 * 1024]
      end
      vb.memory = "1024"
      vb.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './secondDisk.vdi']
      vb.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', './thirdDisk.vdi']
    end
    zfs.vm.provision :shell, path: "provision.sh", keep_color: "true"
  end
  config.vm.define "client" do |client|
#    client.vm.box = "mrlesmithjr/jessie64"
    client.vm.box = "mrlesmithjr/trusty64"
    client.vm.hostname = "client"

    client.vm.network :private_network, ip: "192.168.202.202"
    client.vm.provision :shell, inline: "sudo apt-get update && sudo apt-get -y install python-dev python-pip"
    client.vm.provision :shell, inline: "sudo pip install ansible"
    client.vm.provision :shell, inline: 'ansible-playbook -i "localhost," -c local /vagrant/client.yml'
  end
end
