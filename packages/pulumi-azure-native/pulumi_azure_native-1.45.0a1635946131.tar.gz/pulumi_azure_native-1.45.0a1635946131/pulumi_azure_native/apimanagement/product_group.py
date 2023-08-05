# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProductGroupArgs', 'ProductGroup']

@pulumi.input_type
class ProductGroupArgs:
    def __init__(__self__, *,
                 product_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 group_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProductGroup resource.
        :param pulumi.Input[str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] group_id: Group identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)

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
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Group identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)


class ProductGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Contract details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: Group identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] product_id: Product identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProductGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contract details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param ProductGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProductGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProductGroupArgs.__new__(ProductGroupArgs)

            __props__.__dict__["group_id"] = group_id
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["built_in"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["external_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:ProductGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ProductGroup"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:ProductGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProductGroup, __self__).__init__(
            'azure-native:apimanagement:ProductGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProductGroup':
        """
        Get an existing ProductGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProductGroupArgs.__new__(ProductGroupArgs)

        __props__.__dict__["built_in"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["external_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ProductGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="builtIn")
    def built_in(self) -> pulumi.Output[bool]:
        """
        true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.
        """
        return pulumi.get(self, "built_in")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Group description. Can contain HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Group name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[Optional[str]]:
        """
        For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.
        """
        return pulumi.get(self, "external_id")

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

