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


class ProbableCause(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The value of the probable cause may be a specific standardized string, or any vendor provided string. Probable cause strings are not standardized in the present document. They may be added in a future version. Up to then the mapping of the generic probable cause strings "PROBABLE_CAUSE_001" to "PROBABLE_CAUSE_005" is vendor specific. The value of the probable cause may also be an integer. The mapping of integer values to probable causes is vendor specific.
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class any_of_0(
                    schemas.EnumBase,
                    schemas.StrSchema
                ):
                    
                    @schemas.classproperty
                    def POSITIVE_001(cls):
                        return cls("PROBABLE_CAUSE_001")
                    
                    @schemas.classproperty
                    def POSITIVE_002(cls):
                        return cls("PROBABLE_CAUSE_002")
                    
                    @schemas.classproperty
                    def POSITIVE_003(cls):
                        return cls("PROBABLE_CAUSE_003")
                    
                    @schemas.classproperty
                    def POSITIVE_004(cls):
                        return cls("PROBABLE_CAUSE_004")
                    
                    @schemas.classproperty
                    def POSITIVE_005(cls):
                        return cls("PROBABLE_CAUSE_005")
                any_of_1 = schemas.StrSchema
                
                @classmethod
                @functools.lru_cache()
                def any_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.any_of_0,
                        cls.any_of_1,
                    ]
        
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )
        one_of_1 = schemas.IntSchema
        
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
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProbableCause':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
