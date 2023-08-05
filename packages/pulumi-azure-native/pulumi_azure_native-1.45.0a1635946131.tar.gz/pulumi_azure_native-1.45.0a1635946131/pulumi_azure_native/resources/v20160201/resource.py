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

__all__ = ['ResourceArgs', 'Resource']

@pulumi.input_type
class ResourceArgs:
    def __init__(__self__, *,
                 parent_resource_path: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_provider_namespace: pulumi.Input[str],
                 resource_type: pulumi.Input[str],
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_by: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['PlanArgs']] = None,
                 properties: Optional[Any] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Resource resource.
        :param pulumi.Input[str] parent_resource_path: Resource identity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_provider_namespace: Resource identity.
        :param pulumi.Input[str] resource_type: Resource identity.
        :param pulumi.Input['IdentityArgs'] identity: The identity of the resource.
        :param pulumi.Input[str] kind: The kind of the resource.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] managed_by: Id of the resource that manages this resource.
        :param pulumi.Input['PlanArgs'] plan: The plan of the resource.
        :param Any properties: The resource properties.
        :param pulumi.Input[str] resource_name: Resource identity.
        :param pulumi.Input['SkuArgs'] sku: The sku of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "parent_resource_path", parent_resource_path)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_provider_namespace", resource_provider_namespace)
        pulumi.set(__self__, "resource_type", resource_type)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_by is not None:
            pulumi.set(__self__, "managed_by", managed_by)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="parentResourcePath")
    def parent_resource_path(self) -> pulumi.Input[str]:
        """
        Resource identity.
        """
        return pulumi.get(self, "parent_resource_path")

    @parent_resource_path.setter
    def parent_resource_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_path", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceProviderNamespace")
    def resource_provider_namespace(self) -> pulumi.Input[str]:
        """
        Resource identity.
        """
        return pulumi.get(self, "resource_provider_namespace")

    @resource_provider_namespace.setter
    def resource_provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_provider_namespace", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        Resource identity.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the resource that manages this resource.
        """
        return pulumi.get(self, "managed_by")

    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_by", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['PlanArgs']]:
        """
        The plan of the resource.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['PlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[Any]:
        """
        The resource properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[Any]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource identity.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The sku of the resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Resource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_by: Optional[pulumi.Input[str]] = None,
                 parent_resource_path: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PlanArgs']]] = None,
                 properties: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_provider_namespace: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The identity of the resource.
        :param pulumi.Input[str] kind: The kind of the resource.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] managed_by: Id of the resource that manages this resource.
        :param pulumi.Input[str] parent_resource_path: Resource identity.
        :param pulumi.Input[pulumi.InputType['PlanArgs']] plan: The plan of the resource.
        :param Any properties: The resource properties.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: Resource identity.
        :param pulumi.Input[str] resource_provider_namespace: Resource identity.
        :param pulumi.Input[str] resource_type: Resource identity.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource information.

        :param str resource_name: The name of the resource.
        :param ResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_by: Optional[pulumi.Input[str]] = None,
                 parent_resource_path: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PlanArgs']]] = None,
                 properties: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_provider_namespace: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
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
            __props__ = ResourceArgs.__new__(ResourceArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_by"] = managed_by
            if parent_resource_path is None and not opts.urn:
                raise TypeError("Missing required property 'parent_resource_path'")
            __props__.__dict__["parent_resource_path"] = parent_resource_path
            __props__.__dict__["plan"] = plan
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            if resource_provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'resource_provider_namespace'")
            __props__.__dict__["resource_provider_namespace"] = resource_provider_namespace
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:resources/v20160201:Resource"), pulumi.Alias(type_="azure-native:resources:Resource"), pulumi.Alias(type_="azure-nextgen:resources:Resource"), pulumi.Alias(type_="azure-native:resources/v20151101:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20151101:Resource"), pulumi.Alias(type_="azure-native:resources/v20160701:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20160701:Resource"), pulumi.Alias(type_="azure-native:resources/v20160901:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20160901:Resource"), pulumi.Alias(type_="azure-native:resources/v20170510:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20170510:Resource"), pulumi.Alias(type_="azure-native:resources/v20180201:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20180201:Resource"), pulumi.Alias(type_="azure-native:resources/v20180501:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20180501:Resource"), pulumi.Alias(type_="azure-native:resources/v20190301:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20190301:Resource"), pulumi.Alias(type_="azure-native:resources/v20190501:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20190501:Resource"), pulumi.Alias(type_="azure-native:resources/v20190510:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20190510:Resource"), pulumi.Alias(type_="azure-native:resources/v20190701:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20190701:Resource"), pulumi.Alias(type_="azure-native:resources/v20190801:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20190801:Resource"), pulumi.Alias(type_="azure-native:resources/v20191001:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20191001:Resource"), pulumi.Alias(type_="azure-native:resources/v20200601:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20200601:Resource"), pulumi.Alias(type_="azure-native:resources/v20200801:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20200801:Resource"), pulumi.Alias(type_="azure-native:resources/v20201001:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20201001:Resource"), pulumi.Alias(type_="azure-native:resources/v20210101:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20210101:Resource"), pulumi.Alias(type_="azure-native:resources/v20210401:Resource"), pulumi.Alias(type_="azure-nextgen:resources/v20210401:Resource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Resource, __self__).__init__(
            'azure-native:resources/v20160201:Resource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Resource':
        """
        Get an existing Resource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceArgs.__new__(ResourceArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_by"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["plan"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Resource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[str]]:
        """
        Id of the resource that manages this resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional['outputs.PlanResponse']]:
        """
        The plan of the resource.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        The resource properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

