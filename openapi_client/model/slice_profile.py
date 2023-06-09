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


class SliceProfile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            serviceProfileId = schemas.StrSchema
        
            @staticmethod
            def plmnInfoList() -> typing.Type['PlmnInfoList']:
                return PlmnInfoList
        
            @staticmethod
            def cNSliceSubnetProfile() -> typing.Type['CNSliceSubnetProfile']:
                return CNSliceSubnetProfile
        
            @staticmethod
            def rANSliceSubnetProfile() -> typing.Type['RANSliceSubnetProfile']:
                return RANSliceSubnetProfile
        
            @staticmethod
            def topSliceSubnetProfile() -> typing.Type['TopSliceSubnetProfile']:
                return TopSliceSubnetProfile
            __annotations__ = {
                "serviceProfileId": serviceProfileId,
                "plmnInfoList": plmnInfoList,
                "cNSliceSubnetProfile": cNSliceSubnetProfile,
                "rANSliceSubnetProfile": rANSliceSubnetProfile,
                "topSliceSubnetProfile": topSliceSubnetProfile,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceProfileId"]) -> MetaOapg.properties.serviceProfileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plmnInfoList"]) -> 'PlmnInfoList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cNSliceSubnetProfile"]) -> 'CNSliceSubnetProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rANSliceSubnetProfile"]) -> 'RANSliceSubnetProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topSliceSubnetProfile"]) -> 'TopSliceSubnetProfile': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["serviceProfileId", "plmnInfoList", "cNSliceSubnetProfile", "rANSliceSubnetProfile", "topSliceSubnetProfile", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceProfileId"]) -> typing.Union[MetaOapg.properties.serviceProfileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plmnInfoList"]) -> typing.Union['PlmnInfoList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cNSliceSubnetProfile"]) -> typing.Union['CNSliceSubnetProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rANSliceSubnetProfile"]) -> typing.Union['RANSliceSubnetProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topSliceSubnetProfile"]) -> typing.Union['TopSliceSubnetProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["serviceProfileId", "plmnInfoList", "cNSliceSubnetProfile", "rANSliceSubnetProfile", "topSliceSubnetProfile", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        serviceProfileId: typing.Union[MetaOapg.properties.serviceProfileId, str, schemas.Unset] = schemas.unset,
        plmnInfoList: typing.Union['PlmnInfoList', schemas.Unset] = schemas.unset,
        cNSliceSubnetProfile: typing.Union['CNSliceSubnetProfile', schemas.Unset] = schemas.unset,
        rANSliceSubnetProfile: typing.Union['RANSliceSubnetProfile', schemas.Unset] = schemas.unset,
        topSliceSubnetProfile: typing.Union['TopSliceSubnetProfile', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SliceProfile':
        return super().__new__(
            cls,
            *_args,
            serviceProfileId=serviceProfileId,
            plmnInfoList=plmnInfoList,
            cNSliceSubnetProfile=cNSliceSubnetProfile,
            rANSliceSubnetProfile=rANSliceSubnetProfile,
            topSliceSubnetProfile=topSliceSubnetProfile,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.cn_slice_subnet_profile import CNSliceSubnetProfile
from openapi_client.model.plmn_info_list import PlmnInfoList
from openapi_client.model.ran_slice_subnet_profile import RANSliceSubnetProfile
from openapi_client.model.top_slice_subnet_profile import TopSliceSubnetProfile
