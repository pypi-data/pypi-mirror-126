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
    'ListSiteBackupConfigurationSlotResult',
    'AwaitableListSiteBackupConfigurationSlotResult',
    'list_site_backup_configuration_slot',
    'list_site_backup_configuration_slot_output',
]

@pulumi.output_type
class ListSiteBackupConfigurationSlotResult:
    """
    Description of a backup which will be performed
    """
    def __init__(__self__, backup_schedule=None, databases=None, enabled=None, id=None, kind=None, location=None, name=None, storage_account_url=None, tags=None, type=None):
        if backup_schedule and not isinstance(backup_schedule, dict):
            raise TypeError("Expected argument 'backup_schedule' to be a dict")
        pulumi.set(__self__, "backup_schedule", backup_schedule)
        if databases and not isinstance(databases, list):
            raise TypeError("Expected argument 'databases' to be a list")
        pulumi.set(__self__, "databases", databases)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_account_url and not isinstance(storage_account_url, str):
            raise TypeError("Expected argument 'storage_account_url' to be a str")
        pulumi.set(__self__, "storage_account_url", storage_account_url)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> Optional['outputs.BackupScheduleResponse']:
        """
        Schedule for the backup if it is executed periodically
        """
        return pulumi.get(self, "backup_schedule")

    @property
    @pulumi.getter
    def databases(self) -> Optional[Sequence['outputs.DatabaseBackupSettingResponse']]:
        """
        Databases included in the backup
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[str]:
        """
        SAS URL to the container
        """
        return pulumi.get(self, "storage_account_url")

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
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableListSiteBackupConfigurationSlotResult(ListSiteBackupConfigurationSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSiteBackupConfigurationSlotResult(
            backup_schedule=self.backup_schedule,
            databases=self.databases,
            enabled=self.enabled,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            storage_account_url=self.storage_account_url,
            tags=self.tags,
            type=self.type)


def list_site_backup_configuration_slot(name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        slot: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSiteBackupConfigurationSlotResult:
    """
    Description of a backup which will be performed


    :param str name: Name of web app
    :param str resource_group_name: Name of resource group
    :param str slot: Name of web app slot. If not specified then will default to production slot.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20150801:listSiteBackupConfigurationSlot', __args__, opts=opts, typ=ListSiteBackupConfigurationSlotResult).value

    return AwaitableListSiteBackupConfigurationSlotResult(
        backup_schedule=__ret__.backup_schedule,
        databases=__ret__.databases,
        enabled=__ret__.enabled,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        storage_account_url=__ret__.storage_account_url,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(list_site_backup_configuration_slot)
def list_site_backup_configuration_slot_output(name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               slot: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSiteBackupConfigurationSlotResult]:
    """
    Description of a backup which will be performed


    :param str name: Name of web app
    :param str resource_group_name: Name of resource group
    :param str slot: Name of web app slot. If not specified then will default to production slot.
    """
    ...
