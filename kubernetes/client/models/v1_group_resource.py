    The version of the OpenAPI document: release-1.35
class V1GroupResource(object):
        'group': 'str',
        'resource': 'str'
        'group': 'group',
    def __init__(self, group=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """V1GroupResource - a model defined in OpenAPI"""  # noqa: E501
        self._group = None
        self.group = group
    def group(self):
        """Gets the group of this V1GroupResource.  # noqa: E501
        :return: The group of this V1GroupResource.  # noqa: E501
        return self._group
    @group.setter
    def group(self, group):
        """Sets the group of this V1GroupResource.
        :param group: The group of this V1GroupResource.  # noqa: E501
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501
        self._group = group
        """Gets the resource of this V1GroupResource.  # noqa: E501
        :return: The resource of this V1GroupResource.  # noqa: E501
        :rtype: str
        """Sets the resource of this V1GroupResource.
        :param resource: The resource of this V1GroupResource.  # noqa: E501
        :type: str
        if not isinstance(other, V1GroupResource):
        if not isinstance(other, V1GroupResource):
