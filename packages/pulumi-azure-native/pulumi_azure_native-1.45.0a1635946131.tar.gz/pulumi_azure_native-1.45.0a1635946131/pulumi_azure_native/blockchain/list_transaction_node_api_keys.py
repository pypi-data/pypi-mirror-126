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
    'ListTransactionNodeApiKeysResult',
    'AwaitableListTransactionNodeApiKeysResult',
    'list_transaction_node_api_keys',
    'list_transaction_node_api_keys_output',
]

@pulumi.output_type
class ListTransactionNodeApiKeysResult:
    """
    Collection of the API key payload which is exposed in the response of the resource provider.
    """
    def __init__(__self__, keys=None):
        if keys and not isinstance(keys, list):
            raise TypeError("Expected argument 'keys' to be a list")
        pulumi.set(__self__, "keys", keys)

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence['outputs.ApiKeyResponse']]:
        """
        Gets or sets the collection of API key.
        """
        return pulumi.get(self, "keys")


class AwaitableListTransactionNodeApiKeysResult(ListTransactionNodeApiKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListTransactionNodeApiKeysResult(
            keys=self.keys)


def list_transaction_node_api_keys(blockchain_member_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   transaction_node_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListTransactionNodeApiKeysResult:
    """
    Collection of the API key payload which is exposed in the response of the resource provider.
    API Version: 2018-06-01-preview.


    :param str blockchain_member_name: Blockchain member name.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str transaction_node_name: Transaction node name.
    """
    __args__ = dict()
    __args__['blockchainMemberName'] = blockchain_member_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['transactionNodeName'] = transaction_node_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:blockchain:listTransactionNodeApiKeys', __args__, opts=opts, typ=ListTransactionNodeApiKeysResult).value

    return AwaitableListTransactionNodeApiKeysResult(
        keys=__ret__.keys)


@_utilities.lift_output_func(list_transaction_node_api_keys)
def list_transaction_node_api_keys_output(blockchain_member_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          transaction_node_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListTransactionNodeApiKeysResult]:
    """
    Collection of the API key payload which is exposed in the response of the resource provider.
    API Version: 2018-06-01-preview.


    :param str blockchain_member_name: Blockchain member name.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str transaction_node_name: Transaction node name.
    """
    ...
