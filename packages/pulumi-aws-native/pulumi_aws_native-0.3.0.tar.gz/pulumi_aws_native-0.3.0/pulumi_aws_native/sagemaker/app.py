# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['AppArgs', 'App']

@pulumi.input_type
class AppArgs:
    def __init__(__self__, *,
                 app_name: pulumi.Input[str],
                 app_type: pulumi.Input['AppType'],
                 domain_id: pulumi.Input[str],
                 user_profile_name: pulumi.Input[str],
                 resource_spec: Optional[pulumi.Input['AppResourceSpecArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]]] = None):
        """
        The set of arguments for constructing a App resource.
        :param pulumi.Input[str] app_name: The name of the app.
        :param pulumi.Input['AppType'] app_type: The type of app.
        :param pulumi.Input[str] domain_id: The domain ID.
        :param pulumi.Input[str] user_profile_name: The user profile name.
        :param pulumi.Input['AppResourceSpecArgs'] resource_spec: The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.
        :param pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]] tags: A list of tags to apply to the app.
        """
        pulumi.set(__self__, "app_name", app_name)
        pulumi.set(__self__, "app_type", app_type)
        pulumi.set(__self__, "domain_id", domain_id)
        pulumi.set(__self__, "user_profile_name", user_profile_name)
        if resource_spec is not None:
            pulumi.set(__self__, "resource_spec", resource_spec)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[str]:
        """
        The name of the app.
        """
        return pulumi.get(self, "app_name")

    @app_name.setter
    def app_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_name", value)

    @property
    @pulumi.getter(name="appType")
    def app_type(self) -> pulumi.Input['AppType']:
        """
        The type of app.
        """
        return pulumi.get(self, "app_type")

    @app_type.setter
    def app_type(self, value: pulumi.Input['AppType']):
        pulumi.set(self, "app_type", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[str]:
        """
        The domain ID.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> pulumi.Input[str]:
        """
        The user profile name.
        """
        return pulumi.get(self, "user_profile_name")

    @user_profile_name.setter
    def user_profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_profile_name", value)

    @property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> Optional[pulumi.Input['AppResourceSpecArgs']]:
        """
        The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.
        """
        return pulumi.get(self, "resource_spec")

    @resource_spec.setter
    def resource_spec(self, value: Optional[pulumi.Input['AppResourceSpecArgs']]):
        pulumi.set(self, "resource_spec", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]]]:
        """
        A list of tags to apply to the app.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppTagArgs']]]]):
        pulumi.set(self, "tags", value)


class App(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_name: Optional[pulumi.Input[str]] = None,
                 app_type: Optional[pulumi.Input['AppType']] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input[pulumi.InputType['AppResourceSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTagArgs']]]]] = None,
                 user_profile_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::App

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_name: The name of the app.
        :param pulumi.Input['AppType'] app_type: The type of app.
        :param pulumi.Input[str] domain_id: The domain ID.
        :param pulumi.Input[pulumi.InputType['AppResourceSpecArgs']] resource_spec: The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTagArgs']]]] tags: A list of tags to apply to the app.
        :param pulumi.Input[str] user_profile_name: The user profile name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::App

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
                 app_name: Optional[pulumi.Input[str]] = None,
                 app_type: Optional[pulumi.Input['AppType']] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input[pulumi.InputType['AppResourceSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTagArgs']]]]] = None,
                 user_profile_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AppArgs.__new__(AppArgs)

            if app_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_name'")
            __props__.__dict__["app_name"] = app_name
            if app_type is None and not opts.urn:
                raise TypeError("Missing required property 'app_type'")
            __props__.__dict__["app_type"] = app_type
            if domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'domain_id'")
            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["resource_spec"] = resource_spec
            __props__.__dict__["tags"] = tags
            if user_profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_profile_name'")
            __props__.__dict__["user_profile_name"] = user_profile_name
            __props__.__dict__["app_arn"] = None
        super(App, __self__).__init__(
            'aws-native:sagemaker:App',
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

        __props__.__dict__["app_arn"] = None
        __props__.__dict__["app_name"] = None
        __props__.__dict__["app_type"] = None
        __props__.__dict__["domain_id"] = None
        __props__.__dict__["resource_spec"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_profile_name"] = None
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appArn")
    def app_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the app.
        """
        return pulumi.get(self, "app_arn")

    @property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Output[str]:
        """
        The name of the app.
        """
        return pulumi.get(self, "app_name")

    @property
    @pulumi.getter(name="appType")
    def app_type(self) -> pulumi.Output['AppType']:
        """
        The type of app.
        """
        return pulumi.get(self, "app_type")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The domain ID.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Output[Optional['outputs.AppResourceSpec']]:
        """
        The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.
        """
        return pulumi.get(self, "resource_spec")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AppTag']]]:
        """
        A list of tags to apply to the app.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> pulumi.Output[str]:
        """
        The user profile name.
        """
        return pulumi.get(self, "user_profile_name")

