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


class Resources5gcNrm(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
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
                ProvMnS,
                SubNetworkSingle1,
                ManagedElementSingle1,
                AmfFunctionSingle,
                SmfFunctionSingle,
                UpfFunctionSingle,
                N3iwfFunctionSingle,
                PcfFunctionSingle,
                AusfFunctionSingle,
                UdmFunctionSingle,
                UdrFunctionSingle,
                UdsfFunctionSingle,
                NrfFunctionSingle,
                NssfFunctionSingle,
                SmsfFunctionSingle,
                LmfFunctionSingle,
                NgeirFunctionSingle,
                SeppFunctionSingle,
                NwdafFunctionSingle,
                ScpFunctionSingle,
                NefFunctionSingle,
                NsacfFunctionSingle,
                DDNMFFunctionSingle,
                ExternalAmfFunctionSingle,
                ExternalNrfFunctionSingle,
                ExternalNssfFunctionSingle,
                ExternalSeppFunctionSingle,
                AmfSetSingle,
                AmfRegionSingle,
                QFQoSMonitoringControlSingle,
                GtpUPathQoSMonitoringControlSingle,
                EPN2Single,
                EPN3Single,
                EPN4Single,
                EPN5Single,
                EPN6Single,
                EPN7Single,
                EPN8Single,
                EPN9Single,
                EPN10Single,
                EPN11Single,
                EPN12Single,
                EPN13Single,
                EPN14Single,
                EPN15Single,
                EPN16Single,
                EPN17Single,
                EPN20Single,
                EPN21Single,
                EPN22Single,
                EPN26Single,
                EPN27Single,
                EPN31Single,
                EPN32Single,
                EPN33Single,
                EPN60Single,
                EPN88Single,
                EPNpc4Single,
                EPNpc6Single,
                EPNpc7Single,
                EPNpc8Single,
                EPS5CSingle,
                EPS5USingle,
                EPRxSingle,
                EPMAPSMSCSingle,
                EPNLSSingle,
                EPNLGSingle,
                Configurable5QISetSingle,
                FiveQiDscpMappingSetSingle,
                PredefinedPccRuleSetSingle,
                Dynamic5QISetSingle,
                EASDFFunctionSingle,
                EcmConnectionInfoSingle,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Resources5gcNrm':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.amf_function_single import AmfFunctionSingle
from openapi_client.model.amf_region_single import AmfRegionSingle
from openapi_client.model.amf_set_single import AmfSetSingle
from openapi_client.model.ausf_function_single import AusfFunctionSingle
from openapi_client.model.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_client.model.ddnmf_function_single import DDNMFFunctionSingle
from openapi_client.model.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_client.model.easdf_function_single import EASDFFunctionSingle
from openapi_client.model.ecm_connection_info_single import EcmConnectionInfoSingle
from openapi_client.model.ep_npc4_single import EPNpc4Single
from openapi_client.model.ep_npc6_single import EPNpc6Single
from openapi_client.model.ep_npc7_single import EPNpc7Single
from openapi_client.model.ep_npc8_single import EPNpc8Single
from openapi_client.model.epmapsmsc_single import EPMAPSMSCSingle
from openapi_client.model.epn10_single import EPN10Single
from openapi_client.model.epn11_single import EPN11Single
from openapi_client.model.epn12_single import EPN12Single
from openapi_client.model.epn13_single import EPN13Single
from openapi_client.model.epn14_single import EPN14Single
from openapi_client.model.epn15_single import EPN15Single
from openapi_client.model.epn16_single import EPN16Single
from openapi_client.model.epn17_single import EPN17Single
from openapi_client.model.epn20_single import EPN20Single
from openapi_client.model.epn21_single import EPN21Single
from openapi_client.model.epn22_single import EPN22Single
from openapi_client.model.epn26_single import EPN26Single
from openapi_client.model.epn27_single import EPN27Single
from openapi_client.model.epn2_single import EPN2Single
from openapi_client.model.epn31_single import EPN31Single
from openapi_client.model.epn32_single import EPN32Single
from openapi_client.model.epn33_single import EPN33Single
from openapi_client.model.epn3_single import EPN3Single
from openapi_client.model.epn4_single import EPN4Single
from openapi_client.model.epn5_single import EPN5Single
from openapi_client.model.epn60_single import EPN60Single
from openapi_client.model.epn6_single import EPN6Single
from openapi_client.model.epn7_single import EPN7Single
from openapi_client.model.epn88_single import EPN88Single
from openapi_client.model.epn8_single import EPN8Single
from openapi_client.model.epn9_single import EPN9Single
from openapi_client.model.epnlg_single import EPNLGSingle
from openapi_client.model.epnls_single import EPNLSSingle
from openapi_client.model.eprx_single import EPRxSingle
from openapi_client.model.eps5_c_single import EPS5CSingle
from openapi_client.model.eps5_u_single import EPS5USingle
from openapi_client.model.external_amf_function_single import ExternalAmfFunctionSingle
from openapi_client.model.external_nrf_function_single import ExternalNrfFunctionSingle
from openapi_client.model.external_nssf_function_single import ExternalNssfFunctionSingle
from openapi_client.model.external_sepp_function_single import ExternalSeppFunctionSingle
from openapi_client.model.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle
from openapi_client.model.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle
from openapi_client.model.lmf_function_single import LmfFunctionSingle
from openapi_client.model.managed_element_single1 import ManagedElementSingle1
from openapi_client.model.n3iwf_function_single import N3iwfFunctionSingle
from openapi_client.model.nef_function_single import NefFunctionSingle
from openapi_client.model.ngeir_function_single import NgeirFunctionSingle
from openapi_client.model.nrf_function_single import NrfFunctionSingle
from openapi_client.model.nsacf_function_single import NsacfFunctionSingle
from openapi_client.model.nssf_function_single import NssfFunctionSingle
from openapi_client.model.nwdaf_function_single import NwdafFunctionSingle
from openapi_client.model.pcf_function_single import PcfFunctionSingle
from openapi_client.model.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_client.model.prov_mn_s import ProvMnS
from openapi_client.model.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle
from openapi_client.model.scp_function_single import ScpFunctionSingle
from openapi_client.model.sepp_function_single import SeppFunctionSingle
from openapi_client.model.smf_function_single import SmfFunctionSingle
from openapi_client.model.smsf_function_single import SmsfFunctionSingle
from openapi_client.model.sub_network_single1 import SubNetworkSingle1
from openapi_client.model.udm_function_single import UdmFunctionSingle
from openapi_client.model.udr_function_single import UdrFunctionSingle
from openapi_client.model.udsf_function_single import UdsfFunctionSingle
from openapi_client.model.upf_function_single import UpfFunctionSingle