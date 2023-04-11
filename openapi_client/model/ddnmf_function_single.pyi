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


class DDNMFFunctionSingle(
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
                                    
                                        @staticmethod
                                        def plmnId() -> typing.Type['PlmnId']:
                                            return PlmnId
                                        sBIFqdn = schemas.StrSchema
                                    
                                        @staticmethod
                                        def managedNFProfile() -> typing.Type['ManagedNFProfile']:
                                            return ManagedNFProfile
                                    
                                        @staticmethod
                                        def commModelList() -> typing.Type['CommModelList']:
                                            return CommModelList
                                        __annotations__ = {
                                            "plmnId": plmnId,
                                            "sBIFqdn": sBIFqdn,
                                            "managedNFProfile": managedNFProfile,
                                            "commModelList": commModelList,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["plmnId"]) -> 'PlmnId': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["sBIFqdn"]) -> MetaOapg.properties.sBIFqdn: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["managedNFProfile"]) -> 'ManagedNFProfile': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["commModelList"]) -> 'CommModelList': ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["plmnId", "sBIFqdn", "managedNFProfile", "commModelList", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["plmnId"]) -> typing.Union['PlmnId', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["sBIFqdn"]) -> typing.Union[MetaOapg.properties.sBIFqdn, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["managedNFProfile"]) -> typing.Union['ManagedNFProfile', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["commModelList"]) -> typing.Union['CommModelList', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["plmnId", "sBIFqdn", "managedNFProfile", "commModelList", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    plmnId: typing.Union['PlmnId', schemas.Unset] = schemas.unset,
                                    sBIFqdn: typing.Union[MetaOapg.properties.sBIFqdn, str, schemas.Unset] = schemas.unset,
                                    managedNFProfile: typing.Union['ManagedNFProfile', schemas.Unset] = schemas.unset,
                                    commModelList: typing.Union['CommModelList', schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        plmnId=plmnId,
                                        sBIFqdn=sBIFqdn,
                                        managedNFProfile=managedNFProfile,
                                        commModelList=commModelList,
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
                    def EP_Npc4() -> typing.Type['EPNpc4Multiple']:
                        return EPNpc4Multiple
                
                    @staticmethod
                    def EP_Npc6() -> typing.Type['EPNpc6Multiple']:
                        return EPNpc6Multiple
                
                    @staticmethod
                    def EP_Npc7() -> typing.Type['EPNpc7Multiple']:
                        return EPNpc7Multiple
                
                    @staticmethod
                    def EP_Npc8() -> typing.Type['EPNpc8Multiple']:
                        return EPNpc8Multiple
                    __annotations__ = {
                        "EP_Npc4": EP_Npc4,
                        "EP_Npc6": EP_Npc6,
                        "EP_Npc7": EP_Npc7,
                        "EP_Npc8": EP_Npc8,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_Npc4"]) -> 'EPNpc4Multiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_Npc6"]) -> 'EPNpc6Multiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_Npc7"]) -> 'EPNpc7Multiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EP_Npc8"]) -> 'EPNpc8Multiple': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["EP_Npc4", "EP_Npc6", "EP_Npc7", "EP_Npc8", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_Npc4"]) -> typing.Union['EPNpc4Multiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_Npc6"]) -> typing.Union['EPNpc6Multiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_Npc7"]) -> typing.Union['EPNpc7Multiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EP_Npc8"]) -> typing.Union['EPNpc8Multiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EP_Npc4", "EP_Npc6", "EP_Npc7", "EP_Npc8", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                EP_Npc4: typing.Union['EPNpc4Multiple', schemas.Unset] = schemas.unset,
                EP_Npc6: typing.Union['EPNpc6Multiple', schemas.Unset] = schemas.unset,
                EP_Npc7: typing.Union['EPNpc7Multiple', schemas.Unset] = schemas.unset,
                EP_Npc8: typing.Union['EPNpc8Multiple', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_3':
                return super().__new__(
                    cls,
                    *_args,
                    EP_Npc4=EP_Npc4,
                    EP_Npc6=EP_Npc6,
                    EP_Npc7=EP_Npc7,
                    EP_Npc8=EP_Npc8,
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
    ) -> 'DDNMFFunctionSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.comm_model_list import CommModelList
from openapi_client.model.ep_npc4_multiple import EPNpc4Multiple
from openapi_client.model.ep_npc6_multiple import EPNpc6Multiple
from openapi_client.model.ep_npc7_multiple import EPNpc7Multiple
from openapi_client.model.ep_npc8_multiple import EPNpc8Multiple
from openapi_client.model.managed_function_attr import ManagedFunctionAttr
from openapi_client.model.managed_function_nc_o import ManagedFunctionNcO
from openapi_client.model.managed_nf_profile import ManagedNFProfile
from openapi_client.model.plmn_id import PlmnId
from openapi_client.model.top import Top