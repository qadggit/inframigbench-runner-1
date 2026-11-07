    The version of the OpenAPI document: release-1.35
class V1ResourceClaimStatus(object):
        'allocation': 'V1AllocationResult',
        'devices': 'list[V1AllocatedDeviceStatus]',
        'reserved_for': 'list[V1ResourceClaimConsumerReference]'
        """V1ResourceClaimStatus - a model defined in OpenAPI"""  # noqa: E501
        """Gets the allocation of this V1ResourceClaimStatus.  # noqa: E501
        :return: The allocation of this V1ResourceClaimStatus.  # noqa: E501
        :rtype: V1AllocationResult
        """Sets the allocation of this V1ResourceClaimStatus.
        :param allocation: The allocation of this V1ResourceClaimStatus.  # noqa: E501
        :type: V1AllocationResult
        """Gets the devices of this V1ResourceClaimStatus.  # noqa: E501
        :return: The devices of this V1ResourceClaimStatus.  # noqa: E501
        :rtype: list[V1AllocatedDeviceStatus]
        """Sets the devices of this V1ResourceClaimStatus.
        :param devices: The devices of this V1ResourceClaimStatus.  # noqa: E501
        :type: list[V1AllocatedDeviceStatus]
        """Gets the reserved_for of this V1ResourceClaimStatus.  # noqa: E501
        :return: The reserved_for of this V1ResourceClaimStatus.  # noqa: E501
        :rtype: list[V1ResourceClaimConsumerReference]
        """Sets the reserved_for of this V1ResourceClaimStatus.
        :param reserved_for: The reserved_for of this V1ResourceClaimStatus.  # noqa: E501
        :type: list[V1ResourceClaimConsumerReference]
        if not isinstance(other, V1ResourceClaimStatus):
        if not isinstance(other, V1ResourceClaimStatus):
