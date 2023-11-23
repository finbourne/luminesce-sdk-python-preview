# ConvertToViewData

Representation of view data where will template the data into a 'create view' sql

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | view query | 
**name** | **str** | Name of view | 
**description** | **str** | Description of view | [optional] 
**documentation_link** | **str** | Documentation link | [optional] 
**view_parameters** | [**list[ViewParameter]**](ViewParameter.md) | View parameters | [optional] 
**other_parameters** | **dict(str, str)** | Other parameters not explicitly handled by the ConvertToView generation.  These will be populated by the \&quot;From SQL\&quot; and should simply be returned by  the web GUI should the user edit / update / regenerate | [optional] 
**starting_variable_name** | **str** | Which variable the this start with, null if not started from a full Create View Sql Statement. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


