# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['IotHubResourceArgs', 'IotHubResource']

@pulumi.input_type
class IotHubResourceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['IotHubSkuInfoArgs'],
                 etag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['IotHubPropertiesArgs']] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IotHubResource resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT hub.
        :param pulumi.Input['IotHubSkuInfoArgs'] sku: IotHub SKU info
        :param pulumi.Input[str] etag: The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input['IotHubPropertiesArgs'] properties: IotHub properties
        :param pulumi.Input[str] resource_name: The name of the IoT hub.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the IoT hub.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['IotHubSkuInfoArgs']:
        """
        IotHub SKU info
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['IotHubSkuInfoArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['IotHubPropertiesArgs']]:
        """
        IotHub properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['IotHubPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IoT hub.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class IotHubResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['IotHubPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['IotHubSkuInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The description of the IoT hub.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[pulumi.InputType['IotHubPropertiesArgs']] properties: IotHub properties
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT hub.
        :param pulumi.Input[str] resource_name_: The name of the IoT hub.
        :param pulumi.Input[pulumi.InputType['IotHubSkuInfoArgs']] sku: IotHub SKU info
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotHubResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The description of the IoT hub.

        :param str resource_name: The name of the resource.
        :param IotHubResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotHubResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['IotHubPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['IotHubSkuInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = IotHubResourceArgs.__new__(IotHubResourceArgs)

            __props__.__dict__["etag"] = etag
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:devices/v20181201preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20160203:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20160203:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20170119:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20170119:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20170701:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20170701:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20180122:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20180122:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20180401:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20180401:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20190322:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20190322:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20190322preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20190322preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20190701preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20190701preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20191104:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20191104:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200301:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200301:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200401:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200401:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200615:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200615:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200710preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200710preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200801:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200801:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200831:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200831:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20200831preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20200831preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20210201preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20210201preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20210303preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20210303preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20210331:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20210331:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20210701:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20210701:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20210701preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20210701preview:IotHubResource"), pulumi.Alias(type_="azure-native:devices/v20210702preview:IotHubResource"), pulumi.Alias(type_="azure-nextgen:devices/v20210702preview:IotHubResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotHubResource, __self__).__init__(
            'azure-native:devices/v20181201preview:IotHubResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotHubResource':
        """
        Get an existing IotHubResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotHubResourceArgs.__new__(IotHubResourceArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IotHubResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.IotHubPropertiesResponse']:
        """
        IotHub properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.IotHubSkuInfoResponse']:
        """
        IotHub SKU info
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

