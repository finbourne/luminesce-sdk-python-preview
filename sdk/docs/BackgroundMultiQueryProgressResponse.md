# BackgroundMultiQueryProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **str** | The full progress log (up to this point at least) | [optional] 
**feedback** | [**list[FeedbackEventArgs]**](FeedbackEventArgs.md) | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**queries** | [**list[BackgroundQueryProgressResponse]**](BackgroundQueryProgressResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


