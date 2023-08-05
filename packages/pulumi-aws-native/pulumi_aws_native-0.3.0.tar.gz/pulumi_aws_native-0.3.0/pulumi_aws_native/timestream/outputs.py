# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DatabaseTag',
    'RetentionPropertiesProperties',
    'TableTag',
]

@pulumi.output_type
class DatabaseTag(dict):
    """
    You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
    """
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        """
        You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class RetentionPropertiesProperties(dict):
    """
    The retention duration of the memory store and the magnetic store.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "magneticStoreRetentionPeriodInDays":
            suggest = "magnetic_store_retention_period_in_days"
        elif key == "memoryStoreRetentionPeriodInHours":
            suggest = "memory_store_retention_period_in_hours"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RetentionPropertiesProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RetentionPropertiesProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RetentionPropertiesProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 magnetic_store_retention_period_in_days: Optional[str] = None,
                 memory_store_retention_period_in_hours: Optional[str] = None):
        """
        The retention duration of the memory store and the magnetic store.
        :param str magnetic_store_retention_period_in_days: The duration for which data must be stored in the magnetic store.
        :param str memory_store_retention_period_in_hours: The duration for which data must be stored in the memory store.
        """
        if magnetic_store_retention_period_in_days is not None:
            pulumi.set(__self__, "magnetic_store_retention_period_in_days", magnetic_store_retention_period_in_days)
        if memory_store_retention_period_in_hours is not None:
            pulumi.set(__self__, "memory_store_retention_period_in_hours", memory_store_retention_period_in_hours)

    @property
    @pulumi.getter(name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(self) -> Optional[str]:
        """
        The duration for which data must be stored in the magnetic store.
        """
        return pulumi.get(self, "magnetic_store_retention_period_in_days")

    @property
    @pulumi.getter(name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> Optional[str]:
        """
        The duration for which data must be stored in the memory store.
        """
        return pulumi.get(self, "memory_store_retention_period_in_hours")


@pulumi.output_type
class TableTag(dict):
    """
    You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
    """
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        """
        You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


