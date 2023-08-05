# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AgentPermissionsPropertiesArgs',
    'ProfilingGroupChannelArgs',
    'ProfilingGroupTagArgs',
]

@pulumi.input_type
class AgentPermissionsPropertiesArgs:
    def __init__(__self__, *,
                 principals: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The agent permissions attached to this profiling group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] principals: The principals for the agent permissions.
        """
        pulumi.set(__self__, "principals", principals)

    @property
    @pulumi.getter
    def principals(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The principals for the agent permissions.
        """
        return pulumi.get(self, "principals")

    @principals.setter
    def principals(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "principals", value)


@pulumi.input_type
class ProfilingGroupChannelArgs:
    def __init__(__self__, *,
                 channel_uri: pulumi.Input[str],
                 channel_id: Optional[pulumi.Input[str]] = None):
        """
        Notification medium for users to get alerted for events that occur in application profile. We support SNS topic as a notification channel.
        """
        pulumi.set(__self__, "channel_uri", channel_uri)
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)

    @property
    @pulumi.getter(name="channelUri")
    def channel_uri(self) -> pulumi.Input[str]:
        return pulumi.get(self, "channel_uri")

    @channel_uri.setter
    def channel_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel_uri", value)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_id", value)


@pulumi.input_type
class ProfilingGroupTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


