# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['SystemTopicArgs', 'SystemTopic']

@pulumi.input_type
class SystemTopicArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['IdentityInfoArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 system_topic_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SystemTopic resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input['IdentityInfoArgs'] identity: Identity information for the resource.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] source: Source for the system topic.
        :param pulumi.Input[str] system_topic_name: Name of the system topic.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        :param pulumi.Input[str] topic_type: TopicType for the system topic.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if system_topic_name is not None:
            pulumi.set(__self__, "system_topic_name", system_topic_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if topic_type is not None:
            pulumi.set(__self__, "topic_type", topic_type)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityInfoArgs']]:
        """
        Identity information for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityInfoArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Source for the system topic.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="systemTopicName")
    def system_topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the system topic.
        """
        return pulumi.get(self, "system_topic_name")

    @system_topic_name.setter
    def system_topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "system_topic_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="topicType")
    def topic_type(self) -> Optional[pulumi.Input[str]]:
        """
        TopicType for the system topic.
        """
        return pulumi.get(self, "topic_type")

    @topic_type.setter
    def topic_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_type", value)


class SystemTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityInfoArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 system_topic_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        EventGrid System Topic.
        API Version: 2021-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IdentityInfoArgs']] identity: Identity information for the resource.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] source: Source for the system topic.
        :param pulumi.Input[str] system_topic_name: Name of the system topic.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        :param pulumi.Input[str] topic_type: TopicType for the system topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SystemTopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        EventGrid System Topic.
        API Version: 2021-06-01-preview.

        :param str resource_name: The name of the resource.
        :param SystemTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SystemTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityInfoArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 system_topic_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = SystemTopicArgs.__new__(SystemTopicArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source"] = source
            __props__.__dict__["system_topic_name"] = system_topic_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["topic_type"] = topic_type
            __props__.__dict__["metric_resource_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:eventgrid:SystemTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20200401preview:SystemTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20200401preview:SystemTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20201015preview:SystemTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20201015preview:SystemTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20210601preview:SystemTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20210601preview:SystemTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20211201:SystemTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20211201:SystemTopic")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SystemTopic, __self__).__init__(
            'azure-native:eventgrid:SystemTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SystemTopic':
        """
        Get an existing SystemTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SystemTopicArgs.__new__(SystemTopicArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metric_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["topic_type"] = None
        __props__.__dict__["type"] = None
        return SystemTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityInfoResponse']]:
        """
        Identity information for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricResourceId")
    def metric_resource_id(self) -> pulumi.Output[str]:
        """
        Metric resource id for the system topic.
        """
        return pulumi.get(self, "metric_resource_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the system topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Source for the system topic.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to System Topic resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="topicType")
    def topic_type(self) -> pulumi.Output[Optional[str]]:
        """
        TopicType for the system topic.
        """
        return pulumi.get(self, "topic_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

