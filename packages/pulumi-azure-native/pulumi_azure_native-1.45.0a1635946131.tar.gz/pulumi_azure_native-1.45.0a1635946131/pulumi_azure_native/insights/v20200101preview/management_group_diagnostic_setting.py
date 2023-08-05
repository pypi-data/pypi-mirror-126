# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ManagementGroupDiagnosticSettingArgs', 'ManagementGroupDiagnosticSetting']

@pulumi.input_type
class ManagementGroupDiagnosticSettingArgs:
    def __init__(__self__, *,
                 management_group_id: pulumi.Input[str],
                 event_hub_authorization_rule_id: Optional[pulumi.Input[str]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input['ManagementGroupLogSettingsArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagementGroupDiagnosticSetting resource.
        :param pulumi.Input[str] management_group_id: The management group id.
        :param pulumi.Input[str] event_hub_authorization_rule_id: The resource Id for the event hub authorization rule.
        :param pulumi.Input[str] event_hub_name: The name of the event hub. If none is specified, the default event hub will be selected.
        :param pulumi.Input[str] location: Location of the resource
        :param pulumi.Input[Sequence[pulumi.Input['ManagementGroupLogSettingsArgs']]] logs: The list of logs settings.
        :param pulumi.Input[str] name: The name of the diagnostic setting.
        :param pulumi.Input[str] service_bus_rule_id: The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        :param pulumi.Input[str] storage_account_id: The resource ID of the storage account to which you would like to send Diagnostic Logs.
        :param pulumi.Input[str] workspace_id: The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        pulumi.set(__self__, "management_group_id", management_group_id)
        if event_hub_authorization_rule_id is not None:
            pulumi.set(__self__, "event_hub_authorization_rule_id", event_hub_authorization_rule_id)
        if event_hub_name is not None:
            pulumi.set(__self__, "event_hub_name", event_hub_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_bus_rule_id is not None:
            pulumi.set(__self__, "service_bus_rule_id", service_bus_rule_id)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[str]:
        """
        The management group id.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource Id for the event hub authorization rule.
        """
        return pulumi.get(self, "event_hub_authorization_rule_id")

    @event_hub_authorization_rule_id.setter
    def event_hub_authorization_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_authorization_rule_id", value)

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the event hub. If none is specified, the default event hub will be selected.
        """
        return pulumi.get(self, "event_hub_name")

    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagementGroupLogSettingsArgs']]]]:
        """
        The list of logs settings.
        """
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagementGroupLogSettingsArgs']]]]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the diagnostic setting.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @service_bus_rule_id.setter
    def service_bus_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_bus_rule_id", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the storage account to which you would like to send Diagnostic Logs.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class ManagementGroupDiagnosticSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 event_hub_authorization_rule_id: Optional[pulumi.Input[str]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementGroupLogSettingsArgs']]]]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The management group diagnostic setting resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] event_hub_authorization_rule_id: The resource Id for the event hub authorization rule.
        :param pulumi.Input[str] event_hub_name: The name of the event hub. If none is specified, the default event hub will be selected.
        :param pulumi.Input[str] location: Location of the resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementGroupLogSettingsArgs']]]] logs: The list of logs settings.
        :param pulumi.Input[str] management_group_id: The management group id.
        :param pulumi.Input[str] name: The name of the diagnostic setting.
        :param pulumi.Input[str] service_bus_rule_id: The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        :param pulumi.Input[str] storage_account_id: The resource ID of the storage account to which you would like to send Diagnostic Logs.
        :param pulumi.Input[str] workspace_id: The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagementGroupDiagnosticSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The management group diagnostic setting resource.

        :param str resource_name: The name of the resource.
        :param ManagementGroupDiagnosticSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementGroupDiagnosticSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 event_hub_authorization_rule_id: Optional[pulumi.Input[str]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementGroupLogSettingsArgs']]]]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagementGroupDiagnosticSettingArgs.__new__(ManagementGroupDiagnosticSettingArgs)

            __props__.__dict__["event_hub_authorization_rule_id"] = event_hub_authorization_rule_id
            __props__.__dict__["event_hub_name"] = event_hub_name
            __props__.__dict__["location"] = location
            __props__.__dict__["logs"] = logs
            if management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'management_group_id'")
            __props__.__dict__["management_group_id"] = management_group_id
            __props__.__dict__["name"] = name
            __props__.__dict__["service_bus_rule_id"] = service_bus_rule_id
            __props__.__dict__["storage_account_id"] = storage_account_id
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:insights/v20200101preview:ManagementGroupDiagnosticSetting"), pulumi.Alias(type_="azure-native:insights:ManagementGroupDiagnosticSetting"), pulumi.Alias(type_="azure-nextgen:insights:ManagementGroupDiagnosticSetting"), pulumi.Alias(type_="azure-native:insights/v20210501preview:ManagementGroupDiagnosticSetting"), pulumi.Alias(type_="azure-nextgen:insights/v20210501preview:ManagementGroupDiagnosticSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementGroupDiagnosticSetting, __self__).__init__(
            'azure-native:insights/v20200101preview:ManagementGroupDiagnosticSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementGroupDiagnosticSetting':
        """
        Get an existing ManagementGroupDiagnosticSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagementGroupDiagnosticSettingArgs.__new__(ManagementGroupDiagnosticSettingArgs)

        __props__.__dict__["event_hub_authorization_rule_id"] = None
        __props__.__dict__["event_hub_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["logs"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["service_bus_rule_id"] = None
        __props__.__dict__["storage_account_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workspace_id"] = None
        return ManagementGroupDiagnosticSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource Id for the event hub authorization rule.
        """
        return pulumi.get(self, "event_hub_authorization_rule_id")

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the event hub. If none is specified, the default event hub will be selected.
        """
        return pulumi.get(self, "event_hub_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Output[Optional[Sequence['outputs.ManagementGroupLogSettingsResponse']]]:
        """
        The list of logs settings.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the storage account to which you would like to send Diagnostic Logs.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[Optional[str]]:
        """
        The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        return pulumi.get(self, "workspace_id")

