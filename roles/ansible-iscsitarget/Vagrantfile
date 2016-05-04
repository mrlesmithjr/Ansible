# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
disk = './secondDisk.vdi'
Vagrant.configure(2) do |config|
  config.vm.define "iscsitarget" do |iscsitarget|
    iscsitarget.vm.box = "mrlesmithjr/trusty64"
    iscsitarget.vm.hostname = "iscsitarget"

    iscsitarget.vm.network :private_network, ip: "192.168.202.201"

    iscsitarget.vm.provider "virtualbox" do |vb|
      unless File.exist?(disk)
        vb.customize ['createhd', '--filename', disk, '--variant', 'Fixed', '--size', 20 * 1024]
      end
      vb.memory = "1024"
      vb.customize ['storageattach', :id,  '--storagectl', 'SATAController', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', disk]
    end
  end
  config.vm.provision :shell, path: "provision.sh", keep_color: "true"
end
