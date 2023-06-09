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


class IntentSingle(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    userLabel = schemas.StrSchema
                    
                    
                    class intentExpectations(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.ComposedBase,
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    @classmethod
                                    @functools.lru_cache()
                                    def one_of(cls):
                                        # we need this here to make our import statements work
                                        # we must store _composed_schemas in here so the code is only run
                                        # when we invoke this method. If we kept this at the class
                                        # level we would get an error because the class level
                                        # code would be run when this module is imported, and these composed
                                        # classes don't exist yet because their module has not finished
                                        # loading
                                        return [
                                            IntentExpectation,
                                            RadioNetworkExpectation,
                                            ServiceSupportExpectation,
                                        ]
                            
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'intentExpectations':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class intentContexts(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['IntentContext']:
                                return IntentContext
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['IntentContext'], typing.List['IntentContext']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'intentContexts':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'IntentContext':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def intentFulfilmentInfo() -> typing.Type['FulfilmentInfo']:
                        return FulfilmentInfo
                    __annotations__ = {
                        "userLabel": userLabel,
                        "intentExpectations": intentExpectations,
                        "intentContexts": intentContexts,
                        "intentFulfilmentInfo": intentFulfilmentInfo,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["userLabel"]) -> MetaOapg.properties.userLabel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["intentExpectations"]) -> MetaOapg.properties.intentExpectations: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["intentContexts"]) -> MetaOapg.properties.intentContexts: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["intentFulfilmentInfo"]) -> 'FulfilmentInfo': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["userLabel", "intentExpectations", "intentContexts", "intentFulfilmentInfo", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["userLabel"]) -> typing.Union[MetaOapg.properties.userLabel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["intentExpectations"]) -> typing.Union[MetaOapg.properties.intentExpectations, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["intentContexts"]) -> typing.Union[MetaOapg.properties.intentContexts, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["intentFulfilmentInfo"]) -> typing.Union['FulfilmentInfo', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userLabel", "intentExpectations", "intentContexts", "intentFulfilmentInfo", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                userLabel: typing.Union[MetaOapg.properties.userLabel, str, schemas.Unset] = schemas.unset,
                intentExpectations: typing.Union[MetaOapg.properties.intentExpectations, list, tuple, schemas.Unset] = schemas.unset,
                intentContexts: typing.Union[MetaOapg.properties.intentContexts, list, tuple, schemas.Unset] = schemas.unset,
                intentFulfilmentInfo: typing.Union['FulfilmentInfo', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    userLabel=userLabel,
                    intentExpectations=intentExpectations,
                    intentContexts=intentContexts,
                    intentFulfilmentInfo=intentFulfilmentInfo,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                Top,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntentSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.fulfilment_info import FulfilmentInfo
from openapi_client.model.intent_context import IntentContext
from openapi_client.model.intent_expectation import IntentExpectation
from openapi_client.model.radio_network_expectation import RadioNetworkExpectation
from openapi_client.model.service_support_expectation import ServiceSupportExpectation
from openapi_client.model.top import Top
