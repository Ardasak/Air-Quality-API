# **Usage**

This library is developed using [AirVisualAPI Page](https://www.iqair.com/air-pollution-data-api)

To use this library, you have to make sure that you have an api key. If you don't have one, you can have it on the same link above.

If you want to see API docs, visit [AirVisualAPI Docs](https://api-docs.iqair.com/?version=latest)

# Exceptions 

* InvalidApiKey: _When the api key you logged is invalid._
* PermissionError: _When your key does not have permission to execute that method._
* CallLimitReached: _There is a minute/monthy limit, this exception is raised if you reach that limit._
* ApiKeyExpired: _This is raised when your api key is expired, you have to renew it._
* IpLocationFailed: _If the service can not locate the ip address of request, this exception is raised._
* TooManyRequests: _Returned when more than 10 calls per second are made with the same api key._
* NoNearestStation: _Raised when there is no nearest station to the latitude and longitude you have given as parameter._
* CountryNotFound: _Raised when the country is not found._
* StateNotFound: _Raised when the state is not found._
* CityNotFound: _Raised when the city is not found._
* StationNotFound: _Raised when the station is not found._