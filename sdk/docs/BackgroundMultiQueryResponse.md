# BackgroundMultiQueryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** |  | [optional] [readonly] 
**progress** | [**Link**](Link.md) |  | [optional] 
**cancel** | [**Link**](Link.md) |  | [optional] 
**fetch_json** | [**list[Link]**](Link.md) | Json (as a string) data request links for all of the child queries | [optional] [readonly] 
**fetch_json_proper** | [**list[Link]**](Link.md) | Json-proper data request links for all of the child queries | [optional] [readonly] 
**fetch_xml** | [**list[Link]**](Link.md) | Xml data request links for all of the child queries | [optional] [readonly] 
**fetch_parquet** | [**list[Link]**](Link.md) | Parquet data request links for all of the child queries | [optional] [readonly] 
**fetch_csv** | [**list[Link]**](Link.md) | CSV data request links for all of the child queries | [optional] [readonly] 
**fetch_pipe** | [**list[Link]**](Link.md) | Pipe delimited data request links for all of the child queries | [optional] [readonly] 
**fetch_excel** | [**list[Link]**](Link.md) | Excel workbook data request links for all of the child queries | [optional] [readonly] 
**fetch_sqlite** | [**list[Link]**](Link.md) | SqLite DB data request links for all of the child queries | [optional] [readonly] 
**histogram** | [**list[Link]**](Link.md) | Histogram links for all of the child queries | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


