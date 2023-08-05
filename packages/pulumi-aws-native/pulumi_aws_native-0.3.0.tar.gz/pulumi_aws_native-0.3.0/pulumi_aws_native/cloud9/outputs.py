# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'EnvironmentEC2Repository',
    'EnvironmentEC2Tag',
]

@pulumi.output_type
class EnvironmentEC2Repository(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pathComponent":
            suggest = "path_component"
        elif key == "repositoryUrl":
            suggest = "repository_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnvironmentEC2Repository. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnvironmentEC2Repository.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnvironmentEC2Repository.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 path_component: str,
                 repository_url: str):
        pulumi.set(__self__, "path_component", path_component)
        pulumi.set(__self__, "repository_url", repository_url)

    @property
    @pulumi.getter(name="pathComponent")
    def path_component(self) -> str:
        return pulumi.get(self, "path_component")

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> str:
        return pulumi.get(self, "repository_url")


@pulumi.output_type
class EnvironmentEC2Tag(dict):
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


