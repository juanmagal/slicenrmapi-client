# coding: utf-8

"""
    Provisioning MnS

    OAS 3.0.1 definition of the Provisioning MnS Â© 2022, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.  # noqa: E501

    The version of the OpenAPI document: 17.2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class SliceSimultaneousUse(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ZERO": "ZERO",
            "ONE": "ONE",
            "TWO": "TWO",
            "THREE": "THREE",
            "FOUR": "FOUR",
        }
    
    @schemas.classproperty
    def ZERO(cls):
        return cls("ZERO")
    
    @schemas.classproperty
    def ONE(cls):
        return cls("ONE")
    
    @schemas.classproperty
    def TWO(cls):
        return cls("TWO")
    
    @schemas.classproperty
    def THREE(cls):
        return cls("THREE")
    
    @schemas.classproperty
    def FOUR(cls):
        return cls("FOUR")
