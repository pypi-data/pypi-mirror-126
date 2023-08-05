# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GlobalTableAttributeDefinitionArgs',
    'GlobalTableCapacityAutoScalingSettingsArgs',
    'GlobalTableContributorInsightsSpecificationArgs',
    'GlobalTableGlobalSecondaryIndexArgs',
    'GlobalTableKeySchemaArgs',
    'GlobalTableLocalSecondaryIndexArgs',
    'GlobalTablePointInTimeRecoverySpecificationArgs',
    'GlobalTableProjectionArgs',
    'GlobalTableReadProvisionedThroughputSettingsArgs',
    'GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs',
    'GlobalTableReplicaSSESpecificationArgs',
    'GlobalTableReplicaSpecificationArgs',
    'GlobalTableSSESpecificationArgs',
    'GlobalTableStreamSpecificationArgs',
    'GlobalTableTagArgs',
    'GlobalTableTargetTrackingScalingPolicyConfigurationArgs',
    'GlobalTableTimeToLiveSpecificationArgs',
    'GlobalTableWriteProvisionedThroughputSettingsArgs',
    'TableAttributeDefinitionArgs',
    'TableContributorInsightsSpecificationArgs',
    'TableGlobalSecondaryIndexArgs',
    'TableKeySchemaArgs',
    'TableKinesisStreamSpecificationArgs',
    'TableLocalSecondaryIndexArgs',
    'TablePointInTimeRecoverySpecificationArgs',
    'TableProjectionArgs',
    'TableProvisionedThroughputArgs',
    'TableSSESpecificationArgs',
    'TableStreamSpecificationArgs',
    'TableTagArgs',
    'TableTimeToLiveSpecificationArgs',
]

@pulumi.input_type
class GlobalTableAttributeDefinitionArgs:
    def __init__(__self__, *,
                 attribute_name: pulumi.Input[str],
                 attribute_type: pulumi.Input[str]):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "attribute_type", attribute_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_name", value)

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_type")

    @attribute_type.setter
    def attribute_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_type", value)


@pulumi.input_type
class GlobalTableCapacityAutoScalingSettingsArgs:
    def __init__(__self__, *,
                 max_capacity: pulumi.Input[int],
                 min_capacity: pulumi.Input[int],
                 target_tracking_scaling_policy_configuration: pulumi.Input['GlobalTableTargetTrackingScalingPolicyConfigurationArgs'],
                 seed_capacity: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "max_capacity", max_capacity)
        pulumi.set(__self__, "min_capacity", min_capacity)
        pulumi.set(__self__, "target_tracking_scaling_policy_configuration", target_tracking_scaling_policy_configuration)
        if seed_capacity is not None:
            pulumi.set(__self__, "seed_capacity", seed_capacity)

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Input[int]:
        return pulumi.get(self, "max_capacity")

    @max_capacity.setter
    def max_capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_capacity", value)

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> pulumi.Input[int]:
        return pulumi.get(self, "min_capacity")

    @min_capacity.setter
    def min_capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_capacity", value)

    @property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(self) -> pulumi.Input['GlobalTableTargetTrackingScalingPolicyConfigurationArgs']:
        return pulumi.get(self, "target_tracking_scaling_policy_configuration")

    @target_tracking_scaling_policy_configuration.setter
    def target_tracking_scaling_policy_configuration(self, value: pulumi.Input['GlobalTableTargetTrackingScalingPolicyConfigurationArgs']):
        pulumi.set(self, "target_tracking_scaling_policy_configuration", value)

    @property
    @pulumi.getter(name="seedCapacity")
    def seed_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "seed_capacity")

    @seed_capacity.setter
    def seed_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seed_capacity", value)


@pulumi.input_type
class GlobalTableContributorInsightsSpecificationArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool]):
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class GlobalTableGlobalSecondaryIndexArgs:
    def __init__(__self__, *,
                 index_name: pulumi.Input[str],
                 key_schema: pulumi.Input[Sequence[pulumi.Input['GlobalTableKeySchemaArgs']]],
                 projection: pulumi.Input['GlobalTableProjectionArgs'],
                 write_provisioned_throughput_settings: Optional[pulumi.Input['GlobalTableWriteProvisionedThroughputSettingsArgs']] = None):
        pulumi.set(__self__, "index_name", index_name)
        pulumi.set(__self__, "key_schema", key_schema)
        pulumi.set(__self__, "projection", projection)
        if write_provisioned_throughput_settings is not None:
            pulumi.set(__self__, "write_provisioned_throughput_settings", write_provisioned_throughput_settings)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> pulumi.Input[Sequence[pulumi.Input['GlobalTableKeySchemaArgs']]]:
        return pulumi.get(self, "key_schema")

    @key_schema.setter
    def key_schema(self, value: pulumi.Input[Sequence[pulumi.Input['GlobalTableKeySchemaArgs']]]):
        pulumi.set(self, "key_schema", value)

    @property
    @pulumi.getter
    def projection(self) -> pulumi.Input['GlobalTableProjectionArgs']:
        return pulumi.get(self, "projection")

    @projection.setter
    def projection(self, value: pulumi.Input['GlobalTableProjectionArgs']):
        pulumi.set(self, "projection", value)

    @property
    @pulumi.getter(name="writeProvisionedThroughputSettings")
    def write_provisioned_throughput_settings(self) -> Optional[pulumi.Input['GlobalTableWriteProvisionedThroughputSettingsArgs']]:
        return pulumi.get(self, "write_provisioned_throughput_settings")

    @write_provisioned_throughput_settings.setter
    def write_provisioned_throughput_settings(self, value: Optional[pulumi.Input['GlobalTableWriteProvisionedThroughputSettingsArgs']]):
        pulumi.set(self, "write_provisioned_throughput_settings", value)


@pulumi.input_type
class GlobalTableKeySchemaArgs:
    def __init__(__self__, *,
                 attribute_name: pulumi.Input[str],
                 key_type: pulumi.Input[str]):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "key_type", key_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_name", value)

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key_type")

    @key_type.setter
    def key_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_type", value)


@pulumi.input_type
class GlobalTableLocalSecondaryIndexArgs:
    def __init__(__self__, *,
                 index_name: pulumi.Input[str],
                 key_schema: pulumi.Input[Sequence[pulumi.Input['GlobalTableKeySchemaArgs']]],
                 projection: pulumi.Input['GlobalTableProjectionArgs']):
        pulumi.set(__self__, "index_name", index_name)
        pulumi.set(__self__, "key_schema", key_schema)
        pulumi.set(__self__, "projection", projection)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> pulumi.Input[Sequence[pulumi.Input['GlobalTableKeySchemaArgs']]]:
        return pulumi.get(self, "key_schema")

    @key_schema.setter
    def key_schema(self, value: pulumi.Input[Sequence[pulumi.Input['GlobalTableKeySchemaArgs']]]):
        pulumi.set(self, "key_schema", value)

    @property
    @pulumi.getter
    def projection(self) -> pulumi.Input['GlobalTableProjectionArgs']:
        return pulumi.get(self, "projection")

    @projection.setter
    def projection(self, value: pulumi.Input['GlobalTableProjectionArgs']):
        pulumi.set(self, "projection", value)


@pulumi.input_type
class GlobalTablePointInTimeRecoverySpecificationArgs:
    def __init__(__self__, *,
                 point_in_time_recovery_enabled: Optional[pulumi.Input[bool]] = None):
        if point_in_time_recovery_enabled is not None:
            pulumi.set(__self__, "point_in_time_recovery_enabled", point_in_time_recovery_enabled)

    @property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "point_in_time_recovery_enabled")

    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "point_in_time_recovery_enabled", value)


@pulumi.input_type
class GlobalTableProjectionArgs:
    def __init__(__self__, *,
                 non_key_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 projection_type: Optional[pulumi.Input[str]] = None):
        if non_key_attributes is not None:
            pulumi.set(__self__, "non_key_attributes", non_key_attributes)
        if projection_type is not None:
            pulumi.set(__self__, "projection_type", projection_type)

    @property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "non_key_attributes")

    @non_key_attributes.setter
    def non_key_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "non_key_attributes", value)

    @property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "projection_type")

    @projection_type.setter
    def projection_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "projection_type", value)


@pulumi.input_type
class GlobalTableReadProvisionedThroughputSettingsArgs:
    def __init__(__self__, *,
                 read_capacity_auto_scaling_settings: Optional[pulumi.Input['GlobalTableCapacityAutoScalingSettingsArgs']] = None,
                 read_capacity_units: Optional[pulumi.Input[int]] = None):
        if read_capacity_auto_scaling_settings is not None:
            pulumi.set(__self__, "read_capacity_auto_scaling_settings", read_capacity_auto_scaling_settings)
        if read_capacity_units is not None:
            pulumi.set(__self__, "read_capacity_units", read_capacity_units)

    @property
    @pulumi.getter(name="readCapacityAutoScalingSettings")
    def read_capacity_auto_scaling_settings(self) -> Optional[pulumi.Input['GlobalTableCapacityAutoScalingSettingsArgs']]:
        return pulumi.get(self, "read_capacity_auto_scaling_settings")

    @read_capacity_auto_scaling_settings.setter
    def read_capacity_auto_scaling_settings(self, value: Optional[pulumi.Input['GlobalTableCapacityAutoScalingSettingsArgs']]):
        pulumi.set(self, "read_capacity_auto_scaling_settings", value)

    @property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "read_capacity_units")

    @read_capacity_units.setter
    def read_capacity_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "read_capacity_units", value)


@pulumi.input_type
class GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs:
    def __init__(__self__, *,
                 index_name: pulumi.Input[str],
                 contributor_insights_specification: Optional[pulumi.Input['GlobalTableContributorInsightsSpecificationArgs']] = None,
                 read_provisioned_throughput_settings: Optional[pulumi.Input['GlobalTableReadProvisionedThroughputSettingsArgs']] = None):
        pulumi.set(__self__, "index_name", index_name)
        if contributor_insights_specification is not None:
            pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if read_provisioned_throughput_settings is not None:
            pulumi.set(__self__, "read_provisioned_throughput_settings", read_provisioned_throughput_settings)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional[pulumi.Input['GlobalTableContributorInsightsSpecificationArgs']]:
        return pulumi.get(self, "contributor_insights_specification")

    @contributor_insights_specification.setter
    def contributor_insights_specification(self, value: Optional[pulumi.Input['GlobalTableContributorInsightsSpecificationArgs']]):
        pulumi.set(self, "contributor_insights_specification", value)

    @property
    @pulumi.getter(name="readProvisionedThroughputSettings")
    def read_provisioned_throughput_settings(self) -> Optional[pulumi.Input['GlobalTableReadProvisionedThroughputSettingsArgs']]:
        return pulumi.get(self, "read_provisioned_throughput_settings")

    @read_provisioned_throughput_settings.setter
    def read_provisioned_throughput_settings(self, value: Optional[pulumi.Input['GlobalTableReadProvisionedThroughputSettingsArgs']]):
        pulumi.set(self, "read_provisioned_throughput_settings", value)


@pulumi.input_type
class GlobalTableReplicaSSESpecificationArgs:
    def __init__(__self__, *,
                 k_ms_master_key_id: pulumi.Input[str]):
        pulumi.set(__self__, "k_ms_master_key_id", k_ms_master_key_id)

    @property
    @pulumi.getter(name="kMSMasterKeyId")
    def k_ms_master_key_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "k_ms_master_key_id")

    @k_ms_master_key_id.setter
    def k_ms_master_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "k_ms_master_key_id", value)


@pulumi.input_type
class GlobalTableReplicaSpecificationArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 contributor_insights_specification: Optional[pulumi.Input['GlobalTableContributorInsightsSpecificationArgs']] = None,
                 global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs']]]] = None,
                 point_in_time_recovery_specification: Optional[pulumi.Input['GlobalTablePointInTimeRecoverySpecificationArgs']] = None,
                 read_provisioned_throughput_settings: Optional[pulumi.Input['GlobalTableReadProvisionedThroughputSettingsArgs']] = None,
                 s_se_specification: Optional[pulumi.Input['GlobalTableReplicaSSESpecificationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalTableTagArgs']]]] = None):
        pulumi.set(__self__, "region", region)
        if contributor_insights_specification is not None:
            pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if global_secondary_indexes is not None:
            pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if point_in_time_recovery_specification is not None:
            pulumi.set(__self__, "point_in_time_recovery_specification", point_in_time_recovery_specification)
        if read_provisioned_throughput_settings is not None:
            pulumi.set(__self__, "read_provisioned_throughput_settings", read_provisioned_throughput_settings)
        if s_se_specification is not None:
            pulumi.set(__self__, "s_se_specification", s_se_specification)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional[pulumi.Input['GlobalTableContributorInsightsSpecificationArgs']]:
        return pulumi.get(self, "contributor_insights_specification")

    @contributor_insights_specification.setter
    def contributor_insights_specification(self, value: Optional[pulumi.Input['GlobalTableContributorInsightsSpecificationArgs']]):
        pulumi.set(self, "contributor_insights_specification", value)

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs']]]]:
        return pulumi.get(self, "global_secondary_indexes")

    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs']]]]):
        pulumi.set(self, "global_secondary_indexes", value)

    @property
    @pulumi.getter(name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(self) -> Optional[pulumi.Input['GlobalTablePointInTimeRecoverySpecificationArgs']]:
        return pulumi.get(self, "point_in_time_recovery_specification")

    @point_in_time_recovery_specification.setter
    def point_in_time_recovery_specification(self, value: Optional[pulumi.Input['GlobalTablePointInTimeRecoverySpecificationArgs']]):
        pulumi.set(self, "point_in_time_recovery_specification", value)

    @property
    @pulumi.getter(name="readProvisionedThroughputSettings")
    def read_provisioned_throughput_settings(self) -> Optional[pulumi.Input['GlobalTableReadProvisionedThroughputSettingsArgs']]:
        return pulumi.get(self, "read_provisioned_throughput_settings")

    @read_provisioned_throughput_settings.setter
    def read_provisioned_throughput_settings(self, value: Optional[pulumi.Input['GlobalTableReadProvisionedThroughputSettingsArgs']]):
        pulumi.set(self, "read_provisioned_throughput_settings", value)

    @property
    @pulumi.getter(name="sSESpecification")
    def s_se_specification(self) -> Optional[pulumi.Input['GlobalTableReplicaSSESpecificationArgs']]:
        return pulumi.get(self, "s_se_specification")

    @s_se_specification.setter
    def s_se_specification(self, value: Optional[pulumi.Input['GlobalTableReplicaSSESpecificationArgs']]):
        pulumi.set(self, "s_se_specification", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GlobalTableTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalTableTagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class GlobalTableSSESpecificationArgs:
    def __init__(__self__, *,
                 s_se_enabled: pulumi.Input[bool],
                 s_se_type: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "s_se_enabled", s_se_enabled)
        if s_se_type is not None:
            pulumi.set(__self__, "s_se_type", s_se_type)

    @property
    @pulumi.getter(name="sSEEnabled")
    def s_se_enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "s_se_enabled")

    @s_se_enabled.setter
    def s_se_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "s_se_enabled", value)

    @property
    @pulumi.getter(name="sSEType")
    def s_se_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s_se_type")

    @s_se_type.setter
    def s_se_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s_se_type", value)


@pulumi.input_type
class GlobalTableStreamSpecificationArgs:
    def __init__(__self__, *,
                 stream_view_type: pulumi.Input[str]):
        pulumi.set(__self__, "stream_view_type", stream_view_type)

    @property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stream_view_type")

    @stream_view_type.setter
    def stream_view_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "stream_view_type", value)


@pulumi.input_type
class GlobalTableTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GlobalTableTargetTrackingScalingPolicyConfigurationArgs:
    def __init__(__self__, *,
                 target_value: pulumi.Input[float],
                 disable_scale_in: Optional[pulumi.Input[bool]] = None,
                 scale_in_cooldown: Optional[pulumi.Input[int]] = None,
                 scale_out_cooldown: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "target_value", target_value)
        if disable_scale_in is not None:
            pulumi.set(__self__, "disable_scale_in", disable_scale_in)
        if scale_in_cooldown is not None:
            pulumi.set(__self__, "scale_in_cooldown", scale_in_cooldown)
        if scale_out_cooldown is not None:
            pulumi.set(__self__, "scale_out_cooldown", scale_out_cooldown)

    @property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[float]:
        return pulumi.get(self, "target_value")

    @target_value.setter
    def target_value(self, value: pulumi.Input[float]):
        pulumi.set(self, "target_value", value)

    @property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "disable_scale_in")

    @disable_scale_in.setter
    def disable_scale_in(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_scale_in", value)

    @property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "scale_in_cooldown")

    @scale_in_cooldown.setter
    def scale_in_cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale_in_cooldown", value)

    @property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "scale_out_cooldown")

    @scale_out_cooldown.setter
    def scale_out_cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale_out_cooldown", value)


@pulumi.input_type
class GlobalTableTimeToLiveSpecificationArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 attribute_name: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "enabled", enabled)
        if attribute_name is not None:
            pulumi.set(__self__, "attribute_name", attribute_name)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attribute_name", value)


@pulumi.input_type
class GlobalTableWriteProvisionedThroughputSettingsArgs:
    def __init__(__self__, *,
                 write_capacity_auto_scaling_settings: Optional[pulumi.Input['GlobalTableCapacityAutoScalingSettingsArgs']] = None):
        if write_capacity_auto_scaling_settings is not None:
            pulumi.set(__self__, "write_capacity_auto_scaling_settings", write_capacity_auto_scaling_settings)

    @property
    @pulumi.getter(name="writeCapacityAutoScalingSettings")
    def write_capacity_auto_scaling_settings(self) -> Optional[pulumi.Input['GlobalTableCapacityAutoScalingSettingsArgs']]:
        return pulumi.get(self, "write_capacity_auto_scaling_settings")

    @write_capacity_auto_scaling_settings.setter
    def write_capacity_auto_scaling_settings(self, value: Optional[pulumi.Input['GlobalTableCapacityAutoScalingSettingsArgs']]):
        pulumi.set(self, "write_capacity_auto_scaling_settings", value)


@pulumi.input_type
class TableAttributeDefinitionArgs:
    def __init__(__self__, *,
                 attribute_name: pulumi.Input[str],
                 attribute_type: pulumi.Input[str]):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "attribute_type", attribute_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_name", value)

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_type")

    @attribute_type.setter
    def attribute_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_type", value)


@pulumi.input_type
class TableContributorInsightsSpecificationArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool]):
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class TableGlobalSecondaryIndexArgs:
    def __init__(__self__, *,
                 index_name: pulumi.Input[str],
                 key_schema: pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]],
                 projection: pulumi.Input['TableProjectionArgs'],
                 contributor_insights_specification: Optional[pulumi.Input['TableContributorInsightsSpecificationArgs']] = None,
                 provisioned_throughput: Optional[pulumi.Input['TableProvisionedThroughputArgs']] = None):
        pulumi.set(__self__, "index_name", index_name)
        pulumi.set(__self__, "key_schema", key_schema)
        pulumi.set(__self__, "projection", projection)
        if contributor_insights_specification is not None:
            pulumi.set(__self__, "contributor_insights_specification", contributor_insights_specification)
        if provisioned_throughput is not None:
            pulumi.set(__self__, "provisioned_throughput", provisioned_throughput)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]]:
        return pulumi.get(self, "key_schema")

    @key_schema.setter
    def key_schema(self, value: pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]]):
        pulumi.set(self, "key_schema", value)

    @property
    @pulumi.getter
    def projection(self) -> pulumi.Input['TableProjectionArgs']:
        return pulumi.get(self, "projection")

    @projection.setter
    def projection(self, value: pulumi.Input['TableProjectionArgs']):
        pulumi.set(self, "projection", value)

    @property
    @pulumi.getter(name="contributorInsightsSpecification")
    def contributor_insights_specification(self) -> Optional[pulumi.Input['TableContributorInsightsSpecificationArgs']]:
        return pulumi.get(self, "contributor_insights_specification")

    @contributor_insights_specification.setter
    def contributor_insights_specification(self, value: Optional[pulumi.Input['TableContributorInsightsSpecificationArgs']]):
        pulumi.set(self, "contributor_insights_specification", value)

    @property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input['TableProvisionedThroughputArgs']]:
        return pulumi.get(self, "provisioned_throughput")

    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input['TableProvisionedThroughputArgs']]):
        pulumi.set(self, "provisioned_throughput", value)


@pulumi.input_type
class TableKeySchemaArgs:
    def __init__(__self__, *,
                 attribute_name: pulumi.Input[str],
                 key_type: pulumi.Input[str]):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "key_type", key_type)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_name", value)

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key_type")

    @key_type.setter
    def key_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_type", value)


@pulumi.input_type
class TableKinesisStreamSpecificationArgs:
    def __init__(__self__, *,
                 stream_arn: pulumi.Input[str]):
        pulumi.set(__self__, "stream_arn", stream_arn)

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stream_arn")

    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "stream_arn", value)


@pulumi.input_type
class TableLocalSecondaryIndexArgs:
    def __init__(__self__, *,
                 index_name: pulumi.Input[str],
                 key_schema: pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]],
                 projection: pulumi.Input['TableProjectionArgs']):
        pulumi.set(__self__, "index_name", index_name)
        pulumi.set(__self__, "key_schema", key_schema)
        pulumi.set(__self__, "projection", projection)

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "index_name")

    @index_name.setter
    def index_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_name", value)

    @property
    @pulumi.getter(name="keySchema")
    def key_schema(self) -> pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]]:
        return pulumi.get(self, "key_schema")

    @key_schema.setter
    def key_schema(self, value: pulumi.Input[Sequence[pulumi.Input['TableKeySchemaArgs']]]):
        pulumi.set(self, "key_schema", value)

    @property
    @pulumi.getter
    def projection(self) -> pulumi.Input['TableProjectionArgs']:
        return pulumi.get(self, "projection")

    @projection.setter
    def projection(self, value: pulumi.Input['TableProjectionArgs']):
        pulumi.set(self, "projection", value)


@pulumi.input_type
class TablePointInTimeRecoverySpecificationArgs:
    def __init__(__self__, *,
                 point_in_time_recovery_enabled: Optional[pulumi.Input[bool]] = None):
        if point_in_time_recovery_enabled is not None:
            pulumi.set(__self__, "point_in_time_recovery_enabled", point_in_time_recovery_enabled)

    @property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "point_in_time_recovery_enabled")

    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "point_in_time_recovery_enabled", value)


@pulumi.input_type
class TableProjectionArgs:
    def __init__(__self__, *,
                 non_key_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 projection_type: Optional[pulumi.Input[str]] = None):
        if non_key_attributes is not None:
            pulumi.set(__self__, "non_key_attributes", non_key_attributes)
        if projection_type is not None:
            pulumi.set(__self__, "projection_type", projection_type)

    @property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "non_key_attributes")

    @non_key_attributes.setter
    def non_key_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "non_key_attributes", value)

    @property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "projection_type")

    @projection_type.setter
    def projection_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "projection_type", value)


@pulumi.input_type
class TableProvisionedThroughputArgs:
    def __init__(__self__, *,
                 read_capacity_units: pulumi.Input[int],
                 write_capacity_units: pulumi.Input[int]):
        pulumi.set(__self__, "read_capacity_units", read_capacity_units)
        pulumi.set(__self__, "write_capacity_units", write_capacity_units)

    @property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> pulumi.Input[int]:
        return pulumi.get(self, "read_capacity_units")

    @read_capacity_units.setter
    def read_capacity_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "read_capacity_units", value)

    @property
    @pulumi.getter(name="writeCapacityUnits")
    def write_capacity_units(self) -> pulumi.Input[int]:
        return pulumi.get(self, "write_capacity_units")

    @write_capacity_units.setter
    def write_capacity_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "write_capacity_units", value)


@pulumi.input_type
class TableSSESpecificationArgs:
    def __init__(__self__, *,
                 s_se_enabled: pulumi.Input[bool],
                 k_ms_master_key_id: Optional[pulumi.Input[str]] = None,
                 s_se_type: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "s_se_enabled", s_se_enabled)
        if k_ms_master_key_id is not None:
            pulumi.set(__self__, "k_ms_master_key_id", k_ms_master_key_id)
        if s_se_type is not None:
            pulumi.set(__self__, "s_se_type", s_se_type)

    @property
    @pulumi.getter(name="sSEEnabled")
    def s_se_enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "s_se_enabled")

    @s_se_enabled.setter
    def s_se_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "s_se_enabled", value)

    @property
    @pulumi.getter(name="kMSMasterKeyId")
    def k_ms_master_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "k_ms_master_key_id")

    @k_ms_master_key_id.setter
    def k_ms_master_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "k_ms_master_key_id", value)

    @property
    @pulumi.getter(name="sSEType")
    def s_se_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "s_se_type")

    @s_se_type.setter
    def s_se_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s_se_type", value)


@pulumi.input_type
class TableStreamSpecificationArgs:
    def __init__(__self__, *,
                 stream_view_type: pulumi.Input[str]):
        pulumi.set(__self__, "stream_view_type", stream_view_type)

    @property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stream_view_type")

    @stream_view_type.setter
    def stream_view_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "stream_view_type", value)


@pulumi.input_type
class TableTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class TableTimeToLiveSpecificationArgs:
    def __init__(__self__, *,
                 attribute_name: pulumi.Input[str],
                 enabled: pulumi.Input[bool]):
        pulumi.set(__self__, "attribute_name", attribute_name)
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_name")

    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


