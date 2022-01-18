class InvalidApiKey(Exception):
    pass

class PermissionError(Exception):
    pass

class CallLimitReached(Exception):
    pass

class ApiKeyExpired(Exception):
    pass

class IpLocationFailed(Exception):
    pass

class TooManyRequests(Exception):
    pass

class NoNearestStation(Exception):
    pass

class StateNotFound(Exception):
    pass

class CountryNotFound(Exception):
    pass

class CityNotFound(Exception):
    pass

class StationNotFound(Exception):
    pass

def check_exceptions(message: str):
    if message == "call_limit_reached":
        raise CallLimitReached("Minute/Monthly call limit reached.")
    if message == "api_key_expired":
        raise ApiKeyExpired("API key expired.")
    if message == "ip_location_failed":
        raise IpLocationFailed("IP location failed.")
    if message == "too_many_requests":
        raise TooManyRequests("Too many requests.")
    if message == "permission_denied (you don't have access to this endpoint)":
        raise PermissionError("Permission denied.")
    if message == "incorrect_api_key":
        raise InvalidApiKey("Invalid API key.")
    if message == "no_nearest_station":
        raise NoNearestStation("No nearest station.")
    if message == "state_not_found":
        raise StateNotFound("State not found. Check supported states by calling get_supported_states(country_name). This exception is also raised if the country name is wrong.")
    if message == "country_not_found":
        raise CountryNotFound("Country not found. Check supported countries by calling get_supported_countries().")
    if message == "city_not_found":
        raise CityNotFound("City is not found. Check supported cities by calling get_supported_cities(country_name, state_name). This exception is also raised if the state or country name is wrong.")
    if message == "station_not_found":
        raise StationNotFound("Station not found. Check supported stations by calling get_supported_stations(country_name, state_name, city_name). This exception is also raised if the city or state or country name is wrong.")
    
