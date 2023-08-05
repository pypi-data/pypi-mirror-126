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

__all__ = ['FilterArgs', 'Filter']

@pulumi.input_type
class FilterArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 description: pulumi.Input[str],
                 detector_id: pulumi.Input[str],
                 finding_criteria: pulumi.Input['FilterFindingCriteriaArgs'],
                 name: pulumi.Input[str],
                 rank: pulumi.Input[int]):
        """
        The set of arguments for constructing a Filter resource.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "detector_id", detector_id)
        pulumi.set(__self__, "finding_criteria", finding_criteria)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "rank", rank)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "detector_id")

    @detector_id.setter
    def detector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "detector_id", value)

    @property
    @pulumi.getter(name="findingCriteria")
    def finding_criteria(self) -> pulumi.Input['FilterFindingCriteriaArgs']:
        return pulumi.get(self, "finding_criteria")

    @finding_criteria.setter
    def finding_criteria(self, value: pulumi.Input['FilterFindingCriteriaArgs']):
        pulumi.set(self, "finding_criteria", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rank(self) -> pulumi.Input[int]:
        return pulumi.get(self, "rank")

    @rank.setter
    def rank(self, value: pulumi.Input[int]):
        pulumi.set(self, "rank", value)


warnings.warn("""Filter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Filter(pulumi.CustomResource):
    warnings.warn("""Filter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 finding_criteria: Optional[pulumi.Input[pulumi.InputType['FilterFindingCriteriaArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rank: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::GuardDuty::Filter

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FilterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::GuardDuty::Filter

        :param str resource_name: The name of the resource.
        :param FilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 finding_criteria: Optional[pulumi.Input[pulumi.InputType['FilterFindingCriteriaArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rank: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""Filter is deprecated: Filter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FilterArgs.__new__(FilterArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if detector_id is None and not opts.urn:
                raise TypeError("Missing required property 'detector_id'")
            __props__.__dict__["detector_id"] = detector_id
            if finding_criteria is None and not opts.urn:
                raise TypeError("Missing required property 'finding_criteria'")
            __props__.__dict__["finding_criteria"] = finding_criteria
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if rank is None and not opts.urn:
                raise TypeError("Missing required property 'rank'")
            __props__.__dict__["rank"] = rank
        super(Filter, __self__).__init__(
            'aws-native:guardduty:Filter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Filter':
        """
        Get an existing Filter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FilterArgs.__new__(FilterArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["detector_id"] = None
        __props__.__dict__["finding_criteria"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rank"] = None
        return Filter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter(name="findingCriteria")
    def finding_criteria(self) -> pulumi.Output['outputs.FilterFindingCriteria']:
        return pulumi.get(self, "finding_criteria")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rank(self) -> pulumi.Output[int]:
        return pulumi.get(self, "rank")

