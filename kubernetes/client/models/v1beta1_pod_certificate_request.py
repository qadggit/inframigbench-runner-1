    The version of the OpenAPI document: release-1.35
class V1beta1PodCertificateRequest(object):
        'spec': 'V1beta1PodCertificateRequestSpec',
        'status': 'V1beta1PodCertificateRequestStatus'
        """V1beta1PodCertificateRequest - a model defined in OpenAPI"""  # noqa: E501
        self.spec = spec
        """Gets the api_version of this V1beta1PodCertificateRequest.  # noqa: E501
        :return: The api_version of this V1beta1PodCertificateRequest.  # noqa: E501
        """Sets the api_version of this V1beta1PodCertificateRequest.
        :param api_version: The api_version of this V1beta1PodCertificateRequest.  # noqa: E501
        """Gets the kind of this V1beta1PodCertificateRequest.  # noqa: E501
        :return: The kind of this V1beta1PodCertificateRequest.  # noqa: E501
        """Sets the kind of this V1beta1PodCertificateRequest.
        :param kind: The kind of this V1beta1PodCertificateRequest.  # noqa: E501
        """Gets the metadata of this V1beta1PodCertificateRequest.  # noqa: E501
        :return: The metadata of this V1beta1PodCertificateRequest.  # noqa: E501
        """Sets the metadata of this V1beta1PodCertificateRequest.
        :param metadata: The metadata of this V1beta1PodCertificateRequest.  # noqa: E501
        """Gets the spec of this V1beta1PodCertificateRequest.  # noqa: E501
        :return: The spec of this V1beta1PodCertificateRequest.  # noqa: E501
        :rtype: V1beta1PodCertificateRequestSpec
        """Sets the spec of this V1beta1PodCertificateRequest.
        :param spec: The spec of this V1beta1PodCertificateRequest.  # noqa: E501
        :type: V1beta1PodCertificateRequestSpec
        if self.local_vars_configuration.client_side_validation and spec is None:  # noqa: E501
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501
        """Gets the status of this V1beta1PodCertificateRequest.  # noqa: E501
        :return: The status of this V1beta1PodCertificateRequest.  # noqa: E501
        :rtype: V1beta1PodCertificateRequestStatus
        """Sets the status of this V1beta1PodCertificateRequest.
        :param status: The status of this V1beta1PodCertificateRequest.  # noqa: E501
        :type: V1beta1PodCertificateRequestStatus
        if not isinstance(other, V1beta1PodCertificateRequest):
        if not isinstance(other, V1beta1PodCertificateRequest):
