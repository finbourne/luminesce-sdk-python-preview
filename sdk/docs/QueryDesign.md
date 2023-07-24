# QueryDesign

Representation of a \"designable Query\" suitable for formatting to SQL or being built from compliant SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | Name of the table being designed | 
**alias** | **str** | Alias for the table in the generated SQL, if any | [optional] 
**fields** | [**list[FieldDesign]**](FieldDesign.md) | Fields to be selected, aggregated over and/or filtered on | 
**order_by** | [**list[OrderByTermDesign]**](OrderByTermDesign.md) | Order By clauses to apply | [optional] 
**limit** | **int** | Row limit to apply, if any | [optional] 
**warnings** | **list[str]** | Any warnings to show the user when converting from SQL to this representation | [optional] 
**available_fields** | [**list[AvailableField]**](AvailableField.md) | Fields that are known to be available for design when parsing SQL | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


