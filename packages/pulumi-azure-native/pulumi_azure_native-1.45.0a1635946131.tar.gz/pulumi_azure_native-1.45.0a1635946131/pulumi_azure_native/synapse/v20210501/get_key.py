# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetKeyResult',
    'AwaitableGetKeyResult',
    'get_key',
    'get_key_output',
]

@pulumi.output_type
class GetKeyResult:
    """
    A workspace key
    """
    def __init__(__self__, id=None, is_active_cmk=None, key_vault_url=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_active_cmk and not isinstance(is_active_cmk, bool):
            raise TypeError("Expected argument 'is_active_cmk' to be a bool")
        pulumi.set(__self__, "is_active_cmk", is_active_cmk)
        if key_vault_url and not isinstance(key_vault_url, str):
            raise TypeError("Expected argument 'key_vault_url' to be a str")
        pulumi.set(__self__, "key_vault_url", key_vault_url)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter(name="isActiveCMK")
    def is_active_cmk(self) -> Optional[bool]:
        """
        Used to activate the workspace after a customer managed key is provided.
        """
        return pulumi.get(self, "is_active_cmk")

    @property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[str]:
        """
        The Key Vault Url of the workspace key.
        """
        return pulumi.get(self, "key_vault_url")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetKeyResult(GetKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyResult(
            id=self.id,
            is_active_cmk=self.is_active_cmk,
            key_vault_url=self.key_vault_url,
            name=self.name,
            type=self.type)


def get_key(key_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            workspace_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyResult:
    """
    A workspace key


    :param str key_name: The name of the workspace key
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20210501:getKey', __args__, opts=opts, typ=GetKeyResult).value

    return AwaitableGetKeyResult(
        id=__ret__.id,
        is_active_cmk=__ret__.is_active_cmk,
        key_vault_url=__ret__.key_vault_url,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_key)
def get_key_output(key_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   workspace_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeyResult]:
    """
    A workspace key


    :param str key_name: The name of the workspace key
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace
    """
    ...
