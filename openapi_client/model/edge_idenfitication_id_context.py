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


class EdgeIdenfiticationIdContext(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is the "ObjectContext" data type with specialisations for EdgeIdenfiticationIdContext      
    """


    class MetaOapg:
        
        class properties:
            
            
            class contextAttribute(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "edgeIdentificationId": "EDGE_IDENTIFICATION_ID",
                    }
                
                @schemas.classproperty
                def EDGE_IDENTIFICATION_ID(cls):
                    return cls("edgeIdentificationId")
            
            
            class contextCondition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "IS_EQUAL_TO": "IS_EQUAL_TO",
                    }
                
                @schemas.classproperty
                def IS_EQUAL_TO(cls):
                    return cls("IS_EQUAL_TO")
            
            
            class contextValueRange(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contextValueRange':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "contextAttribute": contextAttribute,
                "contextCondition": contextCondition,
                "contextValueRange": contextValueRange,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextAttribute"]) -> MetaOapg.properties.contextAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextCondition"]) -> MetaOapg.properties.contextCondition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextValueRange"]) -> MetaOapg.properties.contextValueRange: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contextAttribute", "contextCondition", "contextValueRange", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextAttribute"]) -> typing.Union[MetaOapg.properties.contextAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextCondition"]) -> typing.Union[MetaOapg.properties.contextCondition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextValueRange"]) -> typing.Union[MetaOapg.properties.contextValueRange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contextAttribute", "contextCondition", "contextValueRange", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        contextAttribute: typing.Union[MetaOapg.properties.contextAttribute, str, schemas.Unset] = schemas.unset,
        contextCondition: typing.Union[MetaOapg.properties.contextCondition, str, schemas.Unset] = schemas.unset,
        contextValueRange: typing.Union[MetaOapg.properties.contextValueRange, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EdgeIdenfiticationIdContext':
        return super().__new__(
            cls,
            *_args,
            contextAttribute=contextAttribute,
            contextCondition=contextCondition,
            contextValueRange=contextValueRange,
            _configuration=_configuration,
            **kwargs,
        )
