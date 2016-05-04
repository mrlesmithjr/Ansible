# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# ---- Define number of nodes to spin up ----
N = 1

# ---- Define variables below ----
additional_disks = "no"  #Define if additional drives defined should be added (yes | no)
additional_disks_controller = "SATA Controller"
additional_disks_num = 1  #Define the number of additional disks to add
additional_disks_size = 10  #Define disk size in GB
additional_nics = "no"  #Define if additional network adapters should be created (yes | no)
additional_nics_num = 1  #Define the number of additional nics to add
box = "mrlesmithjr/trusty64"  #Define Vagrant box to load
desktop = "no"  #Define if running desktop OS (yes | no)
enable_port_forwards = "yes"  #Define if port forwards should be enabled
generate_random_ips = "no"  #Define if IP addresses should be randomnly generated for additional_nics
linked_clones = "no"  #Defines if nodes should be linked from master VM (yes | no)
port_forwards = [
  {
    :node => "node0",
    :guest => 80,
    :host => 8080
  }
]
provision_nodes = "yes"  #Define if provisioners should run (yes | no)
server_cpus = 1  #Define number of CPU cores
server_memory = 1024  #Define amount of memory to assign to node(s)
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
        if additional_disks == "yes"
          (1..additional_disks_num).each do |disk_num|
            dnum = (disk_num + 1)
            ddev = ("node#{nid}_Disk#{dnum}.vdi")
            unless File.exist?("#{ddev}")
              vb.customize ['createhd', '--filename', ("#{ddev}"), '--variant', 'Fixed', '--size', additional_disks_size * 1024]
            end
            vb.customize ['storageattach', :id,  '--storagectl', "#{additional_disks_controller}", '--port', dnum, '--device', 0, '--type', 'hdd', '--medium', "node#{nid}_Disk#{dnum}.vdi"]
          end
        end
      end
      node.vm.hostname = "node#{nid}"

      ### Define additional network adapters below
      if additional_nics == "yes"
        (1..additional_nics_num).each do |nic_num|
          if generate_random_ips == "yes"
            nnum = Random.rand(0..50)
            node.vm.network :private_network, ip: subnet+"#{subnet_ip_start + nid + nnum}"
          end
          if generate_random_ips == "no"
            node.vm.network :private_network, ip: subnet+"#{subnet_ip_start + nid}"
          end
        end
      end

      ### Define port forwards below
      if enable_port_forwards == "yes"
        port_forwards.each do |pf|
          if pf[:node] == "node#{nid}"
            node.vm.network "forwarded_port", guest: pf[:guest], host: pf[:host] + nid
          end
        end
      end
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
              "zabbix-servers" => [
                "node0"
              ]
            }
          end
        end
      end

    end
  end
  if provision_nodes == "yes"
    config.vm.provision :shell, path: "bootstrap.sh", keep_color: "true"  #runs initial shell script
  end
end
