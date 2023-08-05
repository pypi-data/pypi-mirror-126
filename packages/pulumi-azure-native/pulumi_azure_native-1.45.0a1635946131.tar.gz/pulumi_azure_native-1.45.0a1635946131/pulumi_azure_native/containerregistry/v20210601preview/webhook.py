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

__all__ = ['WebhookArgs', 'Webhook']

@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]],
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_uri: pulumi.Input[str],
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'WebhookStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Webhook resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]] actions: The list of actions that trigger the webhook to post notifications.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] service_uri: The service URI for the webhook to post notifications.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Custom headers that will be added to the webhook notifications.
        :param pulumi.Input[str] location: The location of the webhook. This cannot be changed after the resource is created.
        :param pulumi.Input[str] scope: The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events.
        :param pulumi.Input[Union[str, 'WebhookStatus']] status: The status of the webhook at the time the operation was called.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the webhook.
        :param pulumi.Input[str] webhook_name: The name of the webhook.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_uri", service_uri)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if webhook_name is not None:
            pulumi.set(__self__, "webhook_name", webhook_name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]]:
        """
        The list of actions that trigger the webhook to post notifications.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> pulumi.Input[str]:
        """
        The service URI for the webhook to post notifications.
        """
        return pulumi.get(self, "service_uri")

    @service_uri.setter
    def service_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_uri", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom headers that will be added to the webhook notifications.
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the webhook. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'WebhookStatus']]]:
        """
        The status of the webhook at the time the operation was called.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'WebhookStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags for the webhook.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="webhookName")
    def webhook_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the webhook.
        """
        return pulumi.get(self, "webhook_name")

    @webhook_name.setter
    def webhook_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_name", value)


class Webhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 service_uri: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'WebhookStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a webhook for a container registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]] actions: The list of actions that trigger the webhook to post notifications.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Custom headers that will be added to the webhook notifications.
        :param pulumi.Input[str] location: The location of the webhook. This cannot be changed after the resource is created.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] scope: The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events.
        :param pulumi.Input[str] service_uri: The service URI for the webhook to post notifications.
        :param pulumi.Input[Union[str, 'WebhookStatus']] status: The status of the webhook at the time the operation was called.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the webhook.
        :param pulumi.Input[str] webhook_name: The name of the webhook.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a webhook for a container registry.

        :param str resource_name: The name of the resource.
        :param WebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebhookAction']]]]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 service_uri: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'WebhookStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 webhook_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebhookArgs.__new__(WebhookArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["custom_headers"] = custom_headers
            __props__.__dict__["location"] = location
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            if service_uri is None and not opts.urn:
                raise TypeError("Missing required property 'service_uri'")
            __props__.__dict__["service_uri"] = service_uri
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["webhook_name"] = webhook_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:containerregistry/v20210601preview:Webhook"), pulumi.Alias(type_="azure-native:containerregistry:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry:Webhook"), pulumi.Alias(type_="azure-native:containerregistry/v20170601preview:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20170601preview:Webhook"), pulumi.Alias(type_="azure-native:containerregistry/v20171001:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20171001:Webhook"), pulumi.Alias(type_="azure-native:containerregistry/v20190501:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20190501:Webhook"), pulumi.Alias(type_="azure-native:containerregistry/v20191201preview:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20191201preview:Webhook"), pulumi.Alias(type_="azure-native:containerregistry/v20201101preview:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20201101preview:Webhook"), pulumi.Alias(type_="azure-native:containerregistry/v20210801preview:Webhook"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20210801preview:Webhook")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Webhook, __self__).__init__(
            'azure-native:containerregistry/v20210601preview:Webhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Webhook':
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebhookArgs.__new__(WebhookArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Webhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of actions that trigger the webhook to post notifications.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource. This cannot be changed after the resource is created.
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the webhook at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the webhook at the time the operation was called.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

