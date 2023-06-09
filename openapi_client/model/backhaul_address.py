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


class BackhaulAddress(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            gnbId = schemas.StrSchema
        
            @staticmethod
            def tai() -> typing.Type['Tai']:
                return Tai
            __annotations__ = {
                "gnbId": gnbId,
                "tai": tai,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gnbId"]) -> MetaOapg.properties.gnbId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tai"]) -> 'Tai': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gnbId", "tai", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gnbId"]) -> typing.Union[MetaOapg.properties.gnbId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tai"]) -> typing.Union['Tai', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gnbId", "tai", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gnbId: typing.Union[MetaOapg.properties.gnbId, str, schemas.Unset] = schemas.unset,
        tai: typing.Union['Tai', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BackhaulAddress':
        return super().__new__(
            cls,
            *_args,
            gnbId=gnbId,
            tai=tai,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.tai import Tai
