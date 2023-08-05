# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetFileShareResult',
    'AwaitableGetFileShareResult',
    'get_file_share',
    'get_file_share_output',
]

@pulumi.output_type
class GetFileShareResult:
    """
    Properties of the file share, including Id, resource name, resource type, Etag.
    """
    def __init__(__self__, etag=None, id=None, last_modified_time=None, metadata=None, name=None, share_quota=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if share_quota and not isinstance(share_quota, int):
            raise TypeError("Expected argument 'share_quota' to be a int")
        pulumi.set(__self__, "share_quota", share_quota)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Returns the date and time the share was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, str]]:
        """
        A name-value pair to associate with the share as metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> Optional[int]:
        """
        The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
        """
        return pulumi.get(self, "share_quota")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetFileShareResult(GetFileShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileShareResult(
            etag=self.etag,
            id=self.id,
            last_modified_time=self.last_modified_time,
            metadata=self.metadata,
            name=self.name,
            share_quota=self.share_quota,
            type=self.type)


def get_file_share(account_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   share_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileShareResult:
    """
    Properties of the file share, including Id, resource name, resource type, Etag.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20190401:getFileShare', __args__, opts=opts, typ=GetFileShareResult).value

    return AwaitableGetFileShareResult(
        etag=__ret__.etag,
        id=__ret__.id,
        last_modified_time=__ret__.last_modified_time,
        metadata=__ret__.metadata,
        name=__ret__.name,
        share_quota=__ret__.share_quota,
        type=__ret__.type)


@_utilities.lift_output_func(get_file_share)
def get_file_share_output(account_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          share_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileShareResult]:
    """
    Properties of the file share, including Id, resource name, resource type, Etag.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    """
    ...
