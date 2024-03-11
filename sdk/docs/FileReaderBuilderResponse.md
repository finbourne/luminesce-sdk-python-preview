# FileReaderBuilderResponse

Information on how to construct a file-read sql query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The generated SQL | [optional] 
**error** | **str** | The error from running generated SQL Query, if any | [optional] 
**columns** | [**list[ColumnInfo]**](ColumnInfo.md) | Column information for the results | [optional] 
**data** | **object** | The resulting data from running the Query | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


