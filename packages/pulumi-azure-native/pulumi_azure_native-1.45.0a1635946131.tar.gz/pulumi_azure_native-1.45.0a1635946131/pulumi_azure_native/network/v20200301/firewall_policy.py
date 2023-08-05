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

__all__ = ['FirewallPolicyArgs', 'FirewallPolicy']

@pulumi.input_type
class FirewallPolicyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 base_policy: Optional[pulumi.Input['SubResourceArgs']] = None,
                 firewall_policy_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intel_mode: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]] = None):
        """
        The set of arguments for constructing a FirewallPolicy resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['SubResourceArgs'] base_policy: The parent firewall policy from which rules are inherited.
        :param pulumi.Input[str] firewall_policy_name: The name of the Firewall Policy.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']] threat_intel_mode: The operation mode for Threat Intelligence.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if base_policy is not None:
            pulumi.set(__self__, "base_policy", base_policy)
        if firewall_policy_name is not None:
            pulumi.set(__self__, "firewall_policy_name", firewall_policy_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if threat_intel_mode is not None:
            pulumi.set(__self__, "threat_intel_mode", threat_intel_mode)

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
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The parent firewall policy from which rules are inherited.
        """
        return pulumi.get(self, "base_policy")

    @base_policy.setter
    def base_policy(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "base_policy", value)

    @property
    @pulumi.getter(name="firewallPolicyName")
    def firewall_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Firewall Policy.
        """
        return pulumi.get(self, "firewall_policy_name")

    @firewall_policy_name.setter
    def firewall_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_policy_name", value)

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
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]]:
        """
        The operation mode for Threat Intelligence.
        """
        return pulumi.get(self, "threat_intel_mode")

    @threat_intel_mode.setter
    def threat_intel_mode(self, value: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]]):
        pulumi.set(self, "threat_intel_mode", value)


class FirewallPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_policy: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 firewall_policy_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intel_mode: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]] = None,
                 __props__=None):
        """
        FirewallPolicy Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] base_policy: The parent firewall policy from which rules are inherited.
        :param pulumi.Input[str] firewall_policy_name: The name of the Firewall Policy.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']] threat_intel_mode: The operation mode for Threat Intelligence.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        FirewallPolicy Resource.

        :param str resource_name: The name of the resource.
        :param FirewallPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_policy: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 firewall_policy_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intel_mode: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]] = None,
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
            __props__ = FirewallPolicyArgs.__new__(FirewallPolicyArgs)

            __props__.__dict__["base_policy"] = base_policy
            __props__.__dict__["firewall_policy_name"] = firewall_policy_name
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["threat_intel_mode"] = threat_intel_mode
            __props__.__dict__["child_policies"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["firewalls"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["rule_groups"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20200301:FirewallPolicy"), pulumi.Alias(type_="azure-native:network:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190601:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190601:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190701:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190701:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190801:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190801:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190901:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190901:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20191101:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20191101:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20191201:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20191201:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200401:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200401:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200501:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200501:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200601:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200601:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200701:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200701:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200801:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200801:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20201101:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20201101:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210201:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20210201:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210301:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20210301:FirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210501:FirewallPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20210501:FirewallPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FirewallPolicy, __self__).__init__(
            'azure-native:network/v20200301:FirewallPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallPolicy':
        """
        Get an existing FirewallPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallPolicyArgs.__new__(FirewallPolicyArgs)

        __props__.__dict__["base_policy"] = None
        __props__.__dict__["child_policies"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["firewalls"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rule_groups"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["threat_intel_mode"] = None
        __props__.__dict__["type"] = None
        return FirewallPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The parent firewall policy from which rules are inherited.
        """
        return pulumi.get(self, "base_policy")

    @property
    @pulumi.getter(name="childPolicies")
    def child_policies(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of references to Child Firewall Policies.
        """
        return pulumi.get(self, "child_policies")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def firewalls(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of references to Azure Firewalls that this Firewall Policy is associated with.
        """
        return pulumi.get(self, "firewalls")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the firewall policy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleGroups")
    def rule_groups(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of references to FirewallPolicyRuleGroups.
        """
        return pulumi.get(self, "rule_groups")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The operation mode for Threat Intelligence.
        """
        return pulumi.get(self, "threat_intel_mode")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

