# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ApplianceCredentialKubeconfigResponse',
    'AppliancePropertiesResponseInfrastructureConfig',
    'HybridConnectionConfigResponse',
    'IdentityResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class ApplianceCredentialKubeconfigResponse(dict):
    """
    Cluster User Credential appliance.
    """
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        Cluster User Credential appliance.
        :param str name: Name which contains the role of the kubeconfig.
        :param str value: Contains the kubeconfig value.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name which contains the role of the kubeconfig.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Contains the kubeconfig value.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class AppliancePropertiesResponseInfrastructureConfig(dict):
    """
    Contains infrastructure information about the Appliance
    """
    def __init__(__self__, *,
                 provider: Optional[str] = None):
        """
        Contains infrastructure information about the Appliance
        :param str provider: Information about the connected appliance.
        """
        if provider is not None:
            pulumi.set(__self__, "provider", provider)

    @property
    @pulumi.getter
    def provider(self) -> Optional[str]:
        """
        Information about the connected appliance.
        """
        return pulumi.get(self, "provider")


@pulumi.output_type
class HybridConnectionConfigResponse(dict):
    """
    Contains the REP (rendezvous endpoint) and “Listener” access token from notification service (NS).
    """
    def __init__(__self__, *,
                 expiration_time: float,
                 hybrid_connection_name: str,
                 relay: str,
                 token: str):
        """
        Contains the REP (rendezvous endpoint) and “Listener” access token from notification service (NS).
        :param float expiration_time: Timestamp when this token will be expired.
        :param str hybrid_connection_name: Name of the connection
        :param str relay: Name of the notification service.
        :param str token: Listener access token
        """
        pulumi.set(__self__, "expiration_time", expiration_time)
        pulumi.set(__self__, "hybrid_connection_name", hybrid_connection_name)
        pulumi.set(__self__, "relay", relay)
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> float:
        """
        Timestamp when this token will be expired.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="hybridConnectionName")
    def hybrid_connection_name(self) -> str:
        """
        Name of the connection
        """
        return pulumi.get(self, "hybrid_connection_name")

    @property
    @pulumi.getter
    def relay(self) -> str:
        """
        Name of the notification service.
        """
        return pulumi.get(self, "relay")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        Listener access token
        """
        return pulumi.get(self, "token")


@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


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


