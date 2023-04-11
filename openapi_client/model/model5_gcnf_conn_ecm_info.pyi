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


class Model5GCNfConnEcmInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Store the 5GC NF connection information
    """


    class MetaOapg:
        
        class properties:
            
            
            class _5_gcnf_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PCF(cls):
                    return cls("PCF")
                
                @schemas.classproperty
                def NEF(cls):
                    return cls("NEF")
                
                @schemas.classproperty
                def SCEF(cls):
                    return cls("SCEF")
            _5_gcnfip_address = schemas.StrSchema
            _5_gcnf_ref = schemas.StrSchema
            __annotations__ = {
                "5GCNFType": _5_gcnf_type,
                "5GCNFIpAddress": _5_gcnfip_address,
                "5GCNFRef": _5_gcnf_ref,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["5GCNFType"]) -> MetaOapg.properties._5_gcnf_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["5GCNFIpAddress"]) -> MetaOapg.properties._5_gcnfip_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["5GCNFRef"]) -> MetaOapg.properties._5_gcnf_ref: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["5GCNFType", "5GCNFIpAddress", "5GCNFRef", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["5GCNFType"]) -> typing.Union[MetaOapg.properties._5_gcnf_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["5GCNFIpAddress"]) -> typing.Union[MetaOapg.properties._5_gcnfip_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["5GCNFRef"]) -> typing.Union[MetaOapg.properties._5_gcnf_ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["5GCNFType", "5GCNFIpAddress", "5GCNFRef", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Model5GCNfConnEcmInfo':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )