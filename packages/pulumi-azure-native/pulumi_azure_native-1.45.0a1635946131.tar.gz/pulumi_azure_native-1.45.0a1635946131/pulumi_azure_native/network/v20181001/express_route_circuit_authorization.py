# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ExpressRouteCircuitAuthorizationInitArgs', 'ExpressRouteCircuitAuthorization']

@pulumi.input_type
class ExpressRouteCircuitAuthorizationInitArgs:
    def __init__(__self__, *,
                 circuit_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 authorization_name: Optional[pulumi.Input[str]] = None,
                 authorization_use_status: Optional[pulumi.Input[Union[str, 'AuthorizationUseStatus']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExpressRouteCircuitAuthorization resource.
        :param pulumi.Input[str] circuit_name: The name of the express route circuit.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] authorization_key: The authorization key.
        :param pulumi.Input[str] authorization_name: The name of the authorization.
        :param pulumi.Input[Union[str, 'AuthorizationUseStatus']] authorization_use_status: AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] provisioning_state: Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        pulumi.set(__self__, "circuit_name", circuit_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorization_key is not None:
            pulumi.set(__self__, "authorization_key", authorization_key)
        if authorization_name is not None:
            pulumi.set(__self__, "authorization_name", authorization_name)
        if authorization_use_status is not None:
            pulumi.set(__self__, "authorization_use_status", authorization_use_status)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter(name="circuitName")
    def circuit_name(self) -> pulumi.Input[str]:
        """
        The name of the express route circuit.
        """
        return pulumi.get(self, "circuit_name")

    @circuit_name.setter
    def circuit_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "circuit_name", value)

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
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        The authorization key.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter(name="authorizationName")
    def authorization_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the authorization.
        """
        return pulumi.get(self, "authorization_name")

    @authorization_name.setter
    def authorization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_name", value)

    @property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> Optional[pulumi.Input[Union[str, 'AuthorizationUseStatus']]]:
        """
        AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
        """
        return pulumi.get(self, "authorization_use_status")

    @authorization_use_status.setter
    def authorization_use_status(self, value: Optional[pulumi.Input[Union[str, 'AuthorizationUseStatus']]]):
        pulumi.set(self, "authorization_use_status", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)


class ExpressRouteCircuitAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 authorization_name: Optional[pulumi.Input[str]] = None,
                 authorization_use_status: Optional[pulumi.Input[Union[str, 'AuthorizationUseStatus']]] = None,
                 circuit_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Authorization in an ExpressRouteCircuit resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_key: The authorization key.
        :param pulumi.Input[str] authorization_name: The name of the authorization.
        :param pulumi.Input[Union[str, 'AuthorizationUseStatus']] authorization_use_status: AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
        :param pulumi.Input[str] circuit_name: The name of the express route circuit.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] provisioning_state: Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteCircuitAuthorizationInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Authorization in an ExpressRouteCircuit resource.

        :param str resource_name: The name of the resource.
        :param ExpressRouteCircuitAuthorizationInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteCircuitAuthorizationInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 authorization_name: Optional[pulumi.Input[str]] = None,
                 authorization_use_status: Optional[pulumi.Input[Union[str, 'AuthorizationUseStatus']]] = None,
                 circuit_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExpressRouteCircuitAuthorizationInitArgs.__new__(ExpressRouteCircuitAuthorizationInitArgs)

            __props__.__dict__["authorization_key"] = authorization_key
            __props__.__dict__["authorization_name"] = authorization_name
            __props__.__dict__["authorization_use_status"] = authorization_use_status
            if circuit_name is None and not opts.urn:
                raise TypeError("Missing required property 'circuit_name'")
            __props__.__dict__["circuit_name"] = circuit_name
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20181001:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20150501preview:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20150501preview:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20150615:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20150615:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20160330:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20160330:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20160601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20160601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20160901:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20160901:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20161201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20161201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20170301:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20170301:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20170601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20170601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20170801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20170801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20170901:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20170901:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20171001:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20171001:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20171101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20171101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20180101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20180101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20180201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20180201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20180401:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20180401:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20180601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20180601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20180701:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20180701:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20180801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20181101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20181201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20190201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20190201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20190401:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20190601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20190701:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20190701:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20190801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20190901:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20191101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20191201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20191201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20200301:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20200401:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20200501:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20200601:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20200701:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20200801:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20201101:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20210201:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20210301:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteCircuitAuthorization"), pulumi.Alias(type_="azure-nextgen:network/v20210501:ExpressRouteCircuitAuthorization")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteCircuitAuthorization, __self__).__init__(
            'azure-native:network/v20181001:ExpressRouteCircuitAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteCircuitAuthorization':
        """
        Get an existing ExpressRouteCircuitAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteCircuitAuthorizationInitArgs.__new__(ExpressRouteCircuitAuthorizationInitArgs)

        __props__.__dict__["authorization_key"] = None
        __props__.__dict__["authorization_use_status"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        return ExpressRouteCircuitAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[str]]:
        """
        The authorization key.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> pulumi.Output[Optional[str]]:
        """
        AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
        """
        return pulumi.get(self, "authorization_use_status")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

