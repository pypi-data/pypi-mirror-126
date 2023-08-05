# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetApiManagementServiceDomainOwnershipIdentifierResult',
    'AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult',
    'get_api_management_service_domain_ownership_identifier',
]

@pulumi.output_type
class GetApiManagementServiceDomainOwnershipIdentifierResult:
    """
    Response of the GetDomainOwnershipIdentifier operation.
    """
    def __init__(__self__, domain_ownership_identifier=None):
        if domain_ownership_identifier and not isinstance(domain_ownership_identifier, str):
            raise TypeError("Expected argument 'domain_ownership_identifier' to be a str")
        pulumi.set(__self__, "domain_ownership_identifier", domain_ownership_identifier)

    @property
    @pulumi.getter(name="domainOwnershipIdentifier")
    def domain_ownership_identifier(self) -> str:
        """
        The domain ownership identifier value.
        """
        return pulumi.get(self, "domain_ownership_identifier")


class AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult(GetApiManagementServiceDomainOwnershipIdentifierResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiManagementServiceDomainOwnershipIdentifierResult(
            domain_ownership_identifier=self.domain_ownership_identifier)


def get_api_management_service_domain_ownership_identifier(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult:
    """
    Response of the GetDomainOwnershipIdentifier operation.
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20210401preview:getApiManagementServiceDomainOwnershipIdentifier', __args__, opts=opts, typ=GetApiManagementServiceDomainOwnershipIdentifierResult).value

    return AwaitableGetApiManagementServiceDomainOwnershipIdentifierResult(
        domain_ownership_identifier=__ret__.domain_ownership_identifier)
