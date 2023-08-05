# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['Python2PackageArgs', 'Python2Package']

@pulumi.input_type
class Python2PackageArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 content_link: pulumi.Input['ContentLinkArgs'],
                 resource_group_name: pulumi.Input[str],
                 package_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Python2Package resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input['ContentLinkArgs'] content_link: Gets or sets the module content link.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] package_name: The name of python package.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "content_link", content_link)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if package_name is not None:
            pulumi.set(__self__, "package_name", package_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Input['ContentLinkArgs']:
        """
        Gets or sets the module content link.
        """
        return pulumi.get(self, "content_link")

    @content_link.setter
    def content_link(self, value: pulumi.Input['ContentLinkArgs']):
        pulumi.set(self, "content_link", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of python package.
        """
        return pulumi.get(self, "package_name")

    @package_name.setter
    def package_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "package_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the tags attached to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Python2Package(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 content_link: Optional[pulumi.Input[pulumi.InputType['ContentLinkArgs']]] = None,
                 package_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Definition of the module type.
        API Version: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[pulumi.InputType['ContentLinkArgs']] content_link: Gets or sets the module content link.
        :param pulumi.Input[str] package_name: The name of python package.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Python2PackageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the module type.
        API Version: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param Python2PackageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Python2PackageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 content_link: Optional[pulumi.Input[pulumi.InputType['ContentLinkArgs']]] = None,
                 package_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = Python2PackageArgs.__new__(Python2PackageArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            if content_link is None and not opts.urn:
                raise TypeError("Missing required property 'content_link'")
            __props__.__dict__["content_link"] = content_link
            __props__.__dict__["package_name"] = package_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["activity_count"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["is_composite"] = None
            __props__.__dict__["is_global"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["size_in_bytes"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:automation:Python2Package"), pulumi.Alias(type_="azure-native:automation/v20180630:Python2Package"), pulumi.Alias(type_="azure-nextgen:automation/v20180630:Python2Package"), pulumi.Alias(type_="azure-native:automation/v20190601:Python2Package"), pulumi.Alias(type_="azure-nextgen:automation/v20190601:Python2Package"), pulumi.Alias(type_="azure-native:automation/v20200113preview:Python2Package"), pulumi.Alias(type_="azure-nextgen:automation/v20200113preview:Python2Package")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Python2Package, __self__).__init__(
            'azure-native:automation:Python2Package',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Python2Package':
        """
        Get an existing Python2Package resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = Python2PackageArgs.__new__(Python2PackageArgs)

        __props__.__dict__["activity_count"] = None
        __props__.__dict__["content_link"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["is_composite"] = None
        __props__.__dict__["is_global"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["size_in_bytes"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Python2Package(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activityCount")
    def activity_count(self) -> pulumi.Output[Optional[int]]:
        """
        Gets or sets the activity count of the module.
        """
        return pulumi.get(self, "activity_count")

    @property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Output[Optional['outputs.ContentLinkResponse']]:
        """
        Gets or sets the contentLink of the module.
        """
        return pulumi.get(self, "content_link")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output[Optional['outputs.ModuleErrorInfoResponse']]:
        """
        Gets or sets the error info of the module.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isComposite")
    def is_composite(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets type of module, if its composite or not.
        """
        return pulumi.get(self, "is_composite")

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets the isGlobal flag of the module.
        """
        return pulumi.get(self, "is_global")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the provisioning state of the module.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[Optional[float]]:
        """
        Gets or sets the size in bytes of the module.
        """
        return pulumi.get(self, "size_in_bytes")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the version of the module.
        """
        return pulumi.get(self, "version")

