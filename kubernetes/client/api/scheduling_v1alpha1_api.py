    The version of the OpenAPI document: release-1.35
class SchedulingV1alpha1Api(object):
    def create_namespaced_workload(self, namespace, body, **kwargs):  # noqa: E501
        """create_namespaced_workload  # noqa: E501
        create a Workload  # noqa: E501
        >>> thread = api.create_namespaced_workload(namespace, body, async_req=True)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param V1alpha1Workload body: (required)
        :return: V1alpha1Workload
        return self.create_namespaced_workload_with_http_info(namespace, body, **kwargs)  # noqa: E501
    def create_namespaced_workload_with_http_info(self, namespace, body, **kwargs):  # noqa: E501
        """create_namespaced_workload  # noqa: E501
        create a Workload  # noqa: E501
        >>> thread = api.create_namespaced_workload_with_http_info(namespace, body, async_req=True)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param V1alpha1Workload body: (required)
        :return: tuple(V1alpha1Workload, status_code(int), headers(HTTPHeaderDict))
            'namespace',
                    " to method create_namespaced_workload" % key
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `create_namespaced_workload`")  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `create_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads', 'POST',
            response_type='V1alpha1Workload',  # noqa: E501
    def delete_collection_namespaced_workload(self, namespace, **kwargs):  # noqa: E501
        """delete_collection_namespaced_workload  # noqa: E501
        delete collection of Workload  # noqa: E501
        >>> thread = api.delete_collection_namespaced_workload(namespace, async_req=True)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        return self.delete_collection_namespaced_workload_with_http_info(namespace, **kwargs)  # noqa: E501
    def delete_collection_namespaced_workload_with_http_info(self, namespace, **kwargs):  # noqa: E501
        """delete_collection_namespaced_workload  # noqa: E501
        delete collection of Workload  # noqa: E501
        >>> thread = api.delete_collection_namespaced_workload_with_http_info(namespace, async_req=True)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
            'namespace',
                    " to method delete_collection_namespaced_workload" % key
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `delete_collection_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads', 'DELETE',
    def delete_namespaced_workload(self, name, namespace, **kwargs):  # noqa: E501
        """delete_namespaced_workload  # noqa: E501
        delete a Workload  # noqa: E501
        >>> thread = api.delete_namespaced_workload(name, namespace, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: V1Status
        return self.delete_namespaced_workload_with_http_info(name, namespace, **kwargs)  # noqa: E501
    def delete_namespaced_workload_with_http_info(self, name, namespace, **kwargs):  # noqa: E501
        """delete_namespaced_workload  # noqa: E501
        delete a Workload  # noqa: E501
        >>> thread = api.delete_namespaced_workload_with_http_info(name, namespace, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: tuple(V1Status, status_code(int), headers(HTTPHeaderDict))
            'namespace',
                    " to method delete_namespaced_workload" % key
            raise ApiValueError("Missing the required parameter `name` when calling `delete_namespaced_workload`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `delete_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads/{name}', 'DELETE',
            response_type='V1Status',  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/', 'GET',
    def list_namespaced_workload(self, namespace, **kwargs):  # noqa: E501
        """list_namespaced_workload  # noqa: E501
        list or watch objects of kind Workload  # noqa: E501
        >>> thread = api.list_namespaced_workload(namespace, async_req=True)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: V1alpha1WorkloadList
        return self.list_namespaced_workload_with_http_info(namespace, **kwargs)  # noqa: E501
    def list_namespaced_workload_with_http_info(self, namespace, **kwargs):  # noqa: E501
        """list_namespaced_workload  # noqa: E501
        list or watch objects of kind Workload  # noqa: E501
        >>> thread = api.list_namespaced_workload_with_http_info(namespace, async_req=True)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: tuple(V1alpha1WorkloadList, status_code(int), headers(HTTPHeaderDict))
            'namespace',
                    " to method list_namespaced_workload" % key
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `list_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1WorkloadList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_workload_for_all_namespaces(self, **kwargs):  # noqa: E501
        """list_workload_for_all_namespaces  # noqa: E501

        list or watch objects of kind Workload  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_workload_for_all_namespaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool allow_watch_bookmarks: allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.
        :param str _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
        :param str field_selector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
        :param str label_selector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
        :param int limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
        :param str pretty: If 'true', then the output is pretty printed. Defaults to 'false' unless the user-agent indicates a browser or command-line HTTP tool (curl and wget).
        :param str resource_version: resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset
        :param str resource_version_match: resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset
        :param bool send_initial_events: `sendInitialEvents=true` may be set together with `watch=true`. In that case, the watch stream will begin with synthetic events to produce the current state of objects in the collection. Once all such events have been sent, a synthetic \"Bookmark\" event  will be sent. The bookmark will report the ResourceVersion (RV) corresponding to the set of objects, and be marked with `\"k8s.io/initial-events-end\": \"true\"` annotation. Afterwards, the watch stream will proceed as usual, sending watch events corresponding to changes (subsequent to the RV) to objects watched.  When `sendInitialEvents` option is set, we require `resourceVersionMatch` option to also be set. The semantic of the watch request is as following: - `resourceVersionMatch` = NotOlderThan   is interpreted as \"data at least as new as the provided `resourceVersion`\"   and the bookmark event is send when the state is synced   to a `resourceVersion` at least as fresh as the one provided by the ListOptions.   If `resourceVersion` is unset, this is interpreted as \"consistent read\" and the   bookmark event is send when the state is synced at least to the moment   when request started being processed. - `resourceVersionMatch` set to any other value or unset   Invalid error is returned.  Defaults to true if `resourceVersion=\"\"` or `resourceVersion=\"0\"` (for backward compatibility reasons) and to false otherwise.
        :param int timeout_seconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1alpha1WorkloadList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_workload_for_all_namespaces_with_http_info(**kwargs)  # noqa: E501

    def list_workload_for_all_namespaces_with_http_info(self, **kwargs):  # noqa: E501
        """list_workload_for_all_namespaces  # noqa: E501

        list or watch objects of kind Workload  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_workload_for_all_namespaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool allow_watch_bookmarks: allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.
        :param str _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
        :param str field_selector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
        :param str label_selector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
        :param int limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
        :param str pretty: If 'true', then the output is pretty printed. Defaults to 'false' unless the user-agent indicates a browser or command-line HTTP tool (curl and wget).
        :param str resource_version: resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset
        :param str resource_version_match: resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset
        :param bool send_initial_events: `sendInitialEvents=true` may be set together with `watch=true`. In that case, the watch stream will begin with synthetic events to produce the current state of objects in the collection. Once all such events have been sent, a synthetic \"Bookmark\" event  will be sent. The bookmark will report the ResourceVersion (RV) corresponding to the set of objects, and be marked with `\"k8s.io/initial-events-end\": \"true\"` annotation. Afterwards, the watch stream will proceed as usual, sending watch events corresponding to changes (subsequent to the RV) to objects watched.  When `sendInitialEvents` option is set, we require `resourceVersionMatch` option to also be set. The semantic of the watch request is as following: - `resourceVersionMatch` = NotOlderThan   is interpreted as \"data at least as new as the provided `resourceVersion`\"   and the bookmark event is send when the state is synced   to a `resourceVersion` at least as fresh as the one provided by the ListOptions.   If `resourceVersion` is unset, this is interpreted as \"consistent read\" and the   bookmark event is send when the state is synced at least to the moment   when request started being processed. - `resourceVersionMatch` set to any other value or unset   Invalid error is returned.  Defaults to true if `resourceVersion=\"\"` or `resourceVersion=\"0\"` (for backward compatibility reasons) and to false otherwise.
        :param int timeout_seconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
        :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1alpha1WorkloadList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'allow_watch_bookmarks',
            '_continue',
            'field_selector',
            'label_selector',
            'limit',
            'pretty',
            'resource_version',
            'resource_version_match',
            'send_initial_events',
            'timeout_seconds',
            'watch'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_workload_for_all_namespaces" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'allow_watch_bookmarks' in local_var_params and local_var_params['allow_watch_bookmarks'] is not None:  # noqa: E501
            query_params.append(('allowWatchBookmarks', local_var_params['allow_watch_bookmarks']))  # noqa: E501
        if '_continue' in local_var_params and local_var_params['_continue'] is not None:  # noqa: E501
            query_params.append(('continue', local_var_params['_continue']))  # noqa: E501
        if 'field_selector' in local_var_params and local_var_params['field_selector'] is not None:  # noqa: E501
            query_params.append(('fieldSelector', local_var_params['field_selector']))  # noqa: E501
        if 'label_selector' in local_var_params and local_var_params['label_selector'] is not None:  # noqa: E501
            query_params.append(('labelSelector', local_var_params['label_selector']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'resource_version' in local_var_params and local_var_params['resource_version'] is not None:  # noqa: E501
            query_params.append(('resourceVersion', local_var_params['resource_version']))  # noqa: E501
        if 'resource_version_match' in local_var_params and local_var_params['resource_version_match'] is not None:  # noqa: E501
            query_params.append(('resourceVersionMatch', local_var_params['resource_version_match']))  # noqa: E501
        if 'send_initial_events' in local_var_params and local_var_params['send_initial_events'] is not None:  # noqa: E501
            query_params.append(('sendInitialEvents', local_var_params['send_initial_events']))  # noqa: E501
        if 'timeout_seconds' in local_var_params and local_var_params['timeout_seconds'] is not None:  # noqa: E501
            query_params.append(('timeoutSeconds', local_var_params['timeout_seconds']))  # noqa: E501
        if 'watch' in local_var_params and local_var_params['watch'] is not None:  # noqa: E501
            query_params.append(('watch', local_var_params['watch']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/cbor', 'application/json;stream=watch', 'application/vnd.kubernetes.protobuf;stream=watch', 'application/cbor-seq'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/scheduling.k8s.io/v1alpha1/workloads', 'GET',
            response_type='V1alpha1WorkloadList',  # noqa: E501
    def patch_namespaced_workload(self, name, namespace, body, **kwargs):  # noqa: E501
        """patch_namespaced_workload  # noqa: E501
        partially update the specified Workload  # noqa: E501
        >>> thread = api.patch_namespaced_workload(name, namespace, body, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: V1alpha1Workload
        return self.patch_namespaced_workload_with_http_info(name, namespace, body, **kwargs)  # noqa: E501
    def patch_namespaced_workload_with_http_info(self, name, namespace, body, **kwargs):  # noqa: E501
        """patch_namespaced_workload  # noqa: E501
        partially update the specified Workload  # noqa: E501
        >>> thread = api.patch_namespaced_workload_with_http_info(name, namespace, body, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: tuple(V1alpha1Workload, status_code(int), headers(HTTPHeaderDict))
            'namespace',
                    " to method patch_namespaced_workload" % key
            raise ApiValueError("Missing the required parameter `name` when calling `patch_namespaced_workload`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `patch_namespaced_workload`")  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `patch_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads/{name}', 'PATCH',
            response_type='V1alpha1Workload',  # noqa: E501
    def read_namespaced_workload(self, name, namespace, **kwargs):  # noqa: E501
        """read_namespaced_workload  # noqa: E501
        read the specified Workload  # noqa: E501
        >>> thread = api.read_namespaced_workload(name, namespace, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: V1alpha1Workload
        return self.read_namespaced_workload_with_http_info(name, namespace, **kwargs)  # noqa: E501
    def read_namespaced_workload_with_http_info(self, name, namespace, **kwargs):  # noqa: E501
        """read_namespaced_workload  # noqa: E501
        read the specified Workload  # noqa: E501
        >>> thread = api.read_namespaced_workload_with_http_info(name, namespace, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :return: tuple(V1alpha1Workload, status_code(int), headers(HTTPHeaderDict))
            'namespace',
                    " to method read_namespaced_workload" % key
            raise ApiValueError("Missing the required parameter `name` when calling `read_namespaced_workload`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `read_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads/{name}', 'GET',
            response_type='V1alpha1Workload',  # noqa: E501
    def replace_namespaced_workload(self, name, namespace, body, **kwargs):  # noqa: E501
        """replace_namespaced_workload  # noqa: E501
        replace the specified Workload  # noqa: E501
        >>> thread = api.replace_namespaced_workload(name, namespace, body, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param V1alpha1Workload body: (required)
        :return: V1alpha1Workload
        return self.replace_namespaced_workload_with_http_info(name, namespace, body, **kwargs)  # noqa: E501
    def replace_namespaced_workload_with_http_info(self, name, namespace, body, **kwargs):  # noqa: E501
        """replace_namespaced_workload  # noqa: E501
        replace the specified Workload  # noqa: E501
        >>> thread = api.replace_namespaced_workload_with_http_info(name, namespace, body, async_req=True)
        :param str name: name of the Workload (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param V1alpha1Workload body: (required)
        :return: tuple(V1alpha1Workload, status_code(int), headers(HTTPHeaderDict))
            'namespace',
                    " to method replace_namespaced_workload" % key
            raise ApiValueError("Missing the required parameter `name` when calling `replace_namespaced_workload`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `replace_namespaced_workload`")  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `replace_namespaced_workload`")  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501
            '/apis/scheduling.k8s.io/v1alpha1/namespaces/{namespace}/workloads/{name}', 'PUT',
            response_type='V1alpha1Workload',  # noqa: E501
