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

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 created_at: Optional[pulumi.Input[str]] = None,
                 critical: Optional[pulumi.Input[bool]] = None,
                 data_center: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 namespace_type: Optional[pulumi.Input['NamespaceType']] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[str]] = None,
                 service_bus_endpoint: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] created_at: The time the namespace was created.
        :param pulumi.Input[bool] critical: Whether or not the namespace is set as Critical.
        :param pulumi.Input[str] data_center: Data center for the namespace
        :param pulumi.Input[bool] enabled: Whether or not the namespace is currently enabled.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input['NamespaceType'] namespace_type: The namespace type.
        :param pulumi.Input[str] provisioning_state: Provisioning state of the Namespace.
        :param pulumi.Input[str] region: Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe
        :param pulumi.Input[str] scale_unit: ScaleUnit where the namespace gets created
        :param pulumi.Input[str] service_bus_endpoint: Endpoint you can use to perform NotificationHub operations.
        :param pulumi.Input['SkuArgs'] sku: The sku of the created namespace
        :param pulumi.Input[str] status: Status of the namespace. It can be any of these values:1 = Created/Active2 = Creating3 = Suspended4 = Deleting
        :param pulumi.Input[str] subscription_id: The Id of the Azure subscription associated with the namespace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] updated_at: The time the namespace was updated.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if critical is not None:
            pulumi.set(__self__, "critical", critical)
        if data_center is not None:
            pulumi.set(__self__, "data_center", data_center)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if namespace_type is not None:
            pulumi.set(__self__, "namespace_type", namespace_type)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if scale_unit is not None:
            pulumi.set(__self__, "scale_unit", scale_unit)
        if service_bus_endpoint is not None:
            pulumi.set(__self__, "service_bus_endpoint", service_bus_endpoint)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

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
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time the namespace was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def critical(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the namespace is set as Critical.
        """
        return pulumi.get(self, "critical")

    @critical.setter
    def critical(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "critical", value)

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> Optional[pulumi.Input[str]]:
        """
        Data center for the namespace
        """
        return pulumi.get(self, "data_center")

    @data_center.setter
    def data_center(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_center", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the namespace is currently enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace name.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[pulumi.Input['NamespaceType']]:
        """
        The namespace type.
        """
        return pulumi.get(self, "namespace_type")

    @namespace_type.setter
    def namespace_type(self, value: Optional[pulumi.Input['NamespaceType']]):
        pulumi.set(self, "namespace_type", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Provisioning state of the Namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> Optional[pulumi.Input[str]]:
        """
        ScaleUnit where the namespace gets created
        """
        return pulumi.get(self, "scale_unit")

    @scale_unit.setter
    def scale_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scale_unit", value)

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint you can use to perform NotificationHub operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @service_bus_endpoint.setter
    def service_bus_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_bus_endpoint", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the namespace. It can be any of these values:1 = Created/Active2 = Creating3 = Suspended4 = Deleting
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Id of the Azure subscription associated with the namespace.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

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

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 critical: Optional[pulumi.Input[bool]] = None,
                 data_center: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 namespace_type: Optional[pulumi.Input['NamespaceType']] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[str]] = None,
                 service_bus_endpoint: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Description of a Namespace resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The time the namespace was created.
        :param pulumi.Input[bool] critical: Whether or not the namespace is set as Critical.
        :param pulumi.Input[str] data_center: Data center for the namespace
        :param pulumi.Input[bool] enabled: Whether or not the namespace is currently enabled.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input['NamespaceType'] namespace_type: The namespace type.
        :param pulumi.Input[str] provisioning_state: Provisioning state of the Namespace.
        :param pulumi.Input[str] region: Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] scale_unit: ScaleUnit where the namespace gets created
        :param pulumi.Input[str] service_bus_endpoint: Endpoint you can use to perform NotificationHub operations.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku of the created namespace
        :param pulumi.Input[str] status: Status of the namespace. It can be any of these values:1 = Created/Active2 = Creating3 = Suspended4 = Deleting
        :param pulumi.Input[str] subscription_id: The Id of the Azure subscription associated with the namespace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] updated_at: The time the namespace was updated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of a Namespace resource.

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 critical: Optional[pulumi.Input[bool]] = None,
                 data_center: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 namespace_type: Optional[pulumi.Input['NamespaceType']] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[str]] = None,
                 service_bus_endpoint: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
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
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["critical"] = critical
            __props__.__dict__["data_center"] = data_center
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["namespace_type"] = namespace_type
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["region"] = region
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scale_unit"] = scale_unit
            __props__.__dict__["service_bus_endpoint"] = service_bus_endpoint
            __props__.__dict__["sku"] = sku
            __props__.__dict__["status"] = status
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["updated_at"] = updated_at
            __props__.__dict__["metric_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:notificationhubs/v20170401:Namespace"), pulumi.Alias(type_="azure-native:notificationhubs:Namespace"), pulumi.Alias(type_="azure-nextgen:notificationhubs:Namespace"), pulumi.Alias(type_="azure-native:notificationhubs/v20140901:Namespace"), pulumi.Alias(type_="azure-nextgen:notificationhubs/v20140901:Namespace"), pulumi.Alias(type_="azure-native:notificationhubs/v20160301:Namespace"), pulumi.Alias(type_="azure-nextgen:notificationhubs/v20160301:Namespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Namespace, __self__).__init__(
            'azure-native:notificationhubs/v20170401:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceArgs.__new__(NamespaceArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["critical"] = None
        __props__.__dict__["data_center"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metric_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["namespace_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["scale_unit"] = None
        __props__.__dict__["service_bus_endpoint"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subscription_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[str]]:
        """
        The time the namespace was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def critical(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not the namespace is set as Critical.
        """
        return pulumi.get(self, "critical")

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> pulumi.Output[Optional[str]]:
        """
        Data center for the namespace
        """
        return pulumi.get(self, "data_center")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not the namespace is currently enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> pulumi.Output[str]:
        """
        Identifier for Azure Insights metrics
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace type.
        """
        return pulumi.get(self, "namespace_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning state of the Namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> pulumi.Output[Optional[str]]:
        """
        ScaleUnit where the namespace gets created
        """
        return pulumi.get(self, "scale_unit")

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        Endpoint you can use to perform NotificationHub operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the namespace. It can be any of these values:1 = Created/Active2 = Creating3 = Suspended4 = Deleting
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Id of the Azure subscription associated with the namespace.
        """
        return pulumi.get(self, "subscription_id")

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

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[Optional[str]]:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

