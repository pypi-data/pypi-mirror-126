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

__all__ = [
    'NotificationChannelConfig',
    'NotificationChannelSnsChannelConfig',
    'ResourceCollectionCloudFormationCollectionFilter',
    'ResourceCollectionFilter',
]

@pulumi.output_type
class NotificationChannelConfig(dict):
    """
    Information about notification channels you have configured with DevOps Guru.
    """
    def __init__(__self__, *,
                 sns: Optional['outputs.NotificationChannelSnsChannelConfig'] = None):
        """
        Information about notification channels you have configured with DevOps Guru.
        """
        if sns is not None:
            pulumi.set(__self__, "sns", sns)

    @property
    @pulumi.getter
    def sns(self) -> Optional['outputs.NotificationChannelSnsChannelConfig']:
        return pulumi.get(self, "sns")


@pulumi.output_type
class NotificationChannelSnsChannelConfig(dict):
    """
    Information about a notification channel configured in DevOps Guru to send notifications when insights are created.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "topicArn":
            suggest = "topic_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NotificationChannelSnsChannelConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NotificationChannelSnsChannelConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NotificationChannelSnsChannelConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 topic_arn: Optional[str] = None):
        """
        Information about a notification channel configured in DevOps Guru to send notifications when insights are created.
        """
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[str]:
        return pulumi.get(self, "topic_arn")


@pulumi.output_type
class ResourceCollectionCloudFormationCollectionFilter(dict):
    """
    CloudFormation resource for DevOps Guru to monitor
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "stackNames":
            suggest = "stack_names"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceCollectionCloudFormationCollectionFilter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceCollectionCloudFormationCollectionFilter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceCollectionCloudFormationCollectionFilter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 stack_names: Optional[Sequence[str]] = None):
        """
        CloudFormation resource for DevOps Guru to monitor
        :param Sequence[str] stack_names: An array of CloudFormation stack names.
        """
        if stack_names is not None:
            pulumi.set(__self__, "stack_names", stack_names)

    @property
    @pulumi.getter(name="stackNames")
    def stack_names(self) -> Optional[Sequence[str]]:
        """
        An array of CloudFormation stack names.
        """
        return pulumi.get(self, "stack_names")


@pulumi.output_type
class ResourceCollectionFilter(dict):
    """
    Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudFormation":
            suggest = "cloud_formation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceCollectionFilter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceCollectionFilter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceCollectionFilter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_formation: Optional['outputs.ResourceCollectionCloudFormationCollectionFilter'] = None):
        """
        Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.
        """
        if cloud_formation is not None:
            pulumi.set(__self__, "cloud_formation", cloud_formation)

    @property
    @pulumi.getter(name="cloudFormation")
    def cloud_formation(self) -> Optional['outputs.ResourceCollectionCloudFormationCollectionFilter']:
        return pulumi.get(self, "cloud_formation")


