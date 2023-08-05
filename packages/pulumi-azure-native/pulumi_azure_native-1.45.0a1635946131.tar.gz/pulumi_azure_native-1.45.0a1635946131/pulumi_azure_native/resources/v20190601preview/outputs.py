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
    'SystemDataResponse',
    'TemplateSpecTemplateArtifactResponse',
    'TemplateSpecVersionInfoResponse',
]

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


@pulumi.output_type
class TemplateSpecTemplateArtifactResponse(dict):
    """
    Represents a Template Spec artifact containing an embedded Azure Resource Manager template.
    """
    def __init__(__self__, *,
                 kind: str,
                 path: str,
                 template: Any):
        """
        Represents a Template Spec artifact containing an embedded Azure Resource Manager template.
        :param str kind: The kind of artifact.
               Expected value is 'template'.
        :param str path: A filesystem safe relative path of the artifact.
        :param Any template: The Azure Resource Manager template.
        """
        pulumi.set(__self__, "kind", 'template')
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of artifact.
        Expected value is 'template'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        A filesystem safe relative path of the artifact.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def template(self) -> Any:
        """
        The Azure Resource Manager template.
        """
        return pulumi.get(self, "template")


@pulumi.output_type
class TemplateSpecVersionInfoResponse(dict):
    """
    High-level information about a Template Spec version.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "timeCreated":
            suggest = "time_created"
        elif key == "timeModified":
            suggest = "time_modified"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TemplateSpecVersionInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TemplateSpecVersionInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TemplateSpecVersionInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 time_created: str,
                 time_modified: str):
        """
        High-level information about a Template Spec version.
        :param str description: Template Spec version description.
        :param str time_created: The timestamp of when the version was created.
        :param str time_modified: The timestamp of when the version was last modified.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "time_created", time_created)
        pulumi.set(__self__, "time_modified", time_modified)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Template Spec version description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The timestamp of when the version was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> str:
        """
        The timestamp of when the version was last modified.
        """
        return pulumi.get(self, "time_modified")


