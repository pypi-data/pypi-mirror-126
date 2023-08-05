# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDataSetMappingResult',
    'AwaitableGetDataSetMappingResult',
    'get_data_set_mapping',
    'get_data_set_mapping_output',
]

warnings.warn("""Please use one of the variants: ADLSGen2FileDataSetMapping, ADLSGen2FileSystemDataSetMapping, ADLSGen2FolderDataSetMapping, BlobContainerDataSetMapping, BlobDataSetMapping, BlobFolderDataSetMapping, KustoClusterDataSetMapping, KustoDatabaseDataSetMapping, SqlDBTableDataSetMapping, SqlDWTableDataSetMapping.""", DeprecationWarning)

@pulumi.output_type
class GetDataSetMappingResult:
    """
    A data set mapping data transfer object.
    """
    def __init__(__self__, id=None, kind=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
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
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set mapping.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetDataSetMappingResult(GetDataSetMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSetMappingResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_data_set_mapping(account_name: Optional[str] = None,
                         data_set_mapping_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         share_subscription_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSetMappingResult:
    """
    A data set mapping data transfer object.


    :param str account_name: The name of the share account.
    :param str data_set_mapping_name: The name of the dataSetMapping.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    pulumi.log.warn("""get_data_set_mapping is deprecated: Please use one of the variants: ADLSGen2FileDataSetMapping, ADLSGen2FileSystemDataSetMapping, ADLSGen2FolderDataSetMapping, BlobContainerDataSetMapping, BlobDataSetMapping, BlobFolderDataSetMapping, KustoClusterDataSetMapping, KustoDatabaseDataSetMapping, SqlDBTableDataSetMapping, SqlDWTableDataSetMapping.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetMappingName'] = data_set_mapping_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareSubscriptionName'] = share_subscription_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20191101:getDataSetMapping', __args__, opts=opts, typ=GetDataSetMappingResult).value

    return AwaitableGetDataSetMappingResult(
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_data_set_mapping)
def get_data_set_mapping_output(account_name: Optional[pulumi.Input[str]] = None,
                                data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                share_subscription_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataSetMappingResult]:
    """
    A data set mapping data transfer object.


    :param str account_name: The name of the share account.
    :param str data_set_mapping_name: The name of the dataSetMapping.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    pulumi.log.warn("""get_data_set_mapping is deprecated: Please use one of the variants: ADLSGen2FileDataSetMapping, ADLSGen2FileSystemDataSetMapping, ADLSGen2FolderDataSetMapping, BlobContainerDataSetMapping, BlobDataSetMapping, BlobFolderDataSetMapping, KustoClusterDataSetMapping, KustoDatabaseDataSetMapping, SqlDBTableDataSetMapping, SqlDWTableDataSetMapping.""")
    ...
