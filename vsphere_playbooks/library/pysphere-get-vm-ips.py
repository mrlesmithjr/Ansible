#!/usr/bin/python
import sys, re, getpass, argparse, subprocess
from time import sleep
from pysphere import MORTypes, VIServer, VITask, VIProperty, VIMor, VIException
from pysphere.vi_virtual_machine import VIVirtualMachine

def print_verbose(message):
    if verbose:
        print message

def find_vm(name):
    try:
        vm = con.get_vm_by_name(name)
        return vm
    except VIException:
        return None

def find_ip(vm,ipv6=False):
    ips = None
    net_info = vm.get_property('net',False)
    if net_info:
        for ip in net_info[0]['ip_addresses']:
            if ipv6 and re.match('\d{1,4}\:.*',ip) and not re.match('fe83\:.*',ip):
                print_verbose('IPv6 address found: %s' % ip)
                ips = str(ips) + ';' + ip
                #return ip
            elif not ipv6 and re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip) and ip != '127.0.0.1':
                print_verbose('IPv4 address found: %s' % ip)
                ips = str(ips) + ';' + ip
                #return ip
    return ips

parser = argparse.ArgumentParser(description="Deploy a template into multiple VM's")
parser.add_argument('-6', '--six', required=False, help='Get IPv6 address for VMs instead of IPv4', dest='ipv6', action='store_true')
parser.add_argument('-a', '--all', required=False, help='Get address for all powered on VMs', dest='allvms', action='store_true')
parser.add_argument('-n', '--name', nargs=1, required=False, help='VM Name', dest='vmname', type=str)
parser.add_argument('-s', '--server', nargs=1, required=True, help='The vCenter or ESXi server to connect to', dest='server', type=str)
parser.add_argument('-u', '--user', nargs=1, required=True, help='The username with which to connect to the server', dest='username', type=str)
parser.add_argument('-v', '--verbose', required=False, help='Enable verbose output', dest='verbose', action='store_true')
parser.add_argument('-p', '--password', nargs=1, required=True, help='The password with which to connect to the server', dest='password', type=str)

args = parser.parse_args()

ipv6        = args.ipv6
allvms      = args.allvms
vmname      = None
if args.vmname:
    vmname      = args.vmname[0]
server      = args.server[0]
username    = args.username[0]
verbose     = args.verbose
password    = args.password[0]

# Asking Users password for server
#password=getpass.getpass(prompt='Enter password for vCenter %s for user %s: ' % (server,username))

# Connecting to server
print_verbose('Connecting to server %s with username %s' % (server,username))
con = VIServer()
con.connect(server,username,password)
print_verbose('Connected to server %s' % server)
print_verbose('Server type: %s' % con.get_server_type())
print_verbose('API version: %s' % con.get_api_version())

if allvms:
    vms = con.get_registered_vms(None, None, None, 'poweredOn', None)
    for vmpath in vms:
        print_verbose('================================================================================')
        vm = con.get_vm_by_path(vmpath)
        vmname = vm.get_property('name')
        ip = find_ip(vm,ipv6)
        if ip:
            print '%s : %s' % (vmname,ip)
        else:
            print 'ERROR: IP for VM %s not found' % vmname
else:
    print_verbose('================================================================================')
    print_verbose('Trying to find IP for VM %s' % vmname)
    vm = find_vm(vmname)
    if vm:
        ip = find_ip(vm,ipv6)
        if ip:
            print '%s : %s' % (vmname,ip)
        else:
            print 'ERROR: IP for VM %s not found' % vmname
    else:
        print 'ERROR: %s not found' % vmname

# Disconnecting from server
con.disconnect()
