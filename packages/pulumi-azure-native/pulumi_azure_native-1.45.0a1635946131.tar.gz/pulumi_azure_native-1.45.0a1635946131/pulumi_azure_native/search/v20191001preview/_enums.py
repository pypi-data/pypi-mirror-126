# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EndpointAccess',
    'HostingMode',
    'IdentityType',
    'PrivateLinkServiceConnectionStatus',
    'SkuName',
]


class EndpointAccess(str, Enum):
    """
    The level of access to the search service endpoint. Public, the search service endpoint is reachable from the internet. Private, the search service endpoint can only be accessed via private endpoints. Default is Public.
    """
    PUBLIC = "Public"
    PRIVATE = "Private"


class HostingMode(str, Enum):
    """
    Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For all other SKUs, this value must be 'default'.
    """
    DEFAULT = "default"
    HIGH_DENSITY = "highDensity"


class IdentityType(str, Enum):
    """
    The identity type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"


class PrivateLinkServiceConnectionStatus(str, Enum):
    """
    Status of the the private link service connection. Can be Pending, Approved, Rejected, or Disconnected.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class SkuName(str, Enum):
    """
    The SKU of the Search service. Valid values include: 'free': Shared service. 'basic': Dedicated service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12 replicas. 'standard2': Similar to standard, but with more capacity per search unit. 'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions with more indexes if you also set the hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
    """
    FREE = "free"
    BASIC = "basic"
    STANDARD = "standard"
    STANDARD2 = "standard2"
    STANDARD3 = "standard3"
    STORAGE_OPTIMIZED_L1 = "storage_optimized_l1"
    STORAGE_OPTIMIZED_L2 = "storage_optimized_l2"
