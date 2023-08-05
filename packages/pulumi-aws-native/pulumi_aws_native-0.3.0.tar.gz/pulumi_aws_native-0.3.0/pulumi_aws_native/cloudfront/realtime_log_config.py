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

__all__ = ['RealtimeLogConfigArgs', 'RealtimeLogConfig']

@pulumi.input_type
class RealtimeLogConfigArgs:
    def __init__(__self__, *,
                 end_points: pulumi.Input[Sequence[pulumi.Input['RealtimeLogConfigEndPointArgs']]],
                 fields: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: pulumi.Input[str],
                 sampling_rate: pulumi.Input[float]):
        """
        The set of arguments for constructing a RealtimeLogConfig resource.
        """
        pulumi.set(__self__, "end_points", end_points)
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "sampling_rate", sampling_rate)

    @property
    @pulumi.getter(name="endPoints")
    def end_points(self) -> pulumi.Input[Sequence[pulumi.Input['RealtimeLogConfigEndPointArgs']]]:
        return pulumi.get(self, "end_points")

    @end_points.setter
    def end_points(self, value: pulumi.Input[Sequence[pulumi.Input['RealtimeLogConfigEndPointArgs']]]):
        pulumi.set(self, "end_points", value)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Input[float]:
        return pulumi.get(self, "sampling_rate")

    @sampling_rate.setter
    def sampling_rate(self, value: pulumi.Input[float]):
        pulumi.set(self, "sampling_rate", value)


class RealtimeLogConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_points: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RealtimeLogConfigEndPointArgs']]]]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sampling_rate: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudFront::RealtimeLogConfig

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RealtimeLogConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudFront::RealtimeLogConfig

        :param str resource_name: The name of the resource.
        :param RealtimeLogConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RealtimeLogConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_points: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RealtimeLogConfigEndPointArgs']]]]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sampling_rate: Optional[pulumi.Input[float]] = None,
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
            __props__ = RealtimeLogConfigArgs.__new__(RealtimeLogConfigArgs)

            if end_points is None and not opts.urn:
                raise TypeError("Missing required property 'end_points'")
            __props__.__dict__["end_points"] = end_points
            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if sampling_rate is None and not opts.urn:
                raise TypeError("Missing required property 'sampling_rate'")
            __props__.__dict__["sampling_rate"] = sampling_rate
            __props__.__dict__["arn"] = None
        super(RealtimeLogConfig, __self__).__init__(
            'aws-native:cloudfront:RealtimeLogConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RealtimeLogConfig':
        """
        Get an existing RealtimeLogConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RealtimeLogConfigArgs.__new__(RealtimeLogConfigArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["end_points"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sampling_rate"] = None
        return RealtimeLogConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="endPoints")
    def end_points(self) -> pulumi.Output[Sequence['outputs.RealtimeLogConfigEndPoint']]:
        return pulumi.get(self, "end_points")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Output[float]:
        return pulumi.get(self, "sampling_rate")

