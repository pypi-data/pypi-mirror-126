# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['LinkedStorageAccountArgs', 'LinkedStorageAccount']

@pulumi.input_type
class LinkedStorageAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 data_source_type: Optional[pulumi.Input[str]] = None,
                 storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LinkedStorageAccount resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to get. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of the Log Analytics Workspace that will contain the resource.
        :param pulumi.Input[str] data_source_type: Linked storage accounts type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_ids: Linked storage accounts resources ids.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if data_source_type is not None:
            pulumi.set(__self__, "data_source_type", data_source_type)
        if storage_account_ids is not None:
            pulumi.set(__self__, "storage_account_ids", storage_account_ids)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to get. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of the Log Analytics Workspace that will contain the resource.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> Optional[pulumi.Input[str]]:
        """
        Linked storage accounts type.
        """
        return pulumi.get(self, "data_source_type")

    @data_source_type.setter
    def data_source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_source_type", value)

    @property
    @pulumi.getter(name="storageAccountIds")
    def storage_account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Linked storage accounts resources ids.
        """
        return pulumi.get(self, "storage_account_ids")

    @storage_account_ids.setter
    def storage_account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "storage_account_ids", value)


class LinkedStorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Linked storage accounts top level resource container.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_source_type: Linked storage accounts type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to get. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_ids: Linked storage accounts resources ids.
        :param pulumi.Input[str] workspace_name: Name of the Log Analytics Workspace that will contain the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkedStorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Linked storage accounts top level resource container.

        :param str resource_name: The name of the resource.
        :param LinkedStorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkedStorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkedStorageAccountArgs.__new__(LinkedStorageAccountArgs)

            __props__.__dict__["data_source_type"] = data_source_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_account_ids"] = storage_account_ids
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:operationalinsights/v20190801preview:LinkedStorageAccount"), pulumi.Alias(type_="azure-native:operationalinsights:LinkedStorageAccount"), pulumi.Alias(type_="azure-nextgen:operationalinsights:LinkedStorageAccount"), pulumi.Alias(type_="azure-native:operationalinsights/v20200301preview:LinkedStorageAccount"), pulumi.Alias(type_="azure-nextgen:operationalinsights/v20200301preview:LinkedStorageAccount"), pulumi.Alias(type_="azure-native:operationalinsights/v20200801:LinkedStorageAccount"), pulumi.Alias(type_="azure-nextgen:operationalinsights/v20200801:LinkedStorageAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LinkedStorageAccount, __self__).__init__(
            'azure-native:operationalinsights/v20190801preview:LinkedStorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LinkedStorageAccount':
        """
        Get an existing LinkedStorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkedStorageAccountArgs.__new__(LinkedStorageAccountArgs)

        __props__.__dict__["data_source_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_account_ids"] = None
        __props__.__dict__["type"] = None
        return LinkedStorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> pulumi.Output[str]:
        """
        Linked storage accounts type.
        """
        return pulumi.get(self, "data_source_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountIds")
    def storage_account_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Linked storage accounts resources ids.
        """
        return pulumi.get(self, "storage_account_ids")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

