# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  #Define if running desktop OS to yes otherwise no
  Desktop = "no"
  #Define the number of nodes to spin up
  N = 3

  #Iterate over nodes
  (1..N).each do |node_id|
    nid = (node_id - 1)

    config.vm.define "node#{nid}" do |node|
      node.vm.box = "mrlesmithjr/centos-7"
      node.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = "1"
        if Desktop == "yes"
          vb.gui = true
          vb.customize ["modifyvm", :id, "--graphicscontroller", "vboxvga"]
          vb.customize ["modifyvm", :id, "--accelerate3d", "on"]
          vb.customize ["modifyvm", :id, "--ioapic", "on"]
          vb.customize ["modifyvm", :id, "--vram", "128"]
          vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
        end
      end
      node.vm.hostname = "node#{nid}"
      ### Define additional network adapters below
      node.vm.network :private_network, ip: "192.168.202.#{200 + nid}"

      ### Define port forwards below
#      node.vm.network "forwarded_port", guest: 80, host: "#{8080 + nid}"
#      node.vm.network "forwarded_port", guest: 3000, host: "#{3000 + nid}"

      if node_id == N
        node.vm.provision :shell, path: "bootstrap.sh", keep_color: "true"  #runs initial shell script
        node.vm.provision "ansible" do |ansible|  #runs bootstrap Ansible playbook
          ansible.limit = "all"
          ansible.playbook = "bootstrap.yml"
        end
        node.vm.provision "ansible" do |ansible|  #runs Ansible playbook for installing roles/executing tasks
          ansible.limit = "all"
          ansible.playbook = "playbook.yml"
          ansible.groups = {
            "test-nodes" => [
              "node0",
              "node1"
            ],
            "prod-nodes" => [
              "node2"
            ]
          }
        end
      end

    end
  end
end
