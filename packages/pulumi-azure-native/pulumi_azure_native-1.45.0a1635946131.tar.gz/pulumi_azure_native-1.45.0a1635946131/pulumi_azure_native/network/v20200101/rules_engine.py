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

__all__ = ['RulesEngineArgs', 'RulesEngine']

@pulumi.input_type
class RulesEngineArgs:
    def __init__(__self__, *,
                 front_door_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['RulesEngineRuleArgs']]]] = None,
                 rules_engine_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RulesEngine resource.
        :param pulumi.Input[str] front_door_name: Name of the Front Door which is globally unique.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input['RulesEngineRuleArgs']]] rules: A list of rules that define a particular Rules Engine Configuration.
        :param pulumi.Input[str] rules_engine_name: Name of the Rules Engine which is unique within the Front Door.
        """
        pulumi.set(__self__, "front_door_name", front_door_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if rules_engine_name is not None:
            pulumi.set(__self__, "rules_engine_name", rules_engine_name)

    @property
    @pulumi.getter(name="frontDoorName")
    def front_door_name(self) -> pulumi.Input[str]:
        """
        Name of the Front Door which is globally unique.
        """
        return pulumi.get(self, "front_door_name")

    @front_door_name.setter
    def front_door_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "front_door_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulesEngineRuleArgs']]]]:
        """
        A list of rules that define a particular Rules Engine Configuration.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulesEngineRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="rulesEngineName")
    def rules_engine_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Rules Engine which is unique within the Front Door.
        """
        return pulumi.get(self, "rules_engine_name")

    @rules_engine_name.setter
    def rules_engine_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rules_engine_name", value)


class RulesEngine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 front_door_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesEngineRuleArgs']]]]] = None,
                 rules_engine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A rules engine configuration containing a list of rules that will run to modify the runtime behavior of the request and response.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] front_door_name: Name of the Front Door which is globally unique.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesEngineRuleArgs']]]] rules: A list of rules that define a particular Rules Engine Configuration.
        :param pulumi.Input[str] rules_engine_name: Name of the Rules Engine which is unique within the Front Door.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RulesEngineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A rules engine configuration containing a list of rules that will run to modify the runtime behavior of the request and response.

        :param str resource_name: The name of the resource.
        :param RulesEngineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulesEngineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 front_door_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesEngineRuleArgs']]]]] = None,
                 rules_engine_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = RulesEngineArgs.__new__(RulesEngineArgs)

            if front_door_name is None and not opts.urn:
                raise TypeError("Missing required property 'front_door_name'")
            __props__.__dict__["front_door_name"] = front_door_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rules"] = rules
            __props__.__dict__["rules_engine_name"] = rules_engine_name
            __props__.__dict__["name"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20200101:RulesEngine"), pulumi.Alias(type_="azure-native:network:RulesEngine"), pulumi.Alias(type_="azure-nextgen:network:RulesEngine"), pulumi.Alias(type_="azure-native:network/v20200401:RulesEngine"), pulumi.Alias(type_="azure-nextgen:network/v20200401:RulesEngine"), pulumi.Alias(type_="azure-native:network/v20200501:RulesEngine"), pulumi.Alias(type_="azure-nextgen:network/v20200501:RulesEngine")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RulesEngine, __self__).__init__(
            'azure-native:network/v20200101:RulesEngine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RulesEngine':
        """
        Get an existing RulesEngine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RulesEngineArgs.__new__(RulesEngineArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["type"] = None
        return RulesEngine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.RulesEngineRuleResponse']]]:
        """
        A list of rules that define a particular Rules Engine Configuration.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

