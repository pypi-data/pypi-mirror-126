# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['HybridIdentityMetadatumArgs', 'HybridIdentityMetadatum']

@pulumi.input_type
class HybridIdentityMetadatumArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_machine_name: pulumi.Input[str],
                 metadata_name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HybridIdentityMetadatum resource.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name.
        :param pulumi.Input[str] virtual_machine_name: Name of the vm.
        :param pulumi.Input[str] metadata_name: Name of the hybridIdentityMetadata.
        :param pulumi.Input[str] public_key: Gets or sets the Public Key.
        :param pulumi.Input[str] vm_id: Gets or sets the Vm Id.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_machine_name", virtual_machine_name)
        if metadata_name is not None:
            pulumi.set(__self__, "metadata_name", metadata_name)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group Name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualMachineName")
    def virtual_machine_name(self) -> pulumi.Input[str]:
        """
        Name of the vm.
        """
        return pulumi.get(self, "virtual_machine_name")

    @virtual_machine_name.setter
    def virtual_machine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_machine_name", value)

    @property
    @pulumi.getter(name="metadataName")
    def metadata_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the hybridIdentityMetadata.
        """
        return pulumi.get(self, "metadata_name")

    @metadata_name.setter
    def metadata_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata_name", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the Public Key.
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the Vm Id.
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_id", value)


class HybridIdentityMetadatum(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata_name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the HybridIdentityMetadata.
        API Version: 2020-10-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metadata_name: Name of the hybridIdentityMetadata.
        :param pulumi.Input[str] public_key: Gets or sets the Public Key.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name.
        :param pulumi.Input[str] virtual_machine_name: Name of the vm.
        :param pulumi.Input[str] vm_id: Gets or sets the Vm Id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HybridIdentityMetadatumArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the HybridIdentityMetadata.
        API Version: 2020-10-01-preview.

        :param str resource_name: The name of the resource.
        :param HybridIdentityMetadatumArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HybridIdentityMetadatumArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata_name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = HybridIdentityMetadatumArgs.__new__(HybridIdentityMetadatumArgs)

            __props__.__dict__["metadata_name"] = metadata_name
            __props__.__dict__["public_key"] = public_key
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if virtual_machine_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_name'")
            __props__.__dict__["virtual_machine_name"] = virtual_machine_name
            __props__.__dict__["vm_id"] = vm_id
            __props__.__dict__["identity"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:connectedvmwarevsphere:HybridIdentityMetadatum"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20201001preview:HybridIdentityMetadatum"), pulumi.Alias(type_="azure-nextgen:connectedvmwarevsphere/v20201001preview:HybridIdentityMetadatum")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HybridIdentityMetadatum, __self__).__init__(
            'azure-native:connectedvmwarevsphere:HybridIdentityMetadatum',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HybridIdentityMetadatum':
        """
        Get an existing HybridIdentityMetadatum resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HybridIdentityMetadatumArgs.__new__(HybridIdentityMetadatumArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_key"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_id"] = None
        return HybridIdentityMetadatum(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.IdentityResponse']:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the Public Key.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the Vm Id.
        """
        return pulumi.get(self, "vm_id")

