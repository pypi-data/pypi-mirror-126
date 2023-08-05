# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'FileSystemAuditLogConfigurationArgs',
    'FileSystemLustreConfigurationArgs',
    'FileSystemSelfManagedActiveDirectoryConfigurationArgs',
    'FileSystemTagArgs',
    'FileSystemWindowsConfigurationArgs',
]

@pulumi.input_type
class FileSystemAuditLogConfigurationArgs:
    def __init__(__self__, *,
                 file_access_audit_log_level: pulumi.Input[str],
                 file_share_access_audit_log_level: pulumi.Input[str],
                 audit_log_destination: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "file_access_audit_log_level", file_access_audit_log_level)
        pulumi.set(__self__, "file_share_access_audit_log_level", file_share_access_audit_log_level)
        if audit_log_destination is not None:
            pulumi.set(__self__, "audit_log_destination", audit_log_destination)

    @property
    @pulumi.getter(name="fileAccessAuditLogLevel")
    def file_access_audit_log_level(self) -> pulumi.Input[str]:
        return pulumi.get(self, "file_access_audit_log_level")

    @file_access_audit_log_level.setter
    def file_access_audit_log_level(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_access_audit_log_level", value)

    @property
    @pulumi.getter(name="fileShareAccessAuditLogLevel")
    def file_share_access_audit_log_level(self) -> pulumi.Input[str]:
        return pulumi.get(self, "file_share_access_audit_log_level")

    @file_share_access_audit_log_level.setter
    def file_share_access_audit_log_level(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_share_access_audit_log_level", value)

    @property
    @pulumi.getter(name="auditLogDestination")
    def audit_log_destination(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "audit_log_destination")

    @audit_log_destination.setter
    def audit_log_destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_log_destination", value)


@pulumi.input_type
class FileSystemLustreConfigurationArgs:
    def __init__(__self__, *,
                 auto_import_policy: Optional[pulumi.Input[str]] = None,
                 automatic_backup_retention_days: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_backups: Optional[pulumi.Input[bool]] = None,
                 daily_automatic_backup_start_time: Optional[pulumi.Input[str]] = None,
                 data_compression_type: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 drive_cache_type: Optional[pulumi.Input[str]] = None,
                 export_path: Optional[pulumi.Input[str]] = None,
                 import_path: Optional[pulumi.Input[str]] = None,
                 imported_file_chunk_size: Optional[pulumi.Input[int]] = None,
                 per_unit_storage_throughput: Optional[pulumi.Input[int]] = None,
                 weekly_maintenance_start_time: Optional[pulumi.Input[str]] = None):
        if auto_import_policy is not None:
            pulumi.set(__self__, "auto_import_policy", auto_import_policy)
        if automatic_backup_retention_days is not None:
            pulumi.set(__self__, "automatic_backup_retention_days", automatic_backup_retention_days)
        if copy_tags_to_backups is not None:
            pulumi.set(__self__, "copy_tags_to_backups", copy_tags_to_backups)
        if daily_automatic_backup_start_time is not None:
            pulumi.set(__self__, "daily_automatic_backup_start_time", daily_automatic_backup_start_time)
        if data_compression_type is not None:
            pulumi.set(__self__, "data_compression_type", data_compression_type)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if drive_cache_type is not None:
            pulumi.set(__self__, "drive_cache_type", drive_cache_type)
        if export_path is not None:
            pulumi.set(__self__, "export_path", export_path)
        if import_path is not None:
            pulumi.set(__self__, "import_path", import_path)
        if imported_file_chunk_size is not None:
            pulumi.set(__self__, "imported_file_chunk_size", imported_file_chunk_size)
        if per_unit_storage_throughput is not None:
            pulumi.set(__self__, "per_unit_storage_throughput", per_unit_storage_throughput)
        if weekly_maintenance_start_time is not None:
            pulumi.set(__self__, "weekly_maintenance_start_time", weekly_maintenance_start_time)

    @property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auto_import_policy")

    @auto_import_policy.setter
    def auto_import_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_import_policy", value)

    @property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "automatic_backup_retention_days")

    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatic_backup_retention_days", value)

    @property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "copy_tags_to_backups")

    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_tags_to_backups", value)

    @property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "daily_automatic_backup_start_time")

    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "daily_automatic_backup_start_time", value)

    @property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "data_compression_type")

    @data_compression_type.setter
    def data_compression_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_compression_type", value)

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter(name="driveCacheType")
    def drive_cache_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "drive_cache_type")

    @drive_cache_type.setter
    def drive_cache_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "drive_cache_type", value)

    @property
    @pulumi.getter(name="exportPath")
    def export_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "export_path")

    @export_path.setter
    def export_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_path", value)

    @property
    @pulumi.getter(name="importPath")
    def import_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "import_path")

    @import_path.setter
    def import_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_path", value)

    @property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "imported_file_chunk_size")

    @imported_file_chunk_size.setter
    def imported_file_chunk_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "imported_file_chunk_size", value)

    @property
    @pulumi.getter(name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "per_unit_storage_throughput")

    @per_unit_storage_throughput.setter
    def per_unit_storage_throughput(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "per_unit_storage_throughput", value)

    @property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "weekly_maintenance_start_time")

    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weekly_maintenance_start_time", value)


@pulumi.input_type
class FileSystemSelfManagedActiveDirectoryConfigurationArgs:
    def __init__(__self__, *,
                 dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 file_system_administrators_group: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        if dns_ips is not None:
            pulumi.set(__self__, "dns_ips", dns_ips)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if file_system_administrators_group is not None:
            pulumi.set(__self__, "file_system_administrators_group", file_system_administrators_group)
        if organizational_unit_distinguished_name is not None:
            pulumi.set(__self__, "organizational_unit_distinguished_name", organizational_unit_distinguished_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "dns_ips")

    @dns_ips.setter
    def dns_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_ips", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file_system_administrators_group")

    @file_system_administrators_group.setter
    def file_system_administrators_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_system_administrators_group", value)

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "organizational_unit_distinguished_name")

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organizational_unit_distinguished_name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


@pulumi.input_type
class FileSystemTagArgs:
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
class FileSystemWindowsConfigurationArgs:
    def __init__(__self__, *,
                 throughput_capacity: pulumi.Input[int],
                 active_directory_id: Optional[pulumi.Input[str]] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 audit_log_configuration: Optional[pulumi.Input['FileSystemAuditLogConfigurationArgs']] = None,
                 automatic_backup_retention_days: Optional[pulumi.Input[int]] = None,
                 copy_tags_to_backups: Optional[pulumi.Input[bool]] = None,
                 daily_automatic_backup_start_time: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 preferred_subnet_id: Optional[pulumi.Input[str]] = None,
                 self_managed_active_directory_configuration: Optional[pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs']] = None,
                 weekly_maintenance_start_time: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "throughput_capacity", throughput_capacity)
        if active_directory_id is not None:
            pulumi.set(__self__, "active_directory_id", active_directory_id)
        if aliases is not None:
            pulumi.set(__self__, "aliases", aliases)
        if audit_log_configuration is not None:
            pulumi.set(__self__, "audit_log_configuration", audit_log_configuration)
        if automatic_backup_retention_days is not None:
            pulumi.set(__self__, "automatic_backup_retention_days", automatic_backup_retention_days)
        if copy_tags_to_backups is not None:
            pulumi.set(__self__, "copy_tags_to_backups", copy_tags_to_backups)
        if daily_automatic_backup_start_time is not None:
            pulumi.set(__self__, "daily_automatic_backup_start_time", daily_automatic_backup_start_time)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if preferred_subnet_id is not None:
            pulumi.set(__self__, "preferred_subnet_id", preferred_subnet_id)
        if self_managed_active_directory_configuration is not None:
            pulumi.set(__self__, "self_managed_active_directory_configuration", self_managed_active_directory_configuration)
        if weekly_maintenance_start_time is not None:
            pulumi.set(__self__, "weekly_maintenance_start_time", weekly_maintenance_start_time)

    @property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> pulumi.Input[int]:
        return pulumi.get(self, "throughput_capacity")

    @throughput_capacity.setter
    def throughput_capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "throughput_capacity", value)

    @property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "active_directory_id")

    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_directory_id", value)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "aliases")

    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aliases", value)

    @property
    @pulumi.getter(name="auditLogConfiguration")
    def audit_log_configuration(self) -> Optional[pulumi.Input['FileSystemAuditLogConfigurationArgs']]:
        return pulumi.get(self, "audit_log_configuration")

    @audit_log_configuration.setter
    def audit_log_configuration(self, value: Optional[pulumi.Input['FileSystemAuditLogConfigurationArgs']]):
        pulumi.set(self, "audit_log_configuration", value)

    @property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "automatic_backup_retention_days")

    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatic_backup_retention_days", value)

    @property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "copy_tags_to_backups")

    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_tags_to_backups", value)

    @property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "daily_automatic_backup_start_time")

    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "daily_automatic_backup_start_time", value)

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_subnet_id")

    @preferred_subnet_id.setter
    def preferred_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_subnet_id", value)

    @property
    @pulumi.getter(name="selfManagedActiveDirectoryConfiguration")
    def self_managed_active_directory_configuration(self) -> Optional[pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs']]:
        return pulumi.get(self, "self_managed_active_directory_configuration")

    @self_managed_active_directory_configuration.setter
    def self_managed_active_directory_configuration(self, value: Optional[pulumi.Input['FileSystemSelfManagedActiveDirectoryConfigurationArgs']]):
        pulumi.set(self, "self_managed_active_directory_configuration", value)

    @property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "weekly_maintenance_start_time")

    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weekly_maintenance_start_time", value)


