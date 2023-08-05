# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationInstanceHealthStatus',
    'ApplicationInstanceStatus',
    'ApplicationInstanceStatusFilter',
    'PackageVersionStatus',
]


class ApplicationInstanceHealthStatus(str, Enum):
    RUNNING = "RUNNING"
    ERROR = "ERROR"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class ApplicationInstanceStatus(str, Enum):
    DEPLOYMENT_PENDING = "DEPLOYMENT_PENDING"
    DEPLOYMENT_REQUESTED = "DEPLOYMENT_REQUESTED"
    DEPLOYMENT_IN_PROGRESS = "DEPLOYMENT_IN_PROGRESS"
    DEPLOYMENT_FAILED = "DEPLOYMENT_FAILED"
    DEPLOYMENT_SUCCEEDED = "DEPLOYMENT_SUCCEEDED"
    REMOVAL_PENDING = "REMOVAL_PENDING"
    REMOVAL_REQUESTED = "REMOVAL_REQUESTED"
    REMOVAL_IN_PROGRESS = "REMOVAL_IN_PROGRESS"
    REMOVAL_FAILED = "REMOVAL_FAILED"
    REMOVAL_SUCCEEDED = "REMOVAL_SUCCEEDED"


class ApplicationInstanceStatusFilter(str, Enum):
    DEPLOYMENT_SUCCEEDED = "DEPLOYMENT_SUCCEEDED"
    DEPLOYMENT_FAILED = "DEPLOYMENT_FAILED"
    REMOVAL_SUCCEEDED = "REMOVAL_SUCCEEDED"
    REMOVAL_FAILED = "REMOVAL_FAILED"
    PROCESSING_DEPLOYMENT = "PROCESSING_DEPLOYMENT"
    PROCESSING_REMOVAL = "PROCESSING_REMOVAL"


class PackageVersionStatus(str, Enum):
    REGISTER_PENDING = "REGISTER_PENDING"
    REGISTER_COMPLETED = "REGISTER_COMPLETED"
    FAILED = "FAILED"
    DELETING = "DELETING"
