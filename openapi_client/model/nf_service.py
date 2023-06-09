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


class NFService(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    NF Service is defined in TS 29.510
    """


    class MetaOapg:
        
        class properties:
            serviceInstanceId = schemas.StrSchema
            serviceName = schemas.StrSchema
            version = schemas.StrSchema
            schema = schemas.StrSchema
            fqdn = schemas.StrSchema
            interPlmnFqdn = schemas.StrSchema
            
            
            class ipEndPoints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IpEndPoint']:
                        return IpEndPoint
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['IpEndPoint'], typing.List['IpEndPoint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ipEndPoints':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IpEndPoint':
                    return super().__getitem__(i)
            apiPrfix = schemas.StrSchema
        
            @staticmethod
            def allowedPlmns() -> typing.Type['PlmnId']:
                return PlmnId
            
            
            class allowedNfTypes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NFType']:
                        return NFType
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NFType'], typing.List['NFType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'allowedNfTypes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NFType':
                    return super().__getitem__(i)
            
            
            class allowedNssais(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Snssai']:
                        return Snssai
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Snssai'], typing.List['Snssai']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'allowedNssais':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Snssai':
                    return super().__getitem__(i)
            __annotations__ = {
                "serviceInstanceId": serviceInstanceId,
                "serviceName": serviceName,
                "version": version,
                "schema": schema,
                "fqdn": fqdn,
                "interPlmnFqdn": interPlmnFqdn,
                "ipEndPoints": ipEndPoints,
                "apiPrfix": apiPrfix,
                "allowedPlmns": allowedPlmns,
                "allowedNfTypes": allowedNfTypes,
                "allowedNssais": allowedNssais,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceInstanceId"]) -> MetaOapg.properties.serviceInstanceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceName"]) -> MetaOapg.properties.serviceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interPlmnFqdn"]) -> MetaOapg.properties.interPlmnFqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipEndPoints"]) -> MetaOapg.properties.ipEndPoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiPrfix"]) -> MetaOapg.properties.apiPrfix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedPlmns"]) -> 'PlmnId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedNfTypes"]) -> MetaOapg.properties.allowedNfTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedNssais"]) -> MetaOapg.properties.allowedNssais: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["serviceInstanceId", "serviceName", "version", "schema", "fqdn", "interPlmnFqdn", "ipEndPoints", "apiPrfix", "allowedPlmns", "allowedNfTypes", "allowedNssais", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceInstanceId"]) -> typing.Union[MetaOapg.properties.serviceInstanceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceName"]) -> typing.Union[MetaOapg.properties.serviceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> typing.Union[MetaOapg.properties.schema, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fqdn"]) -> typing.Union[MetaOapg.properties.fqdn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interPlmnFqdn"]) -> typing.Union[MetaOapg.properties.interPlmnFqdn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipEndPoints"]) -> typing.Union[MetaOapg.properties.ipEndPoints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiPrfix"]) -> typing.Union[MetaOapg.properties.apiPrfix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedPlmns"]) -> typing.Union['PlmnId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedNfTypes"]) -> typing.Union[MetaOapg.properties.allowedNfTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedNssais"]) -> typing.Union[MetaOapg.properties.allowedNssais, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["serviceInstanceId", "serviceName", "version", "schema", "fqdn", "interPlmnFqdn", "ipEndPoints", "apiPrfix", "allowedPlmns", "allowedNfTypes", "allowedNssais", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        serviceInstanceId: typing.Union[MetaOapg.properties.serviceInstanceId, str, schemas.Unset] = schemas.unset,
        serviceName: typing.Union[MetaOapg.properties.serviceName, str, schemas.Unset] = schemas.unset,
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        schema: typing.Union[MetaOapg.properties.schema, str, schemas.Unset] = schemas.unset,
        fqdn: typing.Union[MetaOapg.properties.fqdn, str, schemas.Unset] = schemas.unset,
        interPlmnFqdn: typing.Union[MetaOapg.properties.interPlmnFqdn, str, schemas.Unset] = schemas.unset,
        ipEndPoints: typing.Union[MetaOapg.properties.ipEndPoints, list, tuple, schemas.Unset] = schemas.unset,
        apiPrfix: typing.Union[MetaOapg.properties.apiPrfix, str, schemas.Unset] = schemas.unset,
        allowedPlmns: typing.Union['PlmnId', schemas.Unset] = schemas.unset,
        allowedNfTypes: typing.Union[MetaOapg.properties.allowedNfTypes, list, tuple, schemas.Unset] = schemas.unset,
        allowedNssais: typing.Union[MetaOapg.properties.allowedNssais, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NFService':
        return super().__new__(
            cls,
            *_args,
            serviceInstanceId=serviceInstanceId,
            serviceName=serviceName,
            version=version,
            schema=schema,
            fqdn=fqdn,
            interPlmnFqdn=interPlmnFqdn,
            ipEndPoints=ipEndPoints,
            apiPrfix=apiPrfix,
            allowedPlmns=allowedPlmns,
            allowedNfTypes=allowedNfTypes,
            allowedNssais=allowedNssais,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.ip_end_point import IpEndPoint
from openapi_client.model.nf_type import NFType
from openapi_client.model.plmn_id import PlmnId
from openapi_client.model.snssai import Snssai
