    The version of the OpenAPI document: release-1.35
class V1OpaqueDeviceConfiguration(object):
        """V1OpaqueDeviceConfiguration - a model defined in OpenAPI"""  # noqa: E501
        """Gets the driver of this V1OpaqueDeviceConfiguration.  # noqa: E501
        Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.  # noqa: E501
        :return: The driver of this V1OpaqueDeviceConfiguration.  # noqa: E501
        """Sets the driver of this V1OpaqueDeviceConfiguration.
        Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.  # noqa: E501
        :param driver: The driver of this V1OpaqueDeviceConfiguration.  # noqa: E501
        """Gets the parameters of this V1OpaqueDeviceConfiguration.  # noqa: E501
        :return: The parameters of this V1OpaqueDeviceConfiguration.  # noqa: E501
        """Sets the parameters of this V1OpaqueDeviceConfiguration.
        :param parameters: The parameters of this V1OpaqueDeviceConfiguration.  # noqa: E501
        if not isinstance(other, V1OpaqueDeviceConfiguration):
        if not isinstance(other, V1OpaqueDeviceConfiguration):
