# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetProviderInstanceResult',
    'AwaitableGetProviderInstanceResult',
    'get_provider_instance',
    'get_provider_instance_output',
]

@pulumi.output_type
class GetProviderInstanceResult:
    """
    A provider instance associated with a SAP monitor.
    """
    def __init__(__self__, id=None, metadata=None, name=None, properties=None, provisioning_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, str):
            raise TypeError("Expected argument 'metadata' to be a str")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, str):
            raise TypeError("Expected argument 'properties' to be a str")
        pulumi.set(__self__, "properties", properties)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[str]:
        """
        A JSON string containing metadata of the provider instance.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> str:
        """
        A JSON string containing the properties of the provider instance.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of provisioning of the provider instance
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetProviderInstanceResult(GetProviderInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProviderInstanceResult(
            id=self.id,
            metadata=self.metadata,
            name=self.name,
            properties=self.properties,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_provider_instance(provider_instance_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          sap_monitor_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProviderInstanceResult:
    """
    A provider instance associated with a SAP monitor.


    :param str provider_instance_name: Name of the provider instance.
    :param str resource_group_name: Name of the resource group.
    :param str sap_monitor_name: Name of the SAP monitor resource.
    """
    __args__ = dict()
    __args__['providerInstanceName'] = provider_instance_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sapMonitorName'] = sap_monitor_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:hanaonazure/v20200207preview:getProviderInstance', __args__, opts=opts, typ=GetProviderInstanceResult).value

    return AwaitableGetProviderInstanceResult(
        id=__ret__.id,
        metadata=__ret__.metadata,
        name=__ret__.name,
        properties=__ret__.properties,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_provider_instance)
def get_provider_instance_output(provider_instance_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 sap_monitor_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProviderInstanceResult]:
    """
    A provider instance associated with a SAP monitor.


    :param str provider_instance_name: Name of the provider instance.
    :param str resource_group_name: Name of the resource group.
    :param str sap_monitor_name: Name of the SAP monitor resource.
    """
    ...
