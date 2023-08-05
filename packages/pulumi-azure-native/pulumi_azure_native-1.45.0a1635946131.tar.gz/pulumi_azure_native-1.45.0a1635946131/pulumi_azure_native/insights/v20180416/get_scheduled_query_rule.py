# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetScheduledQueryRuleResult',
    'AwaitableGetScheduledQueryRuleResult',
    'get_scheduled_query_rule',
    'get_scheduled_query_rule_output',
]

@pulumi.output_type
class GetScheduledQueryRuleResult:
    """
    The Log Search Rule resource.
    """
    def __init__(__self__, action=None, auto_mitigate=None, created_with_api_version=None, description=None, display_name=None, enabled=None, etag=None, id=None, is_legacy_log_analytics_rule=None, kind=None, last_updated_time=None, location=None, name=None, provisioning_state=None, schedule=None, source=None, tags=None, type=None):
        if action and not isinstance(action, dict):
            raise TypeError("Expected argument 'action' to be a dict")
        pulumi.set(__self__, "action", action)
        if auto_mitigate and not isinstance(auto_mitigate, bool):
            raise TypeError("Expected argument 'auto_mitigate' to be a bool")
        pulumi.set(__self__, "auto_mitigate", auto_mitigate)
        if created_with_api_version and not isinstance(created_with_api_version, str):
            raise TypeError("Expected argument 'created_with_api_version' to be a str")
        pulumi.set(__self__, "created_with_api_version", created_with_api_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enabled and not isinstance(enabled, str):
            raise TypeError("Expected argument 'enabled' to be a str")
        pulumi.set(__self__, "enabled", enabled)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_legacy_log_analytics_rule and not isinstance(is_legacy_log_analytics_rule, bool):
            raise TypeError("Expected argument 'is_legacy_log_analytics_rule' to be a bool")
        pulumi.set(__self__, "is_legacy_log_analytics_rule", is_legacy_log_analytics_rule)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> Any:
        """
        Action needs to be taken on rule execution.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> Optional[bool]:
        """
        The flag that indicates whether the alert should be automatically resolved or not. The default is false.
        """
        return pulumi.get(self, "auto_mitigate")

    @property
    @pulumi.getter(name="createdWithApiVersion")
    def created_with_api_version(self) -> str:
        """
        The api-version used when creating this alert rule
        """
        return pulumi.get(self, "created_with_api_version")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the Log Search rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the alert rule
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[str]:
        """
        The flag which indicates whether the Log Search rule is enabled. Value should be true or false
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. 
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isLegacyLogAnalyticsRule")
    def is_legacy_log_analytics_rule(self) -> bool:
        """
        True if alert rule is legacy Log Analytic rule
        """
        return pulumi.get(self, "is_legacy_log_analytics_rule")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> str:
        """
        Last time the rule was updated in IS08601 format.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the scheduled query rule
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.ScheduleResponse']:
        """
        Schedule (Frequency, Time Window) for rule. Required for action type - AlertingAction
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def source(self) -> 'outputs.SourceResponse':
        """
        Data Source against which rule will Query Data
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetScheduledQueryRuleResult(GetScheduledQueryRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduledQueryRuleResult(
            action=self.action,
            auto_mitigate=self.auto_mitigate,
            created_with_api_version=self.created_with_api_version,
            description=self.description,
            display_name=self.display_name,
            enabled=self.enabled,
            etag=self.etag,
            id=self.id,
            is_legacy_log_analytics_rule=self.is_legacy_log_analytics_rule,
            kind=self.kind,
            last_updated_time=self.last_updated_time,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            schedule=self.schedule,
            source=self.source,
            tags=self.tags,
            type=self.type)


def get_scheduled_query_rule(resource_group_name: Optional[str] = None,
                             rule_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduledQueryRuleResult:
    """
    The Log Search Rule resource.


    :param str resource_group_name: The name of the resource group.
    :param str rule_name: The name of the rule.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleName'] = rule_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20180416:getScheduledQueryRule', __args__, opts=opts, typ=GetScheduledQueryRuleResult).value

    return AwaitableGetScheduledQueryRuleResult(
        action=__ret__.action,
        auto_mitigate=__ret__.auto_mitigate,
        created_with_api_version=__ret__.created_with_api_version,
        description=__ret__.description,
        display_name=__ret__.display_name,
        enabled=__ret__.enabled,
        etag=__ret__.etag,
        id=__ret__.id,
        is_legacy_log_analytics_rule=__ret__.is_legacy_log_analytics_rule,
        kind=__ret__.kind,
        last_updated_time=__ret__.last_updated_time,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        schedule=__ret__.schedule,
        source=__ret__.source,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_scheduled_query_rule)
def get_scheduled_query_rule_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                    rule_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduledQueryRuleResult]:
    """
    The Log Search Rule resource.


    :param str resource_group_name: The name of the resource group.
    :param str rule_name: The name of the rule.
    """
    ...
