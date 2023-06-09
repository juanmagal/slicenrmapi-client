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


class VsDataContainerSingle(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        vsDataType = schemas.StrSchema
                        vsDataFormatVersion = schemas.StrSchema
                        vsData = schemas.AnyTypeSchema
                        __annotations__ = {
                            "vsDataType": vsDataType,
                            "vsDataFormatVersion": vsDataFormatVersion,
                            "vsData": vsData,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["vsDataType"]) -> MetaOapg.properties.vsDataType: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["vsDataFormatVersion"]) -> MetaOapg.properties.vsDataFormatVersion: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["vsData"]) -> MetaOapg.properties.vsData: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["vsDataType", "vsDataFormatVersion", "vsData", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["vsDataType"]) -> typing.Union[MetaOapg.properties.vsDataType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["vsDataFormatVersion"]) -> typing.Union[MetaOapg.properties.vsDataFormatVersion, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["vsData"]) -> typing.Union[MetaOapg.properties.vsData, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vsDataType", "vsDataFormatVersion", "vsData", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    vsDataType: typing.Union[MetaOapg.properties.vsDataType, str, schemas.Unset] = schemas.unset,
                    vsDataFormatVersion: typing.Union[MetaOapg.properties.vsDataFormatVersion, str, schemas.Unset] = schemas.unset,
                    vsData: typing.Union[MetaOapg.properties.vsData, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        vsDataType=vsDataType,
                        vsDataFormatVersion=vsDataFormatVersion,
                        vsData=vsData,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def VsDataContainer() -> typing.Type['VsDataContainerMultiple']:
                return VsDataContainerMultiple
            __annotations__ = {
                "id": id,
                "attributes": attributes,
                "VsDataContainer": VsDataContainer,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["VsDataContainer"]) -> 'VsDataContainerMultiple': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "attributes", "VsDataContainer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["VsDataContainer"]) -> typing.Union['VsDataContainerMultiple', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "attributes", "VsDataContainer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        VsDataContainer: typing.Union['VsDataContainerMultiple', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VsDataContainerSingle':
        return super().__new__(
            cls,
            *_args,
            id=id,
            attributes=attributes,
            VsDataContainer=VsDataContainer,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.vs_data_container_multiple import VsDataContainerMultiple
