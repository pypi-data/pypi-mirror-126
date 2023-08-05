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

__all__ = ['FailoverGroupArgs', 'FailoverGroup']

@pulumi.input_type
class FailoverGroupArgs:
    def __init__(__self__, *,
                 partner_servers: pulumi.Input[Sequence[pulumi.Input['PartnerInfoArgs']]],
                 read_write_endpoint: pulumi.Input['FailoverGroupReadWriteEndpointArgs'],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 failover_group_name: Optional[pulumi.Input[str]] = None,
                 read_only_endpoint: Optional[pulumi.Input['FailoverGroupReadOnlyEndpointArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FailoverGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['PartnerInfoArgs']]] partner_servers: List of partner server information for the failover group.
        :param pulumi.Input['FailoverGroupReadWriteEndpointArgs'] read_write_endpoint: Read-write endpoint of the failover group instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server containing the failover group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: List of databases in the failover group.
        :param pulumi.Input[str] failover_group_name: The name of the failover group.
        :param pulumi.Input['FailoverGroupReadOnlyEndpointArgs'] read_only_endpoint: Read-only endpoint of the failover group instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "partner_servers", partner_servers)
        pulumi.set(__self__, "read_write_endpoint", read_write_endpoint)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if databases is not None:
            pulumi.set(__self__, "databases", databases)
        if failover_group_name is not None:
            pulumi.set(__self__, "failover_group_name", failover_group_name)
        if read_only_endpoint is not None:
            pulumi.set(__self__, "read_only_endpoint", read_only_endpoint)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Input[Sequence[pulumi.Input['PartnerInfoArgs']]]:
        """
        List of partner server information for the failover group.
        """
        return pulumi.get(self, "partner_servers")

    @partner_servers.setter
    def partner_servers(self, value: pulumi.Input[Sequence[pulumi.Input['PartnerInfoArgs']]]):
        pulumi.set(self, "partner_servers", value)

    @property
    @pulumi.getter(name="readWriteEndpoint")
    def read_write_endpoint(self) -> pulumi.Input['FailoverGroupReadWriteEndpointArgs']:
        """
        Read-write endpoint of the failover group instance.
        """
        return pulumi.get(self, "read_write_endpoint")

    @read_write_endpoint.setter
    def read_write_endpoint(self, value: pulumi.Input['FailoverGroupReadWriteEndpointArgs']):
        pulumi.set(self, "read_write_endpoint", value)

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
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server containing the failover group.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of databases in the failover group.
        """
        return pulumi.get(self, "databases")

    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "databases", value)

    @property
    @pulumi.getter(name="failoverGroupName")
    def failover_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the failover group.
        """
        return pulumi.get(self, "failover_group_name")

    @failover_group_name.setter
    def failover_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "failover_group_name", value)

    @property
    @pulumi.getter(name="readOnlyEndpoint")
    def read_only_endpoint(self) -> Optional[pulumi.Input['FailoverGroupReadOnlyEndpointArgs']]:
        """
        Read-only endpoint of the failover group instance.
        """
        return pulumi.get(self, "read_only_endpoint")

    @read_only_endpoint.setter
    def read_only_endpoint(self, value: Optional[pulumi.Input['FailoverGroupReadOnlyEndpointArgs']]):
        pulumi.set(self, "read_only_endpoint", value)

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


class FailoverGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 failover_group_name: Optional[pulumi.Input[str]] = None,
                 partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PartnerInfoArgs']]]]] = None,
                 read_only_endpoint: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadOnlyEndpointArgs']]] = None,
                 read_write_endpoint: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A failover group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: List of databases in the failover group.
        :param pulumi.Input[str] failover_group_name: The name of the failover group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PartnerInfoArgs']]]] partner_servers: List of partner server information for the failover group.
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadOnlyEndpointArgs']] read_only_endpoint: Read-only endpoint of the failover group instance.
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointArgs']] read_write_endpoint: Read-write endpoint of the failover group instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server containing the failover group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FailoverGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A failover group.

        :param str resource_name: The name of the resource.
        :param FailoverGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FailoverGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 failover_group_name: Optional[pulumi.Input[str]] = None,
                 partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PartnerInfoArgs']]]]] = None,
                 read_only_endpoint: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadOnlyEndpointArgs']]] = None,
                 read_write_endpoint: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = FailoverGroupArgs.__new__(FailoverGroupArgs)

            __props__.__dict__["databases"] = databases
            __props__.__dict__["failover_group_name"] = failover_group_name
            if partner_servers is None and not opts.urn:
                raise TypeError("Missing required property 'partner_servers'")
            __props__.__dict__["partner_servers"] = partner_servers
            __props__.__dict__["read_only_endpoint"] = read_only_endpoint
            if read_write_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'read_write_endpoint'")
            __props__.__dict__["read_write_endpoint"] = read_write_endpoint
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["replication_role"] = None
            __props__.__dict__["replication_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:sql/v20210201preview:FailoverGroup"), pulumi.Alias(type_="azure-native:sql:FailoverGroup"), pulumi.Alias(type_="azure-nextgen:sql:FailoverGroup"), pulumi.Alias(type_="azure-native:sql/v20150501preview:FailoverGroup"), pulumi.Alias(type_="azure-nextgen:sql/v20150501preview:FailoverGroup"), pulumi.Alias(type_="azure-native:sql/v20200202preview:FailoverGroup"), pulumi.Alias(type_="azure-nextgen:sql/v20200202preview:FailoverGroup"), pulumi.Alias(type_="azure-native:sql/v20200801preview:FailoverGroup"), pulumi.Alias(type_="azure-nextgen:sql/v20200801preview:FailoverGroup"), pulumi.Alias(type_="azure-native:sql/v20201101preview:FailoverGroup"), pulumi.Alias(type_="azure-nextgen:sql/v20201101preview:FailoverGroup"), pulumi.Alias(type_="azure-native:sql/v20210501preview:FailoverGroup"), pulumi.Alias(type_="azure-nextgen:sql/v20210501preview:FailoverGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FailoverGroup, __self__).__init__(
            'azure-native:sql/v20210201preview:FailoverGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FailoverGroup':
        """
        Get an existing FailoverGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FailoverGroupArgs.__new__(FailoverGroupArgs)

        __props__.__dict__["databases"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_servers"] = None
        __props__.__dict__["read_only_endpoint"] = None
        __props__.__dict__["read_write_endpoint"] = None
        __props__.__dict__["replication_role"] = None
        __props__.__dict__["replication_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return FailoverGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of databases in the failover group.
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Output[Sequence['outputs.PartnerInfoResponse']]:
        """
        List of partner server information for the failover group.
        """
        return pulumi.get(self, "partner_servers")

    @property
    @pulumi.getter(name="readOnlyEndpoint")
    def read_only_endpoint(self) -> pulumi.Output[Optional['outputs.FailoverGroupReadOnlyEndpointResponse']]:
        """
        Read-only endpoint of the failover group instance.
        """
        return pulumi.get(self, "read_only_endpoint")

    @property
    @pulumi.getter(name="readWriteEndpoint")
    def read_write_endpoint(self) -> pulumi.Output['outputs.FailoverGroupReadWriteEndpointResponse']:
        """
        Read-write endpoint of the failover group instance.
        """
        return pulumi.get(self, "read_write_endpoint")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> pulumi.Output[str]:
        """
        Local replication role of the failover group instance.
        """
        return pulumi.get(self, "replication_role")

    @property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> pulumi.Output[str]:
        """
        Replication state of the failover group instance.
        """
        return pulumi.get(self, "replication_state")

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

