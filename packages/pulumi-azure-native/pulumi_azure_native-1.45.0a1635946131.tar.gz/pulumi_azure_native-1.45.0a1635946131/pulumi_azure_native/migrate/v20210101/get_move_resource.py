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
    'GetMoveResourceResult',
    'AwaitableGetMoveResourceResult',
    'get_move_resource',
    'get_move_resource_output',
]

@pulumi.output_type
class GetMoveResourceResult:
    """
    Defines the move resource.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.MoveResourcePropertiesResponse':
        """
        Defines the move resource properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetMoveResourceResult(GetMoveResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMoveResourceResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_move_resource(move_collection_name: Optional[str] = None,
                      move_resource_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMoveResourceResult:
    """
    Defines the move resource.


    :param str move_collection_name: The Move Collection Name.
    :param str move_resource_name: The Move Resource Name.
    :param str resource_group_name: The Resource Group Name.
    """
    __args__ = dict()
    __args__['moveCollectionName'] = move_collection_name
    __args__['moveResourceName'] = move_resource_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20210101:getMoveResource', __args__, opts=opts, typ=GetMoveResourceResult).value

    return AwaitableGetMoveResourceResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_move_resource)
def get_move_resource_output(move_collection_name: Optional[pulumi.Input[str]] = None,
                             move_resource_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMoveResourceResult]:
    """
    Defines the move resource.


    :param str move_collection_name: The Move Collection Name.
    :param str move_resource_name: The Move Resource Name.
    :param str resource_group_name: The Resource Group Name.
    """
    ...
