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
    'AttestationEvidenceArgs',
    'RemediationFiltersArgs',
]

@pulumi.input_type
class AttestationEvidenceArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None):
        """
        A piece of evidence supporting the compliance state set in the attestation.
        :param pulumi.Input[str] description: The description for this piece of evidence.
        :param pulumi.Input[str] source_uri: The URI location of the evidence.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if source_uri is not None:
            pulumi.set(__self__, "source_uri", source_uri)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for this piece of evidence.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI location of the evidence.
        """
        return pulumi.get(self, "source_uri")

    @source_uri.setter
    def source_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_uri", value)


@pulumi.input_type
class RemediationFiltersArgs:
    def __init__(__self__, *,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The filters that will be applied to determine which resources to remediate.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: The resource locations that will be remediated.
        """
        if locations is not None:
            pulumi.set(__self__, "locations", locations)

    @property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The resource locations that will be remediated.
        """
        return pulumi.get(self, "locations")

    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locations", value)


