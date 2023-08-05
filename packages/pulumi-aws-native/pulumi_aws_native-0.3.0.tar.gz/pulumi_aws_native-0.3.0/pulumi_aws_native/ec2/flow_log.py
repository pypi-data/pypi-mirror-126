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

__all__ = ['FlowLogArgs', 'FlowLog']

@pulumi.input_type
class FlowLogArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 resource_type: pulumi.Input['FlowLogResourceType'],
                 traffic_type: pulumi.Input['FlowLogTrafficType'],
                 deliver_logs_permission_arn: Optional[pulumi.Input[str]] = None,
                 log_destination: Optional[pulumi.Input[str]] = None,
                 log_destination_type: Optional[pulumi.Input['FlowLogLogDestinationType']] = None,
                 log_format: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 max_aggregation_interval: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FlowLogTagArgs']]]] = None):
        """
        The set of arguments for constructing a FlowLog resource.
        :param pulumi.Input[str] resource_id: The ID of the subnet, network interface, or VPC for which you want to create a flow log.
        :param pulumi.Input['FlowLogResourceType'] resource_type: The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
        :param pulumi.Input['FlowLogTrafficType'] traffic_type: The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        :param pulumi.Input[str] deliver_logs_permission_arn: The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        :param pulumi.Input[str] log_destination: Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType.
        :param pulumi.Input['FlowLogLogDestinationType'] log_destination_type: Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
        :param pulumi.Input[str] log_format: The fields to include in the flow log record, in the order in which they should appear.
        :param pulumi.Input[str] log_group_name: The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        :param pulumi.Input[int] max_aggregation_interval: The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        :param pulumi.Input[Sequence[pulumi.Input['FlowLogTagArgs']]] tags: The tags to apply to the flow logs.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "resource_type", resource_type)
        pulumi.set(__self__, "traffic_type", traffic_type)
        if deliver_logs_permission_arn is not None:
            pulumi.set(__self__, "deliver_logs_permission_arn", deliver_logs_permission_arn)
        if log_destination is not None:
            pulumi.set(__self__, "log_destination", log_destination)
        if log_destination_type is not None:
            pulumi.set(__self__, "log_destination_type", log_destination_type)
        if log_format is not None:
            pulumi.set(__self__, "log_format", log_format)
        if log_group_name is not None:
            pulumi.set(__self__, "log_group_name", log_group_name)
        if max_aggregation_interval is not None:
            pulumi.set(__self__, "max_aggregation_interval", max_aggregation_interval)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The ID of the subnet, network interface, or VPC for which you want to create a flow log.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input['FlowLogResourceType']:
        """
        The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input['FlowLogResourceType']):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="trafficType")
    def traffic_type(self) -> pulumi.Input['FlowLogTrafficType']:
        """
        The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        """
        return pulumi.get(self, "traffic_type")

    @traffic_type.setter
    def traffic_type(self, value: pulumi.Input['FlowLogTrafficType']):
        pulumi.set(self, "traffic_type", value)

    @property
    @pulumi.getter(name="deliverLogsPermissionArn")
    def deliver_logs_permission_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        """
        return pulumi.get(self, "deliver_logs_permission_arn")

    @deliver_logs_permission_arn.setter
    def deliver_logs_permission_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deliver_logs_permission_arn", value)

    @property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType.
        """
        return pulumi.get(self, "log_destination")

    @log_destination.setter
    def log_destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_destination", value)

    @property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> Optional[pulumi.Input['FlowLogLogDestinationType']]:
        """
        Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
        """
        return pulumi.get(self, "log_destination_type")

    @log_destination_type.setter
    def log_destination_type(self, value: Optional[pulumi.Input['FlowLogLogDestinationType']]):
        pulumi.set(self, "log_destination_type", value)

    @property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[pulumi.Input[str]]:
        """
        The fields to include in the flow log record, in the order in which they should appear.
        """
        return pulumi.get(self, "log_format")

    @log_format.setter
    def log_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_format", value)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        """
        return pulumi.get(self, "log_group_name")

    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_group_name", value)

    @property
    @pulumi.getter(name="maxAggregationInterval")
    def max_aggregation_interval(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        """
        return pulumi.get(self, "max_aggregation_interval")

    @max_aggregation_interval.setter
    def max_aggregation_interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_aggregation_interval", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlowLogTagArgs']]]]:
        """
        The tags to apply to the flow logs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlowLogTagArgs']]]]):
        pulumi.set(self, "tags", value)


class FlowLog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deliver_logs_permission_arn: Optional[pulumi.Input[str]] = None,
                 log_destination: Optional[pulumi.Input[str]] = None,
                 log_destination_type: Optional[pulumi.Input['FlowLogLogDestinationType']] = None,
                 log_format: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 max_aggregation_interval: Optional[pulumi.Input[int]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input['FlowLogResourceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlowLogTagArgs']]]]] = None,
                 traffic_type: Optional[pulumi.Input['FlowLogTrafficType']] = None,
                 __props__=None):
        """
        Specifies a VPC flow log, which enables you to capture IP traffic for a specific network interface, subnet, or VPC.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deliver_logs_permission_arn: The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        :param pulumi.Input[str] log_destination: Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType.
        :param pulumi.Input['FlowLogLogDestinationType'] log_destination_type: Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
        :param pulumi.Input[str] log_format: The fields to include in the flow log record, in the order in which they should appear.
        :param pulumi.Input[str] log_group_name: The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        :param pulumi.Input[int] max_aggregation_interval: The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        :param pulumi.Input[str] resource_id: The ID of the subnet, network interface, or VPC for which you want to create a flow log.
        :param pulumi.Input['FlowLogResourceType'] resource_type: The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlowLogTagArgs']]]] tags: The tags to apply to the flow logs.
        :param pulumi.Input['FlowLogTrafficType'] traffic_type: The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlowLogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies a VPC flow log, which enables you to capture IP traffic for a specific network interface, subnet, or VPC.

        :param str resource_name: The name of the resource.
        :param FlowLogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlowLogArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deliver_logs_permission_arn: Optional[pulumi.Input[str]] = None,
                 log_destination: Optional[pulumi.Input[str]] = None,
                 log_destination_type: Optional[pulumi.Input['FlowLogLogDestinationType']] = None,
                 log_format: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 max_aggregation_interval: Optional[pulumi.Input[int]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input['FlowLogResourceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlowLogTagArgs']]]]] = None,
                 traffic_type: Optional[pulumi.Input['FlowLogTrafficType']] = None,
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
            __props__ = FlowLogArgs.__new__(FlowLogArgs)

            __props__.__dict__["deliver_logs_permission_arn"] = deliver_logs_permission_arn
            __props__.__dict__["log_destination"] = log_destination
            __props__.__dict__["log_destination_type"] = log_destination_type
            __props__.__dict__["log_format"] = log_format
            __props__.__dict__["log_group_name"] = log_group_name
            __props__.__dict__["max_aggregation_interval"] = max_aggregation_interval
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["tags"] = tags
            if traffic_type is None and not opts.urn:
                raise TypeError("Missing required property 'traffic_type'")
            __props__.__dict__["traffic_type"] = traffic_type
        super(FlowLog, __self__).__init__(
            'aws-native:ec2:FlowLog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FlowLog':
        """
        Get an existing FlowLog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FlowLogArgs.__new__(FlowLogArgs)

        __props__.__dict__["deliver_logs_permission_arn"] = None
        __props__.__dict__["log_destination"] = None
        __props__.__dict__["log_destination_type"] = None
        __props__.__dict__["log_format"] = None
        __props__.__dict__["log_group_name"] = None
        __props__.__dict__["max_aggregation_interval"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["traffic_type"] = None
        return FlowLog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deliverLogsPermissionArn")
    def deliver_logs_permission_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        """
        return pulumi.get(self, "deliver_logs_permission_arn")

    @property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType.
        """
        return pulumi.get(self, "log_destination")

    @property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> pulumi.Output[Optional['FlowLogLogDestinationType']]:
        """
        Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
        """
        return pulumi.get(self, "log_destination_type")

    @property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> pulumi.Output[Optional[str]]:
        """
        The fields to include in the flow log record, in the order in which they should appear.
        """
        return pulumi.get(self, "log_format")

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3, do not specify DeliverLogsPermissionArn or LogGroupName.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="maxAggregationInterval")
    def max_aggregation_interval(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        """
        return pulumi.get(self, "max_aggregation_interval")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet, network interface, or VPC for which you want to create a flow log.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output['FlowLogResourceType']:
        """
        The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FlowLogTag']]]:
        """
        The tags to apply to the flow logs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficType")
    def traffic_type(self) -> pulumi.Output['FlowLogTrafficType']:
        """
        The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        """
        return pulumi.get(self, "traffic_type")

