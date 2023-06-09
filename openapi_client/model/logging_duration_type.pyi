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


class LoggingDurationType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    See details in 3GPP TS 32.422 clause 5.10.9.
    """
    
    @schemas.classproperty
    def DIGIT_SIX_00S(cls):
        return cls("600s")
    
    @schemas.classproperty
    def DIGIT_ONE_200S(cls):
        return cls("1200s")
    
    @schemas.classproperty
    def DIGIT_TWO_400S(cls):
        return cls("2400s")
    
    @schemas.classproperty
    def DIGIT_THREE_600S(cls):
        return cls("3600s")
    
    @schemas.classproperty
    def DIGIT_FIVE_400S(cls):
        return cls("5400s")
    
    @schemas.classproperty
    def DIGIT_SEVEN_200S(cls):
        return cls("7200s")
