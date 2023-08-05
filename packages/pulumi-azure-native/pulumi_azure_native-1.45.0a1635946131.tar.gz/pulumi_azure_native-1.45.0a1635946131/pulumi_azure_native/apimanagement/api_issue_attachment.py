# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApiIssueAttachmentArgs', 'ApiIssueAttachment']

@pulumi.input_type
class ApiIssueAttachmentArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 content: pulumi.Input[str],
                 content_format: pulumi.Input[str],
                 issue_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 title: pulumi.Input[str],
                 attachment_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiIssueAttachment resource.
        :param pulumi.Input[str] api_id: API identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] content: An HTTP link or Base64-encoded binary data.
        :param pulumi.Input[str] content_format: Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.
        :param pulumi.Input[str] issue_id: Issue identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] title: Filename by which the binary data will be saved.
        :param pulumi.Input[str] attachment_id: Attachment identifier within an Issue. Must be unique in the current Issue.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "content_format", content_format)
        pulumi.set(__self__, "issue_id", issue_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "title", title)
        if attachment_id is not None:
            pulumi.set(__self__, "attachment_id", attachment_id)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        An HTTP link or Base64-encoded binary data.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentFormat")
    def content_format(self) -> pulumi.Input[str]:
        """
        Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.
        """
        return pulumi.get(self, "content_format")

    @content_format.setter
    def content_format(self, value: pulumi.Input[str]):
        pulumi.set(self, "content_format", value)

    @property
    @pulumi.getter(name="issueId")
    def issue_id(self) -> pulumi.Input[str]:
        """
        Issue identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "issue_id")

    @issue_id.setter
    def issue_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "issue_id", value)

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
    def title(self) -> pulumi.Input[str]:
        """
        Filename by which the binary data will be saved.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Attachment identifier within an Issue. Must be unique in the current Issue.
        """
        return pulumi.get(self, "attachment_id")

    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attachment_id", value)


class ApiIssueAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 attachment_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_format: Optional[pulumi.Input[str]] = None,
                 issue_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Issue Attachment Contract details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: API identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] attachment_id: Attachment identifier within an Issue. Must be unique in the current Issue.
        :param pulumi.Input[str] content: An HTTP link or Base64-encoded binary data.
        :param pulumi.Input[str] content_format: Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.
        :param pulumi.Input[str] issue_id: Issue identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] title: Filename by which the binary data will be saved.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiIssueAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Issue Attachment Contract details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param ApiIssueAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiIssueAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 attachment_id: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_format: Optional[pulumi.Input[str]] = None,
                 issue_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
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
            __props__ = ApiIssueAttachmentArgs.__new__(ApiIssueAttachmentArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["attachment_id"] = attachment_id
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            if content_format is None and not opts.urn:
                raise TypeError("Missing required property 'content_format'")
            __props__.__dict__["content_format"] = content_format
            if issue_id is None and not opts.urn:
                raise TypeError("Missing required property 'issue_id'")
            __props__.__dict__["issue_id"] = issue_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:ApiIssueAttachment"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ApiIssueAttachment"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:ApiIssueAttachment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiIssueAttachment, __self__).__init__(
            'azure-native:apimanagement:ApiIssueAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiIssueAttachment':
        """
        Get an existing ApiIssueAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiIssueAttachmentArgs.__new__(ApiIssueAttachmentArgs)

        __props__.__dict__["content"] = None
        __props__.__dict__["content_format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        return ApiIssueAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        An HTTP link or Base64-encoded binary data.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentFormat")
    def content_format(self) -> pulumi.Output[str]:
        """
        Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.
        """
        return pulumi.get(self, "content_format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        Filename by which the binary data will be saved.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

