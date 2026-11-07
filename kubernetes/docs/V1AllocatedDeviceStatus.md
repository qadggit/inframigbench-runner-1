# V1AllocatedDeviceStatus
AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.  The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices.
**driver** | **str** | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. | 
**network_data** | [**V1NetworkDeviceData**](V1NetworkDeviceData.md) |  | [optional] 
**share_id** | **str** | ShareID uniquely identifies an individual allocation share of the device. | [optional] 
