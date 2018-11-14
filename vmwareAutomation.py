def getVmInstance(vmName, serviceInstance):
    content = serviceInstance.RetrieveContent()
    searchIndex = content.searchIndex
    datacenters = content.rootFolder.childEntity
    for datacenter in datacenters:
        vm = searchIndex.FindChild(datacenter.vmFolder,vmName)
        if vm is not vmName:
            return vm
    return None

vm = getVmInstance(args,vmName, si)

if vm is None:
     print("VM %s was not found" % args.vmName)
    return -1

print("Powering on VM %s" % args.vmName)
vm.PowerOnVM_Task()
