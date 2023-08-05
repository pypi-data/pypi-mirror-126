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
from ._inputs import *

__all__ = ['ApiDiagnosticArgs', 'ApiDiagnostic']

@pulumi.input_type
class ApiDiagnosticArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 logger_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 always_log: Optional[pulumi.Input[Union[str, 'AlwaysLog']]] = None,
                 backend: Optional[pulumi.Input['PipelineDiagnosticSettingsArgs']] = None,
                 diagnostic_id: Optional[pulumi.Input[str]] = None,
                 frontend: Optional[pulumi.Input['PipelineDiagnosticSettingsArgs']] = None,
                 http_correlation_protocol: Optional[pulumi.Input[Union[str, 'HttpCorrelationProtocol']]] = None,
                 log_client_ip: Optional[pulumi.Input[bool]] = None,
                 sampling: Optional[pulumi.Input['SamplingSettingsArgs']] = None,
                 verbosity: Optional[pulumi.Input[Union[str, 'Verbosity']]] = None):
        """
        The set of arguments for constructing a ApiDiagnostic resource.
        :param pulumi.Input[str] api_id: API identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] logger_id: Resource Id of a target logger.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Union[str, 'AlwaysLog']] always_log: Specifies for what type of messages sampling settings should not apply.
        :param pulumi.Input['PipelineDiagnosticSettingsArgs'] backend: Diagnostic settings for incoming/outgoing HTTP messages to the Backend
        :param pulumi.Input[str] diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input['PipelineDiagnosticSettingsArgs'] frontend: Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
        :param pulumi.Input[Union[str, 'HttpCorrelationProtocol']] http_correlation_protocol: Sets correlation protocol to use for Application Insights diagnostics.
        :param pulumi.Input[bool] log_client_ip: Log the ClientIP. Default is false.
        :param pulumi.Input['SamplingSettingsArgs'] sampling: Sampling settings for Diagnostic.
        :param pulumi.Input[Union[str, 'Verbosity']] verbosity: The verbosity level applied to traces emitted by trace policies.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "logger_id", logger_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if always_log is not None:
            pulumi.set(__self__, "always_log", always_log)
        if backend is not None:
            pulumi.set(__self__, "backend", backend)
        if diagnostic_id is not None:
            pulumi.set(__self__, "diagnostic_id", diagnostic_id)
        if frontend is not None:
            pulumi.set(__self__, "frontend", frontend)
        if http_correlation_protocol is not None:
            pulumi.set(__self__, "http_correlation_protocol", http_correlation_protocol)
        if log_client_ip is not None:
            pulumi.set(__self__, "log_client_ip", log_client_ip)
        if sampling is not None:
            pulumi.set(__self__, "sampling", sampling)
        if verbosity is not None:
            pulumi.set(__self__, "verbosity", verbosity)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="loggerId")
    def logger_id(self) -> pulumi.Input[str]:
        """
        Resource Id of a target logger.
        """
        return pulumi.get(self, "logger_id")

    @logger_id.setter
    def logger_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "logger_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="alwaysLog")
    def always_log(self) -> Optional[pulumi.Input[Union[str, 'AlwaysLog']]]:
        """
        Specifies for what type of messages sampling settings should not apply.
        """
        return pulumi.get(self, "always_log")

    @always_log.setter
    def always_log(self, value: Optional[pulumi.Input[Union[str, 'AlwaysLog']]]):
        pulumi.set(self, "always_log", value)

    @property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input['PipelineDiagnosticSettingsArgs']]:
        """
        Diagnostic settings for incoming/outgoing HTTP messages to the Backend
        """
        return pulumi.get(self, "backend")

    @backend.setter
    def backend(self, value: Optional[pulumi.Input['PipelineDiagnosticSettingsArgs']]):
        pulumi.set(self, "backend", value)

    @property
    @pulumi.getter(name="diagnosticId")
    def diagnostic_id(self) -> Optional[pulumi.Input[str]]:
        """
        Diagnostic identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "diagnostic_id")

    @diagnostic_id.setter
    def diagnostic_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "diagnostic_id", value)

    @property
    @pulumi.getter
    def frontend(self) -> Optional[pulumi.Input['PipelineDiagnosticSettingsArgs']]:
        """
        Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
        """
        return pulumi.get(self, "frontend")

    @frontend.setter
    def frontend(self, value: Optional[pulumi.Input['PipelineDiagnosticSettingsArgs']]):
        pulumi.set(self, "frontend", value)

    @property
    @pulumi.getter(name="httpCorrelationProtocol")
    def http_correlation_protocol(self) -> Optional[pulumi.Input[Union[str, 'HttpCorrelationProtocol']]]:
        """
        Sets correlation protocol to use for Application Insights diagnostics.
        """
        return pulumi.get(self, "http_correlation_protocol")

    @http_correlation_protocol.setter
    def http_correlation_protocol(self, value: Optional[pulumi.Input[Union[str, 'HttpCorrelationProtocol']]]):
        pulumi.set(self, "http_correlation_protocol", value)

    @property
    @pulumi.getter(name="logClientIp")
    def log_client_ip(self) -> Optional[pulumi.Input[bool]]:
        """
        Log the ClientIP. Default is false.
        """
        return pulumi.get(self, "log_client_ip")

    @log_client_ip.setter
    def log_client_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_client_ip", value)

    @property
    @pulumi.getter
    def sampling(self) -> Optional[pulumi.Input['SamplingSettingsArgs']]:
        """
        Sampling settings for Diagnostic.
        """
        return pulumi.get(self, "sampling")

    @sampling.setter
    def sampling(self, value: Optional[pulumi.Input['SamplingSettingsArgs']]):
        pulumi.set(self, "sampling", value)

    @property
    @pulumi.getter
    def verbosity(self) -> Optional[pulumi.Input[Union[str, 'Verbosity']]]:
        """
        The verbosity level applied to traces emitted by trace policies.
        """
        return pulumi.get(self, "verbosity")

    @verbosity.setter
    def verbosity(self, value: Optional[pulumi.Input[Union[str, 'Verbosity']]]):
        pulumi.set(self, "verbosity", value)


class ApiDiagnostic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_log: Optional[pulumi.Input[Union[str, 'AlwaysLog']]] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 backend: Optional[pulumi.Input[pulumi.InputType['PipelineDiagnosticSettingsArgs']]] = None,
                 diagnostic_id: Optional[pulumi.Input[str]] = None,
                 frontend: Optional[pulumi.Input[pulumi.InputType['PipelineDiagnosticSettingsArgs']]] = None,
                 http_correlation_protocol: Optional[pulumi.Input[Union[str, 'HttpCorrelationProtocol']]] = None,
                 log_client_ip: Optional[pulumi.Input[bool]] = None,
                 logger_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sampling: Optional[pulumi.Input[pulumi.InputType['SamplingSettingsArgs']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 verbosity: Optional[pulumi.Input[Union[str, 'Verbosity']]] = None,
                 __props__=None):
        """
        Diagnostic details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'AlwaysLog']] always_log: Specifies for what type of messages sampling settings should not apply.
        :param pulumi.Input[str] api_id: API identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[pulumi.InputType['PipelineDiagnosticSettingsArgs']] backend: Diagnostic settings for incoming/outgoing HTTP messages to the Backend
        :param pulumi.Input[str] diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[pulumi.InputType['PipelineDiagnosticSettingsArgs']] frontend: Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
        :param pulumi.Input[Union[str, 'HttpCorrelationProtocol']] http_correlation_protocol: Sets correlation protocol to use for Application Insights diagnostics.
        :param pulumi.Input[bool] log_client_ip: Log the ClientIP. Default is false.
        :param pulumi.Input[str] logger_id: Resource Id of a target logger.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SamplingSettingsArgs']] sampling: Sampling settings for Diagnostic.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Union[str, 'Verbosity']] verbosity: The verbosity level applied to traces emitted by trace policies.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiDiagnosticArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Diagnostic details.

        :param str resource_name: The name of the resource.
        :param ApiDiagnosticArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiDiagnosticArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_log: Optional[pulumi.Input[Union[str, 'AlwaysLog']]] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 backend: Optional[pulumi.Input[pulumi.InputType['PipelineDiagnosticSettingsArgs']]] = None,
                 diagnostic_id: Optional[pulumi.Input[str]] = None,
                 frontend: Optional[pulumi.Input[pulumi.InputType['PipelineDiagnosticSettingsArgs']]] = None,
                 http_correlation_protocol: Optional[pulumi.Input[Union[str, 'HttpCorrelationProtocol']]] = None,
                 log_client_ip: Optional[pulumi.Input[bool]] = None,
                 logger_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sampling: Optional[pulumi.Input[pulumi.InputType['SamplingSettingsArgs']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 verbosity: Optional[pulumi.Input[Union[str, 'Verbosity']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiDiagnosticArgs.__new__(ApiDiagnosticArgs)

            __props__.__dict__["always_log"] = always_log
            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["backend"] = backend
            __props__.__dict__["diagnostic_id"] = diagnostic_id
            __props__.__dict__["frontend"] = frontend
            __props__.__dict__["http_correlation_protocol"] = http_correlation_protocol
            __props__.__dict__["log_client_ip"] = log_client_ip
            if logger_id is None and not opts.urn:
                raise TypeError("Missing required property 'logger_id'")
            __props__.__dict__["logger_id"] = logger_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sampling"] = sampling
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["verbosity"] = verbosity
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210401preview:ApiDiagnostic"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ApiDiagnostic"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210801:ApiDiagnostic")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiDiagnostic, __self__).__init__(
            'azure-native:apimanagement/v20191201preview:ApiDiagnostic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiDiagnostic':
        """
        Get an existing ApiDiagnostic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiDiagnosticArgs.__new__(ApiDiagnosticArgs)

        __props__.__dict__["always_log"] = None
        __props__.__dict__["backend"] = None
        __props__.__dict__["frontend"] = None
        __props__.__dict__["http_correlation_protocol"] = None
        __props__.__dict__["log_client_ip"] = None
        __props__.__dict__["logger_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sampling"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["verbosity"] = None
        return ApiDiagnostic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alwaysLog")
    def always_log(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies for what type of messages sampling settings should not apply.
        """
        return pulumi.get(self, "always_log")

    @property
    @pulumi.getter
    def backend(self) -> pulumi.Output[Optional['outputs.PipelineDiagnosticSettingsResponse']]:
        """
        Diagnostic settings for incoming/outgoing HTTP messages to the Backend
        """
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter
    def frontend(self) -> pulumi.Output[Optional['outputs.PipelineDiagnosticSettingsResponse']]:
        """
        Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
        """
        return pulumi.get(self, "frontend")

    @property
    @pulumi.getter(name="httpCorrelationProtocol")
    def http_correlation_protocol(self) -> pulumi.Output[Optional[str]]:
        """
        Sets correlation protocol to use for Application Insights diagnostics.
        """
        return pulumi.get(self, "http_correlation_protocol")

    @property
    @pulumi.getter(name="logClientIp")
    def log_client_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        Log the ClientIP. Default is false.
        """
        return pulumi.get(self, "log_client_ip")

    @property
    @pulumi.getter(name="loggerId")
    def logger_id(self) -> pulumi.Output[str]:
        """
        Resource Id of a target logger.
        """
        return pulumi.get(self, "logger_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sampling(self) -> pulumi.Output[Optional['outputs.SamplingSettingsResponse']]:
        """
        Sampling settings for Diagnostic.
        """
        return pulumi.get(self, "sampling")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def verbosity(self) -> pulumi.Output[Optional[str]]:
        """
        The verbosity level applied to traces emitted by trace policies.
        """
        return pulumi.get(self, "verbosity")

