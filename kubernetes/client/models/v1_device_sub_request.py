    The version of the OpenAPI document: release-1.35
class V1DeviceSubRequest(object):
        'capacity': 'V1CapacityRequirements',
        'selectors': 'list[V1DeviceSelector]',
        'tolerations': 'list[V1DeviceToleration]'
        'capacity': 'capacity',
    def __init__(self, allocation_mode=None, capacity=None, count=None, device_class_name=None, name=None, selectors=None, tolerations=None, local_vars_configuration=None):  # noqa: E501
        """V1DeviceSubRequest - a model defined in OpenAPI"""  # noqa: E501
        self._capacity = None
        if capacity is not None:
            self.capacity = capacity
        """Gets the allocation_mode of this V1DeviceSubRequest.  # noqa: E501
        AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:  - ExactCount: This request is for a specific number of devices.   This is the default. The exact number is provided in the   count field.  - All: This subrequest is for all of the matching devices in a pool.   Allocation will fail if some devices are already allocated,   unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.  # noqa: E501
        :return: The allocation_mode of this V1DeviceSubRequest.  # noqa: E501
        """Sets the allocation_mode of this V1DeviceSubRequest.
        AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:  - ExactCount: This request is for a specific number of devices.   This is the default. The exact number is provided in the   count field.  - All: This subrequest is for all of the matching devices in a pool.   Allocation will fail if some devices are already allocated,   unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.  # noqa: E501
        :param allocation_mode: The allocation_mode of this V1DeviceSubRequest.  # noqa: E501
    @property
    def capacity(self):
        """Gets the capacity of this V1DeviceSubRequest.  # noqa: E501


        :return: The capacity of this V1DeviceSubRequest.  # noqa: E501
        :rtype: V1CapacityRequirements
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1DeviceSubRequest.


        :param capacity: The capacity of this V1DeviceSubRequest.  # noqa: E501
        :type: V1CapacityRequirements
        """

        self._capacity = capacity

        """Gets the count of this V1DeviceSubRequest.  # noqa: E501
        :return: The count of this V1DeviceSubRequest.  # noqa: E501
        """Sets the count of this V1DeviceSubRequest.
        :param count: The count of this V1DeviceSubRequest.  # noqa: E501
        """Gets the device_class_name of this V1DeviceSubRequest.  # noqa: E501
        :return: The device_class_name of this V1DeviceSubRequest.  # noqa: E501
        """Sets the device_class_name of this V1DeviceSubRequest.
        :param device_class_name: The device_class_name of this V1DeviceSubRequest.  # noqa: E501
        """Gets the name of this V1DeviceSubRequest.  # noqa: E501
        :return: The name of this V1DeviceSubRequest.  # noqa: E501
        """Sets the name of this V1DeviceSubRequest.
        :param name: The name of this V1DeviceSubRequest.  # noqa: E501
        """Gets the selectors of this V1DeviceSubRequest.  # noqa: E501
        Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.  # noqa: E501
        :return: The selectors of this V1DeviceSubRequest.  # noqa: E501
        :rtype: list[V1DeviceSelector]
        """Sets the selectors of this V1DeviceSubRequest.
        Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.  # noqa: E501
        :param selectors: The selectors of this V1DeviceSubRequest.  # noqa: E501
        :type: list[V1DeviceSelector]
        """Gets the tolerations of this V1DeviceSubRequest.  # noqa: E501
        :return: The tolerations of this V1DeviceSubRequest.  # noqa: E501
        :rtype: list[V1DeviceToleration]
        """Sets the tolerations of this V1DeviceSubRequest.
        :param tolerations: The tolerations of this V1DeviceSubRequest.  # noqa: E501
        :type: list[V1DeviceToleration]
        if not isinstance(other, V1DeviceSubRequest):
        if not isinstance(other, V1DeviceSubRequest):
