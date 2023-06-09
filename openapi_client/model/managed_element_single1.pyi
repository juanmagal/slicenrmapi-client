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


class ManagedElementSingle1(
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
                                    ManagedElementAttr,
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
                    def AmfFunction() -> typing.Type['AmfFunctionMultiple']:
                        return AmfFunctionMultiple
                
                    @staticmethod
                    def SmfFunction() -> typing.Type['SmfFunctionMultiple']:
                        return SmfFunctionMultiple
                
                    @staticmethod
                    def UpfFunction() -> typing.Type['UpfFunctionMultiple']:
                        return UpfFunctionMultiple
                
                    @staticmethod
                    def N3iwfFunction() -> typing.Type['N3iwfFunctionMultiple']:
                        return N3iwfFunctionMultiple
                
                    @staticmethod
                    def PcfFunction() -> typing.Type['PcfFunctionMultiple']:
                        return PcfFunctionMultiple
                
                    @staticmethod
                    def AusfFunction() -> typing.Type['AusfFunctionMultiple']:
                        return AusfFunctionMultiple
                
                    @staticmethod
                    def UdmFunction() -> typing.Type['UdmFunctionMultiple']:
                        return UdmFunctionMultiple
                
                    @staticmethod
                    def UdrFunction() -> typing.Type['UdrFunctionMultiple']:
                        return UdrFunctionMultiple
                
                    @staticmethod
                    def UdsfFunction() -> typing.Type['UdsfFunctionMultiple']:
                        return UdsfFunctionMultiple
                
                    @staticmethod
                    def NrfFunction() -> typing.Type['NrfFunctionMultiple']:
                        return NrfFunctionMultiple
                
                    @staticmethod
                    def NssfFunction() -> typing.Type['NssfFunctionMultiple']:
                        return NssfFunctionMultiple
                
                    @staticmethod
                    def SmsfFunction() -> typing.Type['SmsfFunctionMultiple']:
                        return SmsfFunctionMultiple
                
                    @staticmethod
                    def LmfFunction() -> typing.Type['LmfFunctionMultiple']:
                        return LmfFunctionMultiple
                
                    @staticmethod
                    def NgeirFunction() -> typing.Type['NgeirFunctionMultiple']:
                        return NgeirFunctionMultiple
                
                    @staticmethod
                    def SeppFunction() -> typing.Type['SeppFunctionMultiple']:
                        return SeppFunctionMultiple
                
                    @staticmethod
                    def NwdafFunction() -> typing.Type['NwdafFunctionMultiple']:
                        return NwdafFunctionMultiple
                
                    @staticmethod
                    def ScpFunction() -> typing.Type['ScpFunctionMultiple']:
                        return ScpFunctionMultiple
                
                    @staticmethod
                    def NefFunction() -> typing.Type['NefFunctionMultiple']:
                        return NefFunctionMultiple
                
                    @staticmethod
                    def Configurable5QISet() -> typing.Type['Configurable5QISetMultiple']:
                        return Configurable5QISetMultiple
                
                    @staticmethod
                    def Dynamic5QISet() -> typing.Type['Dynamic5QISetMultiple']:
                        return Dynamic5QISetMultiple
                
                    @staticmethod
                    def EcmConnectionInfo() -> typing.Type['EcmConnectionInfoMultiple']:
                        return EcmConnectionInfoMultiple
                
                    @staticmethod
                    def EASDFFunction() -> typing.Type['EASDFFunctionMultiple']:
                        return EASDFFunctionMultiple
                    __annotations__ = {
                        "AmfFunction": AmfFunction,
                        "SmfFunction": SmfFunction,
                        "UpfFunction": UpfFunction,
                        "N3iwfFunction": N3iwfFunction,
                        "PcfFunction": PcfFunction,
                        "AusfFunction": AusfFunction,
                        "UdmFunction": UdmFunction,
                        "UdrFunction": UdrFunction,
                        "UdsfFunction": UdsfFunction,
                        "NrfFunction": NrfFunction,
                        "NssfFunction": NssfFunction,
                        "SmsfFunction": SmsfFunction,
                        "LmfFunction": LmfFunction,
                        "NgeirFunction": NgeirFunction,
                        "SeppFunction": SeppFunction,
                        "NwdafFunction": NwdafFunction,
                        "ScpFunction": ScpFunction,
                        "NefFunction": NefFunction,
                        "Configurable5QISet": Configurable5QISet,
                        "Dynamic5QISet": Dynamic5QISet,
                        "EcmConnectionInfo": EcmConnectionInfo,
                        "EASDFFunction": EASDFFunction,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AmfFunction"]) -> 'AmfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["SmfFunction"]) -> 'SmfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["UpfFunction"]) -> 'UpfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["N3iwfFunction"]) -> 'N3iwfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["PcfFunction"]) -> 'PcfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["AusfFunction"]) -> 'AusfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["UdmFunction"]) -> 'UdmFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["UdrFunction"]) -> 'UdrFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["UdsfFunction"]) -> 'UdsfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["NrfFunction"]) -> 'NrfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["NssfFunction"]) -> 'NssfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["SmsfFunction"]) -> 'SmsfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["LmfFunction"]) -> 'LmfFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["NgeirFunction"]) -> 'NgeirFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["SeppFunction"]) -> 'SeppFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["NwdafFunction"]) -> 'NwdafFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ScpFunction"]) -> 'ScpFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["NefFunction"]) -> 'NefFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Configurable5QISet"]) -> 'Configurable5QISetMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Dynamic5QISet"]) -> 'Dynamic5QISetMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EcmConnectionInfo"]) -> 'EcmConnectionInfoMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EASDFFunction"]) -> 'EASDFFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["AmfFunction", "SmfFunction", "UpfFunction", "N3iwfFunction", "PcfFunction", "AusfFunction", "UdmFunction", "UdrFunction", "UdsfFunction", "NrfFunction", "NssfFunction", "SmsfFunction", "LmfFunction", "NgeirFunction", "SeppFunction", "NwdafFunction", "ScpFunction", "NefFunction", "Configurable5QISet", "Dynamic5QISet", "EcmConnectionInfo", "EASDFFunction", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AmfFunction"]) -> typing.Union['AmfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["SmfFunction"]) -> typing.Union['SmfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["UpfFunction"]) -> typing.Union['UpfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["N3iwfFunction"]) -> typing.Union['N3iwfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["PcfFunction"]) -> typing.Union['PcfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["AusfFunction"]) -> typing.Union['AusfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["UdmFunction"]) -> typing.Union['UdmFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["UdrFunction"]) -> typing.Union['UdrFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["UdsfFunction"]) -> typing.Union['UdsfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["NrfFunction"]) -> typing.Union['NrfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["NssfFunction"]) -> typing.Union['NssfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["SmsfFunction"]) -> typing.Union['SmsfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["LmfFunction"]) -> typing.Union['LmfFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["NgeirFunction"]) -> typing.Union['NgeirFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["SeppFunction"]) -> typing.Union['SeppFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["NwdafFunction"]) -> typing.Union['NwdafFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ScpFunction"]) -> typing.Union['ScpFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["NefFunction"]) -> typing.Union['NefFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Configurable5QISet"]) -> typing.Union['Configurable5QISetMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Dynamic5QISet"]) -> typing.Union['Dynamic5QISetMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EcmConnectionInfo"]) -> typing.Union['EcmConnectionInfoMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EASDFFunction"]) -> typing.Union['EASDFFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AmfFunction", "SmfFunction", "UpfFunction", "N3iwfFunction", "PcfFunction", "AusfFunction", "UdmFunction", "UdrFunction", "UdsfFunction", "NrfFunction", "NssfFunction", "SmsfFunction", "LmfFunction", "NgeirFunction", "SeppFunction", "NwdafFunction", "ScpFunction", "NefFunction", "Configurable5QISet", "Dynamic5QISet", "EcmConnectionInfo", "EASDFFunction", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                AmfFunction: typing.Union['AmfFunctionMultiple', schemas.Unset] = schemas.unset,
                SmfFunction: typing.Union['SmfFunctionMultiple', schemas.Unset] = schemas.unset,
                UpfFunction: typing.Union['UpfFunctionMultiple', schemas.Unset] = schemas.unset,
                N3iwfFunction: typing.Union['N3iwfFunctionMultiple', schemas.Unset] = schemas.unset,
                PcfFunction: typing.Union['PcfFunctionMultiple', schemas.Unset] = schemas.unset,
                AusfFunction: typing.Union['AusfFunctionMultiple', schemas.Unset] = schemas.unset,
                UdmFunction: typing.Union['UdmFunctionMultiple', schemas.Unset] = schemas.unset,
                UdrFunction: typing.Union['UdrFunctionMultiple', schemas.Unset] = schemas.unset,
                UdsfFunction: typing.Union['UdsfFunctionMultiple', schemas.Unset] = schemas.unset,
                NrfFunction: typing.Union['NrfFunctionMultiple', schemas.Unset] = schemas.unset,
                NssfFunction: typing.Union['NssfFunctionMultiple', schemas.Unset] = schemas.unset,
                SmsfFunction: typing.Union['SmsfFunctionMultiple', schemas.Unset] = schemas.unset,
                LmfFunction: typing.Union['LmfFunctionMultiple', schemas.Unset] = schemas.unset,
                NgeirFunction: typing.Union['NgeirFunctionMultiple', schemas.Unset] = schemas.unset,
                SeppFunction: typing.Union['SeppFunctionMultiple', schemas.Unset] = schemas.unset,
                NwdafFunction: typing.Union['NwdafFunctionMultiple', schemas.Unset] = schemas.unset,
                ScpFunction: typing.Union['ScpFunctionMultiple', schemas.Unset] = schemas.unset,
                NefFunction: typing.Union['NefFunctionMultiple', schemas.Unset] = schemas.unset,
                Configurable5QISet: typing.Union['Configurable5QISetMultiple', schemas.Unset] = schemas.unset,
                Dynamic5QISet: typing.Union['Dynamic5QISetMultiple', schemas.Unset] = schemas.unset,
                EcmConnectionInfo: typing.Union['EcmConnectionInfoMultiple', schemas.Unset] = schemas.unset,
                EASDFFunction: typing.Union['EASDFFunctionMultiple', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_3':
                return super().__new__(
                    cls,
                    *_args,
                    AmfFunction=AmfFunction,
                    SmfFunction=SmfFunction,
                    UpfFunction=UpfFunction,
                    N3iwfFunction=N3iwfFunction,
                    PcfFunction=PcfFunction,
                    AusfFunction=AusfFunction,
                    UdmFunction=UdmFunction,
                    UdrFunction=UdrFunction,
                    UdsfFunction=UdsfFunction,
                    NrfFunction=NrfFunction,
                    NssfFunction=NssfFunction,
                    SmsfFunction=SmsfFunction,
                    LmfFunction=LmfFunction,
                    NgeirFunction=NgeirFunction,
                    SeppFunction=SeppFunction,
                    NwdafFunction=NwdafFunction,
                    ScpFunction=ScpFunction,
                    NefFunction=NefFunction,
                    Configurable5QISet=Configurable5QISet,
                    Dynamic5QISet=Dynamic5QISet,
                    EcmConnectionInfo=EcmConnectionInfo,
                    EASDFFunction=EASDFFunction,
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
                ManagedElementNcO,
                cls.all_of_3,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManagedElementSingle1':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.amf_function_multiple import AmfFunctionMultiple
from openapi_client.model.ausf_function_multiple import AusfFunctionMultiple
from openapi_client.model.configurable5_qi_set_multiple import Configurable5QISetMultiple
from openapi_client.model.dynamic5_qi_set_multiple import Dynamic5QISetMultiple
from openapi_client.model.easdf_function_multiple import EASDFFunctionMultiple
from openapi_client.model.ecm_connection_info_multiple import EcmConnectionInfoMultiple
from openapi_client.model.lmf_function_multiple import LmfFunctionMultiple
from openapi_client.model.managed_element_attr import ManagedElementAttr
from openapi_client.model.managed_element_nc_o import ManagedElementNcO
from openapi_client.model.n3iwf_function_multiple import N3iwfFunctionMultiple
from openapi_client.model.nef_function_multiple import NefFunctionMultiple
from openapi_client.model.ngeir_function_multiple import NgeirFunctionMultiple
from openapi_client.model.nrf_function_multiple import NrfFunctionMultiple
from openapi_client.model.nssf_function_multiple import NssfFunctionMultiple
from openapi_client.model.nwdaf_function_multiple import NwdafFunctionMultiple
from openapi_client.model.pcf_function_multiple import PcfFunctionMultiple
from openapi_client.model.scp_function_multiple import ScpFunctionMultiple
from openapi_client.model.sepp_function_multiple import SeppFunctionMultiple
from openapi_client.model.smf_function_multiple import SmfFunctionMultiple
from openapi_client.model.smsf_function_multiple import SmsfFunctionMultiple
from openapi_client.model.top import Top
from openapi_client.model.udm_function_multiple import UdmFunctionMultiple
from openapi_client.model.udr_function_multiple import UdrFunctionMultiple
from openapi_client.model.udsf_function_multiple import UdsfFunctionMultiple
from openapi_client.model.upf_function_multiple import UpfFunctionMultiple
