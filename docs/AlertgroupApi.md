# swagger_client.AlertgroupApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_groups**](AlertgroupApi.md#get_alert_groups) | **GET** /alerts/groups | 


# **get_alert_groups**
> AlertGroups get_alert_groups(active=active, silenced=silenced, inhibited=inhibited, filter=filter, receiver=receiver)



Get a list of alert groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertgroupApi()
active = true # bool | Show active alerts (optional) (default to true)
silenced = true # bool | Show silenced alerts (optional) (default to true)
inhibited = true # bool | Show inhibited alerts (optional) (default to true)
filter = ['filter_example'] # list[str] | A list of matchers to filter alerts by (optional)
receiver = 'receiver_example' # str | A regex matching receivers to filter alerts by (optional)

try:
    api_response = api_instance.get_alert_groups(active=active, silenced=silenced, inhibited=inhibited, filter=filter, receiver=receiver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertgroupApi->get_alert_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Show active alerts | [optional] [default to true]
 **silenced** | **bool**| Show silenced alerts | [optional] [default to true]
 **inhibited** | **bool**| Show inhibited alerts | [optional] [default to true]
 **filter** | [**list[str]**](str.md)| A list of matchers to filter alerts by | [optional] 
 **receiver** | **str**| A regex matching receivers to filter alerts by | [optional] 

### Return type

[**AlertGroups**](AlertGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

