# CaseStatementItem

Information about a case statement.  A typical case statement would look like:  CASE WHEN Field {Filter} Source THEN Target  For example: CASE WHEN 'currency' = 'USD' THEN 'US'  Here the Field is 'currency', the Source is 'USD', the Filter is '=', and the Target is 'US'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | The operator in the case statement SQL expression | 
**source** | **str** | The expression that is on the LHS of the operator  A typical case statement would look like:  CASE Field {Filter} Source THEN Target | 
**target** | **str** | The expression that is on the RHS of the operator  A typical case statement would look like:  CASE Field {Filter} Source THEN Target | 
**is_target_non_literal** | **bool** | The Target can be a literal value or a non literal (field) and  hence will be interpreted differently.  This can be determined from the UI and passed down as a true / false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


