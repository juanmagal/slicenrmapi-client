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


class EUtranFreqRelationSingle(
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
                                def cellIndividualOffset() -> typing.Type['CellIndividualOffset']:
                                    return CellIndividualOffset
                                
                                
                                class blackListEntry(
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
                                    ) -> 'blackListEntry':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                blackListEntryIdleMode = schemas.IntSchema
                                cellReselectionPriority = schemas.IntSchema
                                
                                
                                class cellReselectionSubPriority(
                                    schemas.NumberSchema
                                ):
                                    pass
                                
                                
                                class pMax(
                                    schemas.IntSchema
                                ):
                                    pass
                                qOffsetFreq = schemas.NumberSchema
                                qQualMin = schemas.NumberSchema
                                
                                
                                class qRxLevMin(
                                    schemas.IntSchema
                                ):
                                    pass
                                
                                
                                class threshXHighP(
                                    schemas.IntSchema
                                ):
                                    pass
                                
                                
                                class threshXHighQ(
                                    schemas.IntSchema
                                ):
                                    pass
                                
                                
                                class threshXLowP(
                                    schemas.IntSchema
                                ):
                                    pass
                                
                                
                                class threshXLowQ(
                                    schemas.IntSchema
                                ):
                                    pass
                                
                                
                                class tReselectionEutran(
                                    schemas.IntSchema
                                ):
                                    pass
                            
                                @staticmethod
                                def tReselectionNRSfHigh() -> typing.Type['TReselectionNRSf']:
                                    return TReselectionNRSf
                            
                                @staticmethod
                                def tReselectionNRSfMedium() -> typing.Type['TReselectionNRSf']:
                                    return TReselectionNRSf
                                eUTranFrequencyRef = schemas.StrSchema
                                __annotations__ = {
                                    "cellIndividualOffset": cellIndividualOffset,
                                    "blackListEntry": blackListEntry,
                                    "blackListEntryIdleMode": blackListEntryIdleMode,
                                    "cellReselectionPriority": cellReselectionPriority,
                                    "cellReselectionSubPriority": cellReselectionSubPriority,
                                    "pMax": pMax,
                                    "qOffsetFreq": qOffsetFreq,
                                    "qQualMin": qQualMin,
                                    "qRxLevMin": qRxLevMin,
                                    "threshXHighP": threshXHighP,
                                    "threshXHighQ": threshXHighQ,
                                    "threshXLowP": threshXLowP,
                                    "threshXLowQ": threshXLowQ,
                                    "tReselectionEutran": tReselectionEutran,
                                    "tReselectionNRSfHigh": tReselectionNRSfHigh,
                                    "tReselectionNRSfMedium": tReselectionNRSfMedium,
                                    "eUTranFrequencyRef": eUTranFrequencyRef,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["cellIndividualOffset"]) -> 'CellIndividualOffset': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["blackListEntry"]) -> MetaOapg.properties.blackListEntry: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["blackListEntryIdleMode"]) -> MetaOapg.properties.blackListEntryIdleMode: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["cellReselectionPriority"]) -> MetaOapg.properties.cellReselectionPriority: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["cellReselectionSubPriority"]) -> MetaOapg.properties.cellReselectionSubPriority: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["pMax"]) -> MetaOapg.properties.pMax: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["qOffsetFreq"]) -> MetaOapg.properties.qOffsetFreq: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["qQualMin"]) -> MetaOapg.properties.qQualMin: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["qRxLevMin"]) -> MetaOapg.properties.qRxLevMin: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["threshXHighP"]) -> MetaOapg.properties.threshXHighP: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["threshXHighQ"]) -> MetaOapg.properties.threshXHighQ: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["threshXLowP"]) -> MetaOapg.properties.threshXLowP: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["threshXLowQ"]) -> MetaOapg.properties.threshXLowQ: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["tReselectionEutran"]) -> MetaOapg.properties.tReselectionEutran: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["tReselectionNRSfHigh"]) -> 'TReselectionNRSf': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["tReselectionNRSfMedium"]) -> 'TReselectionNRSf': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["eUTranFrequencyRef"]) -> MetaOapg.properties.eUTranFrequencyRef: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["cellIndividualOffset", "blackListEntry", "blackListEntryIdleMode", "cellReselectionPriority", "cellReselectionSubPriority", "pMax", "qOffsetFreq", "qQualMin", "qRxLevMin", "threshXHighP", "threshXHighQ", "threshXLowP", "threshXLowQ", "tReselectionEutran", "tReselectionNRSfHigh", "tReselectionNRSfMedium", "eUTranFrequencyRef", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["cellIndividualOffset"]) -> typing.Union['CellIndividualOffset', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["blackListEntry"]) -> typing.Union[MetaOapg.properties.blackListEntry, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["blackListEntryIdleMode"]) -> typing.Union[MetaOapg.properties.blackListEntryIdleMode, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["cellReselectionPriority"]) -> typing.Union[MetaOapg.properties.cellReselectionPriority, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["cellReselectionSubPriority"]) -> typing.Union[MetaOapg.properties.cellReselectionSubPriority, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["pMax"]) -> typing.Union[MetaOapg.properties.pMax, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["qOffsetFreq"]) -> typing.Union[MetaOapg.properties.qOffsetFreq, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["qQualMin"]) -> typing.Union[MetaOapg.properties.qQualMin, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["qRxLevMin"]) -> typing.Union[MetaOapg.properties.qRxLevMin, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["threshXHighP"]) -> typing.Union[MetaOapg.properties.threshXHighP, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["threshXHighQ"]) -> typing.Union[MetaOapg.properties.threshXHighQ, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["threshXLowP"]) -> typing.Union[MetaOapg.properties.threshXLowP, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["threshXLowQ"]) -> typing.Union[MetaOapg.properties.threshXLowQ, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["tReselectionEutran"]) -> typing.Union[MetaOapg.properties.tReselectionEutran, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["tReselectionNRSfHigh"]) -> typing.Union['TReselectionNRSf', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["tReselectionNRSfMedium"]) -> typing.Union['TReselectionNRSf', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["eUTranFrequencyRef"]) -> typing.Union[MetaOapg.properties.eUTranFrequencyRef, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cellIndividualOffset", "blackListEntry", "blackListEntryIdleMode", "cellReselectionPriority", "cellReselectionSubPriority", "pMax", "qOffsetFreq", "qQualMin", "qRxLevMin", "threshXHighP", "threshXHighQ", "threshXLowP", "threshXLowQ", "tReselectionEutran", "tReselectionNRSfHigh", "tReselectionNRSfMedium", "eUTranFrequencyRef", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            cellIndividualOffset: typing.Union['CellIndividualOffset', schemas.Unset] = schemas.unset,
                            blackListEntry: typing.Union[MetaOapg.properties.blackListEntry, list, tuple, schemas.Unset] = schemas.unset,
                            blackListEntryIdleMode: typing.Union[MetaOapg.properties.blackListEntryIdleMode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            cellReselectionPriority: typing.Union[MetaOapg.properties.cellReselectionPriority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            cellReselectionSubPriority: typing.Union[MetaOapg.properties.cellReselectionSubPriority, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            pMax: typing.Union[MetaOapg.properties.pMax, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            qOffsetFreq: typing.Union[MetaOapg.properties.qOffsetFreq, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            qQualMin: typing.Union[MetaOapg.properties.qQualMin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            qRxLevMin: typing.Union[MetaOapg.properties.qRxLevMin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            threshXHighP: typing.Union[MetaOapg.properties.threshXHighP, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            threshXHighQ: typing.Union[MetaOapg.properties.threshXHighQ, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            threshXLowP: typing.Union[MetaOapg.properties.threshXLowP, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            threshXLowQ: typing.Union[MetaOapg.properties.threshXLowQ, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            tReselectionEutran: typing.Union[MetaOapg.properties.tReselectionEutran, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            tReselectionNRSfHigh: typing.Union['TReselectionNRSf', schemas.Unset] = schemas.unset,
                            tReselectionNRSfMedium: typing.Union['TReselectionNRSf', schemas.Unset] = schemas.unset,
                            eUTranFrequencyRef: typing.Union[MetaOapg.properties.eUTranFrequencyRef, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
                                cellIndividualOffset=cellIndividualOffset,
                                blackListEntry=blackListEntry,
                                blackListEntryIdleMode=blackListEntryIdleMode,
                                cellReselectionPriority=cellReselectionPriority,
                                cellReselectionSubPriority=cellReselectionSubPriority,
                                pMax=pMax,
                                qOffsetFreq=qOffsetFreq,
                                qQualMin=qQualMin,
                                qRxLevMin=qRxLevMin,
                                threshXHighP=threshXHighP,
                                threshXHighQ=threshXHighQ,
                                threshXLowP=threshXLowP,
                                threshXLowQ=threshXLowQ,
                                tReselectionEutran=tReselectionEutran,
                                tReselectionNRSfHigh=tReselectionNRSfHigh,
                                tReselectionNRSfMedium=tReselectionNRSfMedium,
                                eUTranFrequencyRef=eUTranFrequencyRef,
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
    ) -> 'EUtranFreqRelationSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.cell_individual_offset import CellIndividualOffset
from openapi_client.model.t_reselection_nrsf import TReselectionNRSf
from openapi_client.model.top import Top
