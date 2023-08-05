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

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 administrators: Optional[pulumi.Input['ServerExternalAdministratorArgs']] = None,
                 federated_client_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ResourceIdentityArgs']] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimal_tls_version: Optional[pulumi.Input[str]] = None,
                 primary_user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]] = None,
                 restrict_outbound_network_access: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Server resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] administrator_login: Administrator username for the server. Once created it cannot be changed.
        :param pulumi.Input[str] administrator_login_password: The administrator login password (required for server creation).
        :param pulumi.Input['ServerExternalAdministratorArgs'] administrators: The Azure Active Directory identity of the server.
        :param pulumi.Input[str] federated_client_id: The Client id used for cross tenant CMK scenario
        :param pulumi.Input['ResourceIdentityArgs'] identity: The Azure Active Directory identity of the server.
        :param pulumi.Input[str] key_id: A CMK URI of the key to use for encryption.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] minimal_tls_version: Minimal TLS version. Allowed values: '1.0', '1.1', '1.2'
        :param pulumi.Input[str] primary_user_assigned_identity_id: The resource id of a user assigned identity to be used by default.
        :param pulumi.Input[Union[str, 'ServerNetworkAccessFlag']] public_network_access: Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        :param pulumi.Input[Union[str, 'ServerNetworkAccessFlag']] restrict_outbound_network_access: Whether or not to restrict outbound network access for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] version: The version of the server.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if administrator_login is not None:
            pulumi.set(__self__, "administrator_login", administrator_login)
        if administrator_login_password is not None:
            pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        if administrators is not None:
            pulumi.set(__self__, "administrators", administrators)
        if federated_client_id is not None:
            pulumi.set(__self__, "federated_client_id", federated_client_id)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if key_id is not None:
            pulumi.set(__self__, "key_id", key_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if minimal_tls_version is not None:
            pulumi.set(__self__, "minimal_tls_version", minimal_tls_version)
        if primary_user_assigned_identity_id is not None:
            pulumi.set(__self__, "primary_user_assigned_identity_id", primary_user_assigned_identity_id)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if restrict_outbound_network_access is not None:
            pulumi.set(__self__, "restrict_outbound_network_access", restrict_outbound_network_access)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[pulumi.Input[str]]:
        """
        Administrator username for the server. Once created it cannot be changed.
        """
        return pulumi.get(self, "administrator_login")

    @administrator_login.setter
    def administrator_login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login", value)

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[str]]:
        """
        The administrator login password (required for server creation).
        """
        return pulumi.get(self, "administrator_login_password")

    @administrator_login_password.setter
    def administrator_login_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login_password", value)

    @property
    @pulumi.getter
    def administrators(self) -> Optional[pulumi.Input['ServerExternalAdministratorArgs']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "administrators")

    @administrators.setter
    def administrators(self, value: Optional[pulumi.Input['ServerExternalAdministratorArgs']]):
        pulumi.set(self, "administrators", value)

    @property
    @pulumi.getter(name="federatedClientId")
    def federated_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Client id used for cross tenant CMK scenario
        """
        return pulumi.get(self, "federated_client_id")

    @federated_client_id.setter
    def federated_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "federated_client_id", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ResourceIdentityArgs']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[str]]:
        """
        A CMK URI of the key to use for encryption.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[pulumi.Input[str]]:
        """
        Minimal TLS version. Allowed values: '1.0', '1.1', '1.2'
        """
        return pulumi.get(self, "minimal_tls_version")

    @minimal_tls_version.setter
    def minimal_tls_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minimal_tls_version", value)

    @property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of a user assigned identity to be used by default.
        """
        return pulumi.get(self, "primary_user_assigned_identity_id")

    @primary_user_assigned_identity_id.setter
    def primary_user_assigned_identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_user_assigned_identity_id", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]]:
        """
        Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="restrictOutboundNetworkAccess")
    def restrict_outbound_network_access(self) -> Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]]:
        """
        Whether or not to restrict outbound network access for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "restrict_outbound_network_access")

    @restrict_outbound_network_access.setter
    def restrict_outbound_network_access(self, value: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]]):
        pulumi.set(self, "restrict_outbound_network_access", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the server.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Server(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 administrators: Optional[pulumi.Input[pulumi.InputType['ServerExternalAdministratorArgs']]] = None,
                 federated_client_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimal_tls_version: Optional[pulumi.Input[str]] = None,
                 primary_user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restrict_outbound_network_access: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure SQL Database server.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: Administrator username for the server. Once created it cannot be changed.
        :param pulumi.Input[str] administrator_login_password: The administrator login password (required for server creation).
        :param pulumi.Input[pulumi.InputType['ServerExternalAdministratorArgs']] administrators: The Azure Active Directory identity of the server.
        :param pulumi.Input[str] federated_client_id: The Client id used for cross tenant CMK scenario
        :param pulumi.Input[pulumi.InputType['ResourceIdentityArgs']] identity: The Azure Active Directory identity of the server.
        :param pulumi.Input[str] key_id: A CMK URI of the key to use for encryption.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] minimal_tls_version: Minimal TLS version. Allowed values: '1.0', '1.1', '1.2'
        :param pulumi.Input[str] primary_user_assigned_identity_id: The resource id of a user assigned identity to be used by default.
        :param pulumi.Input[Union[str, 'ServerNetworkAccessFlag']] public_network_access: Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Union[str, 'ServerNetworkAccessFlag']] restrict_outbound_network_access: Whether or not to restrict outbound network access for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] version: The version of the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL Database server.

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 administrators: Optional[pulumi.Input[pulumi.InputType['ServerExternalAdministratorArgs']]] = None,
                 federated_client_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimal_tls_version: Optional[pulumi.Input[str]] = None,
                 primary_user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restrict_outbound_network_access: Optional[pulumi.Input[Union[str, 'ServerNetworkAccessFlag']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["administrator_login"] = administrator_login
            __props__.__dict__["administrator_login_password"] = administrator_login_password
            __props__.__dict__["administrators"] = administrators
            __props__.__dict__["federated_client_id"] = federated_client_id
            __props__.__dict__["identity"] = identity
            __props__.__dict__["key_id"] = key_id
            __props__.__dict__["location"] = location
            __props__.__dict__["minimal_tls_version"] = minimal_tls_version
            __props__.__dict__["primary_user_assigned_identity_id"] = primary_user_assigned_identity_id
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restrict_outbound_network_access"] = restrict_outbound_network_access
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["fully_qualified_domain_name"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workspace_feature"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:sql/v20210201preview:Server"), pulumi.Alias(type_="azure-native:sql:Server"), pulumi.Alias(type_="azure-nextgen:sql:Server"), pulumi.Alias(type_="azure-native:sql/v20140401:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20140401:Server"), pulumi.Alias(type_="azure-native:sql/v20150501preview:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20150501preview:Server"), pulumi.Alias(type_="azure-native:sql/v20190601preview:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20190601preview:Server"), pulumi.Alias(type_="azure-native:sql/v20200202preview:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20200202preview:Server"), pulumi.Alias(type_="azure-native:sql/v20200801preview:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20200801preview:Server"), pulumi.Alias(type_="azure-native:sql/v20201101preview:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20201101preview:Server"), pulumi.Alias(type_="azure-native:sql/v20210501preview:Server"), pulumi.Alias(type_="azure-nextgen:sql/v20210501preview:Server")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Server, __self__).__init__(
            'azure-native:sql/v20210201preview:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerArgs.__new__(ServerArgs)

        __props__.__dict__["administrator_login"] = None
        __props__.__dict__["administrators"] = None
        __props__.__dict__["federated_client_id"] = None
        __props__.__dict__["fully_qualified_domain_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["key_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["minimal_tls_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["primary_user_assigned_identity_id"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["restrict_outbound_network_access"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        __props__.__dict__["workspace_feature"] = None
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        Administrator username for the server. Once created it cannot be changed.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter
    def administrators(self) -> pulumi.Output[Optional['outputs.ServerExternalAdministratorResponse']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "administrators")

    @property
    @pulumi.getter(name="federatedClientId")
    def federated_client_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Client id used for cross tenant CMK scenario
        """
        return pulumi.get(self, "federated_client_id")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name of the server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[Optional[str]]:
        """
        A CMK URI of the key to use for encryption.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of sql server. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> pulumi.Output[Optional[str]]:
        """
        Minimal TLS version. Allowed values: '1.0', '1.1', '1.2'
        """
        return pulumi.get(self, "minimal_tls_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource id of a user assigned identity to be used by default.
        """
        return pulumi.get(self, "primary_user_assigned_identity_id")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.ServerPrivateEndpointConnectionResponse']]:
        """
        List of private endpoint connections on a server
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="restrictOutboundNetworkAccess")
    def restrict_outbound_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Whether or not to restrict outbound network access for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "restrict_outbound_network_access")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the server.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the server.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="workspaceFeature")
    def workspace_feature(self) -> pulumi.Output[str]:
        """
        Whether or not existing server has a workspace created and if it allows connection from workspace
        """
        return pulumi.get(self, "workspace_feature")

