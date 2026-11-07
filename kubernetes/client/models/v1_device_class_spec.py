    The version of the OpenAPI document: release-1.35
class V1DeviceClassSpec(object):
        'config': 'list[V1DeviceClassConfiguration]',
        'extended_resource_name': 'str',
        'selectors': 'list[V1DeviceSelector]'
        'extended_resource_name': 'extendedResourceName',
    def __init__(self, config=None, extended_resource_name=None, selectors=None, local_vars_configuration=None):  # noqa: E501
        """V1DeviceClassSpec - a model defined in OpenAPI"""  # noqa: E501
        self._extended_resource_name = None
        if extended_resource_name is not None:
            self.extended_resource_name = extended_resource_name
        """Gets the config of this V1DeviceClassSpec.  # noqa: E501
        :return: The config of this V1DeviceClassSpec.  # noqa: E501
        :rtype: list[V1DeviceClassConfiguration]
        """Sets the config of this V1DeviceClassSpec.
        :param config: The config of this V1DeviceClassSpec.  # noqa: E501
        :type: list[V1DeviceClassConfiguration]
    @property
    def extended_resource_name(self):
        """Gets the extended_resource_name of this V1DeviceClassSpec.  # noqa: E501

        ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod's extended resource requests. It has the same format as the name of a pod's extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod's extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.  This is an alpha field.  # noqa: E501

        :return: The extended_resource_name of this V1DeviceClassSpec.  # noqa: E501
        :rtype: str
        """
        return self._extended_resource_name

    @extended_resource_name.setter
    def extended_resource_name(self, extended_resource_name):
        """Sets the extended_resource_name of this V1DeviceClassSpec.

        ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod's extended resource requests. It has the same format as the name of a pod's extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod's extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.  This is an alpha field.  # noqa: E501

        :param extended_resource_name: The extended_resource_name of this V1DeviceClassSpec.  # noqa: E501
        :type: str
        """

        self._extended_resource_name = extended_resource_name

        """Gets the selectors of this V1DeviceClassSpec.  # noqa: E501
        :return: The selectors of this V1DeviceClassSpec.  # noqa: E501
        :rtype: list[V1DeviceSelector]
        """Sets the selectors of this V1DeviceClassSpec.
        :param selectors: The selectors of this V1DeviceClassSpec.  # noqa: E501
        :type: list[V1DeviceSelector]
        if not isinstance(other, V1DeviceClassSpec):
        if not isinstance(other, V1DeviceClassSpec):
