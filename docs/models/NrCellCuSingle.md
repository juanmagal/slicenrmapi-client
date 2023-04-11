# openapi_client.model.nr_cell_cu_single.NrCellCuSingle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Top](Top.md) | [**Top**](Top.md) | [**Top**](Top.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[ManagedFunctionNcO](ManagedFunctionNcO.md) | [**ManagedFunctionNcO**](ManagedFunctionNcO.md) | [**ManagedFunctionNcO**](ManagedFunctionNcO.md) |  | 
[all_of_3](#all_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attributes](#attributes)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ManagedFunctionAttr](ManagedFunctionAttr.md) | [**ManagedFunctionAttr**](ManagedFunctionAttr.md) | [**ManagedFunctionAttr**](ManagedFunctionAttr.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cellLocalId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**plmnInfoList** | [**PlmnInfoList**](PlmnInfoList.md) | [**PlmnInfoList**](PlmnInfoList.md) |  | [optional] 
**nRFrequencyRef** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**RRMPolicyRatio** | [**RRMPolicyRatioMultiple**](RRMPolicyRatioMultiple.md) | [**RRMPolicyRatioMultiple**](RRMPolicyRatioMultiple.md) |  | [optional] 
**NRCellRelation** | [**NRCellRelationMultiple**](NRCellRelationMultiple.md) | [**NRCellRelationMultiple**](NRCellRelationMultiple.md) |  | [optional] 
**EUtranCellRelation** | [**EUtranCellRelationMultiple**](EUtranCellRelationMultiple.md) | [**EUtranCellRelationMultiple**](EUtranCellRelationMultiple.md) |  | [optional] 
**NRFreqRelation** | [**NRFreqRelationMultiple**](NRFreqRelationMultiple.md) | [**NRFreqRelationMultiple**](NRFreqRelationMultiple.md) |  | [optional] 
**EUtranFreqRelation** | [**EUtranFreqRelationMultiple**](EUtranFreqRelationMultiple.md) | [**EUtranFreqRelationMultiple**](EUtranFreqRelationMultiple.md) |  | [optional] 
**DESManagementFunction** | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) |  | [optional] 
**DMROFunction** | [**DMROFunctionSingle**](DMROFunctionSingle.md) | [**DMROFunctionSingle**](DMROFunctionSingle.md) |  | [optional] 
**DLBOFunction** | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) |  | [optional] 
**CESManagementFunction** | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) |  | [optional] 
**DPCIConfigurationFunction** | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
