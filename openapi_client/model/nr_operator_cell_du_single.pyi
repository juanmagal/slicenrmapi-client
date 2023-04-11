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


class NrOperatorCellDuSingle(
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
                    cellLocalId = schemas.IntSchema
                
                    @staticmethod
                    def administrativeState() -> typing.Type['AdministrativeState']:
                        return AdministrativeState
                
                    @staticmethod
                    def plmnInfoList() -> typing.Type['PlmnInfoList']:
                        return PlmnInfoList
                
                    @staticmethod
                    def nrTac() -> typing.Type['NrTac']:
                        return NrTac
                    __annotations__ = {
                        "cellLocalId": cellLocalId,
                        "administrativeState": administrativeState,
                        "plmnInfoList": plmnInfoList,
                        "nrTac": nrTac,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cellLocalId"]) -> MetaOapg.properties.cellLocalId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["administrativeState"]) -> 'AdministrativeState': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["plmnInfoList"]) -> 'PlmnInfoList': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["nrTac"]) -> 'NrTac': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["cellLocalId", "administrativeState", "plmnInfoList", "nrTac", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cellLocalId"]) -> typing.Union[MetaOapg.properties.cellLocalId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["administrativeState"]) -> typing.Union['AdministrativeState', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["plmnInfoList"]) -> typing.Union['PlmnInfoList', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["nrTac"]) -> typing.Union['NrTac', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cellLocalId", "administrativeState", "plmnInfoList", "nrTac", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                cellLocalId: typing.Union[MetaOapg.properties.cellLocalId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                administrativeState: typing.Union['AdministrativeState', schemas.Unset] = schemas.unset,
                plmnInfoList: typing.Union['PlmnInfoList', schemas.Unset] = schemas.unset,
                nrTac: typing.Union['NrTac', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    cellLocalId=cellLocalId,
                    administrativeState=administrativeState,
                    plmnInfoList=plmnInfoList,
                    nrTac=nrTac,
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
    ) -> 'NrOperatorCellDuSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.administrative_state import AdministrativeState
from openapi_client.model.nr_tac import NrTac
from openapi_client.model.plmn_info_list import PlmnInfoList
from openapi_client.model.top import Top