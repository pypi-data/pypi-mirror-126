# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetLoadBalancerBackendAddressPoolResult',
    'AwaitableGetLoadBalancerBackendAddressPoolResult',
    'get_load_balancer_backend_address_pool',
    'get_load_balancer_backend_address_pool_output',
]

@pulumi.output_type
class GetLoadBalancerBackendAddressPoolResult:
    """
    Pool of backend IP addresses.
    """
    def __init__(__self__, backend_ip_configurations=None, etag=None, id=None, load_balancer_backend_addresses=None, load_balancing_rules=None, name=None, outbound_rule=None, outbound_rules=None, provisioning_state=None, type=None):
        if backend_ip_configurations and not isinstance(backend_ip_configurations, list):
            raise TypeError("Expected argument 'backend_ip_configurations' to be a list")
        pulumi.set(__self__, "backend_ip_configurations", backend_ip_configurations)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancer_backend_addresses and not isinstance(load_balancer_backend_addresses, list):
            raise TypeError("Expected argument 'load_balancer_backend_addresses' to be a list")
        pulumi.set(__self__, "load_balancer_backend_addresses", load_balancer_backend_addresses)
        if load_balancing_rules and not isinstance(load_balancing_rules, list):
            raise TypeError("Expected argument 'load_balancing_rules' to be a list")
        pulumi.set(__self__, "load_balancing_rules", load_balancing_rules)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outbound_rule and not isinstance(outbound_rule, dict):
            raise TypeError("Expected argument 'outbound_rule' to be a dict")
        pulumi.set(__self__, "outbound_rule", outbound_rule)
        if outbound_rules and not isinstance(outbound_rules, list):
            raise TypeError("Expected argument 'outbound_rules' to be a list")
        pulumi.set(__self__, "outbound_rules", outbound_rules)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backendIPConfigurations")
    def backend_ip_configurations(self) -> Sequence['outputs.NetworkInterfaceIPConfigurationResponse']:
        """
        An array of references to IP addresses defined in network interfaces.
        """
        return pulumi.get(self, "backend_ip_configurations")

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
    @pulumi.getter(name="loadBalancerBackendAddresses")
    def load_balancer_backend_addresses(self) -> Optional[Sequence['outputs.LoadBalancerBackendAddressResponse']]:
        """
        An array of backend addresses.
        """
        return pulumi.get(self, "load_balancer_backend_addresses")

    @property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(self) -> Sequence['outputs.SubResourceResponse']:
        """
        An array of references to load balancing rules that use this backend address pool.
        """
        return pulumi.get(self, "load_balancing_rules")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource that is unique within the set of backend address pools used by the load balancer. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundRule")
    def outbound_rule(self) -> 'outputs.SubResourceResponse':
        """
        A reference to an outbound rule that uses this backend address pool.
        """
        return pulumi.get(self, "outbound_rule")

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Sequence['outputs.SubResourceResponse']:
        """
        An array of references to outbound rules that use this backend address pool.
        """
        return pulumi.get(self, "outbound_rules")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the backend address pool resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetLoadBalancerBackendAddressPoolResult(GetLoadBalancerBackendAddressPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerBackendAddressPoolResult(
            backend_ip_configurations=self.backend_ip_configurations,
            etag=self.etag,
            id=self.id,
            load_balancer_backend_addresses=self.load_balancer_backend_addresses,
            load_balancing_rules=self.load_balancing_rules,
            name=self.name,
            outbound_rule=self.outbound_rule,
            outbound_rules=self.outbound_rules,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_load_balancer_backend_address_pool(backend_address_pool_name: Optional[str] = None,
                                           load_balancer_name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerBackendAddressPoolResult:
    """
    Pool of backend IP addresses.


    :param str backend_address_pool_name: The name of the backend address pool.
    :param str load_balancer_name: The name of the load balancer.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['backendAddressPoolName'] = backend_address_pool_name
    __args__['loadBalancerName'] = load_balancer_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200501:getLoadBalancerBackendAddressPool', __args__, opts=opts, typ=GetLoadBalancerBackendAddressPoolResult).value

    return AwaitableGetLoadBalancerBackendAddressPoolResult(
        backend_ip_configurations=__ret__.backend_ip_configurations,
        etag=__ret__.etag,
        id=__ret__.id,
        load_balancer_backend_addresses=__ret__.load_balancer_backend_addresses,
        load_balancing_rules=__ret__.load_balancing_rules,
        name=__ret__.name,
        outbound_rule=__ret__.outbound_rule,
        outbound_rules=__ret__.outbound_rules,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_load_balancer_backend_address_pool)
def get_load_balancer_backend_address_pool_output(backend_address_pool_name: Optional[pulumi.Input[str]] = None,
                                                  load_balancer_name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoadBalancerBackendAddressPoolResult]:
    """
    Pool of backend IP addresses.


    :param str backend_address_pool_name: The name of the backend address pool.
    :param str load_balancer_name: The name of the load balancer.
    :param str resource_group_name: The name of the resource group.
    """
    ...
