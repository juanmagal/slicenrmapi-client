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


class ManagedElementAttr(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            dnPrefix = schemas.StrSchema
            
            
            class managedElementTypeList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'managedElementTypeList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            userLabel = schemas.StrSchema
            locationName = schemas.StrSchema
        
            @staticmethod
            def managedBy() -> typing.Type['DnList']:
                return DnList
            vendorName = schemas.StrSchema
            userDefinedState = schemas.StrSchema
            swVersion = schemas.StrSchema
            priorityLabel = schemas.IntSchema
            
            
            class supportedPerfMetricGroups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SupportedPerfMetricGroup']:
                        return SupportedPerfMetricGroup
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SupportedPerfMetricGroup'], typing.List['SupportedPerfMetricGroup']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'supportedPerfMetricGroups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SupportedPerfMetricGroup':
                    return super().__getitem__(i)
            
            
            class supportedTraceMetrics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'supportedTraceMetrics':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "dnPrefix": dnPrefix,
                "managedElementTypeList": managedElementTypeList,
                "userLabel": userLabel,
                "locationName": locationName,
                "managedBy": managedBy,
                "vendorName": vendorName,
                "userDefinedState": userDefinedState,
                "swVersion": swVersion,
                "priorityLabel": priorityLabel,
                "supportedPerfMetricGroups": supportedPerfMetricGroups,
                "supportedTraceMetrics": supportedTraceMetrics,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dnPrefix"]) -> MetaOapg.properties.dnPrefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managedElementTypeList"]) -> MetaOapg.properties.managedElementTypeList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userLabel"]) -> MetaOapg.properties.userLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationName"]) -> MetaOapg.properties.locationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managedBy"]) -> 'DnList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendorName"]) -> MetaOapg.properties.vendorName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userDefinedState"]) -> MetaOapg.properties.userDefinedState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["swVersion"]) -> MetaOapg.properties.swVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priorityLabel"]) -> MetaOapg.properties.priorityLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportedPerfMetricGroups"]) -> MetaOapg.properties.supportedPerfMetricGroups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportedTraceMetrics"]) -> MetaOapg.properties.supportedTraceMetrics: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dnPrefix", "managedElementTypeList", "userLabel", "locationName", "managedBy", "vendorName", "userDefinedState", "swVersion", "priorityLabel", "supportedPerfMetricGroups", "supportedTraceMetrics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dnPrefix"]) -> typing.Union[MetaOapg.properties.dnPrefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managedElementTypeList"]) -> typing.Union[MetaOapg.properties.managedElementTypeList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userLabel"]) -> typing.Union[MetaOapg.properties.userLabel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationName"]) -> typing.Union[MetaOapg.properties.locationName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managedBy"]) -> typing.Union['DnList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendorName"]) -> typing.Union[MetaOapg.properties.vendorName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userDefinedState"]) -> typing.Union[MetaOapg.properties.userDefinedState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["swVersion"]) -> typing.Union[MetaOapg.properties.swVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priorityLabel"]) -> typing.Union[MetaOapg.properties.priorityLabel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportedPerfMetricGroups"]) -> typing.Union[MetaOapg.properties.supportedPerfMetricGroups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportedTraceMetrics"]) -> typing.Union[MetaOapg.properties.supportedTraceMetrics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dnPrefix", "managedElementTypeList", "userLabel", "locationName", "managedBy", "vendorName", "userDefinedState", "swVersion", "priorityLabel", "supportedPerfMetricGroups", "supportedTraceMetrics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dnPrefix: typing.Union[MetaOapg.properties.dnPrefix, str, schemas.Unset] = schemas.unset,
        managedElementTypeList: typing.Union[MetaOapg.properties.managedElementTypeList, list, tuple, schemas.Unset] = schemas.unset,
        userLabel: typing.Union[MetaOapg.properties.userLabel, str, schemas.Unset] = schemas.unset,
        locationName: typing.Union[MetaOapg.properties.locationName, str, schemas.Unset] = schemas.unset,
        managedBy: typing.Union['DnList', schemas.Unset] = schemas.unset,
        vendorName: typing.Union[MetaOapg.properties.vendorName, str, schemas.Unset] = schemas.unset,
        userDefinedState: typing.Union[MetaOapg.properties.userDefinedState, str, schemas.Unset] = schemas.unset,
        swVersion: typing.Union[MetaOapg.properties.swVersion, str, schemas.Unset] = schemas.unset,
        priorityLabel: typing.Union[MetaOapg.properties.priorityLabel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        supportedPerfMetricGroups: typing.Union[MetaOapg.properties.supportedPerfMetricGroups, list, tuple, schemas.Unset] = schemas.unset,
        supportedTraceMetrics: typing.Union[MetaOapg.properties.supportedTraceMetrics, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManagedElementAttr':
        return super().__new__(
            cls,
            *_args,
            dnPrefix=dnPrefix,
            managedElementTypeList=managedElementTypeList,
            userLabel=userLabel,
            locationName=locationName,
            managedBy=managedBy,
            vendorName=vendorName,
            userDefinedState=userDefinedState,
            swVersion=swVersion,
            priorityLabel=priorityLabel,
            supportedPerfMetricGroups=supportedPerfMetricGroups,
            supportedTraceMetrics=supportedTraceMetrics,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.dn_list import DnList
from openapi_client.model.supported_perf_metric_group import SupportedPerfMetricGroup
