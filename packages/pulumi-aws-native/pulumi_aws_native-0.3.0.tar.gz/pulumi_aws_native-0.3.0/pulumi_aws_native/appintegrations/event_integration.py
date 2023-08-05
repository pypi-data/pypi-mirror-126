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

__all__ = ['EventIntegrationArgs', 'EventIntegration']

@pulumi.input_type
class EventIntegrationArgs:
    def __init__(__self__, *,
                 event_bridge_bus: pulumi.Input[str],
                 event_filter: pulumi.Input['EventIntegrationEventFilterArgs'],
                 name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EventIntegrationTagArgs']]]] = None):
        """
        The set of arguments for constructing a EventIntegration resource.
        :param pulumi.Input[str] event_bridge_bus: The Amazon Eventbridge bus for the event integration.
        :param pulumi.Input['EventIntegrationEventFilterArgs'] event_filter: The EventFilter (source) associated with the event integration.
        :param pulumi.Input[str] name: The name of the event integration.
        :param pulumi.Input[str] description: The event integration description.
        :param pulumi.Input[Sequence[pulumi.Input['EventIntegrationTagArgs']]] tags: The tags (keys and values) associated with the event integration.
        """
        pulumi.set(__self__, "event_bridge_bus", event_bridge_bus)
        pulumi.set(__self__, "event_filter", event_filter)
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="eventBridgeBus")
    def event_bridge_bus(self) -> pulumi.Input[str]:
        """
        The Amazon Eventbridge bus for the event integration.
        """
        return pulumi.get(self, "event_bridge_bus")

    @event_bridge_bus.setter
    def event_bridge_bus(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_bridge_bus", value)

    @property
    @pulumi.getter(name="eventFilter")
    def event_filter(self) -> pulumi.Input['EventIntegrationEventFilterArgs']:
        """
        The EventFilter (source) associated with the event integration.
        """
        return pulumi.get(self, "event_filter")

    @event_filter.setter
    def event_filter(self, value: pulumi.Input['EventIntegrationEventFilterArgs']):
        pulumi.set(self, "event_filter", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the event integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The event integration description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventIntegrationTagArgs']]]]:
        """
        The tags (keys and values) associated with the event integration.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventIntegrationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class EventIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 event_bridge_bus: Optional[pulumi.Input[str]] = None,
                 event_filter: Optional[pulumi.Input[pulumi.InputType['EventIntegrationEventFilterArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventIntegrationTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppIntegrations::EventIntegration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The event integration description.
        :param pulumi.Input[str] event_bridge_bus: The Amazon Eventbridge bus for the event integration.
        :param pulumi.Input[pulumi.InputType['EventIntegrationEventFilterArgs']] event_filter: The EventFilter (source) associated with the event integration.
        :param pulumi.Input[str] name: The name of the event integration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventIntegrationTagArgs']]]] tags: The tags (keys and values) associated with the event integration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventIntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppIntegrations::EventIntegration

        :param str resource_name: The name of the resource.
        :param EventIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 event_bridge_bus: Optional[pulumi.Input[str]] = None,
                 event_filter: Optional[pulumi.Input[pulumi.InputType['EventIntegrationEventFilterArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventIntegrationTagArgs']]]]] = None,
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
            __props__ = EventIntegrationArgs.__new__(EventIntegrationArgs)

            __props__.__dict__["description"] = description
            if event_bridge_bus is None and not opts.urn:
                raise TypeError("Missing required property 'event_bridge_bus'")
            __props__.__dict__["event_bridge_bus"] = event_bridge_bus
            if event_filter is None and not opts.urn:
                raise TypeError("Missing required property 'event_filter'")
            __props__.__dict__["event_filter"] = event_filter
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associations"] = None
            __props__.__dict__["event_integration_arn"] = None
        super(EventIntegration, __self__).__init__(
            'aws-native:appintegrations:EventIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventIntegration':
        """
        Get an existing EventIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventIntegrationArgs.__new__(EventIntegrationArgs)

        __props__.__dict__["associations"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["event_bridge_bus"] = None
        __props__.__dict__["event_filter"] = None
        __props__.__dict__["event_integration_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return EventIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def associations(self) -> pulumi.Output[Sequence['outputs.EventIntegrationAssociation']]:
        """
        The associations with the event integration.
        """
        return pulumi.get(self, "associations")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The event integration description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eventBridgeBus")
    def event_bridge_bus(self) -> pulumi.Output[str]:
        """
        The Amazon Eventbridge bus for the event integration.
        """
        return pulumi.get(self, "event_bridge_bus")

    @property
    @pulumi.getter(name="eventFilter")
    def event_filter(self) -> pulumi.Output['outputs.EventIntegrationEventFilter']:
        """
        The EventFilter (source) associated with the event integration.
        """
        return pulumi.get(self, "event_filter")

    @property
    @pulumi.getter(name="eventIntegrationArn")
    def event_integration_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the event integration.
        """
        return pulumi.get(self, "event_integration_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the event integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EventIntegrationTag']]]:
        """
        The tags (keys and values) associated with the event integration.
        """
        return pulumi.get(self, "tags")

