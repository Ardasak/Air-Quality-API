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

def check_exceptions(message: str):
    match(message):
        case "call_limit_reached":
            raise CallLimitReached("Minute/Monthly call limit reached.")
        case "api_key_expired":
            raise ApiKeyExpired("API key expired.")
        case "ip_location_failed":
            raise IpLocationFailed("IP location failed.")
        case "too_many_requests":
            raise TooManyRequests("Too many requests.")
        case "permission_denied (you don't have access to this endpoint)":
            raise PermissionError("Permission denied.")
        case "invalid_api_key":
            raise InvalidApiKey("Invalid API key.")
        case "no_nearest_station":
            raise NoNearestStation("No nearest station.")
        case "state_not_found":
            raise StateNotFound("State not found. Check supported states by calling get_supported_states(country_name). This exception is also raised if country name is wrong.")
        case "country_not_found":
            raise CountryNotFound("Country not found. Check supported countries by calling get_supported_countries().")
        
