# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  #Define the number of nodes to spin up
  N = 5

  #Iterate over nodes
  (1..N).each do |node_id|
    nid = (node_id - 1)

    config.vm.define "node#{nid}" do |node|
      node.vm.box = "mrlesmithjr/trusty64"
      node.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
      end
      node.vm.hostname = "node#{nid}"
      node.vm.network :private_network, ip: "192.168.202.#{200 + nid}"
      node.vm.network :forwarded_port, guest: "5050", host: "505#{nid}"
      node.vm.network :forwarded_port, guest: "8080", host: "808#{nid}"

      if node_id == N
        node.vm.provision "ansible" do |ansible|
          ansible.limit = "all"
          ansible.groups = {
            "zookeeper-nodes" => [
              "node0",
              "node1",
              "node2",
              "node3",
              "node4"
            ],
            "zookeeper-master-nodes" => [
              "node0",
              "node1",
              "node2"
            ],
            "zookeeper-slave-nodes" => [
              "node3",
              "node4"
            ]
          }
          ansible.playbook = "playbook.yml"
        end
      end

    end
  end
end
