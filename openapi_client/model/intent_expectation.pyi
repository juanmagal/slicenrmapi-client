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


class IntentExpectation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is the "IntentExpectation" data type without specialisations
    """


    class MetaOapg:
        
        class properties:
            expectationId = schemas.StrSchema
        
            @staticmethod
            def expectationVerb() -> typing.Type['ExpectationVerb']:
                return ExpectationVerb
            
            
            class expectationObjects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExpectationObject']:
                        return ExpectationObject
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExpectationObject'], typing.List['ExpectationObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expectationObjects':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExpectationObject':
                    return super().__getitem__(i)
            
            
            class expectationTargets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExpectationTarget']:
                        return ExpectationTarget
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExpectationTarget'], typing.List['ExpectationTarget']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expectationTargets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExpectationTarget':
                    return super().__getitem__(i)
            
            
            class expectationContexts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExpectationContext']:
                        return ExpectationContext
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExpectationContext'], typing.List['ExpectationContext']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expectationContexts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExpectationContext':
                    return super().__getitem__(i)
        
            @staticmethod
            def expectationfulfilmentInfo() -> typing.Type['FulfilmentInfo']:
                return FulfilmentInfo
            __annotations__ = {
                "expectationId": expectationId,
                "expectationVerb": expectationVerb,
                "expectationObjects": expectationObjects,
                "expectationTargets": expectationTargets,
                "expectationContexts": expectationContexts,
                "expectationfulfilmentInfo": expectationfulfilmentInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectationId"]) -> MetaOapg.properties.expectationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectationVerb"]) -> 'ExpectationVerb': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectationObjects"]) -> MetaOapg.properties.expectationObjects: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectationTargets"]) -> MetaOapg.properties.expectationTargets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectationContexts"]) -> MetaOapg.properties.expectationContexts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectationfulfilmentInfo"]) -> 'FulfilmentInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expectationId", "expectationVerb", "expectationObjects", "expectationTargets", "expectationContexts", "expectationfulfilmentInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectationId"]) -> typing.Union[MetaOapg.properties.expectationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectationVerb"]) -> typing.Union['ExpectationVerb', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectationObjects"]) -> typing.Union[MetaOapg.properties.expectationObjects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectationTargets"]) -> typing.Union[MetaOapg.properties.expectationTargets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectationContexts"]) -> typing.Union[MetaOapg.properties.expectationContexts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectationfulfilmentInfo"]) -> typing.Union['FulfilmentInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expectationId", "expectationVerb", "expectationObjects", "expectationTargets", "expectationContexts", "expectationfulfilmentInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        expectationId: typing.Union[MetaOapg.properties.expectationId, str, schemas.Unset] = schemas.unset,
        expectationVerb: typing.Union['ExpectationVerb', schemas.Unset] = schemas.unset,
        expectationObjects: typing.Union[MetaOapg.properties.expectationObjects, list, tuple, schemas.Unset] = schemas.unset,
        expectationTargets: typing.Union[MetaOapg.properties.expectationTargets, list, tuple, schemas.Unset] = schemas.unset,
        expectationContexts: typing.Union[MetaOapg.properties.expectationContexts, list, tuple, schemas.Unset] = schemas.unset,
        expectationfulfilmentInfo: typing.Union['FulfilmentInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntentExpectation':
        return super().__new__(
            cls,
            *_args,
            expectationId=expectationId,
            expectationVerb=expectationVerb,
            expectationObjects=expectationObjects,
            expectationTargets=expectationTargets,
            expectationContexts=expectationContexts,
            expectationfulfilmentInfo=expectationfulfilmentInfo,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.expectation_context import ExpectationContext
from openapi_client.model.expectation_object import ExpectationObject
from openapi_client.model.expectation_target import ExpectationTarget
from openapi_client.model.expectation_verb import ExpectationVerb
from openapi_client.model.fulfilment_info import FulfilmentInfo
