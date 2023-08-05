# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['RegisteredPrefixArgs', 'RegisteredPrefix']

@pulumi.input_type
class RegisteredPrefixArgs:
    def __init__(__self__, *,
                 peering_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 prefix: Optional[pulumi.Input[str]] = None,
                 registered_prefix_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegisteredPrefix resource.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] prefix: The customer's prefix from which traffic originates.
        :param pulumi.Input[str] registered_prefix_name: The name of the registered prefix.
        """
        pulumi.set(__self__, "peering_name", peering_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if registered_prefix_name is not None:
            pulumi.set(__self__, "registered_prefix_name", registered_prefix_name)

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> pulumi.Input[str]:
        """
        The name of the peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_name", value)

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
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The customer's prefix from which traffic originates.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter(name="registeredPrefixName")
    def registered_prefix_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the registered prefix.
        """
        return pulumi.get(self, "registered_prefix_name")

    @registered_prefix_name.setter
    def registered_prefix_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registered_prefix_name", value)


class RegisteredPrefix(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 registered_prefix_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The customer's prefix that is registered by the peering service provider.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] prefix: The customer's prefix from which traffic originates.
        :param pulumi.Input[str] registered_prefix_name: The name of the registered prefix.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegisteredPrefixArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The customer's prefix that is registered by the peering service provider.

        :param str resource_name: The name of the resource.
        :param RegisteredPrefixArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegisteredPrefixArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 registered_prefix_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = RegisteredPrefixArgs.__new__(RegisteredPrefixArgs)

            if peering_name is None and not opts.urn:
                raise TypeError("Missing required property 'peering_name'")
            __props__.__dict__["peering_name"] = peering_name
            __props__.__dict__["prefix"] = prefix
            __props__.__dict__["registered_prefix_name"] = registered_prefix_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["error_message"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["peering_service_prefix_key"] = None
            __props__.__dict__["prefix_validation_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:peering/v20201001:RegisteredPrefix"), pulumi.Alias(type_="azure-native:peering:RegisteredPrefix"), pulumi.Alias(type_="azure-nextgen:peering:RegisteredPrefix"), pulumi.Alias(type_="azure-native:peering/v20200101preview:RegisteredPrefix"), pulumi.Alias(type_="azure-nextgen:peering/v20200101preview:RegisteredPrefix"), pulumi.Alias(type_="azure-native:peering/v20200401:RegisteredPrefix"), pulumi.Alias(type_="azure-nextgen:peering/v20200401:RegisteredPrefix"), pulumi.Alias(type_="azure-native:peering/v20210101:RegisteredPrefix"), pulumi.Alias(type_="azure-nextgen:peering/v20210101:RegisteredPrefix"), pulumi.Alias(type_="azure-native:peering/v20210601:RegisteredPrefix"), pulumi.Alias(type_="azure-nextgen:peering/v20210601:RegisteredPrefix")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RegisteredPrefix, __self__).__init__(
            'azure-native:peering/v20201001:RegisteredPrefix',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegisteredPrefix':
        """
        Get an existing RegisteredPrefix resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegisteredPrefixArgs.__new__(RegisteredPrefixArgs)

        __props__.__dict__["error_message"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peering_service_prefix_key"] = None
        __props__.__dict__["prefix"] = None
        __props__.__dict__["prefix_validation_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return RegisteredPrefix(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        The error message associated with the validation state, if any.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringServicePrefixKey")
    def peering_service_prefix_key(self) -> pulumi.Output[str]:
        """
        The peering service prefix key that is to be shared with the customer.
        """
        return pulumi.get(self, "peering_service_prefix_key")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The customer's prefix from which traffic originates.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="prefixValidationState")
    def prefix_validation_state(self) -> pulumi.Output[str]:
        """
        The prefix validation state.
        """
        return pulumi.get(self, "prefix_validation_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

