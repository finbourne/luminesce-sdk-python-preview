# IntellisenseResponse

Available intellisense response information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_list** | [**list[IntellisenseItem]**](IntellisenseItem.md) | The available items at this point | 
**try_again_soon_for_more** | **bool** | Should the caller try again soon? (true means a cache is being built and this is a preliminary response!) | 
**sql_with_marker** | **str** | The SQL this is for with characters indicating the location the pop-up is for | 
**start_replacement_position** | [**CursorPosition**](CursorPosition.md) |  | 
**end_replacement_position** | [**CursorPosition**](CursorPosition.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


