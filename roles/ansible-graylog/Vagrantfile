# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "graylog" do |graylog|
    graylog.vm.box = "mrlesmithjr/xenial64"
    graylog.vm.hostname = "graylog"

    graylog.vm.network :private_network, ip: "192.168.202.201"
    graylog.vm.network "forwarded_port", guest: 9000, host: 9000
    graylog.vm.network "forwarded_port", guest: 9200, host: 9200
    graylog.vm.network "forwarded_port", guest: 12900, host: 12900
    graylog.vm.network "forwarded_port", guest: 12201, host: 12201, protocol: "tcp"
    graylog.vm.network "forwarded_port", guest: 12201, host: 12201, protocol: "udp"

    graylog.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = "2"
    end
  end
  config.vm.provision :shell, path: "provision.sh", keep_color: "true"
end
