$vCenterHost = "{{ vsphere_vcsa_network_fqdn }}"
Connect-VIServer $vCenterHost | Out-Null
$vCenter = Get-VC $vCenterHost
$Cluster = Get-Cluster -Server $vCenter
$ClusterHosts = ($Cluster | Get-VMHost).Name
if ($ClusterHosts -notcontains "{{ vsphere_bootstrap_host }}") {
  $vmHost = "{{ hostvars[vsphere_bootstrap_host]['ansible_host'] }}"
  Connect-VIServer -Server $vmHost | Out-Null
{%   for host in groups['vsphere_hosts'] %}
{%     if hostvars[host]['inventory_hostname'] != vsphere_bootstrap_host %}
    $_migrationHost = "{{ hostvars[host]['inventory_hostname'] }}"
    if ($ClusterHosts -contains $_migrationHost) {
      $migrationHost = "{{ hostvars[host]['ansible_host'] }}"
      Connect-VIServer -Server $migrationHost
    }
{%     endif %}
{%   endfor %}
{% for vm in groups['vsphere_lb_vms'] %}
  $vmServer = Get-VMHost -Server $vmHost
  $vms = $vmServer | Get-VM
  $vm = "{{ hostvars[vm]['inventory_hostname'] }}"
  if ($vms.Name -contains $vm) {
    $vm = $vmServer | Get-VM $vm
    $vmPowerState = $vm.PowerState
    $vmView = $vm | Get-View
    $vmSummary = $vmView.Summary.Config
    $vmVMXFile = $vmSummary.VmPathName
    if ($vmPowerState -eq "PoweredOn") {
      $vm | ShutDown-VMGuest -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmServer | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOff")
    }
    $vm | Remove-VM -DeletePermanently:$false -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vmMigrationHost = Get-VMHost -Server $migrationHost
    New-VM -VMFilePath $vmVMXFile -VMHost $vmMigrationHost -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vm = $vmMigrationHost | Get-VM $vm
    $vmPowerState = $vm.PowerState
    if ($vmPowerState -eq "PoweredOff") {
      $vm | Start-VM -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOn")
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmView = $vm | Get-View
        $vmToolsStatus = $vmView.Guest.ToolsStatus
        sleep 3
      }
      until ($vmToolsStatus -eq 'toolsOk')
    }
  }
{% endfor %}
{% for vm in groups['vsphere_dnsdist_vms'] %}
  $vmServer = Get-VMHost -Server $vmHost
  $vms = $vmServer | Get-VM
  $vm = "{{ hostvars[vm]['inventory_hostname'] }}"
  if ($vms.Name -contains $vm) {
    $vm = $vmServer | Get-VM $vm
    $vmPowerState = $vm.PowerState
    $vmView = $vm | Get-View
    $vmSummary = $vmView.Summary.Config
    $vmVMXFile = $vmSummary.VmPathName
    if ($vmPowerState -eq "PoweredOn") {
      $vm | ShutDown-VMGuest -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmServer | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOff")
    }
    $vm | Remove-VM -DeletePermanently:$false -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vmMigrationHost = Get-VMHost -Server $migrationHost
    New-VM -VMFilePath $vmVMXFile -VMHost $vmMigrationHost -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vm = $vmMigrationHost | Get-VM $vm
    $vmPowerState = $vm.PowerState
    if ($vmPowerState -eq "PoweredOff") {
      $vm | Start-VM -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOn")
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmView = $vm | Get-View
        $vmToolsStatus = $vmView.Guest.ToolsStatus
        sleep 3
      }
      until ($vmToolsStatus -eq 'toolsOk')
    }
  }
{% endfor %}
{% for vm in groups['vsphere_ddi_vms'] %}
  $vmServer = Get-VMHost -Server $vmHost
  $vms = $vmServer | Get-VM
  $vm = "{{ hostvars[vm]['inventory_hostname'] }}"
  if ($vms.Name -contains $vm) {
    $vm = $vmServer | Get-VM $vm
    $vmPowerState = $vm.PowerState
    $vmView = $vm | Get-View
    $vmSummary = $vmView.Summary.Config
    $vmVMXFile = $vmSummary.VmPathName
    if ($vmPowerState -eq "PoweredOn") {
      $vm | ShutDown-VMGuest -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmServer | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOff")
    }
    $vm | Remove-VM -DeletePermanently:$false -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vmMigrationHost = Get-VMHost -Server $migrationHost
    New-VM -VMFilePath $vmVMXFile -VMHost $vmMigrationHost -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vm = $vmMigrationHost | Get-VM $vm
    $vmPowerState = $vm.PowerState
    if ($vmPowerState -eq "PoweredOff") {
      $vm | Start-VM -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOn")
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmView = $vm | Get-View
        $vmToolsStatus = $vmView.Guest.ToolsStatus
        sleep 3
      }
      until ($vmToolsStatus -eq 'toolsOk')
    }
  }
{% endfor %}
{% for vm in groups['vsphere_samba_vms'] %}
  $vmServer = Get-VMHost -Server $vmHost
  $vms = $vmServer | Get-VM
  $vm = "{{ hostvars[vm]['inventory_hostname'] }}"
  if ($vms.Name -contains $vm) {
    $vm = $vmServer | Get-VM $vm
    $vmPowerState = $vm.PowerState
    $vmView = $vm | Get-View
    $vmSummary = $vmView.Summary.Config
    $vmVMXFile = $vmSummary.VmPathName
    if ($vmPowerState -eq "PoweredOn") {
      $vm | ShutDown-VMGuest -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmServer | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOff")
    }
    $vm | Remove-VM -DeletePermanently:$false -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vmMigrationHost = Get-VMHost -Server $migrationHost
    New-VM -VMFilePath $vmVMXFile -VMHost $vmMigrationHost -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vm = $vmMigrationHost | Get-VM $vm
    $vmPowerState = $vm.PowerState
    if ($vmPowerState -eq "PoweredOff") {
      $vm | Start-VM -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOn")
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmView = $vm | Get-View
        $vmToolsStatus = $vmView.Guest.ToolsStatus
        sleep 3
      }
      until ($vmToolsStatus -eq 'toolsOk')
    }
  }
{% endfor %}
  $vmServer = Get-VMHost -Server $vmHost
  $vms = $vmServer | Get-VM
  $vm = "{{ vsphere_vcsa_network_fqdn }}"
  if ($vms.Name -contains "{{ vsphere_vcsa_network_fqdn }}") {
    $vm = $vmServer | Get-VM $vm
    $vmPowerState = $vm.PowerState
    $vmView = $vm | Get-View
    $vmSummary = $vmView.Summary.Config
    $vmVMXFile = $vmSummary.VmPathName
    if ($vmPowerState -eq "PoweredOn") {
      $vm | ShutDown-VMGuest -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmServer | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOff")
    }
    $vm | Remove-VM -DeletePermanently:$false -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vmMigrationHost = Get-VMHost -Server $migrationHost
    New-VM -VMFilePath $vmVMXFile -VMHost $vmMigrationHost -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
    $vm = $vmMigrationHost | Get-VM $vm
    $vmPowerState = $vm.PowerState
    if ($vmPowerState -eq "PoweredOff") {
      $vm | Start-VM -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmPowerState = $vm.PowerState
        sleep 3
      }
      until ($vmPowerState -eq "PoweredOn")
      do {
        $vm = $vmMigrationHost | Get-VM $vm
        $vmView = $vm | Get-View
        $vmToolsStatus = $vmView.Guest.ToolsStatus
        sleep 3
      }
      until ($vmToolsStatus -eq 'toolsOk')
    }
  }
  $vmServer = Get-VMHost -Server $vmHost
  $vms = $vmServer | Get-VM
  if ($vms -ne $null) {
    foreach ($vm in $vms) {
      $vm = $vmServer | Get-VM $vm
      $vmPowerState = $vm.PowerState
      if ($vmPowerState -eq "PoweredOn") {
        $vm | ShutDown-VMGuest -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
        do {
          $vm = $vmServer | Get-VM $vm
          $vmPowerState = $vm.PowerState
          sleep 3
        }
        until ($vmPowerState -eq "PoweredOff")
      }
    }
    $vmServer | Set-VMHost -State Maintenance -Confirm:$false | Out-File -Append {{ vsphere_management_log }}
  }
Disconnect-VIServer * -Confirm:$false
}
