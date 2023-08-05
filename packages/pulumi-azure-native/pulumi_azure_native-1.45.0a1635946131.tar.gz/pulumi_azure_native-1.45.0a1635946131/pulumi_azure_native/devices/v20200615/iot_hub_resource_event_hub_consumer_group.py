# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._inputs import *

__all__ = ['IotHubResourceEventHubConsumerGroupArgs', 'IotHubResourceEventHubConsumerGroup']

@pulumi.input_type
class IotHubResourceEventHubConsumerGroupArgs:
    def __init__(__self__, *,
                 event_hub_endpoint_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['EventHubConsumerGroupNameArgs']] = None):
        """
        The set of arguments for constructing a IotHubResourceEventHubConsumerGroup resource.
        :param pulumi.Input[str] event_hub_endpoint_name: The name of the Event Hub-compatible endpoint in the IoT hub.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT hub.
        :param pulumi.Input[str] resource_name: The name of the IoT hub.
        :param pulumi.Input[str] name: The name of the consumer group to add.
        :param pulumi.Input['EventHubConsumerGroupNameArgs'] properties: The EventHub consumer group name.
        """
        pulumi.set(__self__, "event_hub_endpoint_name", event_hub_endpoint_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="eventHubEndpointName")
    def event_hub_endpoint_name(self) -> pulumi.Input[str]:
        """
        The name of the Event Hub-compatible endpoint in the IoT hub.
        """
        return pulumi.get(self, "event_hub_endpoint_name")

    @event_hub_endpoint_name.setter
    def event_hub_endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_hub_endpoint_name", value)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the IoT hub.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the consumer group to add.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['EventHubConsumerGroupNameArgs']]:
        """
        The EventHub consumer group name.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['EventHubConsumerGroupNameArgs']]):
        pulumi.set(self, "properties", value)


class IotHubResourceEventHubConsumerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 event_hub_endpoint_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['EventHubConsumerGroupNameArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The properties of the EventHubConsumerGroupInfo object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] event_hub_endpoint_name: The name of the Event Hub-compatible endpoint in the IoT hub.
        :param pulumi.Input[str] name: The name of the consumer group to add.
        :param pulumi.Input[pulumi.InputType['EventHubConsumerGroupNameArgs']] properties: The EventHub consumer group name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT hub.
        :param pulumi.Input[str] resource_name_: The name of the IoT hub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotHubResourceEventHubConsumerGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The properties of the EventHubConsumerGroupInfo object.

        :param str resource_name: The name of the resource.
        :param IotHubResourceEventHubConsumerGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotHubResourceEventHubConsumerGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 event_hub_endpoint_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['EventHubConsumerGroupNameArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
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
            __props__ = IotHubResourceEventHubConsumerGroupArgs.__new__(IotHubResourceEventHubConsumerGroupArgs)

            if event_hub_endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'event_hub_endpoint_name'")
            __props__.__dict__["event_hub_endpoint_name"] = event_hub_endpoint_name
            __props__.__dict__["name"] = name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["etag"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:devices/v20200615:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20160203:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20160203:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20170119:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20170119:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20170701:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20170701:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20180122:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20180122:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20180401:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20180401:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20181201preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20181201preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20190322:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20190322:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20190322preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20190322preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20190701preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20190701preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20191104:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20191104:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20200301:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20200301:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20200401:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20200401:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20200710preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20200710preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20200801:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20200801:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20200831:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20200831:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20200831preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20200831preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20210201preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20210201preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20210303preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20210303preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20210331:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20210331:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20210701:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20210701:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20210701preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20210701preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-native:devices/v20210702preview:IotHubResourceEventHubConsumerGroup"), pulumi.Alias(type_="azure-nextgen:devices/v20210702preview:IotHubResourceEventHubConsumerGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotHubResourceEventHubConsumerGroup, __self__).__init__(
            'azure-native:devices/v20200615:IotHubResourceEventHubConsumerGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotHubResourceEventHubConsumerGroup':
        """
        Get an existing IotHubResourceEventHubConsumerGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotHubResourceEventHubConsumerGroupArgs.__new__(IotHubResourceEventHubConsumerGroupArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return IotHubResourceEventHubConsumerGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Event Hub-compatible consumer group name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The tags.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        the resource type.
        """
        return pulumi.get(self, "type")

