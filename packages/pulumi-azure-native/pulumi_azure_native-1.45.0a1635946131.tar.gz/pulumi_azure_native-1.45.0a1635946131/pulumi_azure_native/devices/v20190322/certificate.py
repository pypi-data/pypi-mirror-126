# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT hub.
        :param pulumi.Input[str] resource_name: The name of the IoT hub.
        :param pulumi.Input[str] certificate: base-64 representation of the X509 leaf certificate .cer file or just .pem file content.
        :param pulumi.Input[str] certificate_name: The name of the certificate
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if certificate_name is not None:
            pulumi.set(__self__, "certificate_name", certificate_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the IoT hub.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the IoT hub.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        """
        base-64 representation of the X509 leaf certificate .cer file or just .pem file content.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the certificate
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_name", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The X509 Certificate.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: base-64 representation of the X509 leaf certificate .cer file or just .pem file content.
        :param pulumi.Input[str] certificate_name: The name of the certificate
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT hub.
        :param pulumi.Input[str] resource_name_: The name of the IoT hub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The X509 Certificate.

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
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
            __props__ = CertificateArgs.__new__(CertificateArgs)

            __props__.__dict__["certificate"] = certificate
            __props__.__dict__["certificate_name"] = certificate_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:devices/v20190322:Certificate"), pulumi.Alias(type_="azure-native:devices:Certificate"), pulumi.Alias(type_="azure-nextgen:devices:Certificate"), pulumi.Alias(type_="azure-native:devices/v20170701:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20170701:Certificate"), pulumi.Alias(type_="azure-native:devices/v20180122:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20180122:Certificate"), pulumi.Alias(type_="azure-native:devices/v20180401:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20180401:Certificate"), pulumi.Alias(type_="azure-native:devices/v20181201preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20181201preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20190322preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20190322preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20190701preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20190701preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20191104:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20191104:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200301:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200301:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200401:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200401:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200615:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200615:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200710preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200710preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200801:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200801:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200831:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200831:Certificate"), pulumi.Alias(type_="azure-native:devices/v20200831preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20200831preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20210201preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20210201preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20210303preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20210303preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20210331:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20210331:Certificate"), pulumi.Alias(type_="azure-native:devices/v20210701:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20210701:Certificate"), pulumi.Alias(type_="azure-native:devices/v20210701preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20210701preview:Certificate"), pulumi.Alias(type_="azure-native:devices/v20210702preview:Certificate"), pulumi.Alias(type_="azure-nextgen:devices/v20210702preview:Certificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Certificate, __self__).__init__(
            'azure-native:devices/v20190322:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateArgs.__new__(CertificateArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The entity tag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.CertificatePropertiesResponse']:
        """
        The description of an X509 CA Certificate.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

