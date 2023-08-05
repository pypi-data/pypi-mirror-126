# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'WorkbookTemplateGalleryArgs',
    'WorkbookTemplateLocalizedGalleryArgs',
]

@pulumi.input_type
class WorkbookTemplateGalleryArgs:
    def __init__(__self__, *,
                 category: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Gallery information for a workbook template.
        :param pulumi.Input[str] category: Category for the gallery.
        :param pulumi.Input[str] name: Name of the workbook template in the gallery.
        :param pulumi.Input[int] order: Order of the template within the gallery.
        :param pulumi.Input[str] resource_type: Azure resource type supported by the gallery.
        :param pulumi.Input[str] type: Type of workbook supported by the workbook template.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Category for the gallery.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the workbook template in the gallery.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        Order of the template within the gallery.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Azure resource type supported by the gallery.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of workbook supported by the workbook template.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class WorkbookTemplateLocalizedGalleryArgs:
    def __init__(__self__, *,
                 galleries: Optional[pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]]] = None,
                 template_data: Optional[Any] = None):
        """
        Localized template data and gallery information.
        :param pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]] galleries: Workbook galleries supported by the template.
        :param Any template_data: Valid JSON object containing workbook template payload.
        """
        if galleries is not None:
            pulumi.set(__self__, "galleries", galleries)
        if template_data is not None:
            pulumi.set(__self__, "template_data", template_data)

    @property
    @pulumi.getter
    def galleries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]]]:
        """
        Workbook galleries supported by the template.
        """
        return pulumi.get(self, "galleries")

    @galleries.setter
    def galleries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]]]):
        pulumi.set(self, "galleries", value)

    @property
    @pulumi.getter(name="templateData")
    def template_data(self) -> Optional[Any]:
        """
        Valid JSON object containing workbook template payload.
        """
        return pulumi.get(self, "template_data")

    @template_data.setter
    def template_data(self, value: Optional[Any]):
        pulumi.set(self, "template_data", value)


