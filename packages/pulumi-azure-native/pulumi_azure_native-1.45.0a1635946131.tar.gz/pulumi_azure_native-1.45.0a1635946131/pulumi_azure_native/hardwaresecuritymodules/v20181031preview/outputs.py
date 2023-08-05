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

__all__ = [
    'ApiEntityReferenceResponse',
    'NetworkInterfaceResponse',
    'NetworkProfileResponse',
    'SkuResponse',
]

@pulumi.output_type
class ApiEntityReferenceResponse(dict):
    """
    The API entity reference.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        The API entity reference.
        :param str id: The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class NetworkInterfaceResponse(dict):
    """
    The network interface definition.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateIpAddress":
            suggest = "private_ip_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NetworkInterfaceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NetworkInterfaceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NetworkInterfaceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 private_ip_address: Optional[str] = None):
        """
        The network interface definition.
        :param str id: The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        :param str private_ip_address: Private Ip address of the interface
        """
        pulumi.set(__self__, "id", id)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[str]:
        """
        Private Ip address of the interface
        """
        return pulumi.get(self, "private_ip_address")


@pulumi.output_type
class NetworkProfileResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkInterfaces":
            suggest = "network_interfaces"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NetworkProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NetworkProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NetworkProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_interfaces: Optional[Sequence['outputs.NetworkInterfaceResponse']] = None,
                 subnet: Optional['outputs.ApiEntityReferenceResponse'] = None):
        """
        :param Sequence['NetworkInterfaceResponse'] network_interfaces: Specifies the list of resource Ids for the network interfaces associated with the dedicated HSM.
        :param 'ApiEntityReferenceResponse' subnet: Specifies the identifier of the subnet.
        """
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence['outputs.NetworkInterfaceResponse']]:
        """
        Specifies the list of resource Ids for the network interfaces associated with the dedicated HSM.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter
    def subnet(self) -> Optional['outputs.ApiEntityReferenceResponse']:
        """
        Specifies the identifier of the subnet.
        """
        return pulumi.get(self, "subnet")


@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: SKU of the dedicated HSM
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        SKU of the dedicated HSM
        """
        return pulumi.get(self, "name")


