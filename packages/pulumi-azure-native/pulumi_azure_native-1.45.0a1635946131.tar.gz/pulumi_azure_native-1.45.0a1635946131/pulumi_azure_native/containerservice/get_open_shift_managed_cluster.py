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
    'GetOpenShiftManagedClusterResult',
    'AwaitableGetOpenShiftManagedClusterResult',
    'get_open_shift_managed_cluster',
    'get_open_shift_managed_cluster_output',
]

@pulumi.output_type
class GetOpenShiftManagedClusterResult:
    """
    OpenShift Managed cluster.
    """
    def __init__(__self__, agent_pool_profiles=None, auth_profile=None, cluster_version=None, fqdn=None, id=None, location=None, master_pool_profile=None, name=None, network_profile=None, open_shift_version=None, plan=None, provisioning_state=None, public_hostname=None, router_profiles=None, tags=None, type=None):
        if agent_pool_profiles and not isinstance(agent_pool_profiles, list):
            raise TypeError("Expected argument 'agent_pool_profiles' to be a list")
        pulumi.set(__self__, "agent_pool_profiles", agent_pool_profiles)
        if auth_profile and not isinstance(auth_profile, dict):
            raise TypeError("Expected argument 'auth_profile' to be a dict")
        pulumi.set(__self__, "auth_profile", auth_profile)
        if cluster_version and not isinstance(cluster_version, str):
            raise TypeError("Expected argument 'cluster_version' to be a str")
        pulumi.set(__self__, "cluster_version", cluster_version)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if master_pool_profile and not isinstance(master_pool_profile, dict):
            raise TypeError("Expected argument 'master_pool_profile' to be a dict")
        pulumi.set(__self__, "master_pool_profile", master_pool_profile)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if open_shift_version and not isinstance(open_shift_version, str):
            raise TypeError("Expected argument 'open_shift_version' to be a str")
        pulumi.set(__self__, "open_shift_version", open_shift_version)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_hostname and not isinstance(public_hostname, str):
            raise TypeError("Expected argument 'public_hostname' to be a str")
        pulumi.set(__self__, "public_hostname", public_hostname)
        if router_profiles and not isinstance(router_profiles, list):
            raise TypeError("Expected argument 'router_profiles' to be a list")
        pulumi.set(__self__, "router_profiles", router_profiles)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> Optional[Sequence['outputs.OpenShiftManagedClusterAgentPoolProfileResponse']]:
        """
        Configuration of OpenShift cluster VMs.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @property
    @pulumi.getter(name="authProfile")
    def auth_profile(self) -> Optional['outputs.OpenShiftManagedClusterAuthProfileResponse']:
        """
        Configures OpenShift authentication.
        """
        return pulumi.get(self, "auth_profile")

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> str:
        """
        Version of OpenShift specified when creating the cluster.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        Service generated FQDN for OpenShift API server loadbalancer internal hostname.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="masterPoolProfile")
    def master_pool_profile(self) -> Optional['outputs.OpenShiftManagedClusterMasterPoolProfileResponse']:
        """
        Configuration for OpenShift master VMs.
        """
        return pulumi.get(self, "master_pool_profile")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.NetworkProfileResponse']:
        """
        Configuration for OpenShift networking.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="openShiftVersion")
    def open_shift_version(self) -> str:
        """
        Version of OpenShift specified when creating the cluster.
        """
        return pulumi.get(self, "open_shift_version")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.PurchasePlanResponse']:
        """
        Define the resource plan as required by ARM for billing purposes
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicHostname")
    def public_hostname(self) -> str:
        """
        Service generated FQDN for OpenShift API server.
        """
        return pulumi.get(self, "public_hostname")

    @property
    @pulumi.getter(name="routerProfiles")
    def router_profiles(self) -> Optional[Sequence['outputs.OpenShiftRouterProfileResponse']]:
        """
        Configuration for OpenShift router(s).
        """
        return pulumi.get(self, "router_profiles")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetOpenShiftManagedClusterResult(GetOpenShiftManagedClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOpenShiftManagedClusterResult(
            agent_pool_profiles=self.agent_pool_profiles,
            auth_profile=self.auth_profile,
            cluster_version=self.cluster_version,
            fqdn=self.fqdn,
            id=self.id,
            location=self.location,
            master_pool_profile=self.master_pool_profile,
            name=self.name,
            network_profile=self.network_profile,
            open_shift_version=self.open_shift_version,
            plan=self.plan,
            provisioning_state=self.provisioning_state,
            public_hostname=self.public_hostname,
            router_profiles=self.router_profiles,
            tags=self.tags,
            type=self.type)


def get_open_shift_managed_cluster(resource_group_name: Optional[str] = None,
                                   resource_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOpenShiftManagedClusterResult:
    """
    OpenShift Managed cluster.
    API Version: 2019-04-30.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the OpenShift managed cluster resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice:getOpenShiftManagedCluster', __args__, opts=opts, typ=GetOpenShiftManagedClusterResult).value

    return AwaitableGetOpenShiftManagedClusterResult(
        agent_pool_profiles=__ret__.agent_pool_profiles,
        auth_profile=__ret__.auth_profile,
        cluster_version=__ret__.cluster_version,
        fqdn=__ret__.fqdn,
        id=__ret__.id,
        location=__ret__.location,
        master_pool_profile=__ret__.master_pool_profile,
        name=__ret__.name,
        network_profile=__ret__.network_profile,
        open_shift_version=__ret__.open_shift_version,
        plan=__ret__.plan,
        provisioning_state=__ret__.provisioning_state,
        public_hostname=__ret__.public_hostname,
        router_profiles=__ret__.router_profiles,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_open_shift_managed_cluster)
def get_open_shift_managed_cluster_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                          resource_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOpenShiftManagedClusterResult]:
    """
    OpenShift Managed cluster.
    API Version: 2019-04-30.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the OpenShift managed cluster resource.
    """
    ...
