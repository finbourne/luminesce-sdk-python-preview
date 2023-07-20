# FieldDesign

Treatment of a single field within a QueryDesign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Field | 
**alias** | **str** | Alias if any (if none the Name is used) | [optional] 
**data_type** | [**DataType**](DataType.md) |  | [optional] 
**should_select** | **bool** | Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present | [optional] 
**filters** | [**list[FilterTermDesign]**](FilterTermDesign.md) | Filter clauses to apply to this field (And&#39;ed together) | [optional] 
**aggregations** | [**list[Aggregation]**](Aggregation.md) | Aggregations to apply (as opposed to simply selecting) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


