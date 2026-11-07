    The version of the OpenAPI document: release-1.35
class V1AllocationResult(object):
        'allocation_timestamp': 'datetime',
        'devices': 'V1DeviceAllocationResult',
        'allocation_timestamp': 'allocationTimestamp',
    def __init__(self, allocation_timestamp=None, devices=None, node_selector=None, local_vars_configuration=None):  # noqa: E501
        """V1AllocationResult - a model defined in OpenAPI"""  # noqa: E501
        self._allocation_timestamp = None
        if allocation_timestamp is not None:
            self.allocation_timestamp = allocation_timestamp
    @property
    def allocation_timestamp(self):
        """Gets the allocation_timestamp of this V1AllocationResult.  # noqa: E501

        AllocationTimestamp stores the time when the resources were allocated. This field is not guaranteed to be set, in which case that time is unknown.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate.  # noqa: E501

        :return: The allocation_timestamp of this V1AllocationResult.  # noqa: E501
        :rtype: datetime
        """
        return self._allocation_timestamp

    @allocation_timestamp.setter
    def allocation_timestamp(self, allocation_timestamp):
        """Sets the allocation_timestamp of this V1AllocationResult.

        AllocationTimestamp stores the time when the resources were allocated. This field is not guaranteed to be set, in which case that time is unknown.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate.  # noqa: E501

        :param allocation_timestamp: The allocation_timestamp of this V1AllocationResult.  # noqa: E501
        :type: datetime
        """

        self._allocation_timestamp = allocation_timestamp

        """Gets the devices of this V1AllocationResult.  # noqa: E501
        :return: The devices of this V1AllocationResult.  # noqa: E501
        :rtype: V1DeviceAllocationResult
        """Sets the devices of this V1AllocationResult.
        :param devices: The devices of this V1AllocationResult.  # noqa: E501
        :type: V1DeviceAllocationResult
        """Gets the node_selector of this V1AllocationResult.  # noqa: E501
        :return: The node_selector of this V1AllocationResult.  # noqa: E501
        """Sets the node_selector of this V1AllocationResult.
        :param node_selector: The node_selector of this V1AllocationResult.  # noqa: E501
        if not isinstance(other, V1AllocationResult):
        if not isinstance(other, V1AllocationResult):
