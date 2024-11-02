# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from petstore_api.models.test_enum import TestEnum
from petstore_api.models.test_enum_with_default import TestEnumWithDefault

class TestModelWithEnumDefault(BaseModel):
    """
    TestModelWithEnumDefault
    """
    test_enum: TestEnum = Field(...)
    test_string: Optional[StrictStr] = None
    test_enum_with_default: Optional[TestEnumWithDefault] = None
    test_string_with_default: Optional[StrictStr] = 'ahoy matey'
    test_inline_defined_enum_with_default: Optional[StrictStr] = 'B'
    __properties = ["test_enum", "test_string", "test_enum_with_default", "test_string_with_default", "test_inline_defined_enum_with_default"]

    @validator('test_inline_defined_enum_with_default')
    def test_inline_defined_enum_with_default_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('A', 'B', 'C',):
            raise ValueError("must be one of enum values ('A', 'B', 'C')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TestModelWithEnumDefault:
        """Create an instance of TestModelWithEnumDefault from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TestModelWithEnumDefault:
        """Create an instance of TestModelWithEnumDefault from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TestModelWithEnumDefault.parse_obj(obj)

        _obj = TestModelWithEnumDefault.parse_obj({
            "test_enum": obj.get("test_enum"),
            "test_string": obj.get("test_string"),
            "test_enum_with_default": obj.get("test_enum_with_default"),
            "test_string_with_default": obj.get("test_string_with_default") if obj.get("test_string_with_default") is not None else 'ahoy matey',
            "test_inline_defined_enum_with_default": obj.get("test_inline_defined_enum_with_default") if obj.get("test_inline_defined_enum_with_default") is not None else 'B'
        })
        return _obj


