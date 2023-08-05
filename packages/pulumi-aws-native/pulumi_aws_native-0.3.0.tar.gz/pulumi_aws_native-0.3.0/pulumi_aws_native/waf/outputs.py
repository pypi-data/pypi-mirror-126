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
    'ByteMatchSetByteMatchTuple',
    'ByteMatchSetFieldToMatch',
    'IPSetDescriptor',
    'RulePredicate',
    'SizeConstraintSetFieldToMatch',
    'SizeConstraintSetSizeConstraint',
    'SqlInjectionMatchSetFieldToMatch',
    'SqlInjectionMatchSetSqlInjectionMatchTuple',
    'WebACLActivatedRule',
    'WebACLWafAction',
    'XssMatchSetFieldToMatch',
    'XssMatchSetXssMatchTuple',
]

@pulumi.output_type
class ByteMatchSetByteMatchTuple(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fieldToMatch":
            suggest = "field_to_match"
        elif key == "positionalConstraint":
            suggest = "positional_constraint"
        elif key == "textTransformation":
            suggest = "text_transformation"
        elif key == "targetString":
            suggest = "target_string"
        elif key == "targetStringBase64":
            suggest = "target_string_base64"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ByteMatchSetByteMatchTuple. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ByteMatchSetByteMatchTuple.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ByteMatchSetByteMatchTuple.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 field_to_match: 'outputs.ByteMatchSetFieldToMatch',
                 positional_constraint: str,
                 text_transformation: str,
                 target_string: Optional[str] = None,
                 target_string_base64: Optional[str] = None):
        pulumi.set(__self__, "field_to_match", field_to_match)
        pulumi.set(__self__, "positional_constraint", positional_constraint)
        pulumi.set(__self__, "text_transformation", text_transformation)
        if target_string is not None:
            pulumi.set(__self__, "target_string", target_string)
        if target_string_base64 is not None:
            pulumi.set(__self__, "target_string_base64", target_string_base64)

    @property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> 'outputs.ByteMatchSetFieldToMatch':
        return pulumi.get(self, "field_to_match")

    @property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> str:
        return pulumi.get(self, "positional_constraint")

    @property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> str:
        return pulumi.get(self, "text_transformation")

    @property
    @pulumi.getter(name="targetString")
    def target_string(self) -> Optional[str]:
        return pulumi.get(self, "target_string")

    @property
    @pulumi.getter(name="targetStringBase64")
    def target_string_base64(self) -> Optional[str]:
        return pulumi.get(self, "target_string_base64")


@pulumi.output_type
class ByteMatchSetFieldToMatch(dict):
    def __init__(__self__, *,
                 type: str,
                 data: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if data is not None:
            pulumi.set(__self__, "data", data)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def data(self) -> Optional[str]:
        return pulumi.get(self, "data")


@pulumi.output_type
class IPSetDescriptor(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class RulePredicate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataId":
            suggest = "data_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RulePredicate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RulePredicate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RulePredicate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_id: str,
                 negated: bool,
                 type: str):
        pulumi.set(__self__, "data_id", data_id)
        pulumi.set(__self__, "negated", negated)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataId")
    def data_id(self) -> str:
        return pulumi.get(self, "data_id")

    @property
    @pulumi.getter
    def negated(self) -> bool:
        return pulumi.get(self, "negated")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class SizeConstraintSetFieldToMatch(dict):
    def __init__(__self__, *,
                 type: str,
                 data: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if data is not None:
            pulumi.set(__self__, "data", data)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def data(self) -> Optional[str]:
        return pulumi.get(self, "data")


@pulumi.output_type
class SizeConstraintSetSizeConstraint(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "comparisonOperator":
            suggest = "comparison_operator"
        elif key == "fieldToMatch":
            suggest = "field_to_match"
        elif key == "textTransformation":
            suggest = "text_transformation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SizeConstraintSetSizeConstraint. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SizeConstraintSetSizeConstraint.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SizeConstraintSetSizeConstraint.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 comparison_operator: str,
                 field_to_match: 'outputs.SizeConstraintSetFieldToMatch',
                 size: int,
                 text_transformation: str):
        pulumi.set(__self__, "comparison_operator", comparison_operator)
        pulumi.set(__self__, "field_to_match", field_to_match)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "text_transformation", text_transformation)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> str:
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> 'outputs.SizeConstraintSetFieldToMatch':
        return pulumi.get(self, "field_to_match")

    @property
    @pulumi.getter
    def size(self) -> int:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> str:
        return pulumi.get(self, "text_transformation")


@pulumi.output_type
class SqlInjectionMatchSetFieldToMatch(dict):
    def __init__(__self__, *,
                 type: str,
                 data: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if data is not None:
            pulumi.set(__self__, "data", data)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def data(self) -> Optional[str]:
        return pulumi.get(self, "data")


@pulumi.output_type
class SqlInjectionMatchSetSqlInjectionMatchTuple(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fieldToMatch":
            suggest = "field_to_match"
        elif key == "textTransformation":
            suggest = "text_transformation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SqlInjectionMatchSetSqlInjectionMatchTuple. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SqlInjectionMatchSetSqlInjectionMatchTuple.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SqlInjectionMatchSetSqlInjectionMatchTuple.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 field_to_match: 'outputs.SqlInjectionMatchSetFieldToMatch',
                 text_transformation: str):
        pulumi.set(__self__, "field_to_match", field_to_match)
        pulumi.set(__self__, "text_transformation", text_transformation)

    @property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> 'outputs.SqlInjectionMatchSetFieldToMatch':
        return pulumi.get(self, "field_to_match")

    @property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> str:
        return pulumi.get(self, "text_transformation")


@pulumi.output_type
class WebACLActivatedRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ruleId":
            suggest = "rule_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WebACLActivatedRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WebACLActivatedRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WebACLActivatedRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 priority: int,
                 rule_id: str,
                 action: Optional['outputs.WebACLWafAction'] = None):
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "rule_id", rule_id)
        if action is not None:
            pulumi.set(__self__, "action", action)

    @property
    @pulumi.getter
    def priority(self) -> int:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> str:
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter
    def action(self) -> Optional['outputs.WebACLWafAction']:
        return pulumi.get(self, "action")


@pulumi.output_type
class WebACLWafAction(dict):
    def __init__(__self__, *,
                 type: str):
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class XssMatchSetFieldToMatch(dict):
    def __init__(__self__, *,
                 type: str,
                 data: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if data is not None:
            pulumi.set(__self__, "data", data)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def data(self) -> Optional[str]:
        return pulumi.get(self, "data")


@pulumi.output_type
class XssMatchSetXssMatchTuple(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fieldToMatch":
            suggest = "field_to_match"
        elif key == "textTransformation":
            suggest = "text_transformation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in XssMatchSetXssMatchTuple. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        XssMatchSetXssMatchTuple.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        XssMatchSetXssMatchTuple.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 field_to_match: 'outputs.XssMatchSetFieldToMatch',
                 text_transformation: str):
        pulumi.set(__self__, "field_to_match", field_to_match)
        pulumi.set(__self__, "text_transformation", text_transformation)

    @property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> 'outputs.XssMatchSetFieldToMatch':
        return pulumi.get(self, "field_to_match")

    @property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> str:
        return pulumi.get(self, "text_transformation")


