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

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 application_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_identities: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationUserAssignedIdentityArgs']]]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy: Optional[pulumi.Input['ApplicationUpgradePolicyArgs']] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] application_name: The name of the application resource.
        :param pulumi.Input['ManagedIdentityArgs'] identity: Describes the managed identities for an Azure resource.
        :param pulumi.Input[str] location: Resource location depends on the parent resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationUserAssignedIdentityArgs']]] managed_identities: List of user assigned identities for the application, each mapped to a friendly name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: List of application parameters with overridden values from their default values specified in the application manifest.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        :param pulumi.Input['ApplicationUpgradePolicyArgs'] upgrade_policy: Describes the policy for a monitored application upgrade.
        :param pulumi.Input[str] version: The version of the application type as defined in the application manifest.
               This name must be the full Arm Resource ID for the referenced application type version.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_name is not None:
            pulumi.set(__self__, "application_name", application_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_identities is not None:
            pulumi.set(__self__, "managed_identities", managed_identities)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if upgrade_policy is not None:
            pulumi.set(__self__, "upgrade_policy", upgrade_policy)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster resource.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the application resource.
        """
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedIdentityArgs']]:
        """
        Describes the managed identities for an Azure resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedIdentities")
    def managed_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationUserAssignedIdentityArgs']]]]:
        """
        List of user assigned identities for the application, each mapped to a friendly name.
        """
        return pulumi.get(self, "managed_identities")

    @managed_identities.setter
    def managed_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationUserAssignedIdentityArgs']]]]):
        pulumi.set(self, "managed_identities", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        List of application parameters with overridden values from their default values specified in the application manifest.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input['ApplicationUpgradePolicyArgs']]:
        """
        Describes the policy for a monitored application upgrade.
        """
        return pulumi.get(self, "upgrade_policy")

    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input['ApplicationUpgradePolicyArgs']]):
        pulumi.set(self, "upgrade_policy", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the application type as defined in the application manifest.
        This name must be the full Arm Resource ID for the referenced application type version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationUserAssignedIdentityArgs']]]]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationUpgradePolicyArgs']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The application resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_name: The name of the application resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster resource.
        :param pulumi.Input[pulumi.InputType['ManagedIdentityArgs']] identity: Describes the managed identities for an Azure resource.
        :param pulumi.Input[str] location: Resource location depends on the parent resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationUserAssignedIdentityArgs']]]] managed_identities: List of user assigned identities for the application, each mapped to a friendly name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: List of application parameters with overridden values from their default values specified in the application manifest.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        :param pulumi.Input[pulumi.InputType['ApplicationUpgradePolicyArgs']] upgrade_policy: Describes the policy for a monitored application upgrade.
        :param pulumi.Input[str] version: The version of the application type as defined in the application manifest.
               This name must be the full Arm Resource ID for the referenced application type version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The application resource.

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationUserAssignedIdentityArgs']]]]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationUpgradePolicyArgs']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            __props__.__dict__["application_name"] = application_name
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_identities"] = managed_identities
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["upgrade_policy"] = upgrade_policy
            __props__.__dict__["version"] = version
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:servicefabric/v20210901privatepreview:Application"), pulumi.Alias(type_="azure-native:servicefabric/v20210101preview:Application"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20210101preview:Application"), pulumi.Alias(type_="azure-native:servicefabric/v20210501:Application"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20210501:Application"), pulumi.Alias(type_="azure-native:servicefabric/v20210701preview:Application"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20210701preview:Application"), pulumi.Alias(type_="azure-native:servicefabric/v20211101preview:Application"), pulumi.Alias(type_="azure-nextgen:servicefabric/v20211101preview:Application")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Application, __self__).__init__(
            'azure-native:servicefabric/v20210901privatepreview:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationArgs.__new__(ApplicationArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_identities"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["upgrade_policy"] = None
        __props__.__dict__["version"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedIdentityResponse']]:
        """
        Describes the managed identities for an Azure resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentities")
    def managed_identities(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationUserAssignedIdentityResponse']]]:
        """
        List of user assigned identities for the application, each mapped to a friendly name.
        """
        return pulumi.get(self, "managed_identities")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        List of application parameters with overridden values from their default values specified in the application manifest.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> pulumi.Output[Optional['outputs.ApplicationUpgradePolicyResponse']]:
        """
        Describes the policy for a monitored application upgrade.
        """
        return pulumi.get(self, "upgrade_policy")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the application type as defined in the application manifest.
        This name must be the full Arm Resource ID for the referenced application type version.
        """
        return pulumi.get(self, "version")

