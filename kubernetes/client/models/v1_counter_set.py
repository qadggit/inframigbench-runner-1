    The version of the OpenAPI document: release-1.35
class V1CounterSet(object):
        'counters': 'dict(str, V1Counter)',
        """V1CounterSet - a model defined in OpenAPI"""  # noqa: E501
        """Gets the counters of this V1CounterSet.  # noqa: E501
        Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.  The maximum number of counters is 32.  # noqa: E501
        :return: The counters of this V1CounterSet.  # noqa: E501
        :rtype: dict(str, V1Counter)
        """Sets the counters of this V1CounterSet.
        Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.  The maximum number of counters is 32.  # noqa: E501
        :param counters: The counters of this V1CounterSet.  # noqa: E501
        :type: dict(str, V1Counter)
        """Gets the name of this V1CounterSet.  # noqa: E501
        Name defines the name of the counter set. It must be a DNS label.  # noqa: E501
        :return: The name of this V1CounterSet.  # noqa: E501
        """Sets the name of this V1CounterSet.
        Name defines the name of the counter set. It must be a DNS label.  # noqa: E501
        :param name: The name of this V1CounterSet.  # noqa: E501
        if not isinstance(other, V1CounterSet):
        if not isinstance(other, V1CounterSet):
