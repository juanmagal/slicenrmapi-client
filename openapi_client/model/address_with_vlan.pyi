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


class AddressWithVlan(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def ipv4Address() -> typing.Type['Ipv4Addr']:
                return Ipv4Addr
        
            @staticmethod
            def ipv6Address() -> typing.Type['Ipv6Addr']:
                return Ipv6Addr
            
            
            class vlanId(
                schemas.IntSchema
            ):
                pass
            __annotations__ = {
                "ipv4Address": ipv4Address,
                "ipv6Address": ipv6Address,
                "vlanId": vlanId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv4Address"]) -> 'Ipv4Addr': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv6Address"]) -> 'Ipv6Addr': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vlanId"]) -> MetaOapg.properties.vlanId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ipv4Address", "ipv6Address", "vlanId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv4Address"]) -> typing.Union['Ipv4Addr', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv6Address"]) -> typing.Union['Ipv6Addr', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vlanId"]) -> typing.Union[MetaOapg.properties.vlanId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ipv4Address", "ipv6Address", "vlanId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ipv4Address: typing.Union['Ipv4Addr', schemas.Unset] = schemas.unset,
        ipv6Address: typing.Union['Ipv6Addr', schemas.Unset] = schemas.unset,
        vlanId: typing.Union[MetaOapg.properties.vlanId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddressWithVlan':
        return super().__new__(
            cls,
            *_args,
            ipv4Address=ipv4Address,
            ipv6Address=ipv6Address,
            vlanId=vlanId,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.ipv4_addr import Ipv4Addr
from openapi_client.model.ipv6_addr import Ipv6Addr
