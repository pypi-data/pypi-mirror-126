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

__all__ = ['ReferenceDataSetArgs', 'ReferenceDataSet']

@pulumi.input_type
class ReferenceDataSetArgs:
    def __init__(__self__, *,
                 environment_name: pulumi.Input[str],
                 key_properties: pulumi.Input[Sequence[pulumi.Input['ReferenceDataSetKeyPropertyArgs']]],
                 resource_group_name: pulumi.Input[str],
                 data_string_comparison_behavior: Optional[pulumi.Input['DataStringComparisonBehavior']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 reference_data_set_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ReferenceDataSet resource.
        :param pulumi.Input[str] environment_name: The name of the Time Series Insights environment associated with the specified resource group.
        :param pulumi.Input[Sequence[pulumi.Input['ReferenceDataSetKeyPropertyArgs']]] key_properties: The list of key properties for the reference data set.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['DataStringComparisonBehavior'] data_string_comparison_behavior: The reference data set key comparison behavior can be set using this property. By default, the value is 'Ordinal' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When 'OrdinalIgnoreCase' is set, case insensitive comparison will be used.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] reference_data_set_name: Name of the reference data set.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional properties for the resource.
        """
        pulumi.set(__self__, "environment_name", environment_name)
        pulumi.set(__self__, "key_properties", key_properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_string_comparison_behavior is not None:
            pulumi.set(__self__, "data_string_comparison_behavior", data_string_comparison_behavior)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if reference_data_set_name is not None:
            pulumi.set(__self__, "reference_data_set_name", reference_data_set_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        The name of the Time Series Insights environment associated with the specified resource group.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter(name="keyProperties")
    def key_properties(self) -> pulumi.Input[Sequence[pulumi.Input['ReferenceDataSetKeyPropertyArgs']]]:
        """
        The list of key properties for the reference data set.
        """
        return pulumi.get(self, "key_properties")

    @key_properties.setter
    def key_properties(self, value: pulumi.Input[Sequence[pulumi.Input['ReferenceDataSetKeyPropertyArgs']]]):
        pulumi.set(self, "key_properties", value)

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
    @pulumi.getter(name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> Optional[pulumi.Input['DataStringComparisonBehavior']]:
        """
        The reference data set key comparison behavior can be set using this property. By default, the value is 'Ordinal' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When 'OrdinalIgnoreCase' is set, case insensitive comparison will be used.
        """
        return pulumi.get(self, "data_string_comparison_behavior")

    @data_string_comparison_behavior.setter
    def data_string_comparison_behavior(self, value: Optional[pulumi.Input['DataStringComparisonBehavior']]):
        pulumi.set(self, "data_string_comparison_behavior", value)

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
    @pulumi.getter(name="referenceDataSetName")
    def reference_data_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the reference data set.
        """
        return pulumi.get(self, "reference_data_set_name")

    @reference_data_set_name.setter
    def reference_data_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reference_data_set_name", value)

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


class ReferenceDataSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_string_comparison_behavior: Optional[pulumi.Input['DataStringComparisonBehavior']] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReferenceDataSetKeyPropertyArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 reference_data_set_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A reference data set provides metadata about the events in an environment. Metadata in the reference data set will be joined with events as they are read from event sources. The metadata that makes up the reference data set is uploaded or modified through the Time Series Insights data plane APIs.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['DataStringComparisonBehavior'] data_string_comparison_behavior: The reference data set key comparison behavior can be set using this property. By default, the value is 'Ordinal' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When 'OrdinalIgnoreCase' is set, case insensitive comparison will be used.
        :param pulumi.Input[str] environment_name: The name of the Time Series Insights environment associated with the specified resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReferenceDataSetKeyPropertyArgs']]]] key_properties: The list of key properties for the reference data set.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] reference_data_set_name: Name of the reference data set.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional properties for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReferenceDataSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A reference data set provides metadata about the events in an environment. Metadata in the reference data set will be joined with events as they are read from event sources. The metadata that makes up the reference data set is uploaded or modified through the Time Series Insights data plane APIs.

        :param str resource_name: The name of the resource.
        :param ReferenceDataSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReferenceDataSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_string_comparison_behavior: Optional[pulumi.Input['DataStringComparisonBehavior']] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReferenceDataSetKeyPropertyArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 reference_data_set_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ReferenceDataSetArgs.__new__(ReferenceDataSetArgs)

            __props__.__dict__["data_string_comparison_behavior"] = data_string_comparison_behavior
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            if key_properties is None and not opts.urn:
                raise TypeError("Missing required property 'key_properties'")
            __props__.__dict__["key_properties"] = key_properties
            __props__.__dict__["location"] = location
            __props__.__dict__["reference_data_set_name"] = reference_data_set_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20171115:ReferenceDataSet"), pulumi.Alias(type_="azure-native:timeseriesinsights:ReferenceDataSet"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights:ReferenceDataSet"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20170228preview:ReferenceDataSet"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20170228preview:ReferenceDataSet"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20180815preview:ReferenceDataSet"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20180815preview:ReferenceDataSet"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20200515:ReferenceDataSet"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20200515:ReferenceDataSet"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20210331preview:ReferenceDataSet"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20210331preview:ReferenceDataSet"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20210630preview:ReferenceDataSet"), pulumi.Alias(type_="azure-nextgen:timeseriesinsights/v20210630preview:ReferenceDataSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ReferenceDataSet, __self__).__init__(
            'azure-native:timeseriesinsights/v20171115:ReferenceDataSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReferenceDataSet':
        """
        Get an existing ReferenceDataSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReferenceDataSetArgs.__new__(ReferenceDataSetArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["data_string_comparison_behavior"] = None
        __props__.__dict__["key_properties"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ReferenceDataSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time the resource was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> pulumi.Output[Optional[str]]:
        """
        The reference data set key comparison behavior can be set using this property. By default, the value is 'Ordinal' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When 'OrdinalIgnoreCase' is set, case insensitive comparison will be used.
        """
        return pulumi.get(self, "data_string_comparison_behavior")

    @property
    @pulumi.getter(name="keyProperties")
    def key_properties(self) -> pulumi.Output[Sequence['outputs.ReferenceDataSetKeyPropertyResponse']]:
        """
        The list of key properties for the reference data set.
        """
        return pulumi.get(self, "key_properties")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

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

