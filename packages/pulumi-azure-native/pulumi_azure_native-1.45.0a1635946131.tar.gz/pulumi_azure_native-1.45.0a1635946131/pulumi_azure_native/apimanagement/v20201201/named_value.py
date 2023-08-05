# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NamedValueArgs', 'NamedValue']

@pulumi.input_type
class NamedValueArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 key_vault: Optional[pulumi.Input['KeyVaultContractCreatePropertiesArgs']] = None,
                 named_value_id: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamedValue resource.
        :param pulumi.Input[str] display_name: Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input['KeyVaultContractCreatePropertiesArgs'] key_vault: KeyVault location details of the namedValue.
        :param pulumi.Input[str] named_value_id: Identifier of the NamedValue.
        :param pulumi.Input[bool] secret: Determines whether the value is a secret and should be encrypted or not. Default value is false.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Optional tags that when provided can be used to filter the NamedValue list.
        :param pulumi.Input[str] value: Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if named_value_id is not None:
            pulumi.set(__self__, "named_value_id", named_value_id)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input['KeyVaultContractCreatePropertiesArgs']]:
        """
        KeyVault location details of the namedValue.
        """
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input['KeyVaultContractCreatePropertiesArgs']]):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter(name="namedValueId")
    def named_value_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the NamedValue.
        """
        return pulumi.get(self, "named_value_id")

    @named_value_id.setter
    def named_value_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "named_value_id", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether the value is a secret and should be encrypted or not. Default value is false.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional tags that when provided can be used to filter the NamedValue list.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class NamedValue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 key_vault: Optional[pulumi.Input[pulumi.InputType['KeyVaultContractCreatePropertiesArgs']]] = None,
                 named_value_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[bool]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        NamedValue details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.
        :param pulumi.Input[pulumi.InputType['KeyVaultContractCreatePropertiesArgs']] key_vault: KeyVault location details of the namedValue.
        :param pulumi.Input[str] named_value_id: Identifier of the NamedValue.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[bool] secret: Determines whether the value is a secret and should be encrypted or not. Default value is false.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Optional tags that when provided can be used to filter the NamedValue list.
        :param pulumi.Input[str] value: Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamedValueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NamedValue details.

        :param str resource_name: The name of the resource.
        :param NamedValueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamedValueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 key_vault: Optional[pulumi.Input[pulumi.InputType['KeyVaultContractCreatePropertiesArgs']]] = None,
                 named_value_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[bool]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
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
            __props__ = NamedValueArgs.__new__(NamedValueArgs)

            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["key_vault"] = key_vault
            __props__.__dict__["named_value_id"] = named_value_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["secret"] = secret
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["value"] = value
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:NamedValue"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:NamedValue"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:NamedValue")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NamedValue, __self__).__init__(
            'azure-native:apimanagement/v20201201:NamedValue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NamedValue':
        """
        Get an existing NamedValue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamedValueArgs.__new__(NamedValueArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["key_vault"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["secret"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return NamedValue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Output[Optional['outputs.KeyVaultContractPropertiesResponse']]:
        """
        KeyVault location details of the namedValue.
        """
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines whether the value is a secret and should be encrypted or not. Default value is false.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Optional tags that when provided can be used to filter the NamedValue list.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        return pulumi.get(self, "value")

