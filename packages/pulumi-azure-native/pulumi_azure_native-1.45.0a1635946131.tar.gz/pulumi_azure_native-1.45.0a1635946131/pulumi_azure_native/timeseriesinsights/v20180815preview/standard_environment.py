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

__all__ = ['StandardEnvironmentArgs', 'StandardEnvironment']

@pulumi.input_type
class StandardEnvironmentArgs:
    def __init__(__self__, *,
                 data_retention_time: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_key_properties: Optional[pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]]] = None,
                 storage_limit_exceeded_behavior: Optional[pulumi.Input[Union[str, 'StorageLimitExceededBehavior']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StandardEnvironment resource.
        :param pulumi.Input[str] data_retention_time: ISO8601 timespan specifying the minimum number of days the environment's events will be available for query.
        :param pulumi.Input[str] kind: The kind of the environment.
               Expected value is 'Standard'.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['SkuArgs'] sku: The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        :param pulumi.Input[str] environment_name: Name of the environment
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]] partition_key_properties: The list of event properties which will be used to partition data in the environment. Currently, only a single partition key property is supported.
        :param pulumi.Input[Union[str, 'StorageLimitExceededBehavior']] storage_limit_exceeded_behavior: The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional properties for the resource.
        """
        pulumi.set(__self__, "data_retention_time", data_retention_time)
        pulumi.set(__self__, "kind", 'Standard')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if partition_key_properties is not None:
            pulumi.set(__self__, "partition_key_properties", partition_key_properties)
        if storage_limit_exceeded_behavior is not None:
            pulumi.set(__self__, "storage_limit_exceeded_behavior", storage_limit_exceeded_behavior)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataRetentionTime")
    def data_retention_time(self) -> pulumi.Input[str]:
        """
        ISO8601 timespan specifying the minimum number of days the environment's events will be available for query.
        """
        return pulumi.get(self, "data_retention_time")

    @data_retention_time.setter
    def data_retention_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_retention_time", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the environment.
        Expected value is 'Standard'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the environment
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="partitionKeyProperties")
    def partition_key_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]]]:
        """
        The list of event properties which will be used to partition data in the environment. Currently, only a single partition key property is supported.
        """
        return pulumi.get(self, "partition_key_properties")

    @partition_key_properties.setter
    def partition_key_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]]]):
        pulumi.set(self, "partition_key_properties", value)

    @property
    @pulumi.getter(name="storageLimitExceededBehavior")
    def storage_limit_exceeded_behavior(self) -> Optional[pulumi.Input[Union[str, 'StorageLimitExceededBehavior']]]:
        """
        The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.
        """
        return pulumi.get(self, "storage_limit_exceeded_behavior")

    @storage_limit_exceeded_behavior.setter
    def storage_limit_exceeded_behavior(self, value: Optional[pulumi.Input[Union[str, 'StorageLimitExceededBehavior']]]):
        pulumi.set(self, "storage_limit_exceeded_behavior", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs of additional properties for the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StandardEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_retention_time: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TimeSeriesIdPropertyArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_limit_exceeded_behavior: Optional[pulumi.Input[Union[str, 'StorageLimitExceededBehavior']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource. Standard environments have data retention limits.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_retention_time: ISO8601 timespan specifying the minimum number of days the environment's events will be available for query.
        :param pulumi.Input[str] environment_name: Name of the environment
        :param pulumi.Input[str] kind: The kind of the environment.
               Expected value is 'Standard'.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TimeSeriesIdPropertyArgs']]]] partition_key_properties: The list of event properties which will be used to partition data in the environment. Currently, only a single partition key property is supported.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        :param pulumi.Input[Union[str, 'StorageLimitExceededBehavior']] storage_limit_exceeded_behavior: The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional properties for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StandardEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource. Standard environments have data retention limits.

        :param str resource_name: The name of the resource.
        :param StandardEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StandardEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_retention_time: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TimeSeriesIdPropertyArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_limit_exceeded_behavior: Optional[pulumi.Input[Union[str, 'StorageLimitExceededBehavior']]] = None,
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
            __props__ = StandardEnvironmentArgs.__new__(StandardEnvironmentArgs)

            if data_retention_time is None and not opts.urn:
                raise TypeError("Missing required property 'data_retention_time'")
            __props__.__dict__["data_retention_time"] = data_retention_time
            __props__.__dict__["environment_name"] = environment_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Standard'
            __props__.__dict__["location"] = location
            __props__.__dict__["partition_key_properties"] = partition_key_properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["storage_limit_exceeded_behavior"] = storage_limit_exceeded_behavior
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["data_access_fqdn"] = None
            __props__.__dict__["data_access_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20180815preview:StandardEnvironment"), pulumi.Alias(type_="azure-native:timeseriesinsights:StandardEnvironment"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights:StandardEnvironment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20170228preview:StandardEnvironment"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20170228preview:StandardEnvironment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20171115:StandardEnvironment"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20171115:StandardEnvironment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20200515:StandardEnvironment"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20200515:StandardEnvironment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20210331preview:StandardEnvironment"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20210331preview:StandardEnvironment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20210630preview:StandardEnvironment"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20210630preview:StandardEnvironment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StandardEnvironment, __self__).__init__(
            'azure-native:timeseriesinsights/v20180815preview:StandardEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StandardEnvironment':
        """
        Get an existing StandardEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StandardEnvironmentArgs.__new__(StandardEnvironmentArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["data_access_fqdn"] = None
        __props__.__dict__["data_access_id"] = None
        __props__.__dict__["data_retention_time"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partition_key_properties"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_limit_exceeded_behavior"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StandardEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time the resource was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="dataAccessFqdn")
    def data_access_fqdn(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name used to access the environment data, e.g. to query the environment's events or upload reference data for the environment.
        """
        return pulumi.get(self, "data_access_fqdn")

    @property
    @pulumi.getter(name="dataAccessId")
    def data_access_id(self) -> pulumi.Output[str]:
        """
        An id used to access the environment data, e.g. to query the environment's events or upload reference data for the environment.
        """
        return pulumi.get(self, "data_access_id")

    @property
    @pulumi.getter(name="dataRetentionTime")
    def data_retention_time(self) -> pulumi.Output[str]:
        """
        ISO8601 timespan specifying the minimum number of days the environment's events will be available for query.
        """
        return pulumi.get(self, "data_retention_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the environment.
        Expected value is 'Standard'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionKeyProperties")
    def partition_key_properties(self) -> pulumi.Output[Optional[Sequence['outputs.TimeSeriesIdPropertyResponse']]]:
        """
        The list of event properties which will be used to partition data in the environment. Currently, only a single partition key property is supported.
        """
        return pulumi.get(self, "partition_key_properties")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.EnvironmentStatusResponse']:
        """
        An object that represents the status of the environment, and its internal state in the Time Series Insights service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageLimitExceededBehavior")
    def storage_limit_exceeded_behavior(self) -> pulumi.Output[Optional[str]]:
        """
        The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.
        """
        return pulumi.get(self, "storage_limit_exceeded_behavior")

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

