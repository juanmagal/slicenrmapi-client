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


class FileSingle(
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
                                fileLocation = schemas.StrSchema
                                fileCompression = schemas.StrSchema
                                fileSize = schemas.IntSchema
                                
                                
                                class fileDataType(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                    
                                    @schemas.classproperty
                                    def PERFORMANCE(cls):
                                        return cls("PERFORMANCE")
                                    
                                    @schemas.classproperty
                                    def TRACE(cls):
                                        return cls("TRACE")
                                    
                                    @schemas.classproperty
                                    def ANALYTICS(cls):
                                        return cls("ANALYTICS")
                                    
                                    @schemas.classproperty
                                    def PROPRIETARY(cls):
                                        return cls("PROPRIETARY")
                                fileFormat = schemas.StrSchema
                                fileReadyTime = schemas.DateTimeSchema
                                fileExpirationTime = schemas.DateTimeSchema
                                fileContent = schemas.StrSchema
                                jobRef = schemas.StrSchema
                                jobId = schemas.StrSchema
                                __annotations__ = {
                                    "fileLocation": fileLocation,
                                    "fileCompression": fileCompression,
                                    "fileSize": fileSize,
                                    "fileDataType": fileDataType,
                                    "fileFormat": fileFormat,
                                    "fileReadyTime": fileReadyTime,
                                    "fileExpirationTime": fileExpirationTime,
                                    "fileContent": fileContent,
                                    "jobRef": jobRef,
                                    "jobId": jobId,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileLocation"]) -> MetaOapg.properties.fileLocation: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileCompression"]) -> MetaOapg.properties.fileCompression: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileSize"]) -> MetaOapg.properties.fileSize: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileDataType"]) -> MetaOapg.properties.fileDataType: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileFormat"]) -> MetaOapg.properties.fileFormat: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileReadyTime"]) -> MetaOapg.properties.fileReadyTime: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileExpirationTime"]) -> MetaOapg.properties.fileExpirationTime: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["fileContent"]) -> MetaOapg.properties.fileContent: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["jobRef"]) -> MetaOapg.properties.jobRef: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileLocation", "fileCompression", "fileSize", "fileDataType", "fileFormat", "fileReadyTime", "fileExpirationTime", "fileContent", "jobRef", "jobId", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileLocation"]) -> typing.Union[MetaOapg.properties.fileLocation, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileCompression"]) -> typing.Union[MetaOapg.properties.fileCompression, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileSize"]) -> typing.Union[MetaOapg.properties.fileSize, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileDataType"]) -> typing.Union[MetaOapg.properties.fileDataType, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileFormat"]) -> typing.Union[MetaOapg.properties.fileFormat, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileReadyTime"]) -> typing.Union[MetaOapg.properties.fileReadyTime, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileExpirationTime"]) -> typing.Union[MetaOapg.properties.fileExpirationTime, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["fileContent"]) -> typing.Union[MetaOapg.properties.fileContent, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["jobRef"]) -> typing.Union[MetaOapg.properties.jobRef, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> typing.Union[MetaOapg.properties.jobId, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileLocation", "fileCompression", "fileSize", "fileDataType", "fileFormat", "fileReadyTime", "fileExpirationTime", "fileContent", "jobRef", "jobId", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            fileLocation: typing.Union[MetaOapg.properties.fileLocation, str, schemas.Unset] = schemas.unset,
                            fileCompression: typing.Union[MetaOapg.properties.fileCompression, str, schemas.Unset] = schemas.unset,
                            fileSize: typing.Union[MetaOapg.properties.fileSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            fileDataType: typing.Union[MetaOapg.properties.fileDataType, str, schemas.Unset] = schemas.unset,
                            fileFormat: typing.Union[MetaOapg.properties.fileFormat, str, schemas.Unset] = schemas.unset,
                            fileReadyTime: typing.Union[MetaOapg.properties.fileReadyTime, str, datetime, schemas.Unset] = schemas.unset,
                            fileExpirationTime: typing.Union[MetaOapg.properties.fileExpirationTime, str, datetime, schemas.Unset] = schemas.unset,
                            fileContent: typing.Union[MetaOapg.properties.fileContent, str, schemas.Unset] = schemas.unset,
                            jobRef: typing.Union[MetaOapg.properties.jobRef, str, schemas.Unset] = schemas.unset,
                            jobId: typing.Union[MetaOapg.properties.jobId, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
                                fileLocation=fileLocation,
                                fileCompression=fileCompression,
                                fileSize=fileSize,
                                fileDataType=fileDataType,
                                fileFormat=fileFormat,
                                fileReadyTime=fileReadyTime,
                                fileExpirationTime=fileExpirationTime,
                                fileContent=fileContent,
                                jobRef=jobRef,
                                jobId=jobId,
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
    ) -> 'FileSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.top import Top
