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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['AzureSkuArgs'],
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 enable_disk_encryption: Optional[pulumi.Input[bool]] = None,
                 enable_double_encryption: Optional[pulumi.Input[bool]] = None,
                 enable_purge: Optional[pulumi.Input[bool]] = None,
                 enable_streaming_ingest: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 key_vault_properties: Optional[pulumi.Input['KeyVaultPropertiesArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 optimized_autoscale: Optional[pulumi.Input['OptimizedAutoscaleArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_external_tenants: Optional[pulumi.Input[Sequence[pulumi.Input['TrustedExternalTenantArgs']]]] = None,
                 virtual_network_configuration: Optional[pulumi.Input['VirtualNetworkConfigurationArgs']] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input['AzureSkuArgs'] sku: The SKU of the cluster.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[bool] enable_disk_encryption: A boolean value that indicates if the cluster's disks are encrypted.
        :param pulumi.Input[bool] enable_double_encryption: A boolean value that indicates if double encryption is enabled.
        :param pulumi.Input[bool] enable_purge: A boolean value that indicates if the purge operations are enabled.
        :param pulumi.Input[bool] enable_streaming_ingest: A boolean value that indicates if the streaming ingest is enabled.
        :param pulumi.Input['IdentityArgs'] identity: The identity of the cluster, if configured.
        :param pulumi.Input['KeyVaultPropertiesArgs'] key_vault_properties: KeyVault properties for the cluster encryption.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['OptimizedAutoscaleArgs'] optimized_autoscale: Optimized auto scale definition.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['TrustedExternalTenantArgs']]] trusted_external_tenants: The cluster's external tenants.
        :param pulumi.Input['VirtualNetworkConfigurationArgs'] virtual_network_configuration: Virtual network definition.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The availability zones of the cluster.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if enable_disk_encryption is not None:
            pulumi.set(__self__, "enable_disk_encryption", enable_disk_encryption)
        if enable_double_encryption is None:
            enable_double_encryption = False
        if enable_double_encryption is not None:
            pulumi.set(__self__, "enable_double_encryption", enable_double_encryption)
        if enable_purge is None:
            enable_purge = False
        if enable_purge is not None:
            pulumi.set(__self__, "enable_purge", enable_purge)
        if enable_streaming_ingest is None:
            enable_streaming_ingest = False
        if enable_streaming_ingest is not None:
            pulumi.set(__self__, "enable_streaming_ingest", enable_streaming_ingest)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if key_vault_properties is not None:
            pulumi.set(__self__, "key_vault_properties", key_vault_properties)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if optimized_autoscale is not None:
            pulumi.set(__self__, "optimized_autoscale", optimized_autoscale)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trusted_external_tenants is not None:
            pulumi.set(__self__, "trusted_external_tenants", trusted_external_tenants)
        if virtual_network_configuration is not None:
            pulumi.set(__self__, "virtual_network_configuration", virtual_network_configuration)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the Kusto cluster.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['AzureSkuArgs']:
        """
        The SKU of the cluster.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['AzureSkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="enableDiskEncryption")
    def enable_disk_encryption(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean value that indicates if the cluster's disks are encrypted.
        """
        return pulumi.get(self, "enable_disk_encryption")

    @enable_disk_encryption.setter
    def enable_disk_encryption(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_disk_encryption", value)

    @property
    @pulumi.getter(name="enableDoubleEncryption")
    def enable_double_encryption(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean value that indicates if double encryption is enabled.
        """
        return pulumi.get(self, "enable_double_encryption")

    @enable_double_encryption.setter
    def enable_double_encryption(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_double_encryption", value)

    @property
    @pulumi.getter(name="enablePurge")
    def enable_purge(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean value that indicates if the purge operations are enabled.
        """
        return pulumi.get(self, "enable_purge")

    @enable_purge.setter
    def enable_purge(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_purge", value)

    @property
    @pulumi.getter(name="enableStreamingIngest")
    def enable_streaming_ingest(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean value that indicates if the streaming ingest is enabled.
        """
        return pulumi.get(self, "enable_streaming_ingest")

    @enable_streaming_ingest.setter
    def enable_streaming_ingest(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_streaming_ingest", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity of the cluster, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input['KeyVaultPropertiesArgs']]:
        """
        KeyVault properties for the cluster encryption.
        """
        return pulumi.get(self, "key_vault_properties")

    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input['KeyVaultPropertiesArgs']]):
        pulumi.set(self, "key_vault_properties", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="optimizedAutoscale")
    def optimized_autoscale(self) -> Optional[pulumi.Input['OptimizedAutoscaleArgs']]:
        """
        Optimized auto scale definition.
        """
        return pulumi.get(self, "optimized_autoscale")

    @optimized_autoscale.setter
    def optimized_autoscale(self, value: Optional[pulumi.Input['OptimizedAutoscaleArgs']]):
        pulumi.set(self, "optimized_autoscale", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="trustedExternalTenants")
    def trusted_external_tenants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrustedExternalTenantArgs']]]]:
        """
        The cluster's external tenants.
        """
        return pulumi.get(self, "trusted_external_tenants")

    @trusted_external_tenants.setter
    def trusted_external_tenants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrustedExternalTenantArgs']]]]):
        pulumi.set(self, "trusted_external_tenants", value)

    @property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(self) -> Optional[pulumi.Input['VirtualNetworkConfigurationArgs']]:
        """
        Virtual network definition.
        """
        return pulumi.get(self, "virtual_network_configuration")

    @virtual_network_configuration.setter
    def virtual_network_configuration(self, value: Optional[pulumi.Input['VirtualNetworkConfigurationArgs']]):
        pulumi.set(self, "virtual_network_configuration", value)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The availability zones of the cluster.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 enable_disk_encryption: Optional[pulumi.Input[bool]] = None,
                 enable_double_encryption: Optional[pulumi.Input[bool]] = None,
                 enable_purge: Optional[pulumi.Input[bool]] = None,
                 enable_streaming_ingest: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 key_vault_properties: Optional[pulumi.Input[pulumi.InputType['KeyVaultPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 optimized_autoscale: Optional[pulumi.Input[pulumi.InputType['OptimizedAutoscaleArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AzureSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_external_tenants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustedExternalTenantArgs']]]]] = None,
                 virtual_network_configuration: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkConfigurationArgs']]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Class representing a Kusto cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[bool] enable_disk_encryption: A boolean value that indicates if the cluster's disks are encrypted.
        :param pulumi.Input[bool] enable_double_encryption: A boolean value that indicates if double encryption is enabled.
        :param pulumi.Input[bool] enable_purge: A boolean value that indicates if the purge operations are enabled.
        :param pulumi.Input[bool] enable_streaming_ingest: A boolean value that indicates if the streaming ingest is enabled.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The identity of the cluster, if configured.
        :param pulumi.Input[pulumi.InputType['KeyVaultPropertiesArgs']] key_vault_properties: KeyVault properties for the cluster encryption.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['OptimizedAutoscaleArgs']] optimized_autoscale: Optimized auto scale definition.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[pulumi.InputType['AzureSkuArgs']] sku: The SKU of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustedExternalTenantArgs']]]] trusted_external_tenants: The cluster's external tenants.
        :param pulumi.Input[pulumi.InputType['VirtualNetworkConfigurationArgs']] virtual_network_configuration: Virtual network definition.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The availability zones of the cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a Kusto cluster.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 enable_disk_encryption: Optional[pulumi.Input[bool]] = None,
                 enable_double_encryption: Optional[pulumi.Input[bool]] = None,
                 enable_purge: Optional[pulumi.Input[bool]] = None,
                 enable_streaming_ingest: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 key_vault_properties: Optional[pulumi.Input[pulumi.InputType['KeyVaultPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 optimized_autoscale: Optional[pulumi.Input[pulumi.InputType['OptimizedAutoscaleArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AzureSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_external_tenants: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustedExternalTenantArgs']]]]] = None,
                 virtual_network_configuration: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkConfigurationArgs']]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["enable_disk_encryption"] = enable_disk_encryption
            if enable_double_encryption is None:
                enable_double_encryption = False
            __props__.__dict__["enable_double_encryption"] = enable_double_encryption
            if enable_purge is None:
                enable_purge = False
            __props__.__dict__["enable_purge"] = enable_purge
            if enable_streaming_ingest is None:
                enable_streaming_ingest = False
            __props__.__dict__["enable_streaming_ingest"] = enable_streaming_ingest
            __props__.__dict__["identity"] = identity
            __props__.__dict__["key_vault_properties"] = key_vault_properties
            __props__.__dict__["location"] = location
            __props__.__dict__["optimized_autoscale"] = optimized_autoscale
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["trusted_external_tenants"] = trusted_external_tenants
            __props__.__dict__["virtual_network_configuration"] = virtual_network_configuration
            __props__.__dict__["zones"] = zones
            __props__.__dict__["data_ingestion_uri"] = None
            __props__.__dict__["language_extensions"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["state_reason"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uri"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:kusto/v20200614:Cluster"), pulumi.Alias(type_="azure-native:kusto:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20170907privatepreview:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20170907privatepreview:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20180907preview:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20180907preview:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20190121:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20190121:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20190515:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20190515:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20190907:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20190907:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20191109:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20191109:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20200215:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20200215:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20200918:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20200918:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20210101:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20210101:Cluster"), pulumi.Alias(type_="azure-native:kusto/v20210827:Cluster"), pulumi.Alias(type_="azure-nextgen:kusto/v20210827:Cluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cluster, __self__).__init__(
            'azure-native:kusto/v20200614:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["data_ingestion_uri"] = None
        __props__.__dict__["enable_disk_encryption"] = None
        __props__.__dict__["enable_double_encryption"] = None
        __props__.__dict__["enable_purge"] = None
        __props__.__dict__["enable_streaming_ingest"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["key_vault_properties"] = None
        __props__.__dict__["language_extensions"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["optimized_autoscale"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["state_reason"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trusted_external_tenants"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uri"] = None
        __props__.__dict__["virtual_network_configuration"] = None
        __props__.__dict__["zones"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataIngestionUri")
    def data_ingestion_uri(self) -> pulumi.Output[str]:
        """
        The cluster data ingestion URI.
        """
        return pulumi.get(self, "data_ingestion_uri")

    @property
    @pulumi.getter(name="enableDiskEncryption")
    def enable_disk_encryption(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean value that indicates if the cluster's disks are encrypted.
        """
        return pulumi.get(self, "enable_disk_encryption")

    @property
    @pulumi.getter(name="enableDoubleEncryption")
    def enable_double_encryption(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean value that indicates if double encryption is enabled.
        """
        return pulumi.get(self, "enable_double_encryption")

    @property
    @pulumi.getter(name="enablePurge")
    def enable_purge(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean value that indicates if the purge operations are enabled.
        """
        return pulumi.get(self, "enable_purge")

    @property
    @pulumi.getter(name="enableStreamingIngest")
    def enable_streaming_ingest(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean value that indicates if the streaming ingest is enabled.
        """
        return pulumi.get(self, "enable_streaming_ingest")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the cluster, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Output[Optional['outputs.KeyVaultPropertiesResponse']]:
        """
        KeyVault properties for the cluster encryption.
        """
        return pulumi.get(self, "key_vault_properties")

    @property
    @pulumi.getter(name="languageExtensions")
    def language_extensions(self) -> pulumi.Output['outputs.LanguageExtensionsListResponse']:
        """
        List of the cluster's language extensions.
        """
        return pulumi.get(self, "language_extensions")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="optimizedAutoscale")
    def optimized_autoscale(self) -> pulumi.Output[Optional['outputs.OptimizedAutoscaleResponse']]:
        """
        Optimized auto scale definition.
        """
        return pulumi.get(self, "optimized_autoscale")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.AzureSkuResponse']:
        """
        The SKU of the cluster.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Output[str]:
        """
        The reason for the cluster's current state.
        """
        return pulumi.get(self, "state_reason")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedExternalTenants")
    def trusted_external_tenants(self) -> pulumi.Output[Optional[Sequence['outputs.TrustedExternalTenantResponse']]]:
        """
        The cluster's external tenants.
        """
        return pulumi.get(self, "trusted_external_tenants")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        The cluster URI.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(self) -> pulumi.Output[Optional['outputs.VirtualNetworkConfigurationResponse']]:
        """
        Virtual network definition.
        """
        return pulumi.get(self, "virtual_network_configuration")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The availability zones of the cluster.
        """
        return pulumi.get(self, "zones")

