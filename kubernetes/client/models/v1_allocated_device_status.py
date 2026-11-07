    The version of the OpenAPI document: release-1.35
class V1AllocatedDeviceStatus(object):
        'network_data': 'V1NetworkDeviceData',
        'pool': 'str',
        'share_id': 'str'
        'pool': 'pool',
        'share_id': 'shareID'
    def __init__(self, conditions=None, data=None, device=None, driver=None, network_data=None, pool=None, share_id=None, local_vars_configuration=None):  # noqa: E501
        """V1AllocatedDeviceStatus - a model defined in OpenAPI"""  # noqa: E501
        self._share_id = None
        if share_id is not None:
            self.share_id = share_id
        """Gets the conditions of this V1AllocatedDeviceStatus.  # noqa: E501
        :return: The conditions of this V1AllocatedDeviceStatus.  # noqa: E501
        """Sets the conditions of this V1AllocatedDeviceStatus.
        :param conditions: The conditions of this V1AllocatedDeviceStatus.  # noqa: E501
        """Gets the data of this V1AllocatedDeviceStatus.  # noqa: E501
        :return: The data of this V1AllocatedDeviceStatus.  # noqa: E501
        """Sets the data of this V1AllocatedDeviceStatus.
        :param data: The data of this V1AllocatedDeviceStatus.  # noqa: E501
        """Gets the device of this V1AllocatedDeviceStatus.  # noqa: E501
        :return: The device of this V1AllocatedDeviceStatus.  # noqa: E501
        """Sets the device of this V1AllocatedDeviceStatus.
        :param device: The device of this V1AllocatedDeviceStatus.  # noqa: E501
        """Gets the driver of this V1AllocatedDeviceStatus.  # noqa: E501
        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.  # noqa: E501
        :return: The driver of this V1AllocatedDeviceStatus.  # noqa: E501
        """Sets the driver of this V1AllocatedDeviceStatus.
        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.  # noqa: E501
        :param driver: The driver of this V1AllocatedDeviceStatus.  # noqa: E501
        """Gets the network_data of this V1AllocatedDeviceStatus.  # noqa: E501
        :return: The network_data of this V1AllocatedDeviceStatus.  # noqa: E501
        :rtype: V1NetworkDeviceData
        """Sets the network_data of this V1AllocatedDeviceStatus.
        :param network_data: The network_data of this V1AllocatedDeviceStatus.  # noqa: E501
        :type: V1NetworkDeviceData
        """Gets the pool of this V1AllocatedDeviceStatus.  # noqa: E501
        :return: The pool of this V1AllocatedDeviceStatus.  # noqa: E501
        """Sets the pool of this V1AllocatedDeviceStatus.
        :param pool: The pool of this V1AllocatedDeviceStatus.  # noqa: E501
    @property
    def share_id(self):
        """Gets the share_id of this V1AllocatedDeviceStatus.  # noqa: E501

        ShareID uniquely identifies an individual allocation share of the device.  # noqa: E501

        :return: The share_id of this V1AllocatedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this V1AllocatedDeviceStatus.

        ShareID uniquely identifies an individual allocation share of the device.  # noqa: E501

        :param share_id: The share_id of this V1AllocatedDeviceStatus.  # noqa: E501
        :type: str
        """

        self._share_id = share_id

        if not isinstance(other, V1AllocatedDeviceStatus):
        if not isinstance(other, V1AllocatedDeviceStatus):
