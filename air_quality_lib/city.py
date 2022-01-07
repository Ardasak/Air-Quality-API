import requests
from air_quality_lib import exceptions
class City():
    def __init__(self, key):
        self.key = key

    def get_supported_cities(self, country, state, asJson = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/cities?state={state}&country={country}&key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if(asJson):
                return json_data
            supported_cities = []
            for data in json_data["data"]:
                supported_cities.append(data.get("city"))
            return supported_cities
        exceptions.check_exceptions(json_data["data"]["message"])