# FileReaderBuilderDef

Information on how to construct a file-read sql query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_detect** | [**AutoDetectType**](AutoDetectType.md) |  | [optional] 
**columns** | [**list[ColumnInfo]**](ColumnInfo.md) | Column information for the results | [optional] 
**limit** | **int** | What limit be added to the load query?  Less than or equal to zero means none | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**available_sources** | [**list[Source]**](Source.md) | The source locations the user has access to.  The provider in essence. | [optional] 
**variable_name** | **str** | The name of the variable for the &#x60;use&#x60; statement | [optional] 
**file_path** | **str** | The file (or folder) path | [optional] 
**folder_filter** | **str** | The filter to apply to a folder (all matching files then being read) a RegExp | [optional] 
**zip_filter** | **str** | The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp | [optional] 
**add_file_name** | **bool** | Should a file name column be added to the output? | [optional] 
**csv** | [**OptionsCsv**](OptionsCsv.md) |  | [optional] 
**excel** | [**OptionsExcel**](OptionsExcel.md) |  | [optional] 
**sq_lite** | [**OptionsSqLite**](OptionsSqLite.md) |  | [optional] 
**xml** | [**OptionsXml**](OptionsXml.md) |  | [optional] 
**parquet** | [**OptionsParquet**](OptionsParquet.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


