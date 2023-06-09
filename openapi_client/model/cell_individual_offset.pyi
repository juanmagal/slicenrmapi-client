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


class CellIndividualOffset(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            rsrpOffsetSSB = schemas.IntSchema
            rsrqOffsetSSB = schemas.IntSchema
            sinrOffsetSSB = schemas.IntSchema
            rsrp_offset_csi_rs = schemas.IntSchema
            rsrq_offset_csi_rs = schemas.IntSchema
            sinr_offset_csi_rs = schemas.IntSchema
            __annotations__ = {
                "rsrpOffsetSSB": rsrpOffsetSSB,
                "rsrqOffsetSSB": rsrqOffsetSSB,
                "sinrOffsetSSB": sinrOffsetSSB,
                "rsrpOffsetCSI-RS": rsrp_offset_csi_rs,
                "rsrqOffsetCSI-RS": rsrq_offset_csi_rs,
                "sinrOffsetCSI-RS": sinr_offset_csi_rs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rsrpOffsetSSB"]) -> MetaOapg.properties.rsrpOffsetSSB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rsrqOffsetSSB"]) -> MetaOapg.properties.rsrqOffsetSSB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sinrOffsetSSB"]) -> MetaOapg.properties.sinrOffsetSSB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rsrpOffsetCSI-RS"]) -> MetaOapg.properties.rsrp_offset_csi_rs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rsrqOffsetCSI-RS"]) -> MetaOapg.properties.rsrq_offset_csi_rs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sinrOffsetCSI-RS"]) -> MetaOapg.properties.sinr_offset_csi_rs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rsrpOffsetSSB", "rsrqOffsetSSB", "sinrOffsetSSB", "rsrpOffsetCSI-RS", "rsrqOffsetCSI-RS", "sinrOffsetCSI-RS", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rsrpOffsetSSB"]) -> typing.Union[MetaOapg.properties.rsrpOffsetSSB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rsrqOffsetSSB"]) -> typing.Union[MetaOapg.properties.rsrqOffsetSSB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sinrOffsetSSB"]) -> typing.Union[MetaOapg.properties.sinrOffsetSSB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rsrpOffsetCSI-RS"]) -> typing.Union[MetaOapg.properties.rsrp_offset_csi_rs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rsrqOffsetCSI-RS"]) -> typing.Union[MetaOapg.properties.rsrq_offset_csi_rs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sinrOffsetCSI-RS"]) -> typing.Union[MetaOapg.properties.sinr_offset_csi_rs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rsrpOffsetSSB", "rsrqOffsetSSB", "sinrOffsetSSB", "rsrpOffsetCSI-RS", "rsrqOffsetCSI-RS", "sinrOffsetCSI-RS", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        rsrpOffsetSSB: typing.Union[MetaOapg.properties.rsrpOffsetSSB, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rsrqOffsetSSB: typing.Union[MetaOapg.properties.rsrqOffsetSSB, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sinrOffsetSSB: typing.Union[MetaOapg.properties.sinrOffsetSSB, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CellIndividualOffset':
        return super().__new__(
            cls,
            *_args,
            rsrpOffsetSSB=rsrpOffsetSSB,
            rsrqOffsetSSB=rsrqOffsetSSB,
            sinrOffsetSSB=sinrOffsetSSB,
            _configuration=_configuration,
            **kwargs,
        )
