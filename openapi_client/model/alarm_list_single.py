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


class AlarmListSingle(
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
                            
                                @staticmethod
                                def administrativeState() -> typing.Type['AdministrativeState']:
                                    return AdministrativeState
                            
                                @staticmethod
                                def operationalState() -> typing.Type['OperationalState']:
                                    return OperationalState
                                numOfAlarmRecords = schemas.IntSchema
                                lastModification = schemas.DateTimeSchema
                                
                                
                                class alarmRecords(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def additional_properties() -> typing.Type['AlarmRecord']:
                                            return AlarmRecord
                                    
                                    def __getitem__(self, name: typing.Union[str, ]) -> 'AlarmRecord':
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    def get_item_oapg(self, name: typing.Union[str, ]) -> 'AlarmRecord':
                                        return super().get_item_oapg(name)
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: 'AlarmRecord',
                                    ) -> 'alarmRecords':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "administrativeState": administrativeState,
                                    "operationalState": operationalState,
                                    "numOfAlarmRecords": numOfAlarmRecords,
                                    "lastModification": lastModification,
                                    "alarmRecords": alarmRecords,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["administrativeState"]) -> 'AdministrativeState': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["operationalState"]) -> 'OperationalState': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["numOfAlarmRecords"]) -> MetaOapg.properties.numOfAlarmRecords: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["lastModification"]) -> MetaOapg.properties.lastModification: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["alarmRecords"]) -> MetaOapg.properties.alarmRecords: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["administrativeState", "operationalState", "numOfAlarmRecords", "lastModification", "alarmRecords", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["administrativeState"]) -> typing.Union['AdministrativeState', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["operationalState"]) -> typing.Union['OperationalState', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["numOfAlarmRecords"]) -> typing.Union[MetaOapg.properties.numOfAlarmRecords, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["lastModification"]) -> typing.Union[MetaOapg.properties.lastModification, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["alarmRecords"]) -> typing.Union[MetaOapg.properties.alarmRecords, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["administrativeState", "operationalState", "numOfAlarmRecords", "lastModification", "alarmRecords", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            administrativeState: typing.Union['AdministrativeState', schemas.Unset] = schemas.unset,
                            operationalState: typing.Union['OperationalState', schemas.Unset] = schemas.unset,
                            numOfAlarmRecords: typing.Union[MetaOapg.properties.numOfAlarmRecords, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            lastModification: typing.Union[MetaOapg.properties.lastModification, str, datetime, schemas.Unset] = schemas.unset,
                            alarmRecords: typing.Union[MetaOapg.properties.alarmRecords, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
                                administrativeState=administrativeState,
                                operationalState=operationalState,
                                numOfAlarmRecords=numOfAlarmRecords,
                                lastModification=lastModification,
                                alarmRecords=alarmRecords,
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
    ) -> 'AlarmListSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.administrative_state import AdministrativeState
from openapi_client.model.alarm_record import AlarmRecord
from openapi_client.model.operational_state import OperationalState
from openapi_client.model.top import Top
