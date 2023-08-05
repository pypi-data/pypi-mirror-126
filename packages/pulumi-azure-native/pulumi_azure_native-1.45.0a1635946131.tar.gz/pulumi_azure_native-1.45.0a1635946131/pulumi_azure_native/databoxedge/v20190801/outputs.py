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
    'AddressResponse',
    'AsymmetricEncryptedSecretResponse',
    'AuthenticationResponse',
    'AzureContainerInfoResponse',
    'ClientAccessRightResponse',
    'ContactDetailsResponse',
    'FileSourceInfoResponse',
    'IoTDeviceInfoResponse',
    'MountPointMapResponse',
    'OrderStatusResponse',
    'PeriodicTimerSourceInfoResponse',
    'RefreshDetailsResponse',
    'RoleSinkInfoResponse',
    'ShareAccessRightResponse',
    'SkuResponse',
    'SymmetricKeyResponse',
    'TrackingInfoResponse',
    'UserAccessRightResponse',
]

@pulumi.output_type
class AddressResponse(dict):
    """
    The shipping address of the customer.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "addressLine1":
            suggest = "address_line1"
        elif key == "postalCode":
            suggest = "postal_code"
        elif key == "addressLine2":
            suggest = "address_line2"
        elif key == "addressLine3":
            suggest = "address_line3"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AddressResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AddressResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AddressResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 address_line1: str,
                 city: str,
                 country: str,
                 postal_code: str,
                 state: str,
                 address_line2: Optional[str] = None,
                 address_line3: Optional[str] = None):
        """
        The shipping address of the customer.
        :param str address_line1: The address line1.
        :param str city: The city name.
        :param str country: The country name.
        :param str postal_code: The postal code.
        :param str state: The state name.
        :param str address_line2: The address line2.
        :param str address_line3: The address line3.
        """
        pulumi.set(__self__, "address_line1", address_line1)
        pulumi.set(__self__, "city", city)
        pulumi.set(__self__, "country", country)
        pulumi.set(__self__, "postal_code", postal_code)
        pulumi.set(__self__, "state", state)
        if address_line2 is not None:
            pulumi.set(__self__, "address_line2", address_line2)
        if address_line3 is not None:
            pulumi.set(__self__, "address_line3", address_line3)

    @property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> str:
        """
        The address line1.
        """
        return pulumi.get(self, "address_line1")

    @property
    @pulumi.getter
    def city(self) -> str:
        """
        The city name.
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        The country name.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> str:
        """
        The postal code.
        """
        return pulumi.get(self, "postal_code")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state name.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[str]:
        """
        The address line2.
        """
        return pulumi.get(self, "address_line2")

    @property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[str]:
        """
        The address line3.
        """
        return pulumi.get(self, "address_line3")


@pulumi.output_type
class AsymmetricEncryptedSecretResponse(dict):
    """
    Represent the secrets intended for encryption with asymmetric key pair.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionAlgorithm":
            suggest = "encryption_algorithm"
        elif key == "encryptionCertThumbprint":
            suggest = "encryption_cert_thumbprint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AsymmetricEncryptedSecretResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AsymmetricEncryptedSecretResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AsymmetricEncryptedSecretResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encryption_algorithm: str,
                 value: str,
                 encryption_cert_thumbprint: Optional[str] = None):
        """
        Represent the secrets intended for encryption with asymmetric key pair.
        :param str encryption_algorithm: The algorithm used to encrypt "Value".
        :param str value: The value of the secret.
        :param str encryption_cert_thumbprint: Thumbprint certificate used to encrypt \"Value\". If the value is unencrypted, it will be null.
        """
        pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        pulumi.set(__self__, "value", value)
        if encryption_cert_thumbprint is not None:
            pulumi.set(__self__, "encryption_cert_thumbprint", encryption_cert_thumbprint)

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> str:
        """
        The algorithm used to encrypt "Value".
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the secret.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="encryptionCertThumbprint")
    def encryption_cert_thumbprint(self) -> Optional[str]:
        """
        Thumbprint certificate used to encrypt \"Value\". If the value is unencrypted, it will be null.
        """
        return pulumi.get(self, "encryption_cert_thumbprint")


@pulumi.output_type
class AuthenticationResponse(dict):
    """
    Authentication mechanism for IoT devices.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "symmetricKey":
            suggest = "symmetric_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuthenticationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuthenticationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuthenticationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 symmetric_key: Optional['outputs.SymmetricKeyResponse'] = None):
        """
        Authentication mechanism for IoT devices.
        :param 'SymmetricKeyResponse' symmetric_key: Symmetric key for authentication.
        """
        if symmetric_key is not None:
            pulumi.set(__self__, "symmetric_key", symmetric_key)

    @property
    @pulumi.getter(name="symmetricKey")
    def symmetric_key(self) -> Optional['outputs.SymmetricKeyResponse']:
        """
        Symmetric key for authentication.
        """
        return pulumi.get(self, "symmetric_key")


@pulumi.output_type
class AzureContainerInfoResponse(dict):
    """
    Azure container mapping of the endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "containerName":
            suggest = "container_name"
        elif key == "dataFormat":
            suggest = "data_format"
        elif key == "storageAccountCredentialId":
            suggest = "storage_account_credential_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureContainerInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureContainerInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureContainerInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 container_name: str,
                 data_format: str,
                 storage_account_credential_id: str):
        """
        Azure container mapping of the endpoint.
        :param str container_name: Container name (Based on the data format specified, this represents the name of Azure Files/Page blob/Block blob).
        :param str data_format: Storage format used for the file represented by the share.
        :param str storage_account_credential_id: ID of the storage account credential used to access storage.
        """
        pulumi.set(__self__, "container_name", container_name)
        pulumi.set(__self__, "data_format", data_format)
        pulumi.set(__self__, "storage_account_credential_id", storage_account_credential_id)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> str:
        """
        Container name (Based on the data format specified, this represents the name of Azure Files/Page blob/Block blob).
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> str:
        """
        Storage format used for the file represented by the share.
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> str:
        """
        ID of the storage account credential used to access storage.
        """
        return pulumi.get(self, "storage_account_credential_id")


@pulumi.output_type
class ClientAccessRightResponse(dict):
    """
    The mapping between a particular client IP and the type of access client has on the NFS share.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessPermission":
            suggest = "access_permission"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClientAccessRightResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClientAccessRightResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClientAccessRightResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_permission: str,
                 client: str):
        """
        The mapping between a particular client IP and the type of access client has on the NFS share.
        :param str access_permission: Type of access to be allowed for the client.
        :param str client: IP of the client.
        """
        pulumi.set(__self__, "access_permission", access_permission)
        pulumi.set(__self__, "client", client)

    @property
    @pulumi.getter(name="accessPermission")
    def access_permission(self) -> str:
        """
        Type of access to be allowed for the client.
        """
        return pulumi.get(self, "access_permission")

    @property
    @pulumi.getter
    def client(self) -> str:
        """
        IP of the client.
        """
        return pulumi.get(self, "client")


@pulumi.output_type
class ContactDetailsResponse(dict):
    """
    Contains all the contact details of the customer.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "companyName":
            suggest = "company_name"
        elif key == "contactPerson":
            suggest = "contact_person"
        elif key == "emailList":
            suggest = "email_list"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactDetailsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactDetailsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactDetailsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 company_name: str,
                 contact_person: str,
                 email_list: Sequence[str],
                 phone: str):
        """
        Contains all the contact details of the customer.
        :param str company_name: The name of the company.
        :param str contact_person: The contact person name.
        :param Sequence[str] email_list: The email list.
        :param str phone: The phone number.
        """
        pulumi.set(__self__, "company_name", company_name)
        pulumi.set(__self__, "contact_person", contact_person)
        pulumi.set(__self__, "email_list", email_list)
        pulumi.set(__self__, "phone", phone)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> str:
        """
        The name of the company.
        """
        return pulumi.get(self, "company_name")

    @property
    @pulumi.getter(name="contactPerson")
    def contact_person(self) -> str:
        """
        The contact person name.
        """
        return pulumi.get(self, "contact_person")

    @property
    @pulumi.getter(name="emailList")
    def email_list(self) -> Sequence[str]:
        """
        The email list.
        """
        return pulumi.get(self, "email_list")

    @property
    @pulumi.getter
    def phone(self) -> str:
        """
        The phone number.
        """
        return pulumi.get(self, "phone")


@pulumi.output_type
class FileSourceInfoResponse(dict):
    """
    File source details.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "shareId":
            suggest = "share_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FileSourceInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FileSourceInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FileSourceInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 share_id: str):
        """
        File source details.
        :param str share_id: File share ID.
        """
        pulumi.set(__self__, "share_id", share_id)

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> str:
        """
        File share ID.
        """
        return pulumi.get(self, "share_id")


@pulumi.output_type
class IoTDeviceInfoResponse(dict):
    """
    Metadata of IoT device/IoT Edge device to be configured.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deviceId":
            suggest = "device_id"
        elif key == "ioTHostHub":
            suggest = "io_t_host_hub"
        elif key == "ioTHostHubId":
            suggest = "io_t_host_hub_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IoTDeviceInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IoTDeviceInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IoTDeviceInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 device_id: str,
                 io_t_host_hub: str,
                 authentication: Optional['outputs.AuthenticationResponse'] = None,
                 io_t_host_hub_id: Optional[str] = None):
        """
        Metadata of IoT device/IoT Edge device to be configured.
        :param str device_id: ID of the IoT device/edge device.
        :param str io_t_host_hub: Host name for the IoT hub associated to the device.
        :param 'AuthenticationResponse' authentication: IoT device authentication info.
        :param str io_t_host_hub_id: Id for the IoT hub associated to the device.
        """
        pulumi.set(__self__, "device_id", device_id)
        pulumi.set(__self__, "io_t_host_hub", io_t_host_hub)
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if io_t_host_hub_id is not None:
            pulumi.set(__self__, "io_t_host_hub_id", io_t_host_hub_id)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> str:
        """
        ID of the IoT device/edge device.
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="ioTHostHub")
    def io_t_host_hub(self) -> str:
        """
        Host name for the IoT hub associated to the device.
        """
        return pulumi.get(self, "io_t_host_hub")

    @property
    @pulumi.getter
    def authentication(self) -> Optional['outputs.AuthenticationResponse']:
        """
        IoT device authentication info.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="ioTHostHubId")
    def io_t_host_hub_id(self) -> Optional[str]:
        """
        Id for the IoT hub associated to the device.
        """
        return pulumi.get(self, "io_t_host_hub_id")


@pulumi.output_type
class MountPointMapResponse(dict):
    """
    The share mount point.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mountPoint":
            suggest = "mount_point"
        elif key == "roleId":
            suggest = "role_id"
        elif key == "roleType":
            suggest = "role_type"
        elif key == "shareId":
            suggest = "share_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MountPointMapResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MountPointMapResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MountPointMapResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 mount_point: str,
                 role_id: str,
                 role_type: str,
                 share_id: str):
        """
        The share mount point.
        :param str mount_point: Mount point for the share.
        :param str role_id: ID of the role to which share is mounted.
        :param str role_type: Role type.
        :param str share_id: ID of the share mounted to the role VM.
        """
        pulumi.set(__self__, "mount_point", mount_point)
        pulumi.set(__self__, "role_id", role_id)
        pulumi.set(__self__, "role_type", role_type)
        pulumi.set(__self__, "share_id", share_id)

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> str:
        """
        Mount point for the share.
        """
        return pulumi.get(self, "mount_point")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> str:
        """
        ID of the role to which share is mounted.
        """
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> str:
        """
        Role type.
        """
        return pulumi.get(self, "role_type")

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> str:
        """
        ID of the share mounted to the role VM.
        """
        return pulumi.get(self, "share_id")


@pulumi.output_type
class OrderStatusResponse(dict):
    """
    Represents a single status change.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalOrderDetails":
            suggest = "additional_order_details"
        elif key == "updateDateTime":
            suggest = "update_date_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrderStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrderStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrderStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_order_details: Mapping[str, str],
                 status: str,
                 update_date_time: str,
                 comments: Optional[str] = None):
        """
        Represents a single status change.
        :param Mapping[str, str] additional_order_details: Dictionary to hold generic information which is not stored
               by the already existing properties
        :param str status: Status of the order as per the allowed status types.
        :param str update_date_time: Time of status update.
        :param str comments: Comments related to this status change.
        """
        pulumi.set(__self__, "additional_order_details", additional_order_details)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "update_date_time", update_date_time)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)

    @property
    @pulumi.getter(name="additionalOrderDetails")
    def additional_order_details(self) -> Mapping[str, str]:
        """
        Dictionary to hold generic information which is not stored
        by the already existing properties
        """
        return pulumi.get(self, "additional_order_details")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the order as per the allowed status types.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updateDateTime")
    def update_date_time(self) -> str:
        """
        Time of status update.
        """
        return pulumi.get(self, "update_date_time")

    @property
    @pulumi.getter
    def comments(self) -> Optional[str]:
        """
        Comments related to this status change.
        """
        return pulumi.get(self, "comments")


@pulumi.output_type
class PeriodicTimerSourceInfoResponse(dict):
    """
    Periodic timer event source.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PeriodicTimerSourceInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PeriodicTimerSourceInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PeriodicTimerSourceInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 schedule: str,
                 start_time: str,
                 topic: Optional[str] = None):
        """
        Periodic timer event source.
        :param str schedule: Periodic frequency at which timer event needs to be raised. Supports daily, hourly, minutes, and seconds.
        :param str start_time: The time of the day that results in a valid trigger. Schedule is computed with reference to the time specified upto seconds. If timezone is not specified the time will considered to be in device timezone. The value will always be returned as UTC time.
        :param str topic: Topic where periodic events are published to IoT device.
        """
        pulumi.set(__self__, "schedule", schedule)
        pulumi.set(__self__, "start_time", start_time)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def schedule(self) -> str:
        """
        Periodic frequency at which timer event needs to be raised. Supports daily, hourly, minutes, and seconds.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The time of the day that results in a valid trigger. Schedule is computed with reference to the time specified upto seconds. If timezone is not specified the time will considered to be in device timezone. The value will always be returned as UTC time.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def topic(self) -> Optional[str]:
        """
        Topic where periodic events are published to IoT device.
        """
        return pulumi.get(self, "topic")


@pulumi.output_type
class RefreshDetailsResponse(dict):
    """
    Fields for tracking refresh job on the share or container.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "errorManifestFile":
            suggest = "error_manifest_file"
        elif key == "inProgressRefreshJobId":
            suggest = "in_progress_refresh_job_id"
        elif key == "lastCompletedRefreshJobTimeInUTC":
            suggest = "last_completed_refresh_job_time_in_utc"
        elif key == "lastJob":
            suggest = "last_job"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RefreshDetailsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RefreshDetailsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RefreshDetailsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 error_manifest_file: Optional[str] = None,
                 in_progress_refresh_job_id: Optional[str] = None,
                 last_completed_refresh_job_time_in_utc: Optional[str] = None,
                 last_job: Optional[str] = None):
        """
        Fields for tracking refresh job on the share or container.
        :param str error_manifest_file: Indicates the relative path of the error xml for the last refresh job on this particular share or container, if any. This could be a failed job or a successful job.
        :param str in_progress_refresh_job_id: If a refresh job is currently in progress on this share or container, this field indicates the ARM resource ID of that job. The field is empty if no job is in progress.
        :param str last_completed_refresh_job_time_in_utc: Indicates the completed time for the last refresh job on this particular share or container, if any.This could be a failed job or a successful job.
        :param str last_job: Indicates the id of the last refresh job on this particular share or container,if any. This could be a failed job or a successful job.
        """
        if error_manifest_file is not None:
            pulumi.set(__self__, "error_manifest_file", error_manifest_file)
        if in_progress_refresh_job_id is not None:
            pulumi.set(__self__, "in_progress_refresh_job_id", in_progress_refresh_job_id)
        if last_completed_refresh_job_time_in_utc is not None:
            pulumi.set(__self__, "last_completed_refresh_job_time_in_utc", last_completed_refresh_job_time_in_utc)
        if last_job is not None:
            pulumi.set(__self__, "last_job", last_job)

    @property
    @pulumi.getter(name="errorManifestFile")
    def error_manifest_file(self) -> Optional[str]:
        """
        Indicates the relative path of the error xml for the last refresh job on this particular share or container, if any. This could be a failed job or a successful job.
        """
        return pulumi.get(self, "error_manifest_file")

    @property
    @pulumi.getter(name="inProgressRefreshJobId")
    def in_progress_refresh_job_id(self) -> Optional[str]:
        """
        If a refresh job is currently in progress on this share or container, this field indicates the ARM resource ID of that job. The field is empty if no job is in progress.
        """
        return pulumi.get(self, "in_progress_refresh_job_id")

    @property
    @pulumi.getter(name="lastCompletedRefreshJobTimeInUTC")
    def last_completed_refresh_job_time_in_utc(self) -> Optional[str]:
        """
        Indicates the completed time for the last refresh job on this particular share or container, if any.This could be a failed job or a successful job.
        """
        return pulumi.get(self, "last_completed_refresh_job_time_in_utc")

    @property
    @pulumi.getter(name="lastJob")
    def last_job(self) -> Optional[str]:
        """
        Indicates the id of the last refresh job on this particular share or container,if any. This could be a failed job or a successful job.
        """
        return pulumi.get(self, "last_job")


@pulumi.output_type
class RoleSinkInfoResponse(dict):
    """
    Compute role against which events will be raised.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleId":
            suggest = "role_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoleSinkInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoleSinkInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoleSinkInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 role_id: str):
        """
        Compute role against which events will be raised.
        :param str role_id: Compute role ID.
        """
        pulumi.set(__self__, "role_id", role_id)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> str:
        """
        Compute role ID.
        """
        return pulumi.get(self, "role_id")


@pulumi.output_type
class ShareAccessRightResponse(dict):
    """
    Specifies the mapping between this particular user and the type of access he has on shares on this device.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessType":
            suggest = "access_type"
        elif key == "shareId":
            suggest = "share_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ShareAccessRightResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ShareAccessRightResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ShareAccessRightResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_type: str,
                 share_id: str):
        """
        Specifies the mapping between this particular user and the type of access he has on shares on this device.
        :param str access_type: Type of access to be allowed on the share for this user.
        :param str share_id: The share ID.
        """
        pulumi.set(__self__, "access_type", access_type)
        pulumi.set(__self__, "share_id", share_id)

    @property
    @pulumi.getter(name="accessType")
    def access_type(self) -> str:
        """
        Type of access to be allowed on the share for this user.
        """
        return pulumi.get(self, "access_type")

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> str:
        """
        The share ID.
        """
        return pulumi.get(self, "share_id")


@pulumi.output_type
class SkuResponse(dict):
    """
    The SKU type.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        The SKU type.
        :param str name: SKU name.
        :param str tier: The SKU tier. This is based on the SKU name.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        SKU name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The SKU tier. This is based on the SKU name.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class SymmetricKeyResponse(dict):
    """
    Symmetric key for authentication.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "connectionString":
            suggest = "connection_string"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SymmetricKeyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SymmetricKeyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SymmetricKeyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 connection_string: Optional['outputs.AsymmetricEncryptedSecretResponse'] = None):
        """
        Symmetric key for authentication.
        :param 'AsymmetricEncryptedSecretResponse' connection_string: Connection string based on the symmetric key.
        """
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional['outputs.AsymmetricEncryptedSecretResponse']:
        """
        Connection string based on the symmetric key.
        """
        return pulumi.get(self, "connection_string")


@pulumi.output_type
class TrackingInfoResponse(dict):
    """
    Tracking courier information.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "carrierName":
            suggest = "carrier_name"
        elif key == "serialNumber":
            suggest = "serial_number"
        elif key == "trackingId":
            suggest = "tracking_id"
        elif key == "trackingUrl":
            suggest = "tracking_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TrackingInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TrackingInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TrackingInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 carrier_name: Optional[str] = None,
                 serial_number: Optional[str] = None,
                 tracking_id: Optional[str] = None,
                 tracking_url: Optional[str] = None):
        """
        Tracking courier information.
        :param str carrier_name: Name of the carrier used in the delivery.
        :param str serial_number: Serial number of the device being tracked.
        :param str tracking_id: Tracking ID of the shipment.
        :param str tracking_url: Tracking URL of the shipment.
        """
        if carrier_name is not None:
            pulumi.set(__self__, "carrier_name", carrier_name)
        if serial_number is not None:
            pulumi.set(__self__, "serial_number", serial_number)
        if tracking_id is not None:
            pulumi.set(__self__, "tracking_id", tracking_id)
        if tracking_url is not None:
            pulumi.set(__self__, "tracking_url", tracking_url)

    @property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[str]:
        """
        Name of the carrier used in the delivery.
        """
        return pulumi.get(self, "carrier_name")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[str]:
        """
        Serial number of the device being tracked.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[str]:
        """
        Tracking ID of the shipment.
        """
        return pulumi.get(self, "tracking_id")

    @property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> Optional[str]:
        """
        Tracking URL of the shipment.
        """
        return pulumi.get(self, "tracking_url")


@pulumi.output_type
class UserAccessRightResponse(dict):
    """
    The mapping between a particular user and the access type on the SMB share.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessType":
            suggest = "access_type"
        elif key == "userId":
            suggest = "user_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAccessRightResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAccessRightResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAccessRightResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_type: str,
                 user_id: str):
        """
        The mapping between a particular user and the access type on the SMB share.
        :param str access_type: Type of access to be allowed for the user.
        :param str user_id: User ID (already existing in the device).
        """
        pulumi.set(__self__, "access_type", access_type)
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="accessType")
    def access_type(self) -> str:
        """
        Type of access to be allowed for the user.
        """
        return pulumi.get(self, "access_type")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        User ID (already existing in the device).
        """
        return pulumi.get(self, "user_id")


