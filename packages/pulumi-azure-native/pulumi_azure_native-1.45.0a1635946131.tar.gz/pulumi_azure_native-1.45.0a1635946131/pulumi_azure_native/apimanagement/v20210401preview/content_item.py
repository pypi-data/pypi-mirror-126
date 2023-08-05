# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ContentItemArgs', 'ContentItem']

@pulumi.input_type
class ContentItemArgs:
    def __init__(__self__, *,
                 content_type_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 content_item_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ContentItem resource.
        :param pulumi.Input[str] content_type_id: Content type identifier.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] content_item_id: Content item identifier.
        """
        pulumi.set(__self__, "content_type_id", content_type_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if content_item_id is not None:
            pulumi.set(__self__, "content_item_id", content_item_id)

    @property
    @pulumi.getter(name="contentTypeId")
    def content_type_id(self) -> pulumi.Input[str]:
        """
        Content type identifier.
        """
        return pulumi.get(self, "content_type_id")

    @content_type_id.setter
    def content_type_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "content_type_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="contentItemId")
    def content_item_id(self) -> Optional[pulumi.Input[str]]:
        """
        Content item identifier.
        """
        return pulumi.get(self, "content_item_id")

    @content_item_id.setter
    def content_item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_item_id", value)


class ContentItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_item_id: Optional[pulumi.Input[str]] = None,
                 content_type_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Content type contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content_item_id: Content item identifier.
        :param pulumi.Input[str] content_type_id: Content type identifier.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContentItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Content type contract details.

        :param str resource_name: The name of the resource.
        :param ContentItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContentItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_item_id: Optional[pulumi.Input[str]] = None,
                 content_type_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ContentItemArgs.__new__(ContentItemArgs)

            __props__.__dict__["content_item_id"] = content_item_id
            if content_type_id is None and not opts.urn:
                raise TypeError("Missing required property 'content_type_id'")
            __props__.__dict__["content_type_id"] = content_type_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:ContentItem"), pulumi.Alias(type_="azure-native:apimanagement:ContentItem"), pulumi.Alias(type_="azure-nextgen:apimanagement:ContentItem"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ContentItem"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:ContentItem"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ContentItem"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:ContentItem"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ContentItem"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:ContentItem"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ContentItem"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:ContentItem"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ContentItem"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:ContentItem")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ContentItem, __self__).__init__(
            'azure-native:apimanagement/v20210401preview:ContentItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContentItem':
        """
        Get an existing ContentItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContentItemArgs.__new__(ContentItemArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return ContentItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Properties of the content item.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

