import requests
from air_quality_lib import exceptions
class Country():

    def __init__(self, key):
        self.key = key

    def get_supported_countries(self, asJson = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/countries?key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if(asJson):
                return json_data
            supported_countries = []
            for data in json_data["data"]:
                supported_countries.append(data.get("country"))
            return supported_countries
        exceptions.check_exceptions(json_data["data"]["message"])