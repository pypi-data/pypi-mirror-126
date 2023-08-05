# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .availability_set import *
from .capacity_reservation import *
from .capacity_reservation_group import *
from .cloud_service import *
from .dedicated_host import *
from .dedicated_host_group import *
from .disk import *
from .disk_access import *
from .disk_access_a_private_endpoint_connection import *
from .disk_encryption_set import *
from .gallery import *
from .gallery_application import *
from .gallery_application_version import *
from .gallery_image import *
from .gallery_image_version import *
from .get_availability_set import *
from .get_capacity_reservation import *
from .get_capacity_reservation_group import *
from .get_cloud_service import *
from .get_dedicated_host import *
from .get_dedicated_host_group import *
from .get_disk import *
from .get_disk_access import *
from .get_disk_access_a_private_endpoint_connection import *
from .get_disk_encryption_set import *
from .get_gallery import *
from .get_gallery_application import *
from .get_gallery_application_version import *
from .get_gallery_image import *
from .get_gallery_image_version import *
from .get_image import *
from .get_log_analytic_export_request_rate_by_interval import *
from .get_log_analytic_export_throttled_requests import *
from .get_proximity_placement_group import *
from .get_restore_point import *
from .get_restore_point_collection import *
from .get_snapshot import *
from .get_ssh_public_key import *
from .get_virtual_machine import *
from .get_virtual_machine_extension import *
from .get_virtual_machine_run_command_by_virtual_machine import *
from .get_virtual_machine_scale_set import *
from .get_virtual_machine_scale_set_extension import *
from .get_virtual_machine_scale_set_vm import *
from .get_virtual_machine_scale_set_vm_extension import *
from .get_virtual_machine_scale_set_vm_run_command import *
from .image import *
from .proximity_placement_group import *
from .restore_point import *
from .restore_point_collection import *
from .snapshot import *
from .ssh_public_key import *
from .virtual_machine import *
from .virtual_machine_extension import *
from .virtual_machine_run_command_by_virtual_machine import *
from .virtual_machine_scale_set import *
from .virtual_machine_scale_set_extension import *
from .virtual_machine_scale_set_vm import *
from .virtual_machine_scale_set_vm_extension import *
from .virtual_machine_scale_set_vm_run_command import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.compute.v20150615 as __v20150615
    v20150615 = __v20150615
    import pulumi_azure_native.compute.v20160330 as __v20160330
    v20160330 = __v20160330
    import pulumi_azure_native.compute.v20160430preview as __v20160430preview
    v20160430preview = __v20160430preview
    import pulumi_azure_native.compute.v20170330 as __v20170330
    v20170330 = __v20170330
    import pulumi_azure_native.compute.v20171201 as __v20171201
    v20171201 = __v20171201
    import pulumi_azure_native.compute.v20180401 as __v20180401
    v20180401 = __v20180401
    import pulumi_azure_native.compute.v20180601 as __v20180601
    v20180601 = __v20180601
    import pulumi_azure_native.compute.v20180930 as __v20180930
    v20180930 = __v20180930
    import pulumi_azure_native.compute.v20181001 as __v20181001
    v20181001 = __v20181001
    import pulumi_azure_native.compute.v20190301 as __v20190301
    v20190301 = __v20190301
    import pulumi_azure_native.compute.v20190701 as __v20190701
    v20190701 = __v20190701
    import pulumi_azure_native.compute.v20191101 as __v20191101
    v20191101 = __v20191101
    import pulumi_azure_native.compute.v20191201 as __v20191201
    v20191201 = __v20191201
    import pulumi_azure_native.compute.v20200501 as __v20200501
    v20200501 = __v20200501
    import pulumi_azure_native.compute.v20200601 as __v20200601
    v20200601 = __v20200601
    import pulumi_azure_native.compute.v20200630 as __v20200630
    v20200630 = __v20200630
    import pulumi_azure_native.compute.v20200930 as __v20200930
    v20200930 = __v20200930
    import pulumi_azure_native.compute.v20201001preview as __v20201001preview
    v20201001preview = __v20201001preview
    import pulumi_azure_native.compute.v20201201 as __v20201201
    v20201201 = __v20201201
    import pulumi_azure_native.compute.v20210301 as __v20210301
    v20210301 = __v20210301
    import pulumi_azure_native.compute.v20210401 as __v20210401
    v20210401 = __v20210401
    import pulumi_azure_native.compute.v20210701 as __v20210701
    v20210701 = __v20210701
else:
    v20150615 = _utilities.lazy_import('pulumi_azure_native.compute.v20150615')
    v20160330 = _utilities.lazy_import('pulumi_azure_native.compute.v20160330')
    v20160430preview = _utilities.lazy_import('pulumi_azure_native.compute.v20160430preview')
    v20170330 = _utilities.lazy_import('pulumi_azure_native.compute.v20170330')
    v20171201 = _utilities.lazy_import('pulumi_azure_native.compute.v20171201')
    v20180401 = _utilities.lazy_import('pulumi_azure_native.compute.v20180401')
    v20180601 = _utilities.lazy_import('pulumi_azure_native.compute.v20180601')
    v20180930 = _utilities.lazy_import('pulumi_azure_native.compute.v20180930')
    v20181001 = _utilities.lazy_import('pulumi_azure_native.compute.v20181001')
    v20190301 = _utilities.lazy_import('pulumi_azure_native.compute.v20190301')
    v20190701 = _utilities.lazy_import('pulumi_azure_native.compute.v20190701')
    v20191101 = _utilities.lazy_import('pulumi_azure_native.compute.v20191101')
    v20191201 = _utilities.lazy_import('pulumi_azure_native.compute.v20191201')
    v20200501 = _utilities.lazy_import('pulumi_azure_native.compute.v20200501')
    v20200601 = _utilities.lazy_import('pulumi_azure_native.compute.v20200601')
    v20200630 = _utilities.lazy_import('pulumi_azure_native.compute.v20200630')
    v20200930 = _utilities.lazy_import('pulumi_azure_native.compute.v20200930')
    v20201001preview = _utilities.lazy_import('pulumi_azure_native.compute.v20201001preview')
    v20201201 = _utilities.lazy_import('pulumi_azure_native.compute.v20201201')
    v20210301 = _utilities.lazy_import('pulumi_azure_native.compute.v20210301')
    v20210401 = _utilities.lazy_import('pulumi_azure_native.compute.v20210401')
    v20210701 = _utilities.lazy_import('pulumi_azure_native.compute.v20210701')

