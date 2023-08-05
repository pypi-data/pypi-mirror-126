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

__all__ = ['LiveEventArgs', 'LiveEvent']

@pulumi.input_type
class LiveEventArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 input: pulumi.Input['LiveEventInputArgs'],
                 resource_group_name: pulumi.Input[str],
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 cross_site_access_policies: Optional[pulumi.Input['CrossSiteAccessPoliciesArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input['LiveEventEncodingArgs']] = None,
                 live_event_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input['LiveEventPreviewArgs']] = None,
                 stream_options: Optional[pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vanity_url: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a LiveEvent resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input['LiveEventInputArgs'] input: The Live Event input.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[bool] auto_start: The flag indicates if auto start the Live Event.
        :param pulumi.Input['CrossSiteAccessPoliciesArgs'] cross_site_access_policies: The Live Event access policies.
        :param pulumi.Input[str] description: The Live Event description.
        :param pulumi.Input['LiveEventEncodingArgs'] encoding: The Live Event encoding.
        :param pulumi.Input[str] live_event_name: The name of the Live Event.
        :param pulumi.Input[str] location: The Azure Region of the resource.
        :param pulumi.Input['LiveEventPreviewArgs'] preview: The Live Event preview.
        :param pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]] stream_options: The stream options.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] vanity_url: The Live Event vanity URL flag.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "input", input)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_start is not None:
            pulumi.set(__self__, "auto_start", auto_start)
        if cross_site_access_policies is not None:
            pulumi.set(__self__, "cross_site_access_policies", cross_site_access_policies)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if live_event_name is not None:
            pulumi.set(__self__, "live_event_name", live_event_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if preview is not None:
            pulumi.set(__self__, "preview", preview)
        if stream_options is not None:
            pulumi.set(__self__, "stream_options", stream_options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vanity_url is not None:
            pulumi.set(__self__, "vanity_url", vanity_url)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Media Services account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def input(self) -> pulumi.Input['LiveEventInputArgs']:
        """
        The Live Event input.
        """
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: pulumi.Input['LiveEventInputArgs']):
        pulumi.set(self, "input", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag indicates if auto start the Live Event.
        """
        return pulumi.get(self, "auto_start")

    @auto_start.setter
    def auto_start(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_start", value)

    @property
    @pulumi.getter(name="crossSiteAccessPolicies")
    def cross_site_access_policies(self) -> Optional[pulumi.Input['CrossSiteAccessPoliciesArgs']]:
        """
        The Live Event access policies.
        """
        return pulumi.get(self, "cross_site_access_policies")

    @cross_site_access_policies.setter
    def cross_site_access_policies(self, value: Optional[pulumi.Input['CrossSiteAccessPoliciesArgs']]):
        pulumi.set(self, "cross_site_access_policies", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Live Event description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input['LiveEventEncodingArgs']]:
        """
        The Live Event encoding.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input['LiveEventEncodingArgs']]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="liveEventName")
    def live_event_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Live Event.
        """
        return pulumi.get(self, "live_event_name")

    @live_event_name.setter
    def live_event_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "live_event_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input['LiveEventPreviewArgs']]:
        """
        The Live Event preview.
        """
        return pulumi.get(self, "preview")

    @preview.setter
    def preview(self, value: Optional[pulumi.Input['LiveEventPreviewArgs']]):
        pulumi.set(self, "preview", value)

    @property
    @pulumi.getter(name="streamOptions")
    def stream_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]]]:
        """
        The stream options.
        """
        return pulumi.get(self, "stream_options")

    @stream_options.setter
    def stream_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]]]):
        pulumi.set(self, "stream_options", value)

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
    @pulumi.getter(name="vanityUrl")
    def vanity_url(self) -> Optional[pulumi.Input[bool]]:
        """
        The Live Event vanity URL flag.
        """
        return pulumi.get(self, "vanity_url")

    @vanity_url.setter
    def vanity_url(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "vanity_url", value)


class LiveEvent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 cross_site_access_policies: Optional[pulumi.Input[pulumi.InputType['CrossSiteAccessPoliciesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[pulumi.InputType['LiveEventEncodingArgs']]] = None,
                 input: Optional[pulumi.Input[pulumi.InputType['LiveEventInputArgs']]] = None,
                 live_event_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[pulumi.InputType['LiveEventPreviewArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_options: Optional[pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vanity_url: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The Live Event.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[bool] auto_start: The flag indicates if auto start the Live Event.
        :param pulumi.Input[pulumi.InputType['CrossSiteAccessPoliciesArgs']] cross_site_access_policies: The Live Event access policies.
        :param pulumi.Input[str] description: The Live Event description.
        :param pulumi.Input[pulumi.InputType['LiveEventEncodingArgs']] encoding: The Live Event encoding.
        :param pulumi.Input[pulumi.InputType['LiveEventInputArgs']] input: The Live Event input.
        :param pulumi.Input[str] live_event_name: The name of the Live Event.
        :param pulumi.Input[str] location: The Azure Region of the resource.
        :param pulumi.Input[pulumi.InputType['LiveEventPreviewArgs']] preview: The Live Event preview.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]] stream_options: The stream options.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] vanity_url: The Live Event vanity URL flag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LiveEventArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Live Event.

        :param str resource_name: The name of the resource.
        :param LiveEventArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LiveEventArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 cross_site_access_policies: Optional[pulumi.Input[pulumi.InputType['CrossSiteAccessPoliciesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[pulumi.InputType['LiveEventEncodingArgs']]] = None,
                 input: Optional[pulumi.Input[pulumi.InputType['LiveEventInputArgs']]] = None,
                 live_event_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[pulumi.InputType['LiveEventPreviewArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_options: Optional[pulumi.Input[Sequence[pulumi.Input['StreamOptionsFlag']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vanity_url: Optional[pulumi.Input[bool]] = None,
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
            __props__ = LiveEventArgs.__new__(LiveEventArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["auto_start"] = auto_start
            __props__.__dict__["cross_site_access_policies"] = cross_site_access_policies
            __props__.__dict__["description"] = description
            __props__.__dict__["encoding"] = encoding
            if input is None and not opts.urn:
                raise TypeError("Missing required property 'input'")
            __props__.__dict__["input"] = input
            __props__.__dict__["live_event_name"] = live_event_name
            __props__.__dict__["location"] = location
            __props__.__dict__["preview"] = preview
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["stream_options"] = stream_options
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vanity_url"] = vanity_url
            __props__.__dict__["created"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:media/v20180601preview:LiveEvent"), pulumi.Alias(type_="azure-native:media:LiveEvent"), pulumi.Alias(type_="azure-nextgen:media:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20180330preview:LiveEvent"), pulumi.Alias(type_="azure-nextgen:media/v20180330preview:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20180701:LiveEvent"), pulumi.Alias(type_="azure-nextgen:media/v20180701:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20190501preview:LiveEvent"), pulumi.Alias(type_="azure-nextgen:media/v20190501preview:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20200501:LiveEvent"), pulumi.Alias(type_="azure-nextgen:media/v20200501:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20210601:LiveEvent"), pulumi.Alias(type_="azure-nextgen:media/v20210601:LiveEvent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LiveEvent, __self__).__init__(
            'azure-native:media/v20180601preview:LiveEvent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LiveEvent':
        """
        Get an existing LiveEvent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LiveEventArgs.__new__(LiveEventArgs)

        __props__.__dict__["created"] = None
        __props__.__dict__["cross_site_access_policies"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["encoding"] = None
        __props__.__dict__["input"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["preview"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["stream_options"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vanity_url"] = None
        return LiveEvent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The exact time the Live Event was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="crossSiteAccessPolicies")
    def cross_site_access_policies(self) -> pulumi.Output[Optional['outputs.CrossSiteAccessPoliciesResponse']]:
        """
        The Live Event access policies.
        """
        return pulumi.get(self, "cross_site_access_policies")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The Live Event description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encoding(self) -> pulumi.Output[Optional['outputs.LiveEventEncodingResponse']]:
        """
        The Live Event encoding.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter
    def input(self) -> pulumi.Output['outputs.LiveEventInputResponse']:
        """
        The Live Event input.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The exact time the Live Event was last modified.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Region of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional['outputs.LiveEventPreviewResponse']]:
        """
        The Live Event preview.
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the Live Event.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        The resource state of the Live Event.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="streamOptions")
    def stream_options(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The stream options.
        """
        return pulumi.get(self, "stream_options")

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
    @pulumi.getter(name="vanityUrl")
    def vanity_url(self) -> pulumi.Output[Optional[bool]]:
        """
        The Live Event vanity URL flag.
        """
        return pulumi.get(self, "vanity_url")

