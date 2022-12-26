#===============================================================================
# vSphere Provider
#===============================================================================
provider "vsphere" {
  vsphere_server = "vcenter1.lab.newpathexchange.com"
  user           = "REDACTED"
  password       = "REDACTED"
  allow_unverified_ssl = "true"
}

module "vmware_ubuntu_18" {
  source = "../../modules/vsphere-server"

  vm_name = "zkd"
  vm_template = "Template-Ubuntu1804"
  network_interface_prefix = "ens"
  cloud_init_user_data = "userdata.yaml"
  num_srv = "3"
  num_cpu = "1"
  num_disk = "1"
  disk_size = "50"
  mem_size = "4096"

  vsphere_datacenter = "NPX-Lab"
  vsphere_host = "vmware4.lab.newpathexchange.com"
  vsphere_datastore = "datastore4-1"
  vsphere_network = "VM Network"

  device_list = ["/dev/sdb", "/dev/sdc", "/dev/sdd", "/dev/sde", "/dev/sdf", "/dev/sdg", "/dev/sdh", "/dev/sdi"]
  mount_list = ["/data1", "/data2", "/data3", "/data4", "/data5", "/data6", "/data7", "/data8"]

}

