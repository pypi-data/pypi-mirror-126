# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ProductPolicyArgs', 'ProductPolicy']

@pulumi.input_type
class ProductPolicyArgs:
    def __init__(__self__, *,
                 product_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 value: pulumi.Input[str],
                 format: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProductPolicy resource.
        :param pulumi.Input[str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] value: Contents of the Policy as defined by the format.
        :param pulumi.Input[Union[str, 'PolicyContentFormat']] format: Format of the policyContent.
        :param pulumi.Input[str] policy_id: The identifier of the Policy.
        """
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "value", value)
        if format is None:
            format = 'xml'
        if format is not None:
            pulumi.set(__self__, "format", format)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[str]:
        """
        Product identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_id", value)

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
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Contents of the Policy as defined by the format.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]]:
        """
        Format of the policyContent.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the Policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)


class ProductPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 format: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Policy Contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'PolicyContentFormat']] format: Format of the policyContent.
        :param pulumi.Input[str] policy_id: The identifier of the Policy.
        :param pulumi.Input[str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] value: Contents of the Policy as defined by the format.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProductPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Policy Contract details.

        :param str resource_name: The name of the resource.
        :param ProductPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProductPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 format: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProductPolicyArgs.__new__(ProductPolicyArgs)

            if format is None:
                format = 'xml'
            __props__.__dict__["format"] = format
            __props__.__dict__["policy_id"] = policy_id
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:ProductPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ProductPolicy"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:ProductPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProductPolicy, __self__).__init__(
            'azure-native:apimanagement/v20210801:ProductPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProductPolicy':
        """
        Get an existing ProductPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProductPolicyArgs.__new__(ProductPolicyArgs)

        __props__.__dict__["format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return ProductPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        Format of the policyContent.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        Contents of the Policy as defined by the format.
        """
        return pulumi.get(self, "value")

