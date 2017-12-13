data "vsphere_datacenter" "dc" {
  name = "${var.vsphere_datacenter}"
}

data "vsphere_host" "esxi_hosts" {
  count = "${length(var.esxi_hosts)}"
  name = "${var.esxi_hosts[count.index]}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_distributed_virtual_switch" "dvs" {
  count = "${length(var.dvSwitches)}"
  name = "${var.dvSwitches[count.index]}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "net" {
  count = "${length(var.vsphere_networks)}"
  name = "${var.vsphere_networks[count.index]}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}
