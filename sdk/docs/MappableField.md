# MappableField

Information about a field that can be designed on (regardless if it currently is)  Kind of a \"mini-available catalog entry\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the field in need of mapping (The field name from within the Table Parameter itself) | [optional] 
**type** | [**DataType**](DataType.md) |  | [optional] 
**description** | **str** | Description of the field (just for rendering to the user) | [optional] 
**display_name** | **str** | Display Name of the field (just for rendering to the user) | [optional] 
**sample_values** | **str** | Example values for the field (just for rendering to the user) | [optional] 
**allowed_values** | **str** | Any set of exactly allowed values for the field (perhaps just for rendering to the user, if nothing else) | [optional] 
**mandatory_for_actions** | **str** | Which &#x60;Actions&#x60; is this mandatory for? If any (and potentially when), perhaps just for rendering to the user, if nothing else | [optional] 
**mapping** | [**ExpressionWithAlias**](ExpressionWithAlias.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


