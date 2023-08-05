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

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 first_name: pulumi.Input[str],
                 last_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 confirmation: Optional[pulumi.Input[Union[str, 'Confirmation']]] = None,
                 identities: Optional[pulumi.Input[Sequence[pulumi.Input['UserIdentityContractArgs']]]] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UserState']]] = None,
                 uid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] email: Email address. Must not be empty and must be unique within the service instance.
        :param pulumi.Input[str] first_name: First name.
        :param pulumi.Input[str] last_name: Last name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Union[str, 'Confirmation']] confirmation: Determines the type of confirmation e-mail that will be sent to the newly created user.
        :param pulumi.Input[Sequence[pulumi.Input['UserIdentityContractArgs']]] identities: Collection of user identities.
        :param pulumi.Input[str] note: Optional note about a user set by the administrator.
        :param pulumi.Input[str] password: User Password. If no value is provided, a default password is generated.
        :param pulumi.Input[Union[str, 'UserState']] state: Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.
        :param pulumi.Input[str] uid: User identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "first_name", first_name)
        pulumi.set(__self__, "last_name", last_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if confirmation is not None:
            pulumi.set(__self__, "confirmation", confirmation)
        if identities is not None:
            pulumi.set(__self__, "identities", identities)
        if note is not None:
            pulumi.set(__self__, "note", note)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if state is None:
            state = 'active'
        if state is not None:
            pulumi.set(__self__, "state", state)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email address. Must not be empty and must be unique within the service instance.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[str]:
        """
        First name.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[str]:
        """
        Last name.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "last_name", value)

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
    @pulumi.getter
    def confirmation(self) -> Optional[pulumi.Input[Union[str, 'Confirmation']]]:
        """
        Determines the type of confirmation e-mail that will be sent to the newly created user.
        """
        return pulumi.get(self, "confirmation")

    @confirmation.setter
    def confirmation(self, value: Optional[pulumi.Input[Union[str, 'Confirmation']]]):
        pulumi.set(self, "confirmation", value)

    @property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserIdentityContractArgs']]]]:
        """
        Collection of user identities.
        """
        return pulumi.get(self, "identities")

    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserIdentityContractArgs']]]]):
        pulumi.set(self, "identities", value)

    @property
    @pulumi.getter
    def note(self) -> Optional[pulumi.Input[str]]:
        """
        Optional note about a user set by the administrator.
        """
        return pulumi.get(self, "note")

    @note.setter
    def note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "note", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        User Password. If no value is provided, a default password is generated.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'UserState']]]:
        """
        Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'UserState']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        User identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 confirmation: Optional[pulumi.Input[Union[str, 'Confirmation']]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserIdentityContractArgs']]]]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UserState']]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        User details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'Confirmation']] confirmation: Determines the type of confirmation e-mail that will be sent to the newly created user.
        :param pulumi.Input[str] email: Email address. Must not be empty and must be unique within the service instance.
        :param pulumi.Input[str] first_name: First name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserIdentityContractArgs']]]] identities: Collection of user identities.
        :param pulumi.Input[str] last_name: Last name.
        :param pulumi.Input[str] note: Optional note about a user set by the administrator.
        :param pulumi.Input[str] password: User Password. If no value is provided, a default password is generated.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Union[str, 'UserState']] state: Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.
        :param pulumi.Input[str] uid: User identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        User details.

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 confirmation: Optional[pulumi.Input[Union[str, 'Confirmation']]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserIdentityContractArgs']]]]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'UserState']]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
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
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["confirmation"] = confirmation
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if first_name is None and not opts.urn:
                raise TypeError("Missing required property 'first_name'")
            __props__.__dict__["first_name"] = first_name
            __props__.__dict__["identities"] = identities
            if last_name is None and not opts.urn:
                raise TypeError("Missing required property 'last_name'")
            __props__.__dict__["last_name"] = last_name
            __props__.__dict__["note"] = note
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if state is None:
                state = 'active'
            __props__.__dict__["state"] = state
            __props__.__dict__["uid"] = uid
            __props__.__dict__["groups"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["registration_date"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:User"), pulumi.Alias(type_="azure-native:apimanagement:User"), pulumi.Alias(type_="azure-nextgen:apimanagement:User"), pulumi.Alias(type_="azure-native:apimanagement/v20160707:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20160707:User"), pulumi.Alias(type_="azure-native:apimanagement/v20161010:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20161010:User"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:User"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:User"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:User"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:User"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:User"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:User"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:User"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:User"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:User"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:User"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:User")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(User, __self__).__init__(
            'azure-native:apimanagement/v20180101:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserArgs.__new__(UserArgs)

        __props__.__dict__["email"] = None
        __props__.__dict__["first_name"] = None
        __props__.__dict__["groups"] = None
        __props__.__dict__["identities"] = None
        __props__.__dict__["last_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["note"] = None
        __props__.__dict__["registration_date"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        """
        Email address.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[str]]:
        """
        First name.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Sequence['outputs.GroupContractPropertiesResponse']]:
        """
        Collection of groups user is part of.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def identities(self) -> pulumi.Output[Optional[Sequence['outputs.UserIdentityContractResponse']]]:
        """
        Collection of user identities.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[str]]:
        """
        Last name.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def note(self) -> pulumi.Output[Optional[str]]:
        """
        Optional note about a user set by the administrator.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> pulumi.Output[Optional[str]]:
        """
        Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "registration_date")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

