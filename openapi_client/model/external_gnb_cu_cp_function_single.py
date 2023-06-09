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


class ExternalGnbCuCpFunctionSingle(
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
                            
                            
                            class all_of_1(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        gnbId = schemas.StrSchema
                                    
                                        @staticmethod
                                        def gnbIdLength() -> typing.Type['GnbIdLength']:
                                            return GnbIdLength
                                    
                                        @staticmethod
                                        def plmnId() -> typing.Type['PlmnId']:
                                            return PlmnId
                                        __annotations__ = {
                                            "gnbId": gnbId,
                                            "gnbIdLength": gnbIdLength,
                                            "plmnId": plmnId,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gnbId"]) -> MetaOapg.properties.gnbId: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gnbIdLength"]) -> 'GnbIdLength': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["plmnId"]) -> 'PlmnId': ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["gnbId", "gnbIdLength", "plmnId", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gnbId"]) -> typing.Union[MetaOapg.properties.gnbId, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gnbIdLength"]) -> typing.Union['GnbIdLength', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["plmnId"]) -> typing.Union['PlmnId', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gnbId", "gnbIdLength", "plmnId", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    gnbId: typing.Union[MetaOapg.properties.gnbId, str, schemas.Unset] = schemas.unset,
                                    gnbIdLength: typing.Union['GnbIdLength', schemas.Unset] = schemas.unset,
                                    plmnId: typing.Union['PlmnId', schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        gnbId=gnbId,
                                        gnbIdLength=gnbIdLength,
                                        plmnId=plmnId,
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
                                    ManagedFunctionAttr,
                                    cls.all_of_1,
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
        
        
        class all_of_3(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def ExternalNrCellCu() -> typing.Type['ExternalNrCellCuMultiple']:
                        return ExternalNrCellCuMultiple
                
                    @staticmethod
                    def EP_XnC() -> typing.Type['EPXnCMultiple']:
                        return EPXnCMultiple
                
                    @staticmethod
                    def EP_E1() -> typing.Type['EPE1Multiple']:
                        return EPE1Multiple
                
                    @staticmethod
                    def EP_F1C() -> typing.Type['EPF1CMultiple']:
                        return EPF1CMultiple
                    __annotations__ = {
                        "ExternalNrCellCu": ExternalNrCellCu,
                        "EP_XnC": EP_XnC,
                        "EP_E1": EP_E1,
                        "EP_F1C": EP_F1C,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ExternalNrCellCu"]) -> 'ExternalNrCellCuMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_XnC"]) -> 'EPXnCMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_E1"]) -> 'EPE1Multiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_F1C"]) -> 'EPF1CMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["ExternalNrCellCu", "EP_XnC", "EP_E1", "EP_F1C", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ExternalNrCellCu"]) -> typing.Union['ExternalNrCellCuMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_XnC"]) -> typing.Union['EPXnCMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_E1"]) -> typing.Union['EPE1Multiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_F1C"]) -> typing.Union['EPF1CMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ExternalNrCellCu", "EP_XnC", "EP_E1", "EP_F1C", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                ExternalNrCellCu: typing.Union['ExternalNrCellCuMultiple', schemas.Unset] = schemas.unset,
                EP_XnC: typing.Union['EPXnCMultiple', schemas.Unset] = schemas.unset,
                EP_E1: typing.Union['EPE1Multiple', schemas.Unset] = schemas.unset,
                EP_F1C: typing.Union['EPF1CMultiple', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_3':
                return super().__new__(
                    cls,
                    *_args,
                    ExternalNrCellCu=ExternalNrCellCu,
                    EP_XnC=EP_XnC,
                    EP_E1=EP_E1,
                    EP_F1C=EP_F1C,
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
                ManagedFunctionNcO,
                cls.all_of_3,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExternalGnbCuCpFunctionSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.epe1_multiple import EPE1Multiple
from openapi_client.model.epf1_c_multiple import EPF1CMultiple
from openapi_client.model.epxn_c_multiple import EPXnCMultiple
from openapi_client.model.external_nr_cell_cu_multiple import ExternalNrCellCuMultiple
from openapi_client.model.gnb_id_length import GnbIdLength
from openapi_client.model.managed_function_attr import ManagedFunctionAttr
from openapi_client.model.managed_function_nc_o import ManagedFunctionNcO
from openapi_client.model.plmn_id import PlmnId
from openapi_client.model.top import Top
