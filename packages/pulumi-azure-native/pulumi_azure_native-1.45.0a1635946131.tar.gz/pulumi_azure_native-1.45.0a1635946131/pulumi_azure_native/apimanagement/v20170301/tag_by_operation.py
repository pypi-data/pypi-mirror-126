# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['TagByOperationArgs', 'TagByOperation']

@pulumi.input_type
class TagByOperationArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 operation_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 tag_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TagByOperation resource.
        :param pulumi.Input[str] api_id: API identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] tag_id: Tag identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "operation_id", operation_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if tag_id is not None:
            pulumi.set(__self__, "tag_id", tag_id)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Input[str]:
        """
        Operation identifier within an API. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "operation_id", value)

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
    @pulumi.getter(name="tagId")
    def tag_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tag identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "tag_id")

    @tag_id.setter
    def tag_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_id", value)


class TagByOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Tag Contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: API identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] tag_id: Tag identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagByOperationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Tag Contract details.

        :param str resource_name: The name of the resource.
        :param TagByOperationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagByOperationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = TagByOperationArgs.__new__(TagByOperationArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            if operation_id is None and not opts.urn:
                raise TypeError("Missing required property 'operation_id'")
            __props__.__dict__["operation_id"] = operation_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["tag_id"] = tag_id
            __props__.__dict__["display_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:TagByOperation"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:TagByOperation"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:TagByOperation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TagByOperation, __self__).__init__(
            'azure-native:apimanagement/v20170301:TagByOperation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TagByOperation':
        """
        Get an existing TagByOperation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagByOperationArgs.__new__(TagByOperationArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return TagByOperation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Tag name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

