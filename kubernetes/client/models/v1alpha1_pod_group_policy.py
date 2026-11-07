    The version of the OpenAPI document: release-1.35
class V1alpha1PodGroupPolicy(object):
        'basic': 'object',
        'gang': 'V1alpha1GangSchedulingPolicy'
        'gang': 'gang'
    def __init__(self, basic=None, gang=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1PodGroupPolicy - a model defined in OpenAPI"""  # noqa: E501
        self._gang = None
        if gang is not None:
            self.gang = gang
        """Gets the basic of this V1alpha1PodGroupPolicy.  # noqa: E501
        Basic specifies that the pods in this group should be scheduled using standard Kubernetes scheduling behavior.  # noqa: E501
        :return: The basic of this V1alpha1PodGroupPolicy.  # noqa: E501
        :rtype: object
        """Sets the basic of this V1alpha1PodGroupPolicy.
        Basic specifies that the pods in this group should be scheduled using standard Kubernetes scheduling behavior.  # noqa: E501
        :param basic: The basic of this V1alpha1PodGroupPolicy.  # noqa: E501
        :type: object
    def gang(self):
        """Gets the gang of this V1alpha1PodGroupPolicy.  # noqa: E501
        :return: The gang of this V1alpha1PodGroupPolicy.  # noqa: E501
        :rtype: V1alpha1GangSchedulingPolicy
        return self._gang
    @gang.setter
    def gang(self, gang):
        """Sets the gang of this V1alpha1PodGroupPolicy.
        :param gang: The gang of this V1alpha1PodGroupPolicy.  # noqa: E501
        :type: V1alpha1GangSchedulingPolicy
        self._gang = gang
        if not isinstance(other, V1alpha1PodGroupPolicy):
        if not isinstance(other, V1alpha1PodGroupPolicy):
