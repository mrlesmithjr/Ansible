# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# ---- Define number of nodes to spin up ----
N = 5

# ---- Define variables below ----
additional_nics = "yes"  #Define if additional network adapters should be created (yes | no)
box = "mrlesmithjr/trusty64"
desktop = "no"  #Define if running desktop OS (yes | no)
linked_clones = "no"  #Defines if nodes should be linked from master VM (yes | no)
provision_nodes = "yes"  #Define if provisioners should run (yes | no)
server_cpus = "1"  #Define number of CPU cores
server_memory = "1024"  #Define amount of memory to assign to node(s)
subnet = "192.168.202."  #Define subnet for private_network
subnet_ip_start = 200  #Define starting last octet of the subnet range to begin addresses for node(s)

Vagrant.configure(2) do |config|

  #Iterate over nodes
  (1..N).each do |node_id|
    nid = (node_id - 1)

    config.vm.define "node#{nid}" do |node|
      node.vm.box = box
      node.vm.provider "virtualbox" do |vb|
        if linked_clones == "yes"
          vb.linked_clone = true
        end
        vb.customize ["modifyvm", :id, "--cpus", server_cpus]
        vb.customize ["modifyvm", :id, "--memory", server_memory]
        if desktop == "yes"
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
      if additional_nics == "yes"
        node.vm.network :private_network, ip: subnet+"#{subnet_ip_start + nid}"
      end

      ### Define port forwards below
#      node.vm.network "forwarded_port", guest: 80, host: "#{8080 + nid}"
#      node.vm.network "forwarded_port", guest: 3000, host: "#{3000 + nid}"

      if provision_nodes == "yes"
        if node_id == N
          node.vm.provision "ansible" do |ansible|  #runs bootstrap Ansible playbook
            ansible.limit = "all"
            ansible.playbook = "bootstrap.yml"
          end
          node.vm.provision "ansible" do |ansible|  #runs Ansible playbook for installing roles/executing tasks
            ansible.limit = "all"
            ansible.playbook = "playbook.yml"
            ansible.groups = {
              "consul-servers" => [
                "node0",
                "node1",
                "node2"
              ],
              "consul-clients" => [
                "node3",
                "node4"
              ]
            }
          end
        end
      end

    end
  end
  config.vm.provision :shell, path: "bootstrap.sh", keep_color: "true"  #runs initial shell script
end
