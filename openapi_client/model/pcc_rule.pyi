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


class PccRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            pccRuleId = schemas.StrSchema
            
            
            class flowInfoList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FlowInformation']:
                        return FlowInformation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FlowInformation'], typing.List['FlowInformation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'flowInfoList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FlowInformation':
                    return super().__getitem__(i)
            applicationId = schemas.StrSchema
            appDescriptor = schemas.StrSchema
            contentVersion = schemas.IntSchema
        
            @staticmethod
            def precedence() -> typing.Type['Uinteger']:
                return Uinteger
        
            @staticmethod
            def afSigProtocol() -> typing.Type['AfSigProtocol']:
                return AfSigProtocol
            isAppRelocatable = schemas.BoolSchema
            isUeAddrPreserved = schemas.BoolSchema
            
            
            class qosData(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['QosDataList']:
                        return QosDataList
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['QosDataList'], typing.List['QosDataList']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'qosData':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'QosDataList':
                    return super().__getitem__(i)
            
            
            class altQosParams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['QosDataList']:
                        return QosDataList
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['QosDataList'], typing.List['QosDataList']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'altQosParams':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'QosDataList':
                    return super().__getitem__(i)
            
            
            class trafficControlData(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TrafficControlDataList']:
                        return TrafficControlDataList
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TrafficControlDataList'], typing.List['TrafficControlDataList']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'trafficControlData':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TrafficControlDataList':
                    return super().__getitem__(i)
        
            @staticmethod
            def conditionData() -> typing.Type['ConditionData']:
                return ConditionData
        
            @staticmethod
            def tscaiInputDl() -> typing.Type['TscaiInputContainer']:
                return TscaiInputContainer
        
            @staticmethod
            def tscaiInputUl() -> typing.Type['TscaiInputContainer']:
                return TscaiInputContainer
            __annotations__ = {
                "pccRuleId": pccRuleId,
                "flowInfoList": flowInfoList,
                "applicationId": applicationId,
                "appDescriptor": appDescriptor,
                "contentVersion": contentVersion,
                "precedence": precedence,
                "afSigProtocol": afSigProtocol,
                "isAppRelocatable": isAppRelocatable,
                "isUeAddrPreserved": isUeAddrPreserved,
                "qosData": qosData,
                "altQosParams": altQosParams,
                "trafficControlData": trafficControlData,
                "conditionData": conditionData,
                "tscaiInputDl": tscaiInputDl,
                "tscaiInputUl": tscaiInputUl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pccRuleId"]) -> MetaOapg.properties.pccRuleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flowInfoList"]) -> MetaOapg.properties.flowInfoList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationId"]) -> MetaOapg.properties.applicationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appDescriptor"]) -> MetaOapg.properties.appDescriptor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentVersion"]) -> MetaOapg.properties.contentVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["precedence"]) -> 'Uinteger': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["afSigProtocol"]) -> 'AfSigProtocol': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAppRelocatable"]) -> MetaOapg.properties.isAppRelocatable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isUeAddrPreserved"]) -> MetaOapg.properties.isUeAddrPreserved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qosData"]) -> MetaOapg.properties.qosData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["altQosParams"]) -> MetaOapg.properties.altQosParams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trafficControlData"]) -> MetaOapg.properties.trafficControlData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditionData"]) -> 'ConditionData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tscaiInputDl"]) -> 'TscaiInputContainer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tscaiInputUl"]) -> 'TscaiInputContainer': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pccRuleId", "flowInfoList", "applicationId", "appDescriptor", "contentVersion", "precedence", "afSigProtocol", "isAppRelocatable", "isUeAddrPreserved", "qosData", "altQosParams", "trafficControlData", "conditionData", "tscaiInputDl", "tscaiInputUl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pccRuleId"]) -> typing.Union[MetaOapg.properties.pccRuleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flowInfoList"]) -> typing.Union[MetaOapg.properties.flowInfoList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationId"]) -> typing.Union[MetaOapg.properties.applicationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appDescriptor"]) -> typing.Union[MetaOapg.properties.appDescriptor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentVersion"]) -> typing.Union[MetaOapg.properties.contentVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["precedence"]) -> typing.Union['Uinteger', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["afSigProtocol"]) -> typing.Union['AfSigProtocol', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAppRelocatable"]) -> typing.Union[MetaOapg.properties.isAppRelocatable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isUeAddrPreserved"]) -> typing.Union[MetaOapg.properties.isUeAddrPreserved, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qosData"]) -> typing.Union[MetaOapg.properties.qosData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["altQosParams"]) -> typing.Union[MetaOapg.properties.altQosParams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trafficControlData"]) -> typing.Union[MetaOapg.properties.trafficControlData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditionData"]) -> typing.Union['ConditionData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tscaiInputDl"]) -> typing.Union['TscaiInputContainer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tscaiInputUl"]) -> typing.Union['TscaiInputContainer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pccRuleId", "flowInfoList", "applicationId", "appDescriptor", "contentVersion", "precedence", "afSigProtocol", "isAppRelocatable", "isUeAddrPreserved", "qosData", "altQosParams", "trafficControlData", "conditionData", "tscaiInputDl", "tscaiInputUl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pccRuleId: typing.Union[MetaOapg.properties.pccRuleId, str, schemas.Unset] = schemas.unset,
        flowInfoList: typing.Union[MetaOapg.properties.flowInfoList, list, tuple, schemas.Unset] = schemas.unset,
        applicationId: typing.Union[MetaOapg.properties.applicationId, str, schemas.Unset] = schemas.unset,
        appDescriptor: typing.Union[MetaOapg.properties.appDescriptor, str, schemas.Unset] = schemas.unset,
        contentVersion: typing.Union[MetaOapg.properties.contentVersion, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        precedence: typing.Union['Uinteger', schemas.Unset] = schemas.unset,
        afSigProtocol: typing.Union['AfSigProtocol', schemas.Unset] = schemas.unset,
        isAppRelocatable: typing.Union[MetaOapg.properties.isAppRelocatable, bool, schemas.Unset] = schemas.unset,
        isUeAddrPreserved: typing.Union[MetaOapg.properties.isUeAddrPreserved, bool, schemas.Unset] = schemas.unset,
        qosData: typing.Union[MetaOapg.properties.qosData, list, tuple, schemas.Unset] = schemas.unset,
        altQosParams: typing.Union[MetaOapg.properties.altQosParams, list, tuple, schemas.Unset] = schemas.unset,
        trafficControlData: typing.Union[MetaOapg.properties.trafficControlData, list, tuple, schemas.Unset] = schemas.unset,
        conditionData: typing.Union['ConditionData', schemas.Unset] = schemas.unset,
        tscaiInputDl: typing.Union['TscaiInputContainer', schemas.Unset] = schemas.unset,
        tscaiInputUl: typing.Union['TscaiInputContainer', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PccRule':
        return super().__new__(
            cls,
            *_args,
            pccRuleId=pccRuleId,
            flowInfoList=flowInfoList,
            applicationId=applicationId,
            appDescriptor=appDescriptor,
            contentVersion=contentVersion,
            precedence=precedence,
            afSigProtocol=afSigProtocol,
            isAppRelocatable=isAppRelocatable,
            isUeAddrPreserved=isUeAddrPreserved,
            qosData=qosData,
            altQosParams=altQosParams,
            trafficControlData=trafficControlData,
            conditionData=conditionData,
            tscaiInputDl=tscaiInputDl,
            tscaiInputUl=tscaiInputUl,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.af_sig_protocol import AfSigProtocol
from openapi_client.model.condition_data import ConditionData
from openapi_client.model.flow_information import FlowInformation
from openapi_client.model.qos_data_list import QosDataList
from openapi_client.model.traffic_control_data_list import TrafficControlDataList
from openapi_client.model.tscai_input_container import TscaiInputContainer
from openapi_client.model.uinteger import Uinteger
