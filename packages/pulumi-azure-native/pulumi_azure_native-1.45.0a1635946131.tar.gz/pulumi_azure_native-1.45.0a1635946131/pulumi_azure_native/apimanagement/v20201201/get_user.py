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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    User details.
    """
    def __init__(__self__, email=None, first_name=None, groups=None, id=None, identities=None, last_name=None, name=None, note=None, registration_date=None, state=None, type=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if note and not isinstance(note, str):
            raise TypeError("Expected argument 'note' to be a str")
        pulumi.set(__self__, "note", note)
        if registration_date and not isinstance(registration_date, str):
            raise TypeError("Expected argument 'registration_date' to be a str")
        pulumi.set(__self__, "registration_date", registration_date)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email address.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[str]:
        """
        First name.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GroupContractPropertiesResponse']:
        """
        Collection of groups user is part of.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Optional[Sequence['outputs.UserIdentityContractResponse']]:
        """
        Collection of user identities.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[str]:
        """
        Last name.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def note(self) -> Optional[str]:
        """
        Optional note about a user set by the administrator.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> Optional[str]:
        """
        Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "registration_date")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            email=self.email,
            first_name=self.first_name,
            groups=self.groups,
            id=self.id,
            identities=self.identities,
            last_name=self.last_name,
            name=self.name,
            note=self.note,
            registration_date=self.registration_date,
            state=self.state,
            type=self.type)


def get_user(resource_group_name: Optional[str] = None,
             service_name: Optional[str] = None,
             user_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    User details.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    :param str user_id: User identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['userId'] = user_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20201201:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        email=__ret__.email,
        first_name=__ret__.first_name,
        groups=__ret__.groups,
        id=__ret__.id,
        identities=__ret__.identities,
        last_name=__ret__.last_name,
        name=__ret__.name,
        note=__ret__.note,
        registration_date=__ret__.registration_date,
        state=__ret__.state,
        type=__ret__.type)


@_utilities.lift_output_func(get_user)
def get_user_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                    service_name: Optional[pulumi.Input[str]] = None,
                    user_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserResult]:
    """
    User details.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    :param str user_id: User identifier. Must be unique in the current API Management service instance.
    """
    ...
