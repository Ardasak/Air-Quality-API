import requests
from air_quality_lib import exceptions
import json
class City():
    def __init__(self, key):
        self.key = key

    def get_supported_cities(self, country, state, asJson = False, beautify = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/cities?state={state}&country={country}&key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if asJson:
                if beautify:
                    return json.dumps(json_data, indent=4)
                return json_data
            supported_cities = []
            for data in json_data["data"]:
                supported_cities.append(data.get("city"))
            return supported_cities
        exceptions.check_exceptions(json_data["data"]["message"])
        

    def get_nearest_city_data(self, beautify = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/nearest_city?key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if beautify:
                return json.dumps(json_data, indent=4)
            return json_data
        exceptions.check_exceptions(json_data["data"]["message"])
       