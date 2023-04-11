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


class ExternalGnbCuCpFunctionMultiple(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExternalGnbCuCpFunctionSingle']:
            return ExternalGnbCuCpFunctionSingle

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['ExternalGnbCuCpFunctionSingle'], typing.List['ExternalGnbCuCpFunctionSingle']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExternalGnbCuCpFunctionMultiple':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ExternalGnbCuCpFunctionSingle':
        return super().__getitem__(i)

from openapi_client.model.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle