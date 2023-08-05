# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['VirtualWanArgs', 'VirtualWan']

@pulumi.input_type
class VirtualWanArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 allow_branch_to_branch_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_vnet_to_vnet_traffic: Optional[pulumi.Input[bool]] = None,
                 disable_vpn_encryption: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 virtual_wan_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualWan resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualWan.
        :param pulumi.Input[bool] allow_branch_to_branch_traffic: True if branch to branch traffic is allowed.
        :param pulumi.Input[bool] allow_vnet_to_vnet_traffic: True if Vnet to Vnet traffic is allowed.
        :param pulumi.Input[bool] disable_vpn_encryption: Vpn encryption to be disabled or not.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] type: The type of the VirtualWAN.
        :param pulumi.Input[str] virtual_wan_name: The name of the VirtualWAN being created or updated.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if allow_branch_to_branch_traffic is not None:
            pulumi.set(__self__, "allow_branch_to_branch_traffic", allow_branch_to_branch_traffic)
        if allow_vnet_to_vnet_traffic is not None:
            pulumi.set(__self__, "allow_vnet_to_vnet_traffic", allow_vnet_to_vnet_traffic)
        if disable_vpn_encryption is not None:
            pulumi.set(__self__, "disable_vpn_encryption", disable_vpn_encryption)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if virtual_wan_name is not None:
            pulumi.set(__self__, "virtual_wan_name", virtual_wan_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the VirtualWan.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        True if branch to branch traffic is allowed.
        """
        return pulumi.get(self, "allow_branch_to_branch_traffic")

    @allow_branch_to_branch_traffic.setter
    def allow_branch_to_branch_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_branch_to_branch_traffic", value)

    @property
    @pulumi.getter(name="allowVnetToVnetTraffic")
    def allow_vnet_to_vnet_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        True if Vnet to Vnet traffic is allowed.
        """
        return pulumi.get(self, "allow_vnet_to_vnet_traffic")

    @allow_vnet_to_vnet_traffic.setter
    def allow_vnet_to_vnet_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_vnet_to_vnet_traffic", value)

    @property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> Optional[pulumi.Input[bool]]:
        """
        Vpn encryption to be disabled or not.
        """
        return pulumi.get(self, "disable_vpn_encryption")

    @disable_vpn_encryption.setter
    def disable_vpn_encryption(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_vpn_encryption", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the VirtualWAN.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="virtualWANName")
    def virtual_wan_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VirtualWAN being created or updated.
        """
        return pulumi.get(self, "virtual_wan_name")

    @virtual_wan_name.setter
    def virtual_wan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_wan_name", value)


class VirtualWan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_branch_to_branch_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_vnet_to_vnet_traffic: Optional[pulumi.Input[bool]] = None,
                 disable_vpn_encryption: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 virtual_wan_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        VirtualWAN Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_branch_to_branch_traffic: True if branch to branch traffic is allowed.
        :param pulumi.Input[bool] allow_vnet_to_vnet_traffic: True if Vnet to Vnet traffic is allowed.
        :param pulumi.Input[bool] disable_vpn_encryption: Vpn encryption to be disabled or not.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualWan.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] type: The type of the VirtualWAN.
        :param pulumi.Input[str] virtual_wan_name: The name of the VirtualWAN being created or updated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualWanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VirtualWAN Resource.

        :param str resource_name: The name of the resource.
        :param VirtualWanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualWanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_branch_to_branch_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_vnet_to_vnet_traffic: Optional[pulumi.Input[bool]] = None,
                 disable_vpn_encryption: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 virtual_wan_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualWanArgs.__new__(VirtualWanArgs)

            __props__.__dict__["allow_branch_to_branch_traffic"] = allow_branch_to_branch_traffic
            __props__.__dict__["allow_vnet_to_vnet_traffic"] = allow_vnet_to_vnet_traffic
            __props__.__dict__["disable_vpn_encryption"] = disable_vpn_encryption
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["virtual_wan_name"] = virtual_wan_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["office365_local_breakout_category"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["virtual_hubs"] = None
            __props__.__dict__["vpn_sites"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20210501:VirtualWan"), pulumi.Alias(type_="azure-native:network:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20180401:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20180401:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20180601:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20180601:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20180701:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20180701:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20180801:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20180801:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20181001:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20181001:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20181101:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20181101:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20181201:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20181201:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20190201:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20190201:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20190401:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20190401:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20190601:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20190601:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20190701:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20190701:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20190801:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20190801:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20190901:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20190901:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20191101:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20191101:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20191201:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20191201:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20200301:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20200301:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20200401:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20200401:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20200501:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20200601:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20200701:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20200801:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20201101:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20201101:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20210201:VirtualWan"), pulumi.Alias(type_="azure-native:network/v20210301:VirtualWan"), pulumi.Alias(type_="azure-nextgen:network/v20210301:VirtualWan")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualWan, __self__).__init__(
            'azure-native:network/v20210501:VirtualWan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualWan':
        """
        Get an existing VirtualWan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualWanArgs.__new__(VirtualWanArgs)

        __props__.__dict__["allow_branch_to_branch_traffic"] = None
        __props__.__dict__["allow_vnet_to_vnet_traffic"] = None
        __props__.__dict__["disable_vpn_encryption"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["office365_local_breakout_category"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hubs"] = None
        __props__.__dict__["vpn_sites"] = None
        return VirtualWan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(self) -> pulumi.Output[Optional[bool]]:
        """
        True if branch to branch traffic is allowed.
        """
        return pulumi.get(self, "allow_branch_to_branch_traffic")

    @property
    @pulumi.getter(name="allowVnetToVnetTraffic")
    def allow_vnet_to_vnet_traffic(self) -> pulumi.Output[Optional[bool]]:
        """
        True if Vnet to Vnet traffic is allowed.
        """
        return pulumi.get(self, "allow_vnet_to_vnet_traffic")

    @property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> pulumi.Output[Optional[bool]]:
        """
        Vpn encryption to be disabled or not.
        """
        return pulumi.get(self, "disable_vpn_encryption")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="office365LocalBreakoutCategory")
    def office365_local_breakout_category(self) -> pulumi.Output[str]:
        """
        The office local breakout category.
        """
        return pulumi.get(self, "office365_local_breakout_category")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the virtual WAN resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHubs")
    def virtual_hubs(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of VirtualHubs in the VirtualWAN.
        """
        return pulumi.get(self, "virtual_hubs")

    @property
    @pulumi.getter(name="vpnSites")
    def vpn_sites(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of VpnSites in the VirtualWAN.
        """
        return pulumi.get(self, "vpn_sites")

