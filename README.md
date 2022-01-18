# **Usage**

This library is developed using [AirVisualAPI](https://www.iqair.com/air-pollution-data-api)

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

# Some of the Terms
Comment: _Data is returned according to your api plan. So if you can't get some of the datas specified below. That could be the reason._
* ts: _timestamp_
* aqius: _AQI value based on US EPA standard_
* aqicn: _AQI value based on Chinese Mep standard_
* tp: _Air temperature in Celcius_
* tp_min: _Minimum air temperature in Celsius_
* pr: _Atmospheric pressure in hPa_
* hu: _Humidity in %_
* ws: _Wind speed in m/s_
* wd: _Wind direction as an angle of 360° (N=0, E=90, S=180, W=270)_
* ic: _Weather icon code (if you visit https://airvisual.com/images/iconcode.png, you will find the icon according to the weather condition)_
* mainus: _Main pollutant for US AQI_
* maincn: _Main pollutant for Chinese AQI_
* conc: _Concentration of particulate matter in ug/m3_
* p2: _ugm3 (pm2.5)_
* p1: _ugm3 (pm10)_
* o3: _ppb (Ozone O3)_
* n2: _ppb (Nitrogen dioxide NO2)_
* s2: _ppb (Sulfur dioxide SO2)_
* co: _ppm (Carbon monoxide CO)_