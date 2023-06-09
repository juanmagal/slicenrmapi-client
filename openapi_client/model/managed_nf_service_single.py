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


class ManagedNFServiceSingle(
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
                    
                    
                    class attributes(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                userLabel = schemas.StrSchema
                            
                                @staticmethod
                                def nFServiceType() -> typing.Type['NFServiceType']:
                                    return NFServiceType
                            
                                @staticmethod
                                def sAP() -> typing.Type['SAP']:
                                    return SAP
                                
                                
                                class operations(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['Operation1']:
                                            return Operation1
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple['Operation1'], typing.List['Operation1']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'operations':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'Operation1':
                                        return super().__getitem__(i)
                            
                                @staticmethod
                                def administrativeState() -> typing.Type['AdministrativeState']:
                                    return AdministrativeState
                            
                                @staticmethod
                                def operationalState() -> typing.Type['OperationalState']:
                                    return OperationalState
                            
                                @staticmethod
                                def usageState() -> typing.Type['UsageState']:
                                    return UsageState
                            
                                @staticmethod
                                def registrationState() -> typing.Type['RegistrationState']:
                                    return RegistrationState
                                __annotations__ = {
                                    "userLabel": userLabel,
                                    "nFServiceType": nFServiceType,
                                    "sAP": sAP,
                                    "operations": operations,
                                    "administrativeState": administrativeState,
                                    "operationalState": operationalState,
                                    "usageState": usageState,
                                    "registrationState": registrationState,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["userLabel"]) -> MetaOapg.properties.userLabel: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["nFServiceType"]) -> 'NFServiceType': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["sAP"]) -> 'SAP': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["operations"]) -> MetaOapg.properties.operations: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["administrativeState"]) -> 'AdministrativeState': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["operationalState"]) -> 'OperationalState': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["usageState"]) -> 'UsageState': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["registrationState"]) -> 'RegistrationState': ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["userLabel", "nFServiceType", "sAP", "operations", "administrativeState", "operationalState", "usageState", "registrationState", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["userLabel"]) -> typing.Union[MetaOapg.properties.userLabel, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["nFServiceType"]) -> typing.Union['NFServiceType', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["sAP"]) -> typing.Union['SAP', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["operations"]) -> typing.Union[MetaOapg.properties.operations, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["administrativeState"]) -> typing.Union['AdministrativeState', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["operationalState"]) -> typing.Union['OperationalState', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["usageState"]) -> typing.Union['UsageState', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["registrationState"]) -> typing.Union['RegistrationState', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userLabel", "nFServiceType", "sAP", "operations", "administrativeState", "operationalState", "usageState", "registrationState", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            userLabel: typing.Union[MetaOapg.properties.userLabel, str, schemas.Unset] = schemas.unset,
                            nFServiceType: typing.Union['NFServiceType', schemas.Unset] = schemas.unset,
                            sAP: typing.Union['SAP', schemas.Unset] = schemas.unset,
                            operations: typing.Union[MetaOapg.properties.operations, list, tuple, schemas.Unset] = schemas.unset,
                            administrativeState: typing.Union['AdministrativeState', schemas.Unset] = schemas.unset,
                            operationalState: typing.Union['OperationalState', schemas.Unset] = schemas.unset,
                            usageState: typing.Union['UsageState', schemas.Unset] = schemas.unset,
                            registrationState: typing.Union['RegistrationState', schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
                                userLabel=userLabel,
                                nFServiceType=nFServiceType,
                                sAP=sAP,
                                operations=operations,
                                administrativeState=administrativeState,
                                operationalState=operationalState,
                                usageState=usageState,
                                registrationState=registrationState,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "attributes": attributes,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    attributes=attributes,
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
    ) -> 'ManagedNFServiceSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.administrative_state import AdministrativeState
from openapi_client.model.nf_service_type import NFServiceType
from openapi_client.model.operation1 import Operation1
from openapi_client.model.operational_state import OperationalState
from openapi_client.model.registration_state import RegistrationState
from openapi_client.model.sap import SAP
from openapi_client.model.top import Top
from openapi_client.model.usage_state import UsageState
