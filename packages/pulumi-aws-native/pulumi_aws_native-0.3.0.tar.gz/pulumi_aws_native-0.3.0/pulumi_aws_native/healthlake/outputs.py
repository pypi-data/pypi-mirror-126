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
    'FHIRDatastoreCreatedAt',
    'FHIRDatastoreKmsEncryptionConfig',
    'FHIRDatastorePreloadDataConfig',
    'FHIRDatastoreSseConfiguration',
    'FHIRDatastoreTag',
]

@pulumi.output_type
class FHIRDatastoreCreatedAt(dict):
    """
    The time that a Data Store was created.
    """
    def __init__(__self__, *,
                 nanos: int,
                 seconds: str):
        """
        The time that a Data Store was created.
        :param int nanos: Nanoseconds.
        :param str seconds: Seconds since epoch.
        """
        pulumi.set(__self__, "nanos", nanos)
        pulumi.set(__self__, "seconds", seconds)

    @property
    @pulumi.getter
    def nanos(self) -> int:
        """
        Nanoseconds.
        """
        return pulumi.get(self, "nanos")

    @property
    @pulumi.getter
    def seconds(self) -> str:
        """
        Seconds since epoch.
        """
        return pulumi.get(self, "seconds")


@pulumi.output_type
class FHIRDatastoreKmsEncryptionConfig(dict):
    """
    The customer-managed-key (CMK) used when creating a Data Store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cmkType":
            suggest = "cmk_type"
        elif key == "kmsKeyId":
            suggest = "kms_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FHIRDatastoreKmsEncryptionConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FHIRDatastoreKmsEncryptionConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FHIRDatastoreKmsEncryptionConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cmk_type: 'FHIRDatastoreKmsEncryptionConfigCmkType',
                 kms_key_id: Optional[str] = None):
        """
        The customer-managed-key (CMK) used when creating a Data Store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
        :param 'FHIRDatastoreKmsEncryptionConfigCmkType' cmk_type: The type of customer-managed-key (CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.
        :param str kms_key_id: The KMS encryption key id/alias used to encrypt the Data Store contents at rest.
        """
        pulumi.set(__self__, "cmk_type", cmk_type)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)

    @property
    @pulumi.getter(name="cmkType")
    def cmk_type(self) -> 'FHIRDatastoreKmsEncryptionConfigCmkType':
        """
        The type of customer-managed-key (CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.
        """
        return pulumi.get(self, "cmk_type")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The KMS encryption key id/alias used to encrypt the Data Store contents at rest.
        """
        return pulumi.get(self, "kms_key_id")


@pulumi.output_type
class FHIRDatastorePreloadDataConfig(dict):
    """
    The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "preloadDataType":
            suggest = "preload_data_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FHIRDatastorePreloadDataConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FHIRDatastorePreloadDataConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FHIRDatastorePreloadDataConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 preload_data_type: 'FHIRDatastorePreloadDataConfigPreloadDataType'):
        """
        The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
        :param 'FHIRDatastorePreloadDataConfigPreloadDataType' preload_data_type: The type of preloaded data. Only Synthea preloaded data is supported.
        """
        pulumi.set(__self__, "preload_data_type", preload_data_type)

    @property
    @pulumi.getter(name="preloadDataType")
    def preload_data_type(self) -> 'FHIRDatastorePreloadDataConfigPreloadDataType':
        """
        The type of preloaded data. Only Synthea preloaded data is supported.
        """
        return pulumi.get(self, "preload_data_type")


@pulumi.output_type
class FHIRDatastoreSseConfiguration(dict):
    """
    The server-side encryption key configuration for a customer provided encryption key.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsEncryptionConfig":
            suggest = "kms_encryption_config"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FHIRDatastoreSseConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FHIRDatastoreSseConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FHIRDatastoreSseConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_encryption_config: 'outputs.FHIRDatastoreKmsEncryptionConfig'):
        """
        The server-side encryption key configuration for a customer provided encryption key.
        """
        pulumi.set(__self__, "kms_encryption_config", kms_encryption_config)

    @property
    @pulumi.getter(name="kmsEncryptionConfig")
    def kms_encryption_config(self) -> 'outputs.FHIRDatastoreKmsEncryptionConfig':
        return pulumi.get(self, "kms_encryption_config")


@pulumi.output_type
class FHIRDatastoreTag(dict):
    """
    A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        :param str key: The key of the tag.
        :param str value: The value of the tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the tag.
        """
        return pulumi.get(self, "value")


