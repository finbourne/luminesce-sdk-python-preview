# WriterDesign

Representation of a \"designable Query for a writer\" suitable for formatting to SQL or being built from compliant SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | Original SQL that started this off | 
**available_to_map_from** | [**list[ExpressionWithAlias]**](ExpressionWithAlias.md) | The data able to be mapped from as derived from the Sql | [optional] 
**parameter** | [**AvailableParameter**](AvailableParameter.md) |  | [optional] 
**available_parameters** | [**list[AvailableParameter]**](AvailableParameter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


