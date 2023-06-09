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


class QFQoSMonitoringControlSingle(
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
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        
                                        
                                        class qFQoSMonitoringState(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def ENABLED(cls):
                                                return cls("ENABLED")
                                            
                                            @schemas.classproperty
                                            def DISABLED(cls):
                                                return cls("DISABLED")
                                        
                                        
                                        class qFMonitoredSNSSAIs(
                                            schemas.ListSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                @staticmethod
                                                def items() -> typing.Type['Snssai']:
                                                    return Snssai
                                        
                                            def __new__(
                                                cls,
                                                _arg: typing.Union[typing.Tuple['Snssai'], typing.List['Snssai']],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'qFMonitoredSNSSAIs':
                                                return super().__new__(
                                                    cls,
                                                    _arg,
                                                    _configuration=_configuration,
                                                )
                                        
                                            def __getitem__(self, i: int) -> 'Snssai':
                                                return super().__getitem__(i)
                                        
                                        
                                        class qFMonitored5QIs(
                                            schemas.ListSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                
                                                class items(
                                                    schemas.IntSchema
                                                ):
                                                    pass
                                        
                                            def __new__(
                                                cls,
                                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'qFMonitored5QIs':
                                                return super().__new__(
                                                    cls,
                                                    _arg,
                                                    _configuration=_configuration,
                                                )
                                        
                                            def __getitem__(self, i: int) -> MetaOapg.items:
                                                return super().__getitem__(i)
                                        isEventTriggeredQFMonitoringSupported = schemas.BoolSchema
                                        isPeriodicQFMonitoringSupported = schemas.BoolSchema
                                        isSessionReleasedQFMonitoringSupported = schemas.BoolSchema
                                    
                                        @staticmethod
                                        def qFPacketDelayThresholds() -> typing.Type['QFPacketDelayThresholdsType']:
                                            return QFPacketDelayThresholdsType
                                        qFMinimumWaitTime = schemas.IntSchema
                                        qFMeasurementPeriod = schemas.IntSchema
                                        __annotations__ = {
                                            "qFQoSMonitoringState": qFQoSMonitoringState,
                                            "qFMonitoredSNSSAIs": qFMonitoredSNSSAIs,
                                            "qFMonitored5QIs": qFMonitored5QIs,
                                            "isEventTriggeredQFMonitoringSupported": isEventTriggeredQFMonitoringSupported,
                                            "isPeriodicQFMonitoringSupported": isPeriodicQFMonitoringSupported,
                                            "isSessionReleasedQFMonitoringSupported": isSessionReleasedQFMonitoringSupported,
                                            "qFPacketDelayThresholds": qFPacketDelayThresholds,
                                            "qFMinimumWaitTime": qFMinimumWaitTime,
                                            "qFMeasurementPeriod": qFMeasurementPeriod,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["qFQoSMonitoringState"]) -> MetaOapg.properties.qFQoSMonitoringState: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["qFMonitoredSNSSAIs"]) -> MetaOapg.properties.qFMonitoredSNSSAIs: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["qFMonitored5QIs"]) -> MetaOapg.properties.qFMonitored5QIs: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["isEventTriggeredQFMonitoringSupported"]) -> MetaOapg.properties.isEventTriggeredQFMonitoringSupported: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["isPeriodicQFMonitoringSupported"]) -> MetaOapg.properties.isPeriodicQFMonitoringSupported: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["isSessionReleasedQFMonitoringSupported"]) -> MetaOapg.properties.isSessionReleasedQFMonitoringSupported: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["qFPacketDelayThresholds"]) -> 'QFPacketDelayThresholdsType': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["qFMinimumWaitTime"]) -> MetaOapg.properties.qFMinimumWaitTime: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["qFMeasurementPeriod"]) -> MetaOapg.properties.qFMeasurementPeriod: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["qFQoSMonitoringState", "qFMonitoredSNSSAIs", "qFMonitored5QIs", "isEventTriggeredQFMonitoringSupported", "isPeriodicQFMonitoringSupported", "isSessionReleasedQFMonitoringSupported", "qFPacketDelayThresholds", "qFMinimumWaitTime", "qFMeasurementPeriod", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["qFQoSMonitoringState"]) -> typing.Union[MetaOapg.properties.qFQoSMonitoringState, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["qFMonitoredSNSSAIs"]) -> typing.Union[MetaOapg.properties.qFMonitoredSNSSAIs, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["qFMonitored5QIs"]) -> typing.Union[MetaOapg.properties.qFMonitored5QIs, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["isEventTriggeredQFMonitoringSupported"]) -> typing.Union[MetaOapg.properties.isEventTriggeredQFMonitoringSupported, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["isPeriodicQFMonitoringSupported"]) -> typing.Union[MetaOapg.properties.isPeriodicQFMonitoringSupported, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["isSessionReleasedQFMonitoringSupported"]) -> typing.Union[MetaOapg.properties.isSessionReleasedQFMonitoringSupported, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["qFPacketDelayThresholds"]) -> typing.Union['QFPacketDelayThresholdsType', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["qFMinimumWaitTime"]) -> typing.Union[MetaOapg.properties.qFMinimumWaitTime, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["qFMeasurementPeriod"]) -> typing.Union[MetaOapg.properties.qFMeasurementPeriod, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["qFQoSMonitoringState", "qFMonitoredSNSSAIs", "qFMonitored5QIs", "isEventTriggeredQFMonitoringSupported", "isPeriodicQFMonitoringSupported", "isSessionReleasedQFMonitoringSupported", "qFPacketDelayThresholds", "qFMinimumWaitTime", "qFMeasurementPeriod", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    qFQoSMonitoringState: typing.Union[MetaOapg.properties.qFQoSMonitoringState, str, schemas.Unset] = schemas.unset,
                                    qFMonitoredSNSSAIs: typing.Union[MetaOapg.properties.qFMonitoredSNSSAIs, list, tuple, schemas.Unset] = schemas.unset,
                                    qFMonitored5QIs: typing.Union[MetaOapg.properties.qFMonitored5QIs, list, tuple, schemas.Unset] = schemas.unset,
                                    isEventTriggeredQFMonitoringSupported: typing.Union[MetaOapg.properties.isEventTriggeredQFMonitoringSupported, bool, schemas.Unset] = schemas.unset,
                                    isPeriodicQFMonitoringSupported: typing.Union[MetaOapg.properties.isPeriodicQFMonitoringSupported, bool, schemas.Unset] = schemas.unset,
                                    isSessionReleasedQFMonitoringSupported: typing.Union[MetaOapg.properties.isSessionReleasedQFMonitoringSupported, bool, schemas.Unset] = schemas.unset,
                                    qFPacketDelayThresholds: typing.Union['QFPacketDelayThresholdsType', schemas.Unset] = schemas.unset,
                                    qFMinimumWaitTime: typing.Union[MetaOapg.properties.qFMinimumWaitTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                    qFMeasurementPeriod: typing.Union[MetaOapg.properties.qFMeasurementPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_0':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        qFQoSMonitoringState=qFQoSMonitoringState,
                                        qFMonitoredSNSSAIs=qFMonitoredSNSSAIs,
                                        qFMonitored5QIs=qFMonitored5QIs,
                                        isEventTriggeredQFMonitoringSupported=isEventTriggeredQFMonitoringSupported,
                                        isPeriodicQFMonitoringSupported=isPeriodicQFMonitoringSupported,
                                        isSessionReleasedQFMonitoringSupported=isSessionReleasedQFMonitoringSupported,
                                        qFPacketDelayThresholds=qFPacketDelayThresholds,
                                        qFMinimumWaitTime=qFMinimumWaitTime,
                                        qFMeasurementPeriod=qFMeasurementPeriod,
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
                                    cls.all_of_0,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
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
                attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
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
    ) -> 'QFQoSMonitoringControlSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.qf_packet_delay_thresholds_type import QFPacketDelayThresholdsType
from openapi_client.model.snssai import Snssai
from openapi_client.model.top import Top
