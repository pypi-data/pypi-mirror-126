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

__all__ = [
    'CspmMonitorAwsOfferingResponse',
    'CspmMonitorAwsOfferingResponseNativeCloudConnection',
    'DefenderForContainersAwsOfferingResponse',
    'DefenderForContainersAwsOfferingResponseCloudWatchToKinesis',
    'DefenderForContainersAwsOfferingResponseKinesisToS3',
    'DefenderForContainersAwsOfferingResponseKubernetesScubaReader',
    'DefenderForContainersAwsOfferingResponseKubernetesService',
    'DefenderForServersAwsOfferingResponse',
    'DefenderForServersAwsOfferingResponseArcAutoProvisioning',
    'DefenderForServersAwsOfferingResponseDefenderForServers',
    'DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata',
    'SecurityConnectorPropertiesResponseOrganizationalData',
    'SystemDataResponse',
]

@pulumi.output_type
class CspmMonitorAwsOfferingResponse(dict):
    """
    The CSPM monitoring for AWS offering configurations
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "offeringType":
            suggest = "offering_type"
        elif key == "nativeCloudConnection":
            suggest = "native_cloud_connection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CspmMonitorAwsOfferingResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CspmMonitorAwsOfferingResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CspmMonitorAwsOfferingResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 offering_type: str,
                 native_cloud_connection: Optional['outputs.CspmMonitorAwsOfferingResponseNativeCloudConnection'] = None):
        """
        The CSPM monitoring for AWS offering configurations
        :param str description: The offering description.
        :param str offering_type: The type of the security offering.
               Expected value is 'CspmMonitorAws'.
        :param 'CspmMonitorAwsOfferingResponseNativeCloudConnection' native_cloud_connection: The native cloud connection configuration
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "offering_type", 'CspmMonitorAws')
        if native_cloud_connection is not None:
            pulumi.set(__self__, "native_cloud_connection", native_cloud_connection)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The offering description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> str:
        """
        The type of the security offering.
        Expected value is 'CspmMonitorAws'.
        """
        return pulumi.get(self, "offering_type")

    @property
    @pulumi.getter(name="nativeCloudConnection")
    def native_cloud_connection(self) -> Optional['outputs.CspmMonitorAwsOfferingResponseNativeCloudConnection']:
        """
        The native cloud connection configuration
        """
        return pulumi.get(self, "native_cloud_connection")


@pulumi.output_type
class CspmMonitorAwsOfferingResponseNativeCloudConnection(dict):
    """
    The native cloud connection configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudRoleArn":
            suggest = "cloud_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CspmMonitorAwsOfferingResponseNativeCloudConnection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CspmMonitorAwsOfferingResponseNativeCloudConnection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CspmMonitorAwsOfferingResponseNativeCloudConnection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_role_arn: Optional[str] = None):
        """
        The native cloud connection configuration
        :param str cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[str]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")


@pulumi.output_type
class DefenderForContainersAwsOfferingResponse(dict):
    """
    The Defender for Containers AWS offering configurations
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "offeringType":
            suggest = "offering_type"
        elif key == "cloudWatchToKinesis":
            suggest = "cloud_watch_to_kinesis"
        elif key == "kinesisToS3":
            suggest = "kinesis_to_s3"
        elif key == "kubernetesScubaReader":
            suggest = "kubernetes_scuba_reader"
        elif key == "kubernetesService":
            suggest = "kubernetes_service"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForContainersAwsOfferingResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForContainersAwsOfferingResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForContainersAwsOfferingResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 offering_type: str,
                 cloud_watch_to_kinesis: Optional['outputs.DefenderForContainersAwsOfferingResponseCloudWatchToKinesis'] = None,
                 kinesis_to_s3: Optional['outputs.DefenderForContainersAwsOfferingResponseKinesisToS3'] = None,
                 kubernetes_scuba_reader: Optional['outputs.DefenderForContainersAwsOfferingResponseKubernetesScubaReader'] = None,
                 kubernetes_service: Optional['outputs.DefenderForContainersAwsOfferingResponseKubernetesService'] = None):
        """
        The Defender for Containers AWS offering configurations
        :param str description: The offering description.
        :param str offering_type: The type of the security offering.
               Expected value is 'DefenderForContainersAws'.
        :param 'DefenderForContainersAwsOfferingResponseCloudWatchToKinesis' cloud_watch_to_kinesis: The cloudwatch to kinesis connection configuration
        :param 'DefenderForContainersAwsOfferingResponseKinesisToS3' kinesis_to_s3: The kinesis to s3 connection configuration
        :param 'DefenderForContainersAwsOfferingResponseKubernetesScubaReader' kubernetes_scuba_reader: The kubernetes to scuba connection configuration
        :param 'DefenderForContainersAwsOfferingResponseKubernetesService' kubernetes_service: The kubernetes service connection configuration
        """
        pulumi.set(__self__, "description", description)
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
    @pulumi.getter
    def description(self) -> str:
        """
        The offering description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> str:
        """
        The type of the security offering.
        Expected value is 'DefenderForContainersAws'.
        """
        return pulumi.get(self, "offering_type")

    @property
    @pulumi.getter(name="cloudWatchToKinesis")
    def cloud_watch_to_kinesis(self) -> Optional['outputs.DefenderForContainersAwsOfferingResponseCloudWatchToKinesis']:
        """
        The cloudwatch to kinesis connection configuration
        """
        return pulumi.get(self, "cloud_watch_to_kinesis")

    @property
    @pulumi.getter(name="kinesisToS3")
    def kinesis_to_s3(self) -> Optional['outputs.DefenderForContainersAwsOfferingResponseKinesisToS3']:
        """
        The kinesis to s3 connection configuration
        """
        return pulumi.get(self, "kinesis_to_s3")

    @property
    @pulumi.getter(name="kubernetesScubaReader")
    def kubernetes_scuba_reader(self) -> Optional['outputs.DefenderForContainersAwsOfferingResponseKubernetesScubaReader']:
        """
        The kubernetes to scuba connection configuration
        """
        return pulumi.get(self, "kubernetes_scuba_reader")

    @property
    @pulumi.getter(name="kubernetesService")
    def kubernetes_service(self) -> Optional['outputs.DefenderForContainersAwsOfferingResponseKubernetesService']:
        """
        The kubernetes service connection configuration
        """
        return pulumi.get(self, "kubernetes_service")


@pulumi.output_type
class DefenderForContainersAwsOfferingResponseCloudWatchToKinesis(dict):
    """
    The cloudwatch to kinesis connection configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudRoleArn":
            suggest = "cloud_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForContainersAwsOfferingResponseCloudWatchToKinesis. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForContainersAwsOfferingResponseCloudWatchToKinesis.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForContainersAwsOfferingResponseCloudWatchToKinesis.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_role_arn: Optional[str] = None):
        """
        The cloudwatch to kinesis connection configuration
        :param str cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[str]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")


@pulumi.output_type
class DefenderForContainersAwsOfferingResponseKinesisToS3(dict):
    """
    The kinesis to s3 connection configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudRoleArn":
            suggest = "cloud_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForContainersAwsOfferingResponseKinesisToS3. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForContainersAwsOfferingResponseKinesisToS3.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForContainersAwsOfferingResponseKinesisToS3.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_role_arn: Optional[str] = None):
        """
        The kinesis to s3 connection configuration
        :param str cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[str]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")


@pulumi.output_type
class DefenderForContainersAwsOfferingResponseKubernetesScubaReader(dict):
    """
    The kubernetes to scuba connection configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudRoleArn":
            suggest = "cloud_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForContainersAwsOfferingResponseKubernetesScubaReader. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForContainersAwsOfferingResponseKubernetesScubaReader.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForContainersAwsOfferingResponseKubernetesScubaReader.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_role_arn: Optional[str] = None):
        """
        The kubernetes to scuba connection configuration
        :param str cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[str]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")


@pulumi.output_type
class DefenderForContainersAwsOfferingResponseKubernetesService(dict):
    """
    The kubernetes service connection configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudRoleArn":
            suggest = "cloud_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForContainersAwsOfferingResponseKubernetesService. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForContainersAwsOfferingResponseKubernetesService.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForContainersAwsOfferingResponseKubernetesService.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_role_arn: Optional[str] = None):
        """
        The kubernetes service connection configuration
        :param str cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[str]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")


@pulumi.output_type
class DefenderForServersAwsOfferingResponse(dict):
    """
    The Defender for Servers AWS offering configurations
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "offeringType":
            suggest = "offering_type"
        elif key == "arcAutoProvisioning":
            suggest = "arc_auto_provisioning"
        elif key == "defenderForServers":
            suggest = "defender_for_servers"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForServersAwsOfferingResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForServersAwsOfferingResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForServersAwsOfferingResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 offering_type: str,
                 arc_auto_provisioning: Optional['outputs.DefenderForServersAwsOfferingResponseArcAutoProvisioning'] = None,
                 defender_for_servers: Optional['outputs.DefenderForServersAwsOfferingResponseDefenderForServers'] = None):
        """
        The Defender for Servers AWS offering configurations
        :param str description: The offering description.
        :param str offering_type: The type of the security offering.
               Expected value is 'DefenderForServersAWS'.
        :param 'DefenderForServersAwsOfferingResponseArcAutoProvisioning' arc_auto_provisioning: The ARC autoprovisioning configuration
        :param 'DefenderForServersAwsOfferingResponseDefenderForServers' defender_for_servers: The Defender for servers connection configuration
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "offering_type", 'DefenderForServersAWS')
        if arc_auto_provisioning is not None:
            pulumi.set(__self__, "arc_auto_provisioning", arc_auto_provisioning)
        if defender_for_servers is not None:
            pulumi.set(__self__, "defender_for_servers", defender_for_servers)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The offering description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> str:
        """
        The type of the security offering.
        Expected value is 'DefenderForServersAWS'.
        """
        return pulumi.get(self, "offering_type")

    @property
    @pulumi.getter(name="arcAutoProvisioning")
    def arc_auto_provisioning(self) -> Optional['outputs.DefenderForServersAwsOfferingResponseArcAutoProvisioning']:
        """
        The ARC autoprovisioning configuration
        """
        return pulumi.get(self, "arc_auto_provisioning")

    @property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(self) -> Optional['outputs.DefenderForServersAwsOfferingResponseDefenderForServers']:
        """
        The Defender for servers connection configuration
        """
        return pulumi.get(self, "defender_for_servers")


@pulumi.output_type
class DefenderForServersAwsOfferingResponseArcAutoProvisioning(dict):
    """
    The ARC autoprovisioning configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "servicePrincipalSecretMetadata":
            suggest = "service_principal_secret_metadata"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForServersAwsOfferingResponseArcAutoProvisioning. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForServersAwsOfferingResponseArcAutoProvisioning.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForServersAwsOfferingResponseArcAutoProvisioning.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 service_principal_secret_metadata: Optional['outputs.DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata'] = None):
        """
        The ARC autoprovisioning configuration
        :param bool enabled: Is arc auto provisioning enabled
        :param 'DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata' service_principal_secret_metadata: Metadata of Service Principal secret for autoprovisioning
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if service_principal_secret_metadata is not None:
            pulumi.set(__self__, "service_principal_secret_metadata", service_principal_secret_metadata)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Is arc auto provisioning enabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="servicePrincipalSecretMetadata")
    def service_principal_secret_metadata(self) -> Optional['outputs.DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata']:
        """
        Metadata of Service Principal secret for autoprovisioning
        """
        return pulumi.get(self, "service_principal_secret_metadata")


@pulumi.output_type
class DefenderForServersAwsOfferingResponseDefenderForServers(dict):
    """
    The Defender for servers connection configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudRoleArn":
            suggest = "cloud_role_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForServersAwsOfferingResponseDefenderForServers. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForServersAwsOfferingResponseDefenderForServers.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForServersAwsOfferingResponseDefenderForServers.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_role_arn: Optional[str] = None):
        """
        The Defender for servers connection configuration
        :param str cloud_role_arn: The cloud role ARN in AWS for this feature
        """
        if cloud_role_arn is not None:
            pulumi.set(__self__, "cloud_role_arn", cloud_role_arn)

    @property
    @pulumi.getter(name="cloudRoleArn")
    def cloud_role_arn(self) -> Optional[str]:
        """
        The cloud role ARN in AWS for this feature
        """
        return pulumi.get(self, "cloud_role_arn")


@pulumi.output_type
class DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata(dict):
    """
    Metadata of Service Principal secret for autoprovisioning
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expiryDate":
            suggest = "expiry_date"
        elif key == "parameterNameInStore":
            suggest = "parameter_name_in_store"
        elif key == "parameterStoreRegion":
            suggest = "parameter_store_region"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DefenderForServersAwsOfferingResponseServicePrincipalSecretMetadata.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 expiry_date: Optional[str] = None,
                 parameter_name_in_store: Optional[str] = None,
                 parameter_store_region: Optional[str] = None):
        """
        Metadata of Service Principal secret for autoprovisioning
        :param str expiry_date: expiration date of service principal secret
        :param str parameter_name_in_store: name of secret resource in parameter store
        :param str parameter_store_region: region of parameter store where secret is kept
        """
        if expiry_date is not None:
            pulumi.set(__self__, "expiry_date", expiry_date)
        if parameter_name_in_store is not None:
            pulumi.set(__self__, "parameter_name_in_store", parameter_name_in_store)
        if parameter_store_region is not None:
            pulumi.set(__self__, "parameter_store_region", parameter_store_region)

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[str]:
        """
        expiration date of service principal secret
        """
        return pulumi.get(self, "expiry_date")

    @property
    @pulumi.getter(name="parameterNameInStore")
    def parameter_name_in_store(self) -> Optional[str]:
        """
        name of secret resource in parameter store
        """
        return pulumi.get(self, "parameter_name_in_store")

    @property
    @pulumi.getter(name="parameterStoreRegion")
    def parameter_store_region(self) -> Optional[str]:
        """
        region of parameter store where secret is kept
        """
        return pulumi.get(self, "parameter_store_region")


@pulumi.output_type
class SecurityConnectorPropertiesResponseOrganizationalData(dict):
    """
    The multi cloud account's organizational data
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "excludedAccountIds":
            suggest = "excluded_account_ids"
        elif key == "organizationMembershipType":
            suggest = "organization_membership_type"
        elif key == "parentHierarchyId":
            suggest = "parent_hierarchy_id"
        elif key == "stacksetName":
            suggest = "stackset_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecurityConnectorPropertiesResponseOrganizationalData. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecurityConnectorPropertiesResponseOrganizationalData.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecurityConnectorPropertiesResponseOrganizationalData.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 excluded_account_ids: Optional[Sequence[str]] = None,
                 organization_membership_type: Optional[str] = None,
                 parent_hierarchy_id: Optional[str] = None,
                 stackset_name: Optional[str] = None):
        """
        The multi cloud account's organizational data
        :param Sequence[str] excluded_account_ids: If the multi cloud account is of membership type organization, list of accounts excluded from offering
        :param str organization_membership_type: The multi cloud account's membership type in the organization
        :param str parent_hierarchy_id: If the multi cloud account is not of membership type organization, this will be the ID of the account's parent
        :param str stackset_name: If the multi cloud account is of membership type organization, this will be the name of the onboarding stackset
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
    def excluded_account_ids(self) -> Optional[Sequence[str]]:
        """
        If the multi cloud account is of membership type organization, list of accounts excluded from offering
        """
        return pulumi.get(self, "excluded_account_ids")

    @property
    @pulumi.getter(name="organizationMembershipType")
    def organization_membership_type(self) -> Optional[str]:
        """
        The multi cloud account's membership type in the organization
        """
        return pulumi.get(self, "organization_membership_type")

    @property
    @pulumi.getter(name="parentHierarchyId")
    def parent_hierarchy_id(self) -> Optional[str]:
        """
        If the multi cloud account is not of membership type organization, this will be the ID of the account's parent
        """
        return pulumi.get(self, "parent_hierarchy_id")

    @property
    @pulumi.getter(name="stacksetName")
    def stackset_name(self) -> Optional[str]:
        """
        If the multi cloud account is of membership type organization, this will be the name of the onboarding stackset
        """
        return pulumi.get(self, "stackset_name")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


