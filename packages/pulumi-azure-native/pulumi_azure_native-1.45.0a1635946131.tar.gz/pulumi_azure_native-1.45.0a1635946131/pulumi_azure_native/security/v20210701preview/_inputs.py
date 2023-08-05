# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'CspmMonitorAwsOfferingNativeCloudConnectionArgs',
    'CspmMonitorAwsOfferingArgs',
    'DefenderForContainersAwsOfferingCloudWatchToKinesisArgs',
    'DefenderForContainersAwsOfferingKinesisToS3Args',
    'DefenderForContainersAwsOfferingKubernetesScubaReaderArgs',
    'DefenderForContainersAwsOfferingKubernetesServiceArgs',
    'DefenderForContainersAwsOfferingArgs',
    'DefenderForServersAwsOfferingArcAutoProvisioningArgs',
    'DefenderForServersAwsOfferingDefenderForServersArgs',
    'DefenderForServersAwsOfferingServicePrincipalSecretMetadataArgs',
    'DefenderForServersAwsOfferingArgs',
    'SecurityConnectorPropertiesOrganizationalDataArgs',
]

@pulumi.input_type
class CspmMonitorAwsOfferingNativeCloudConnectionArgs:
    def __init__(__self__, *,
                 cloud_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The native cloud connection configuration
        :param pulumi.Input[str] cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")

    @cloud_role_arn.setter
    def cloud_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_role_arn", value)


@pulumi.input_type
class CspmMonitorAwsOfferingArgs:
    def __init__(__self__, *,
                 offering_type: pulumi.Input[str],
                 native_cloud_connection: Optional[pulumi.Input['CspmMonitorAwsOfferingNativeCloudConnectionArgs']] = None):
        """
        The CSPM monitoring for AWS offering configurations
        :param pulumi.Input[str] offering_type: The type of the security offering.
               Expected value is 'CspmMonitorAws'.
        :param pulumi.Input['CspmMonitorAwsOfferingNativeCloudConnectionArgs'] native_cloud_connection: The native cloud connection configuration
        """
        pulumi.set(__self__, "offering_type", 'CspmMonitorAws')
        if native_cloud_connection is not None:
            pulumi.set(__self__, "native_cloud_connection", native_cloud_connection)

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> pulumi.Input[str]:
        """
        The type of the security offering.
        Expected value is 'CspmMonitorAws'.
        """
        return pulumi.get(self, "offering_type")

    @offering_type.setter
    def offering_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "offering_type", value)

    @property
    @pulumi.getter(name="nativeCloudConnection")
    def native_cloud_connection(self) -> Optional[pulumi.Input['CspmMonitorAwsOfferingNativeCloudConnectionArgs']]:
        """
        The native cloud connection configuration
        """
        return pulumi.get(self, "native_cloud_connection")

    @native_cloud_connection.setter
    def native_cloud_connection(self, value: Optional[pulumi.Input['CspmMonitorAwsOfferingNativeCloudConnectionArgs']]):
        pulumi.set(self, "native_cloud_connection", value)


@pulumi.input_type
class DefenderForContainersAwsOfferingCloudWatchToKinesisArgs:
    def __init__(__self__, *,
                 cloud_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The cloudwatch to kinesis connection configuration
        :param pulumi.Input[str] cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")

    @cloud_role_arn.setter
    def cloud_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_role_arn", value)


@pulumi.input_type
class DefenderForContainersAwsOfferingKinesisToS3Args:
    def __init__(__self__, *,
                 cloud_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The kinesis to s3 connection configuration
        :param pulumi.Input[str] cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")

    @cloud_role_arn.setter
    def cloud_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_role_arn", value)


@pulumi.input_type
class DefenderForContainersAwsOfferingKubernetesScubaReaderArgs:
    def __init__(__self__, *,
                 cloud_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The kubernetes to scuba connection configuration
        :param pulumi.Input[str] cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")

    @cloud_role_arn.setter
    def cloud_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_role_arn", value)


@pulumi.input_type
class DefenderForContainersAwsOfferingKubernetesServiceArgs:
    def __init__(__self__, *,
                 cloud_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The kubernetes service connection configuration
        :param pulumi.Input[str] cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")

    @cloud_role_arn.setter
    def cloud_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_role_arn", value)


@pulumi.input_type
class DefenderForContainersAwsOfferingArgs:
    def __init__(__self__, *,
                 offering_type: pulumi.Input[str],
                 cloud_watch_to_kinesis: Optional[pulumi.Input['DefenderForContainersAwsOfferingCloudWatchToKinesisArgs']] = None,
                 kinesis_to_s3: Optional[pulumi.Input['DefenderForContainersAwsOfferingKinesisToS3Args']] = None,
                 kubernetes_scuba_reader: Optional[pulumi.Input['DefenderForContainersAwsOfferingKubernetesScubaReaderArgs']] = None,
                 kubernetes_service: Optional[pulumi.Input['DefenderForContainersAwsOfferingKubernetesServiceArgs']] = None):
        """
        The Defender for Containers AWS offering configurations
        :param pulumi.Input[str] offering_type: The type of the security offering.
               Expected value is 'DefenderForContainersAws'.
        :param pulumi.Input['DefenderForContainersAwsOfferingCloudWatchToKinesisArgs'] cloud_watch_to_kinesis: The cloudwatch to kinesis connection configuration
        :param pulumi.Input['DefenderForContainersAwsOfferingKinesisToS3Args'] kinesis_to_s3: The kinesis to s3 connection configuration
        :param pulumi.Input['DefenderForContainersAwsOfferingKubernetesScubaReaderArgs'] kubernetes_scuba_reader: The kubernetes to scuba connection configuration
        :param pulumi.Input['DefenderForContainersAwsOfferingKubernetesServiceArgs'] kubernetes_service: The kubernetes service connection configuration
        """
        pulumi.set(__self__, "offering_type", 'DefenderForContainersAws')
        if cloud_watch_to_kinesis is not None:
            pulumi.set(__self__, "cloud_watch_to_kinesis", cloud_watch_to_kinesis)
        if kinesis_to_s3 is not None:
            pulumi.set(__self__, "kinesis_to_s3", kinesis_to_s3)
        if kubernetes_scuba_reader is not None:
            pulumi.set(__self__, "kubernetes_scuba_reader", kubernetes_scuba_reader)
        if kubernetes_service is not None:
            pulumi.set(__self__, "kubernetes_service", kubernetes_service)

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> pulumi.Input[str]:
        """
        The type of the security offering.
        Expected value is 'DefenderForContainersAws'.
        """
        return pulumi.get(self, "offering_type")

    @offering_type.setter
    def offering_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "offering_type", value)

    @property
    @pulumi.getter(name="cloudWatchToKinesis")
    def cloud_watch_to_kinesis(self) -> Optional[pulumi.Input['DefenderForContainersAwsOfferingCloudWatchToKinesisArgs']]:
        """
        The cloudwatch to kinesis connection configuration
        """
        return pulumi.get(self, "cloud_watch_to_kinesis")

    @cloud_watch_to_kinesis.setter
    def cloud_watch_to_kinesis(self, value: Optional[pulumi.Input['DefenderForContainersAwsOfferingCloudWatchToKinesisArgs']]):
        pulumi.set(self, "cloud_watch_to_kinesis", value)

    @property
    @pulumi.getter(name="kinesisToS3")
    def kinesis_to_s3(self) -> Optional[pulumi.Input['DefenderForContainersAwsOfferingKinesisToS3Args']]:
        """
        The kinesis to s3 connection configuration
        """
        return pulumi.get(self, "kinesis_to_s3")

    @kinesis_to_s3.setter
    def kinesis_to_s3(self, value: Optional[pulumi.Input['DefenderForContainersAwsOfferingKinesisToS3Args']]):
        pulumi.set(self, "kinesis_to_s3", value)

    @property
    @pulumi.getter(name="kubernetesScubaReader")
    def kubernetes_scuba_reader(self) -> Optional[pulumi.Input['DefenderForContainersAwsOfferingKubernetesScubaReaderArgs']]:
        """
        The kubernetes to scuba connection configuration
        """
        return pulumi.get(self, "kubernetes_scuba_reader")

    @kubernetes_scuba_reader.setter
    def kubernetes_scuba_reader(self, value: Optional[pulumi.Input['DefenderForContainersAwsOfferingKubernetesScubaReaderArgs']]):
        pulumi.set(self, "kubernetes_scuba_reader", value)

    @property
    @pulumi.getter(name="kubernetesService")
    def kubernetes_service(self) -> Optional[pulumi.Input['DefenderForContainersAwsOfferingKubernetesServiceArgs']]:
        """
        The kubernetes service connection configuration
        """
        return pulumi.get(self, "kubernetes_service")

    @kubernetes_service.setter
    def kubernetes_service(self, value: Optional[pulumi.Input['DefenderForContainersAwsOfferingKubernetesServiceArgs']]):
        pulumi.set(self, "kubernetes_service", value)


@pulumi.input_type
class DefenderForServersAwsOfferingArcAutoProvisioningArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 service_principal_secret_metadata: Optional[pulumi.Input['DefenderForServersAwsOfferingServicePrincipalSecretMetadataArgs']] = None):
        """
        The ARC autoprovisioning configuration
        :param pulumi.Input[bool] enabled: Is arc auto provisioning enabled
        :param pulumi.Input['DefenderForServersAwsOfferingServicePrincipalSecretMetadataArgs'] service_principal_secret_metadata: Metadata of Service Principal secret for autoprovisioning
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if service_principal_secret_metadata is not None:
            pulumi.set(__self__, "service_principal_secret_metadata", service_principal_secret_metadata)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is arc auto provisioning enabled
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="servicePrincipalSecretMetadata")
    def service_principal_secret_metadata(self) -> Optional[pulumi.Input['DefenderForServersAwsOfferingServicePrincipalSecretMetadataArgs']]:
        """
        Metadata of Service Principal secret for autoprovisioning
        """
        return pulumi.get(self, "service_principal_secret_metadata")

    @service_principal_secret_metadata.setter
    def service_principal_secret_metadata(self, value: Optional[pulumi.Input['DefenderForServersAwsOfferingServicePrincipalSecretMetadataArgs']]):
        pulumi.set(self, "service_principal_secret_metadata", value)


@pulumi.input_type
class DefenderForServersAwsOfferingDefenderForServersArgs:
    def __init__(__self__, *,
                 cloud_role_arn: Optional[pulumi.Input[str]] = None):
        """
        The Defender for servers connection configuration
        :param pulumi.Input[str] cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")

    @cloud_role_arn.setter
    def cloud_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_role_arn", value)


@pulumi.input_type
class DefenderForServersAwsOfferingServicePrincipalSecretMetadataArgs:
    def __init__(__self__, *,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 parameter_name_in_store: Optional[pulumi.Input[str]] = None,
                 parameter_store_region: Optional[pulumi.Input[str]] = None):
        """
        Metadata of Service Principal secret for autoprovisioning
        :param pulumi.Input[str] expiry_date: expiration date of service principal secret
        :param pulumi.Input[str] parameter_name_in_store: name of secret resource in parameter store
        :param pulumi.Input[str] parameter_store_region: region of parameter store where secret is kept
        """
        if expiry_date is not None:
            pulumi.set(__self__, "expiry_date", expiry_date)
        if parameter_name_in_store is not None:
            pulumi.set(__self__, "parameter_name_in_store", parameter_name_in_store)
        if parameter_store_region is not None:
            pulumi.set(__self__, "parameter_store_region", parameter_store_region)

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[pulumi.Input[str]]:
        """
        expiration date of service principal secret
        """
        return pulumi.get(self, "expiry_date")

    @expiry_date.setter
    def expiry_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_date", value)

    @property
    @pulumi.getter(name="parameterNameInStore")
    def parameter_name_in_store(self) -> Optional[pulumi.Input[str]]:
        """
        name of secret resource in parameter store
        """
        return pulumi.get(self, "parameter_name_in_store")

    @parameter_name_in_store.setter
    def parameter_name_in_store(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_name_in_store", value)

    @property
    @pulumi.getter(name="parameterStoreRegion")
    def parameter_store_region(self) -> Optional[pulumi.Input[str]]:
        """
        region of parameter store where secret is kept
        """
        return pulumi.get(self, "parameter_store_region")

    @parameter_store_region.setter
    def parameter_store_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_store_region", value)


@pulumi.input_type
class DefenderForServersAwsOfferingArgs:
    def __init__(__self__, *,
                 offering_type: pulumi.Input[str],
                 arc_auto_provisioning: Optional[pulumi.Input['DefenderForServersAwsOfferingArcAutoProvisioningArgs']] = None,
                 defender_for_servers: Optional[pulumi.Input['DefenderForServersAwsOfferingDefenderForServersArgs']] = None):
        """
        The Defender for Servers AWS offering configurations
        :param pulumi.Input[str] offering_type: The type of the security offering.
               Expected value is 'DefenderForServersAWS'.
        :param pulumi.Input['DefenderForServersAwsOfferingArcAutoProvisioningArgs'] arc_auto_provisioning: The ARC autoprovisioning configuration
        :param pulumi.Input['DefenderForServersAwsOfferingDefenderForServersArgs'] defender_for_servers: The Defender for servers connection configuration
        """
        pulumi.set(__self__, "offering_type", 'DefenderForServersAWS')
        if arc_auto_provisioning is not None:
            pulumi.set(__self__, "arc_auto_provisioning", arc_auto_provisioning)
        if defender_for_servers is not None:
            pulumi.set(__self__, "defender_for_servers", defender_for_servers)

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> pulumi.Input[str]:
        """
        The type of the security offering.
        Expected value is 'DefenderForServersAWS'.
        """
        return pulumi.get(self, "offering_type")

    @offering_type.setter
    def offering_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "offering_type", value)

    @property
    @pulumi.getter(name="arcAutoProvisioning")
    def arc_auto_provisioning(self) -> Optional[pulumi.Input['DefenderForServersAwsOfferingArcAutoProvisioningArgs']]:
        """
        The ARC autoprovisioning configuration
        """
        return pulumi.get(self, "arc_auto_provisioning")

    @arc_auto_provisioning.setter
    def arc_auto_provisioning(self, value: Optional[pulumi.Input['DefenderForServersAwsOfferingArcAutoProvisioningArgs']]):
        pulumi.set(self, "arc_auto_provisioning", value)

    @property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(self) -> Optional[pulumi.Input['DefenderForServersAwsOfferingDefenderForServersArgs']]:
        """
        The Defender for servers connection configuration
        """
        return pulumi.get(self, "defender_for_servers")

    @defender_for_servers.setter
    def defender_for_servers(self, value: Optional[pulumi.Input['DefenderForServersAwsOfferingDefenderForServersArgs']]):
        pulumi.set(self, "defender_for_servers", value)


@pulumi.input_type
class SecurityConnectorPropertiesOrganizationalDataArgs:
    def __init__(__self__, *,
                 excluded_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 organization_membership_type: Optional[pulumi.Input[Union[str, 'OrganizationMembershipType']]] = None,
                 parent_hierarchy_id: Optional[pulumi.Input[str]] = None,
                 stackset_name: Optional[pulumi.Input[str]] = None):
        """
        The multi cloud account's organizational data
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_account_ids: If the multi cloud account is of membership type organization, list of accounts excluded from offering
        :param pulumi.Input[Union[str, 'OrganizationMembershipType']] organization_membership_type: The multi cloud account's membership type in the organization
        :param pulumi.Input[str] parent_hierarchy_id: If the multi cloud account is not of membership type organization, this will be the ID of the account's parent
        :param pulumi.Input[str] stackset_name: If the multi cloud account is of membership type organization, this will be the name of the onboarding stackset
        """
        if excluded_account_ids is not None:
            pulumi.set(__self__, "excluded_account_ids", excluded_account_ids)
        if organization_membership_type is not None:
            pulumi.set(__self__, "organization_membership_type", organization_membership_type)
        if parent_hierarchy_id is not None:
            pulumi.set(__self__, "parent_hierarchy_id", parent_hierarchy_id)
        if stackset_name is not None:
            pulumi.set(__self__, "stackset_name", stackset_name)

    @property
    @pulumi.getter(name="excludedAccountIds")
    def excluded_account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        If the multi cloud account is of membership type organization, list of accounts excluded from offering
        """
        return pulumi.get(self, "excluded_account_ids")

    @excluded_account_ids.setter
    def excluded_account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_account_ids", value)

    @property
    @pulumi.getter(name="organizationMembershipType")
    def organization_membership_type(self) -> Optional[pulumi.Input[Union[str, 'OrganizationMembershipType']]]:
        """
        The multi cloud account's membership type in the organization
        """
        return pulumi.get(self, "organization_membership_type")

    @organization_membership_type.setter
    def organization_membership_type(self, value: Optional[pulumi.Input[Union[str, 'OrganizationMembershipType']]]):
        pulumi.set(self, "organization_membership_type", value)

    @property
    @pulumi.getter(name="parentHierarchyId")
    def parent_hierarchy_id(self) -> Optional[pulumi.Input[str]]:
        """
        If the multi cloud account is not of membership type organization, this will be the ID of the account's parent
        """
        return pulumi.get(self, "parent_hierarchy_id")

    @parent_hierarchy_id.setter
    def parent_hierarchy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_hierarchy_id", value)

    @property
    @pulumi.getter(name="stacksetName")
    def stackset_name(self) -> Optional[pulumi.Input[str]]:
        """
        If the multi cloud account is of membership type organization, this will be the name of the onboarding stackset
        """
        return pulumi.get(self, "stackset_name")

    @stackset_name.setter
    def stackset_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stackset_name", value)


