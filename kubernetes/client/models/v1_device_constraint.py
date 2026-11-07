    The version of the OpenAPI document: release-1.35
class V1DeviceConstraint(object):
        'distinct_attribute': 'str',
        'distinct_attribute': 'distinctAttribute',
    def __init__(self, distinct_attribute=None, match_attribute=None, requests=None, local_vars_configuration=None):  # noqa: E501
        """V1DeviceConstraint - a model defined in OpenAPI"""  # noqa: E501
        self._distinct_attribute = None
        if distinct_attribute is not None:
            self.distinct_attribute = distinct_attribute
    @property
    def distinct_attribute(self):
        """Gets the distinct_attribute of this V1DeviceConstraint.  # noqa: E501

        DistinctAttribute requires that all devices in question have this attribute and that its type and value are unique across those devices.  This acts as the inverse of MatchAttribute.  This constraint is used to avoid allocating multiple requests to the same device by ensuring attribute-level differentiation.  This is useful for scenarios where resource requests must be fulfilled by separate physical devices. For example, a container requests two network interfaces that must be allocated from two different physical NICs.  # noqa: E501

        :return: The distinct_attribute of this V1DeviceConstraint.  # noqa: E501
        :rtype: str
        """
        return self._distinct_attribute

    @distinct_attribute.setter
    def distinct_attribute(self, distinct_attribute):
        """Sets the distinct_attribute of this V1DeviceConstraint.

        DistinctAttribute requires that all devices in question have this attribute and that its type and value are unique across those devices.  This acts as the inverse of MatchAttribute.  This constraint is used to avoid allocating multiple requests to the same device by ensuring attribute-level differentiation.  This is useful for scenarios where resource requests must be fulfilled by separate physical devices. For example, a container requests two network interfaces that must be allocated from two different physical NICs.  # noqa: E501

        :param distinct_attribute: The distinct_attribute of this V1DeviceConstraint.  # noqa: E501
        :type: str
        """

        self._distinct_attribute = distinct_attribute

        """Gets the match_attribute of this V1DeviceConstraint.  # noqa: E501
        :return: The match_attribute of this V1DeviceConstraint.  # noqa: E501
        """Sets the match_attribute of this V1DeviceConstraint.
        :param match_attribute: The match_attribute of this V1DeviceConstraint.  # noqa: E501
        """Gets the requests of this V1DeviceConstraint.  # noqa: E501
        :return: The requests of this V1DeviceConstraint.  # noqa: E501
        """Sets the requests of this V1DeviceConstraint.
        :param requests: The requests of this V1DeviceConstraint.  # noqa: E501
        if not isinstance(other, V1DeviceConstraint):
        if not isinstance(other, V1DeviceConstraint):
