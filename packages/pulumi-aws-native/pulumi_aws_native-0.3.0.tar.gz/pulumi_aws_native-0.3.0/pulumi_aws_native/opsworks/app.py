# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AppArgs', 'App']

@pulumi.input_type
class AppArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 stack_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 app_source: Optional[pulumi.Input['AppSourceArgs']] = None,
                 attributes: Optional[Any] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input['AppDataSourceArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_ssl: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]] = None,
                 shortname: Optional[pulumi.Input[str]] = None,
                 ssl_configuration: Optional[pulumi.Input['AppSslConfigurationArgs']] = None):
        """
        The set of arguments for constructing a App resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "stack_id", stack_id)
        pulumi.set(__self__, "type", type)
        if app_source is not None:
            pulumi.set(__self__, "app_source", app_source)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if data_sources is not None:
            pulumi.set(__self__, "data_sources", data_sources)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domains is not None:
            pulumi.set(__self__, "domains", domains)
        if enable_ssl is not None:
            pulumi.set(__self__, "enable_ssl", enable_ssl)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if shortname is not None:
            pulumi.set(__self__, "shortname", shortname)
        if ssl_configuration is not None:
            pulumi.set(__self__, "ssl_configuration", ssl_configuration)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stack_id")

    @stack_id.setter
    def stack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "stack_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="appSource")
    def app_source(self) -> Optional[pulumi.Input['AppSourceArgs']]:
        return pulumi.get(self, "app_source")

    @app_source.setter
    def app_source(self, value: Optional[pulumi.Input['AppSourceArgs']]):
        pulumi.set(self, "app_source", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[Any]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppDataSourceArgs']]]]:
        return pulumi.get(self, "data_sources")

    @data_sources.setter
    def data_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppDataSourceArgs']]]]):
        pulumi.set(self, "data_sources", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter(name="enableSsl")
    def enable_ssl(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_ssl")

    @enable_ssl.setter
    def enable_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ssl", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]:
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def shortname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "shortname")

    @shortname.setter
    def shortname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shortname", value)

    @property
    @pulumi.getter(name="sslConfiguration")
    def ssl_configuration(self) -> Optional[pulumi.Input['AppSslConfigurationArgs']]:
        return pulumi.get(self, "ssl_configuration")

    @ssl_configuration.setter
    def ssl_configuration(self, value: Optional[pulumi.Input['AppSslConfigurationArgs']]):
        pulumi.set(self, "ssl_configuration", value)


warnings.warn("""App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class App(pulumi.CustomResource):
    warnings.warn("""App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_source: Optional[pulumi.Input[pulumi.InputType['AppSourceArgs']]] = None,
                 attributes: Optional[Any] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppDataSourceArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_ssl: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppEnvironmentVariableArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shortname: Optional[pulumi.Input[str]] = None,
                 ssl_configuration: Optional[pulumi.Input[pulumi.InputType['AppSslConfigurationArgs']]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::OpsWorks::App

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::OpsWorks::App

        :param str resource_name: The name of the resource.
        :param AppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_source: Optional[pulumi.Input[pulumi.InputType['AppSourceArgs']]] = None,
                 attributes: Optional[Any] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppDataSourceArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_ssl: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppEnvironmentVariableArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shortname: Optional[pulumi.Input[str]] = None,
                 ssl_configuration: Optional[pulumi.Input[pulumi.InputType['AppSslConfigurationArgs']]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""App is deprecated: App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppArgs.__new__(AppArgs)

            __props__.__dict__["app_source"] = app_source
            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["data_sources"] = data_sources
            __props__.__dict__["description"] = description
            __props__.__dict__["domains"] = domains
            __props__.__dict__["enable_ssl"] = enable_ssl
            __props__.__dict__["environment"] = environment
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["shortname"] = shortname
            __props__.__dict__["ssl_configuration"] = ssl_configuration
            if stack_id is None and not opts.urn:
                raise TypeError("Missing required property 'stack_id'")
            __props__.__dict__["stack_id"] = stack_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(App, __self__).__init__(
            'aws-native:opsworks:App',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'App':
        """
        Get an existing App resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppArgs.__new__(AppArgs)

        __props__.__dict__["app_source"] = None
        __props__.__dict__["attributes"] = None
        __props__.__dict__["data_sources"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["domains"] = None
        __props__.__dict__["enable_ssl"] = None
        __props__.__dict__["environment"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["shortname"] = None
        __props__.__dict__["ssl_configuration"] = None
        __props__.__dict__["stack_id"] = None
        __props__.__dict__["type"] = None
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appSource")
    def app_source(self) -> pulumi.Output[Optional['outputs.AppSource']]:
        return pulumi.get(self, "app_source")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> pulumi.Output[Optional[Sequence['outputs.AppDataSource']]]:
        return pulumi.get(self, "data_sources")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter(name="enableSsl")
    def enable_ssl(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_ssl")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional[Sequence['outputs.AppEnvironmentVariable']]]:
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def shortname(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "shortname")

    @property
    @pulumi.getter(name="sslConfiguration")
    def ssl_configuration(self) -> pulumi.Output[Optional['outputs.AppSslConfiguration']]:
        return pulumi.get(self, "ssl_configuration")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stack_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

