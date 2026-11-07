    The version of the OpenAPI document: release-1.35
class V1DeviceCounterConsumption(object):
        'counters': 'dict(str, V1Counter)'
        """V1DeviceCounterConsumption - a model defined in OpenAPI"""  # noqa: E501
        """Gets the counter_set of this V1DeviceCounterConsumption.  # noqa: E501
        CounterSet is the name of the set from which the counters defined will be consumed.  # noqa: E501
        :return: The counter_set of this V1DeviceCounterConsumption.  # noqa: E501
        """Sets the counter_set of this V1DeviceCounterConsumption.
        CounterSet is the name of the set from which the counters defined will be consumed.  # noqa: E501
        :param counter_set: The counter_set of this V1DeviceCounterConsumption.  # noqa: E501
        """Gets the counters of this V1DeviceCounterConsumption.  # noqa: E501
        Counters defines the counters that will be consumed by the device.  The maximum number of counters is 32.  # noqa: E501
        :return: The counters of this V1DeviceCounterConsumption.  # noqa: E501
        :rtype: dict(str, V1Counter)
        """Sets the counters of this V1DeviceCounterConsumption.
        Counters defines the counters that will be consumed by the device.  The maximum number of counters is 32.  # noqa: E501
        :param counters: The counters of this V1DeviceCounterConsumption.  # noqa: E501
        :type: dict(str, V1Counter)
        if not isinstance(other, V1DeviceCounterConsumption):
        if not isinstance(other, V1DeviceCounterConsumption):
