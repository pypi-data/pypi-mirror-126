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

__all__ = ['RemediationAtResourceArgs', 'RemediationAtResource']

@pulumi.input_type
class RemediationAtResourceArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 deployment_status: Optional[pulumi.Input['RemediationDeploymentSummaryArgs']] = None,
                 filters: Optional[pulumi.Input['RemediationFiltersArgs']] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 remediation_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RemediationAtResource resource.
        :param pulumi.Input[str] resource_id: Resource ID.
        :param pulumi.Input['RemediationDeploymentSummaryArgs'] deployment_status: The deployment status summary for all deployments created by the remediation.
        :param pulumi.Input['RemediationFiltersArgs'] filters: The filters that will be applied to determine which resources to remediate.
        :param pulumi.Input[str] policy_assignment_id: The resource ID of the policy assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_reference_id: The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[str] remediation_name: The name of the remediation.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        if deployment_status is not None:
            pulumi.set(__self__, "deployment_status", deployment_status)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if policy_assignment_id is not None:
            pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        if policy_definition_reference_id is not None:
            pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)
        if remediation_name is not None:
            pulumi.set(__self__, "remediation_name", remediation_name)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> Optional[pulumi.Input['RemediationDeploymentSummaryArgs']]:
        """
        The deployment status summary for all deployments created by the remediation.
        """
        return pulumi.get(self, "deployment_status")

    @deployment_status.setter
    def deployment_status(self, value: Optional[pulumi.Input['RemediationDeploymentSummaryArgs']]):
        pulumi.set(self, "deployment_status", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['RemediationFiltersArgs']]:
        """
        The filters that will be applied to determine which resources to remediate.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['RemediationFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the policy assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @policy_definition_reference_id.setter
    def policy_definition_reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_reference_id", value)

    @property
    @pulumi.getter(name="remediationName")
    def remediation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the remediation.
        """
        return pulumi.get(self, "remediation_name")

    @remediation_name.setter
    def remediation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation_name", value)


class RemediationAtResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_status: Optional[pulumi.Input[pulumi.InputType['RemediationDeploymentSummaryArgs']]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['RemediationFiltersArgs']]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 remediation_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The remediation definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RemediationDeploymentSummaryArgs']] deployment_status: The deployment status summary for all deployments created by the remediation.
        :param pulumi.Input[pulumi.InputType['RemediationFiltersArgs']] filters: The filters that will be applied to determine which resources to remediate.
        :param pulumi.Input[str] policy_assignment_id: The resource ID of the policy assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_reference_id: The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[str] remediation_name: The name of the remediation.
        :param pulumi.Input[str] resource_id: Resource ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RemediationAtResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The remediation definition.

        :param str resource_name: The name of the resource.
        :param RemediationAtResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RemediationAtResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_status: Optional[pulumi.Input[pulumi.InputType['RemediationDeploymentSummaryArgs']]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['RemediationFiltersArgs']]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 remediation_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = RemediationAtResourceArgs.__new__(RemediationAtResourceArgs)

            __props__.__dict__["deployment_status"] = deployment_status
            __props__.__dict__["filters"] = filters
            __props__.__dict__["policy_assignment_id"] = policy_assignment_id
            __props__.__dict__["policy_definition_reference_id"] = policy_definition_reference_id
            __props__.__dict__["remediation_name"] = remediation_name
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["created_on"] = None
            __props__.__dict__["last_updated_on"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:policyinsights/v20180701preview:RemediationAtResource"), pulumi.Alias(type_="azure-native:policyinsights:RemediationAtResource"), pulumi.Alias(type_="azure-nextgen:policyinsights:RemediationAtResource"), pulumi.Alias(type_="azure-native:policyinsights/v20190701:RemediationAtResource"), pulumi.Alias(type_="azure-nextgen:policyinsights/v20190701:RemediationAtResource"), pulumi.Alias(type_="azure-native:policyinsights/v20211001:RemediationAtResource"), pulumi.Alias(type_="azure-nextgen:policyinsights/v20211001:RemediationAtResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RemediationAtResource, __self__).__init__(
            'azure-native:policyinsights/v20180701preview:RemediationAtResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RemediationAtResource':
        """
        Get an existing RemediationAtResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RemediationAtResourceArgs.__new__(RemediationAtResourceArgs)

        __props__.__dict__["created_on"] = None
        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["filters"] = None
        __props__.__dict__["last_updated_on"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy_assignment_id"] = None
        __props__.__dict__["policy_definition_reference_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return RemediationAtResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        The time at which the remediation was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[Optional['outputs.RemediationDeploymentSummaryResponse']]:
        """
        The deployment status summary for all deployments created by the remediation.
        """
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional['outputs.RemediationFiltersResponse']]:
        """
        The filters that will be applied to determine which resources to remediate.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> pulumi.Output[str]:
        """
        The time at which the remediation was last updated.
        """
        return pulumi.get(self, "last_updated_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the remediation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the policy assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the remediation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the remediation.
        """
        return pulumi.get(self, "type")

