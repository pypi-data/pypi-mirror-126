# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'PipelineField',
    'PipelineObject',
    'PipelineParameterAttribute',
    'PipelineParameterObject',
    'PipelineParameterValue',
    'PipelineTag',
]

@pulumi.output_type
class PipelineField(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "refValue":
            suggest = "ref_value"
        elif key == "stringValue":
            suggest = "string_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineField. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineField.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineField.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key: str,
                 ref_value: Optional[str] = None,
                 string_value: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if ref_value is not None:
            pulumi.set(__self__, "ref_value", ref_value)
        if string_value is not None:
            pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="refValue")
    def ref_value(self) -> Optional[str]:
        return pulumi.get(self, "ref_value")

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[str]:
        return pulumi.get(self, "string_value")


@pulumi.output_type
class PipelineObject(dict):
    def __init__(__self__, *,
                 fields: Sequence['outputs.PipelineField'],
                 id: str,
                 name: str):
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fields(self) -> Sequence['outputs.PipelineField']:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class PipelineParameterAttribute(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "stringValue":
            suggest = "string_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineParameterAttribute. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineParameterAttribute.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineParameterAttribute.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key: str,
                 string_value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> str:
        return pulumi.get(self, "string_value")


@pulumi.output_type
class PipelineParameterObject(dict):
    def __init__(__self__, *,
                 attributes: Sequence['outputs.PipelineParameterAttribute'],
                 id: str):
        pulumi.set(__self__, "attributes", attributes)
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def attributes(self) -> Sequence['outputs.PipelineParameterAttribute']:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")


@pulumi.output_type
class PipelineParameterValue(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "stringValue":
            suggest = "string_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineParameterValue. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineParameterValue.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineParameterValue.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 string_value: str):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "string_value", string_value)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> str:
        return pulumi.get(self, "string_value")


@pulumi.output_type
class PipelineTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


