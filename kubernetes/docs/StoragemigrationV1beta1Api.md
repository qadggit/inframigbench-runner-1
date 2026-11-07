# kubernetes.client.StoragemigrationV1beta1Api
[**create_storage_version_migration**](StoragemigrationV1beta1Api.md#create_storage_version_migration) | **POST** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations | 
[**delete_collection_storage_version_migration**](StoragemigrationV1beta1Api.md#delete_collection_storage_version_migration) | **DELETE** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations | 
[**delete_storage_version_migration**](StoragemigrationV1beta1Api.md#delete_storage_version_migration) | **DELETE** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name} | 
[**get_api_resources**](StoragemigrationV1beta1Api.md#get_api_resources) | **GET** /apis/storagemigration.k8s.io/v1beta1/ | 
[**list_storage_version_migration**](StoragemigrationV1beta1Api.md#list_storage_version_migration) | **GET** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations | 
[**patch_storage_version_migration**](StoragemigrationV1beta1Api.md#patch_storage_version_migration) | **PATCH** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name} | 
[**patch_storage_version_migration_status**](StoragemigrationV1beta1Api.md#patch_storage_version_migration_status) | **PATCH** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name}/status | 
[**read_storage_version_migration**](StoragemigrationV1beta1Api.md#read_storage_version_migration) | **GET** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name} | 
[**read_storage_version_migration_status**](StoragemigrationV1beta1Api.md#read_storage_version_migration_status) | **GET** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name}/status | 
[**replace_storage_version_migration**](StoragemigrationV1beta1Api.md#replace_storage_version_migration) | **PUT** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name} | 
[**replace_storage_version_migration_status**](StoragemigrationV1beta1Api.md#replace_storage_version_migration_status) | **PUT** /apis/storagemigration.k8s.io/v1beta1/storageversionmigrations/{name}/status | 
> V1beta1StorageVersionMigration create_storage_version_migration(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
    body = kubernetes.client.V1beta1StorageVersionMigration() # V1beta1StorageVersionMigration | 
        print("Exception when calling StoragemigrationV1beta1Api->create_storage_version_migration: %s\n" % e)
 **body** | [**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)|  | 
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->delete_collection_storage_version_migration: %s\n" % e)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->delete_storage_version_migration: %s\n" % e)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->get_api_resources: %s\n" % e)
> V1beta1StorageVersionMigrationList list_storage_version_migration(pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, resource_version_match=resource_version_match, send_initial_events=send_initial_events, timeout_seconds=timeout_seconds, watch=watch)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->list_storage_version_migration: %s\n" % e)
[**V1beta1StorageVersionMigrationList**](V1beta1StorageVersionMigrationList.md)
> V1beta1StorageVersionMigration patch_storage_version_migration(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation, force=force)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->patch_storage_version_migration: %s\n" % e)
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
> V1beta1StorageVersionMigration patch_storage_version_migration_status(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation, force=force)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->patch_storage_version_migration_status: %s\n" % e)
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
> V1beta1StorageVersionMigration read_storage_version_migration(name, pretty=pretty)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->read_storage_version_migration: %s\n" % e)
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
> V1beta1StorageVersionMigration read_storage_version_migration_status(name, pretty=pretty)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
        print("Exception when calling StoragemigrationV1beta1Api->read_storage_version_migration_status: %s\n" % e)
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
> V1beta1StorageVersionMigration replace_storage_version_migration(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
body = kubernetes.client.V1beta1StorageVersionMigration() # V1beta1StorageVersionMigration | 
        print("Exception when calling StoragemigrationV1beta1Api->replace_storage_version_migration: %s\n" % e)
 **body** | [**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)|  | 
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
> V1beta1StorageVersionMigration replace_storage_version_migration_status(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation)
    api_instance = kubernetes.client.StoragemigrationV1beta1Api(api_client)
body = kubernetes.client.V1beta1StorageVersionMigration() # V1beta1StorageVersionMigration | 
        print("Exception when calling StoragemigrationV1beta1Api->replace_storage_version_migration_status: %s\n" % e)
 **body** | [**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)|  | 
[**V1beta1StorageVersionMigration**](V1beta1StorageVersionMigration.md)
