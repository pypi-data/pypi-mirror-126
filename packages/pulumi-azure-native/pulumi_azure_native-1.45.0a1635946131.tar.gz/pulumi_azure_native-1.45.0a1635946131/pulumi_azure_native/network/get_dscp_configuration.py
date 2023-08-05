# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDscpConfigurationResult',
    'AwaitableGetDscpConfigurationResult',
    'get_dscp_configuration',
    'get_dscp_configuration_output',
]

@pulumi.output_type
class GetDscpConfigurationResult:
    """
    DSCP Configuration in a resource group.
    """
    def __init__(__self__, associated_network_interfaces=None, destination_ip_ranges=None, destination_port_ranges=None, etag=None, id=None, location=None, markings=None, name=None, protocol=None, provisioning_state=None, qos_collection_id=None, resource_guid=None, source_ip_ranges=None, source_port_ranges=None, tags=None, type=None):
        if associated_network_interfaces and not isinstance(associated_network_interfaces, list):
            raise TypeError("Expected argument 'associated_network_interfaces' to be a list")
        pulumi.set(__self__, "associated_network_interfaces", associated_network_interfaces)
        if destination_ip_ranges and not isinstance(destination_ip_ranges, list):
            raise TypeError("Expected argument 'destination_ip_ranges' to be a list")
        pulumi.set(__self__, "destination_ip_ranges", destination_ip_ranges)
        if destination_port_ranges and not isinstance(destination_port_ranges, list):
            raise TypeError("Expected argument 'destination_port_ranges' to be a list")
        pulumi.set(__self__, "destination_port_ranges", destination_port_ranges)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if markings and not isinstance(markings, list):
            raise TypeError("Expected argument 'markings' to be a list")
        pulumi.set(__self__, "markings", markings)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if qos_collection_id and not isinstance(qos_collection_id, str):
            raise TypeError("Expected argument 'qos_collection_id' to be a str")
        pulumi.set(__self__, "qos_collection_id", qos_collection_id)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if source_ip_ranges and not isinstance(source_ip_ranges, list):
            raise TypeError("Expected argument 'source_ip_ranges' to be a list")
        pulumi.set(__self__, "source_ip_ranges", source_ip_ranges)
        if source_port_ranges and not isinstance(source_port_ranges, list):
            raise TypeError("Expected argument 'source_port_ranges' to be a list")
        pulumi.set(__self__, "source_port_ranges", source_port_ranges)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="associatedNetworkInterfaces")
    def associated_network_interfaces(self) -> Sequence['outputs.NetworkInterfaceResponse']:
        """
        Associated Network Interfaces to the DSCP Configuration.
        """
        return pulumi.get(self, "associated_network_interfaces")

    @property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> Optional[Sequence['outputs.QosIpRangeResponse']]:
        """
        Destination IP ranges.
        """
        return pulumi.get(self, "destination_ip_ranges")

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence['outputs.QosPortRangeResponse']]:
        """
        Destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def markings(self) -> Optional[Sequence[int]]:
        """
        List of markings to be used in the configuration.
        """
        return pulumi.get(self, "markings")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        RNM supported protocol types.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the DSCP Configuration resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="qosCollectionId")
    def qos_collection_id(self) -> str:
        """
        Qos Collection ID generated by RNM.
        """
        return pulumi.get(self, "qos_collection_id")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        The resource GUID property of the DSCP Configuration resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Optional[Sequence['outputs.QosIpRangeResponse']]:
        """
        Source IP ranges.
        """
        return pulumi.get(self, "source_ip_ranges")

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence['outputs.QosPortRangeResponse']]:
        """
        Sources port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetDscpConfigurationResult(GetDscpConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDscpConfigurationResult(
            associated_network_interfaces=self.associated_network_interfaces,
            destination_ip_ranges=self.destination_ip_ranges,
            destination_port_ranges=self.destination_port_ranges,
            etag=self.etag,
            id=self.id,
            location=self.location,
            markings=self.markings,
            name=self.name,
            protocol=self.protocol,
            provisioning_state=self.provisioning_state,
            qos_collection_id=self.qos_collection_id,
            resource_guid=self.resource_guid,
            source_ip_ranges=self.source_ip_ranges,
            source_port_ranges=self.source_port_ranges,
            tags=self.tags,
            type=self.type)


def get_dscp_configuration(dscp_configuration_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDscpConfigurationResult:
    """
    DSCP Configuration in a resource group.
    API Version: 2020-11-01.


    :param str dscp_configuration_name: The name of the resource.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['dscpConfigurationName'] = dscp_configuration_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network:getDscpConfiguration', __args__, opts=opts, typ=GetDscpConfigurationResult).value

    return AwaitableGetDscpConfigurationResult(
        associated_network_interfaces=__ret__.associated_network_interfaces,
        destination_ip_ranges=__ret__.destination_ip_ranges,
        destination_port_ranges=__ret__.destination_port_ranges,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        markings=__ret__.markings,
        name=__ret__.name,
        protocol=__ret__.protocol,
        provisioning_state=__ret__.provisioning_state,
        qos_collection_id=__ret__.qos_collection_id,
        resource_guid=__ret__.resource_guid,
        source_ip_ranges=__ret__.source_ip_ranges,
        source_port_ranges=__ret__.source_port_ranges,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_dscp_configuration)
def get_dscp_configuration_output(dscp_configuration_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDscpConfigurationResult]:
    """
    DSCP Configuration in a resource group.
    API Version: 2020-11-01.


    :param str dscp_configuration_name: The name of the resource.
    :param str resource_group_name: The name of the resource group.
    """
    ...
