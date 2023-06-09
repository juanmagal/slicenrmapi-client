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


class ReportingCtrl(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    fileReportingPeriod = schemas.IntSchema
                    __annotations__ = {
                        "fileReportingPeriod": fileReportingPeriod,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileReportingPeriod"]) -> MetaOapg.properties.fileReportingPeriod: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileReportingPeriod", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileReportingPeriod"]) -> typing.Union[MetaOapg.properties.fileReportingPeriod, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileReportingPeriod", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                fileReportingPeriod: typing.Union[MetaOapg.properties.fileReportingPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    fileReportingPeriod=fileReportingPeriod,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    fileReportingPeriod = schemas.IntSchema
                    fileLocation = schemas.StrSchema
                    __annotations__ = {
                        "fileReportingPeriod": fileReportingPeriod,
                        "fileLocation": fileLocation,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileReportingPeriod"]) -> MetaOapg.properties.fileReportingPeriod: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fileLocation"]) -> MetaOapg.properties.fileLocation: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileReportingPeriod", "fileLocation", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileReportingPeriod"]) -> typing.Union[MetaOapg.properties.fileReportingPeriod, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fileLocation"]) -> typing.Union[MetaOapg.properties.fileLocation, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileReportingPeriod", "fileLocation", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                fileReportingPeriod: typing.Union[MetaOapg.properties.fileReportingPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                fileLocation: typing.Union[MetaOapg.properties.fileLocation, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    fileReportingPeriod=fileReportingPeriod,
                    fileLocation=fileLocation,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    streamTarget = schemas.StrSchema
                    __annotations__ = {
                        "streamTarget": streamTarget,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["streamTarget"]) -> MetaOapg.properties.streamTarget: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["streamTarget", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["streamTarget"]) -> typing.Union[MetaOapg.properties.streamTarget, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["streamTarget", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                streamTarget: typing.Union[MetaOapg.properties.streamTarget, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_2':
                return super().__new__(
                    cls,
                    *_args,
                    streamTarget=streamTarget,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
                cls.one_of_2,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportingCtrl':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
