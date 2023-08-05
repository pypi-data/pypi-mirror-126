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

__all__ = ['BrokerArgs', 'Broker']

@pulumi.input_type
class BrokerArgs:
    def __init__(__self__, *,
                 auto_minor_version_upgrade: pulumi.Input[bool],
                 broker_name: pulumi.Input[str],
                 deployment_mode: pulumi.Input[str],
                 engine_type: pulumi.Input[str],
                 engine_version: pulumi.Input[str],
                 host_instance_type: pulumi.Input[str],
                 publicly_accessible: pulumi.Input[bool],
                 users: pulumi.Input[Sequence[pulumi.Input['BrokerUserArgs']]],
                 authentication_strategy: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input['BrokerConfigurationIdArgs']] = None,
                 encryption_options: Optional[pulumi.Input['BrokerEncryptionOptionsArgs']] = None,
                 ldap_server_metadata: Optional[pulumi.Input['BrokerLdapServerMetadataArgs']] = None,
                 logs: Optional[pulumi.Input['BrokerLogListArgs']] = None,
                 maintenance_window_start_time: Optional[pulumi.Input['BrokerMaintenanceWindowArgs']] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['BrokerTagsEntryArgs']]]] = None):
        """
        The set of arguments for constructing a Broker resource.
        """
        pulumi.set(__self__, "auto_minor_version_upgrade", auto_minor_version_upgrade)
        pulumi.set(__self__, "broker_name", broker_name)
        pulumi.set(__self__, "deployment_mode", deployment_mode)
        pulumi.set(__self__, "engine_type", engine_type)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "host_instance_type", host_instance_type)
        pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        pulumi.set(__self__, "users", users)
        if authentication_strategy is not None:
            pulumi.set(__self__, "authentication_strategy", authentication_strategy)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if encryption_options is not None:
            pulumi.set(__self__, "encryption_options", encryption_options)
        if ldap_server_metadata is not None:
            pulumi.set(__self__, "ldap_server_metadata", ldap_server_metadata)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if maintenance_window_start_time is not None:
            pulumi.set(__self__, "maintenance_window_start_time", maintenance_window_start_time)
        if security_groups is not None:
            pulumi.set(__self__, "security_groups", security_groups)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "auto_minor_version_upgrade")

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auto_minor_version_upgrade", value)

    @property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "broker_name")

    @broker_name.setter
    def broker_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "broker_name", value)

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Input[str]:
        return pulumi.get(self, "deployment_mode")

    @deployment_mode.setter
    def deployment_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_mode", value)

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "engine_type")

    @engine_type.setter
    def engine_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_type", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Input[str]:
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "host_instance_type")

    @host_instance_type.setter
    def host_instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_instance_type", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: pulumi.Input[bool]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter
    def users(self) -> pulumi.Input[Sequence[pulumi.Input['BrokerUserArgs']]]:
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: pulumi.Input[Sequence[pulumi.Input['BrokerUserArgs']]]):
        pulumi.set(self, "users", value)

    @property
    @pulumi.getter(name="authenticationStrategy")
    def authentication_strategy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authentication_strategy")

    @authentication_strategy.setter
    def authentication_strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_strategy", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['BrokerConfigurationIdArgs']]:
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['BrokerConfigurationIdArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter(name="encryptionOptions")
    def encryption_options(self) -> Optional[pulumi.Input['BrokerEncryptionOptionsArgs']]:
        return pulumi.get(self, "encryption_options")

    @encryption_options.setter
    def encryption_options(self, value: Optional[pulumi.Input['BrokerEncryptionOptionsArgs']]):
        pulumi.set(self, "encryption_options", value)

    @property
    @pulumi.getter(name="ldapServerMetadata")
    def ldap_server_metadata(self) -> Optional[pulumi.Input['BrokerLdapServerMetadataArgs']]:
        return pulumi.get(self, "ldap_server_metadata")

    @ldap_server_metadata.setter
    def ldap_server_metadata(self, value: Optional[pulumi.Input['BrokerLdapServerMetadataArgs']]):
        pulumi.set(self, "ldap_server_metadata", value)

    @property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input['BrokerLogListArgs']]:
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: Optional[pulumi.Input['BrokerLogListArgs']]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter(name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> Optional[pulumi.Input['BrokerMaintenanceWindowArgs']]:
        return pulumi.get(self, "maintenance_window_start_time")

    @maintenance_window_start_time.setter
    def maintenance_window_start_time(self, value: Optional[pulumi.Input['BrokerMaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window_start_time", value)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_groups")

    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_groups", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BrokerTagsEntryArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BrokerTagsEntryArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Broker is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Broker(pulumi.CustomResource):
    warnings.warn("""Broker is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_strategy: Optional[pulumi.Input[str]] = None,
                 auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 broker_name: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['BrokerConfigurationIdArgs']]] = None,
                 deployment_mode: Optional[pulumi.Input[str]] = None,
                 encryption_options: Optional[pulumi.Input[pulumi.InputType['BrokerEncryptionOptionsArgs']]] = None,
                 engine_type: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 host_instance_type: Optional[pulumi.Input[str]] = None,
                 ldap_server_metadata: Optional[pulumi.Input[pulumi.InputType['BrokerLdapServerMetadataArgs']]] = None,
                 logs: Optional[pulumi.Input[pulumi.InputType['BrokerLogListArgs']]] = None,
                 maintenance_window_start_time: Optional[pulumi.Input[pulumi.InputType['BrokerMaintenanceWindowArgs']]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BrokerTagsEntryArgs']]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BrokerUserArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AmazonMQ::Broker

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BrokerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AmazonMQ::Broker

        :param str resource_name: The name of the resource.
        :param BrokerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BrokerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_strategy: Optional[pulumi.Input[str]] = None,
                 auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 broker_name: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['BrokerConfigurationIdArgs']]] = None,
                 deployment_mode: Optional[pulumi.Input[str]] = None,
                 encryption_options: Optional[pulumi.Input[pulumi.InputType['BrokerEncryptionOptionsArgs']]] = None,
                 engine_type: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 host_instance_type: Optional[pulumi.Input[str]] = None,
                 ldap_server_metadata: Optional[pulumi.Input[pulumi.InputType['BrokerLdapServerMetadataArgs']]] = None,
                 logs: Optional[pulumi.Input[pulumi.InputType['BrokerLogListArgs']]] = None,
                 maintenance_window_start_time: Optional[pulumi.Input[pulumi.InputType['BrokerMaintenanceWindowArgs']]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BrokerTagsEntryArgs']]]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BrokerUserArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Broker is deprecated: Broker is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BrokerArgs.__new__(BrokerArgs)

            __props__.__dict__["authentication_strategy"] = authentication_strategy
            if auto_minor_version_upgrade is None and not opts.urn:
                raise TypeError("Missing required property 'auto_minor_version_upgrade'")
            __props__.__dict__["auto_minor_version_upgrade"] = auto_minor_version_upgrade
            if broker_name is None and not opts.urn:
                raise TypeError("Missing required property 'broker_name'")
            __props__.__dict__["broker_name"] = broker_name
            __props__.__dict__["configuration"] = configuration
            if deployment_mode is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_mode'")
            __props__.__dict__["deployment_mode"] = deployment_mode
            __props__.__dict__["encryption_options"] = encryption_options
            if engine_type is None and not opts.urn:
                raise TypeError("Missing required property 'engine_type'")
            __props__.__dict__["engine_type"] = engine_type
            if engine_version is None and not opts.urn:
                raise TypeError("Missing required property 'engine_version'")
            __props__.__dict__["engine_version"] = engine_version
            if host_instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'host_instance_type'")
            __props__.__dict__["host_instance_type"] = host_instance_type
            __props__.__dict__["ldap_server_metadata"] = ldap_server_metadata
            __props__.__dict__["logs"] = logs
            __props__.__dict__["maintenance_window_start_time"] = maintenance_window_start_time
            if publicly_accessible is None and not opts.urn:
                raise TypeError("Missing required property 'publicly_accessible'")
            __props__.__dict__["publicly_accessible"] = publicly_accessible
            __props__.__dict__["security_groups"] = security_groups
            __props__.__dict__["storage_type"] = storage_type
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            if users is None and not opts.urn:
                raise TypeError("Missing required property 'users'")
            __props__.__dict__["users"] = users
            __props__.__dict__["amqp_endpoints"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["configuration_id"] = None
            __props__.__dict__["configuration_revision"] = None
            __props__.__dict__["ip_addresses"] = None
            __props__.__dict__["mqtt_endpoints"] = None
            __props__.__dict__["open_wire_endpoints"] = None
            __props__.__dict__["stomp_endpoints"] = None
            __props__.__dict__["wss_endpoints"] = None
        super(Broker, __self__).__init__(
            'aws-native:amazonmq:Broker',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Broker':
        """
        Get an existing Broker resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BrokerArgs.__new__(BrokerArgs)

        __props__.__dict__["amqp_endpoints"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["authentication_strategy"] = None
        __props__.__dict__["auto_minor_version_upgrade"] = None
        __props__.__dict__["broker_name"] = None
        __props__.__dict__["configuration"] = None
        __props__.__dict__["configuration_id"] = None
        __props__.__dict__["configuration_revision"] = None
        __props__.__dict__["deployment_mode"] = None
        __props__.__dict__["encryption_options"] = None
        __props__.__dict__["engine_type"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["host_instance_type"] = None
        __props__.__dict__["ip_addresses"] = None
        __props__.__dict__["ldap_server_metadata"] = None
        __props__.__dict__["logs"] = None
        __props__.__dict__["maintenance_window_start_time"] = None
        __props__.__dict__["mqtt_endpoints"] = None
        __props__.__dict__["open_wire_endpoints"] = None
        __props__.__dict__["publicly_accessible"] = None
        __props__.__dict__["security_groups"] = None
        __props__.__dict__["stomp_endpoints"] = None
        __props__.__dict__["storage_type"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["users"] = None
        __props__.__dict__["wss_endpoints"] = None
        return Broker(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="amqpEndpoints")
    def amqp_endpoints(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "amqp_endpoints")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authenticationStrategy")
    def authentication_strategy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "authentication_strategy")

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "broker_name")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional['outputs.BrokerConfigurationId']]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "configuration_id")

    @property
    @pulumi.getter(name="configurationRevision")
    def configuration_revision(self) -> pulumi.Output[int]:
        return pulumi.get(self, "configuration_revision")

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_mode")

    @property
    @pulumi.getter(name="encryptionOptions")
    def encryption_options(self) -> pulumi.Output[Optional['outputs.BrokerEncryptionOptions']]:
        return pulumi.get(self, "encryption_options")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "host_instance_type")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="ldapServerMetadata")
    def ldap_server_metadata(self) -> pulumi.Output[Optional['outputs.BrokerLdapServerMetadata']]:
        return pulumi.get(self, "ldap_server_metadata")

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Output[Optional['outputs.BrokerLogList']]:
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter(name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> pulumi.Output[Optional['outputs.BrokerMaintenanceWindow']]:
        return pulumi.get(self, "maintenance_window_start_time")

    @property
    @pulumi.getter(name="mqttEndpoints")
    def mqtt_endpoints(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "mqtt_endpoints")

    @property
    @pulumi.getter(name="openWireEndpoints")
    def open_wire_endpoints(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "open_wire_endpoints")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter(name="stompEndpoints")
    def stomp_endpoints(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "stomp_endpoints")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.BrokerTagsEntry']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Sequence['outputs.BrokerUser']]:
        return pulumi.get(self, "users")

    @property
    @pulumi.getter(name="wssEndpoints")
    def wss_endpoints(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "wss_endpoints")

