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

__all__ = ['CustomAssessmentAutomationArgs', 'CustomAssessmentAutomation']

@pulumi.input_type
class CustomAssessmentAutomationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 compressed_query: Optional[pulumi.Input[str]] = None,
                 custom_assessment_automation_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 implementation_effort: Optional[pulumi.Input[Union[str, 'ImplementationEffortEnum']]] = None,
                 remediation_description: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'SeverityEnum']]] = None,
                 supported_cloud: Optional[pulumi.Input[Union[str, 'SupportedCloudEnum']]] = None,
                 user_impact: Optional[pulumi.Input[Union[str, 'UserImpactEnum']]] = None):
        """
        The set of arguments for constructing a CustomAssessmentAutomation resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] compressed_query: Base 64 encoded KQL query representing the assessment automation results required.
        :param pulumi.Input[str] custom_assessment_automation_name: Name of the Custom Assessment Automation.
        :param pulumi.Input[str] description: The description to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[Union[str, 'ImplementationEffortEnum']] implementation_effort: The implementation effort to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[str] remediation_description: The remediation description to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[Union[str, 'SeverityEnum']] severity: The severity to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[Union[str, 'SupportedCloudEnum']] supported_cloud: Relevant cloud for the custom assessment automation.
        :param pulumi.Input[Union[str, 'UserImpactEnum']] user_impact: The user impact to relate to the assessments generated by this assessment automation.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if compressed_query is not None:
            pulumi.set(__self__, "compressed_query", compressed_query)
        if custom_assessment_automation_name is not None:
            pulumi.set(__self__, "custom_assessment_automation_name", custom_assessment_automation_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if implementation_effort is not None:
            pulumi.set(__self__, "implementation_effort", implementation_effort)
        if remediation_description is not None:
            pulumi.set(__self__, "remediation_description", remediation_description)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if supported_cloud is not None:
            pulumi.set(__self__, "supported_cloud", supported_cloud)
        if user_impact is not None:
            pulumi.set(__self__, "user_impact", user_impact)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="compressedQuery")
    def compressed_query(self) -> Optional[pulumi.Input[str]]:
        """
        Base 64 encoded KQL query representing the assessment automation results required.
        """
        return pulumi.get(self, "compressed_query")

    @compressed_query.setter
    def compressed_query(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compressed_query", value)

    @property
    @pulumi.getter(name="customAssessmentAutomationName")
    def custom_assessment_automation_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Custom Assessment Automation.
        """
        return pulumi.get(self, "custom_assessment_automation_name")

    @custom_assessment_automation_name.setter
    def custom_assessment_automation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_assessment_automation_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> Optional[pulumi.Input[Union[str, 'ImplementationEffortEnum']]]:
        """
        The implementation effort to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "implementation_effort")

    @implementation_effort.setter
    def implementation_effort(self, value: Optional[pulumi.Input[Union[str, 'ImplementationEffortEnum']]]):
        pulumi.set(self, "implementation_effort", value)

    @property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[pulumi.Input[str]]:
        """
        The remediation description to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "remediation_description")

    @remediation_description.setter
    def remediation_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation_description", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[Union[str, 'SeverityEnum']]]:
        """
        The severity to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[Union[str, 'SeverityEnum']]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="supportedCloud")
    def supported_cloud(self) -> Optional[pulumi.Input[Union[str, 'SupportedCloudEnum']]]:
        """
        Relevant cloud for the custom assessment automation.
        """
        return pulumi.get(self, "supported_cloud")

    @supported_cloud.setter
    def supported_cloud(self, value: Optional[pulumi.Input[Union[str, 'SupportedCloudEnum']]]):
        pulumi.set(self, "supported_cloud", value)

    @property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> Optional[pulumi.Input[Union[str, 'UserImpactEnum']]]:
        """
        The user impact to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "user_impact")

    @user_impact.setter
    def user_impact(self, value: Optional[pulumi.Input[Union[str, 'UserImpactEnum']]]):
        pulumi.set(self, "user_impact", value)


class CustomAssessmentAutomation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compressed_query: Optional[pulumi.Input[str]] = None,
                 custom_assessment_automation_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 implementation_effort: Optional[pulumi.Input[Union[str, 'ImplementationEffortEnum']]] = None,
                 remediation_description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'SeverityEnum']]] = None,
                 supported_cloud: Optional[pulumi.Input[Union[str, 'SupportedCloudEnum']]] = None,
                 user_impact: Optional[pulumi.Input[Union[str, 'UserImpactEnum']]] = None,
                 __props__=None):
        """
        Custom Assessment Automation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compressed_query: Base 64 encoded KQL query representing the assessment automation results required.
        :param pulumi.Input[str] custom_assessment_automation_name: Name of the Custom Assessment Automation.
        :param pulumi.Input[str] description: The description to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[Union[str, 'ImplementationEffortEnum']] implementation_effort: The implementation effort to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[str] remediation_description: The remediation description to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Union[str, 'SeverityEnum']] severity: The severity to relate to the assessments generated by this assessment automation.
        :param pulumi.Input[Union[str, 'SupportedCloudEnum']] supported_cloud: Relevant cloud for the custom assessment automation.
        :param pulumi.Input[Union[str, 'UserImpactEnum']] user_impact: The user impact to relate to the assessments generated by this assessment automation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomAssessmentAutomationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Custom Assessment Automation

        :param str resource_name: The name of the resource.
        :param CustomAssessmentAutomationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomAssessmentAutomationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compressed_query: Optional[pulumi.Input[str]] = None,
                 custom_assessment_automation_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 implementation_effort: Optional[pulumi.Input[Union[str, 'ImplementationEffortEnum']]] = None,
                 remediation_description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'SeverityEnum']]] = None,
                 supported_cloud: Optional[pulumi.Input[Union[str, 'SupportedCloudEnum']]] = None,
                 user_impact: Optional[pulumi.Input[Union[str, 'UserImpactEnum']]] = None,
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
            __props__ = CustomAssessmentAutomationArgs.__new__(CustomAssessmentAutomationArgs)

            __props__.__dict__["compressed_query"] = compressed_query
            __props__.__dict__["custom_assessment_automation_name"] = custom_assessment_automation_name
            __props__.__dict__["description"] = description
            __props__.__dict__["implementation_effort"] = implementation_effort
            __props__.__dict__["remediation_description"] = remediation_description
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["severity"] = severity
            __props__.__dict__["supported_cloud"] = supported_cloud
            __props__.__dict__["user_impact"] = user_impact
            __props__.__dict__["assessment_key"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:security/v20210701preview:CustomAssessmentAutomation"), pulumi.Alias(type_="azure-native:security:CustomAssessmentAutomation"), pulumi.Alias(type_="azure-nextgen:security:CustomAssessmentAutomation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomAssessmentAutomation, __self__).__init__(
            'azure-native:security/v20210701preview:CustomAssessmentAutomation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomAssessmentAutomation':
        """
        Get an existing CustomAssessmentAutomation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomAssessmentAutomationArgs.__new__(CustomAssessmentAutomationArgs)

        __props__.__dict__["assessment_key"] = None
        __props__.__dict__["compressed_query"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["implementation_effort"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["remediation_description"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["supported_cloud"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_impact"] = None
        return CustomAssessmentAutomation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assessmentKey")
    def assessment_key(self) -> pulumi.Output[Optional[str]]:
        """
        The assessment metadata key used when an assessment is generated for this assessment automation.
        """
        return pulumi.get(self, "assessment_key")

    @property
    @pulumi.getter(name="compressedQuery")
    def compressed_query(self) -> pulumi.Output[Optional[str]]:
        """
        GZip encoded KQL query representing the assessment automation results required.
        """
        return pulumi.get(self, "compressed_query")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> pulumi.Output[Optional[str]]:
        """
        The implementation effort to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "implementation_effort")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> pulumi.Output[Optional[str]]:
        """
        The remediation description to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "remediation_description")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[str]]:
        """
        The severity to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="supportedCloud")
    def supported_cloud(self) -> pulumi.Output[Optional[str]]:
        """
        Relevant cloud for the custom assessment automation.
        """
        return pulumi.get(self, "supported_cloud")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> pulumi.Output[Optional[str]]:
        """
        The user impact to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "user_impact")

