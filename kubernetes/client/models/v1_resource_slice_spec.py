    The version of the OpenAPI document: release-1.35
class V1ResourceSliceSpec(object):
        'devices': 'list[V1Device]',
        'pool': 'V1ResourcePool',
        'shared_counters': 'list[V1CounterSet]'
        """V1ResourceSliceSpec - a model defined in OpenAPI"""  # noqa: E501
        """Gets the all_nodes of this V1ResourceSliceSpec.  # noqa: E501
        :return: The all_nodes of this V1ResourceSliceSpec.  # noqa: E501
        """Sets the all_nodes of this V1ResourceSliceSpec.
        :param all_nodes: The all_nodes of this V1ResourceSliceSpec.  # noqa: E501
        """Gets the devices of this V1ResourceSliceSpec.  # noqa: E501
        Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.  Only one of Devices and SharedCounters can be set in a ResourceSlice.  # noqa: E501
        :return: The devices of this V1ResourceSliceSpec.  # noqa: E501
        :rtype: list[V1Device]
        """Sets the devices of this V1ResourceSliceSpec.
        Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.  Only one of Devices and SharedCounters can be set in a ResourceSlice.  # noqa: E501
        :param devices: The devices of this V1ResourceSliceSpec.  # noqa: E501
        :type: list[V1Device]
        """Gets the driver of this V1ResourceSliceSpec.  # noqa: E501
        Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. This field is immutable.  # noqa: E501
        :return: The driver of this V1ResourceSliceSpec.  # noqa: E501
        """Sets the driver of this V1ResourceSliceSpec.
        Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. This field is immutable.  # noqa: E501
        :param driver: The driver of this V1ResourceSliceSpec.  # noqa: E501
        """Gets the node_name of this V1ResourceSliceSpec.  # noqa: E501
        :return: The node_name of this V1ResourceSliceSpec.  # noqa: E501
        """Sets the node_name of this V1ResourceSliceSpec.
        :param node_name: The node_name of this V1ResourceSliceSpec.  # noqa: E501
        """Gets the node_selector of this V1ResourceSliceSpec.  # noqa: E501
        :return: The node_selector of this V1ResourceSliceSpec.  # noqa: E501
        """Sets the node_selector of this V1ResourceSliceSpec.
        :param node_selector: The node_selector of this V1ResourceSliceSpec.  # noqa: E501
        """Gets the per_device_node_selection of this V1ResourceSliceSpec.  # noqa: E501
        :return: The per_device_node_selection of this V1ResourceSliceSpec.  # noqa: E501
        """Sets the per_device_node_selection of this V1ResourceSliceSpec.
        :param per_device_node_selection: The per_device_node_selection of this V1ResourceSliceSpec.  # noqa: E501
        """Gets the pool of this V1ResourceSliceSpec.  # noqa: E501
        :return: The pool of this V1ResourceSliceSpec.  # noqa: E501
        :rtype: V1ResourcePool
        """Sets the pool of this V1ResourceSliceSpec.
        :param pool: The pool of this V1ResourceSliceSpec.  # noqa: E501
        :type: V1ResourcePool
        """Gets the shared_counters of this V1ResourceSliceSpec.  # noqa: E501
        SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.  The names of the counter sets must be unique in the ResourcePool.  Only one of Devices and SharedCounters can be set in a ResourceSlice.  The maximum number of counter sets is 8.  # noqa: E501
        :return: The shared_counters of this V1ResourceSliceSpec.  # noqa: E501
        :rtype: list[V1CounterSet]
        """Sets the shared_counters of this V1ResourceSliceSpec.
        SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.  The names of the counter sets must be unique in the ResourcePool.  Only one of Devices and SharedCounters can be set in a ResourceSlice.  The maximum number of counter sets is 8.  # noqa: E501
        :param shared_counters: The shared_counters of this V1ResourceSliceSpec.  # noqa: E501
        :type: list[V1CounterSet]
        if not isinstance(other, V1ResourceSliceSpec):
        if not isinstance(other, V1ResourceSliceSpec):
