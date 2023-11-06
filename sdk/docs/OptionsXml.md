# OptionsXml

Additional options applicable to the given SourceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_types** | **str** | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) | [optional] 
**infer_type_row_count** | **int** | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified | [optional] 
**values_to_make_null** | **str** | Regex of values to map to &#39;null&#39; in the returned data. | [optional] 
**column_names** | **str** | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) | [optional] 
**node_path** | **str** | XPath query that selects the nodes to map to rows | [optional] 
**namespaces** | **str** | Selected prefix(es) and namespace(s):prefix1&#x3D;namespace1-uri1,prefix2&#x3D;namespace2-uri2,...prefixN&#x3D;namespaceN-uriN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


