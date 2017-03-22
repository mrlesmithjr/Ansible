# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# Ensure yaml module is loaded
require 'yaml'

# Read yaml node definitions to create
# **Update nodes.yml to reflect any changes
nodes = YAML.load_file(File.join(File.dirname(__FILE__), 'nodes.yml'))

# Define global variables
#
# Define if provisioners should run (true|false)
provision_nodes = true


Vagrant.configure(2) do |config|
  # Iterate over nodes to get a count
  # Define as 0 for counting the number of nodes to create from nodes.yml
  groups = [] # Define array to hold ansible groups
  num_nodes = 0
  populated_ansible_groups = Hash.new # Create hash to contain iterated groups

  # Create array of Ansible Groups from iterated nodes
  nodes.each do |node|
    num_nodes = node
    node['ansible_groups'].each do |group|
      groups.push(group)
    end
  end

  # Remove duplicate Ansible Groups
  groups = groups.uniq

  # Iterate through array of Ansible Groups
  groups.each do |group|
    group_nodes = []
    # Iterate list of nodes
    nodes.each do |node|
      node['ansible_groups'].each do |nodegroup|
        # Check if node is a member of iterated group
        if nodegroup == group
          group_nodes.push(node['name'])
        end
      end
      populated_ansible_groups[group] = group_nodes
    end
  end

  # Dynamic Ansible Groups iterated from nodes.yml
  ansible_groups = populated_ansible_groups

  # Define Ansible groups statically for more control
  # ansible_groups = {
  #   "spines" => ["node0", "node7"],
  #   "leafs" => ["node[1:2]", "node[8:9]"],
  #   "quagga-routers:children" => ["spines", "leafs", "compute-nodes"],
  #   "compute-nodes" => ["node[3:6]"],
  #   "docker-swarm:children" => ["docker-swarm-managers", "docker-swarm-workers"],
  #   "docker-swarm-managers" => ["node[3:4]"],
  #   "docker-swarm-workers" => ["node[5:6]"]
  # }

  #Iterate over nodes
  nodes.each do |node_id|
    # Below is needed if not using Guest Additions
    # config.vm.synced_folder ".", "/vagrant", type: "rsync",
    #   rsync__exclude: "hosts"
    config.vm.define node_id['name'] do |node|
      node.vm.box = node_id['box']
      node.vm.hostname = node_id['name']
      node.vm.provider "virtualbox" do |vb|
        vb.memory = node_id['mem']
        vb.cpus = node_id['vcpu']

        # Setup desktop environment
        if not node_id['desktop'].nil?
          if node_id['desktop']
            vb.gui = true
            vb.customize ["modifyvm", :id, "--graphicscontroller", "vboxvga"]
            vb.customize ["modifyvm", :id, "--accelerate3d", "on"]
            vb.customize ["modifyvm", :id, "--ioapic", "on"]
            vb.customize ["modifyvm", :id, "--vram", "128"]
            vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
          end
        end

        # Add additional disk(s)
        if not node_id['disks'].nil?
          dnum = 0
          node_id['disks'].each do |disk_num|
            dnum = (dnum.to_i + 1)
            ddev = ("#{node_id['name']}_Disk#{dnum}.vdi")
            dsize = disk_num['size'].to_i * 1024
            unless File.exist?("#{ddev}")
              vb.customize ['createhd', '--filename', ("#{ddev}"), \
                '--variant', 'Fixed', '--size', dsize]
            end
            vb.customize ['storageattach', :id,  '--storagectl', \
              "#{disk_num['controller']}", '--port', dnum, '--device', 0, \
              '--type', 'hdd', '--medium', "#{ddev}"]
          end
        end
      end

      # Provision network interfaces
      if not node_id['interfaces'].nil?
        node_id['interfaces'].each do |int|
          if int['method'] == 'dhcp'
            if int['network_name'] == "None"
              node.vm.network :private_network, \
              type: "dhcp"
            end
            if int['network_name'] != "None"
              node.vm.network :private_network, \
              virtualbox__intnet: int['network_name'], \
              type: "dhcp"
            end
          end
          if int['method'] == "static"
            if int['network_name'] == "None"
              node.vm.network :private_network, \
              ip: int['ip'], \
              auto_config: int['auto_config']
            end
            if int['network_name'] != "None"
              node.vm.network :private_network, \
              virtualbox__intnet: int['network_name'], \
              ip: int['ip'], \
              auto_config: int['auto_config']
            end
          end
        end
      end

      # Port Forwards
      if not node_id['port_forwards'].nil?
        node_id['port_forwards'].each do |pf|
          node.vm.network :forwarded_port, \
          guest: pf['guest'], \
          host: pf['host']
        end
      end

      # Provisioners
      if provision_nodes
        if node_id == num_nodes
          node.vm.provision "ansible" do |ansible|
            ansible.limit = "all"
            #runs bootstrap Ansible playbook
            ansible.playbook = "bootstrap.yml"
          end
          node.vm.provision "ansible" do |ansible|
            ansible.limit = "all"
            #runs Ansible playbook for installing roles/executing tasks
            ansible.playbook = "playbook.yml"
            ansible.groups = ansible_groups
          end
        end
      end

    end
  end

  #runs initial shell script
  if provision_nodes
    config.vm.provision :shell, path: "bootstrap.sh", keep_color: "true"
  end

end
