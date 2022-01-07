import requests
from air_quality_lib import exceptions
class State():      
    def __init__(self, key):
        self.key = key

    def get_supported_states(self, country, asJson = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/states?country={country}&key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if(asJson):
                return json_data
            supported_states = []
            for data in json_data["data"]:
                supported_states.append(data.get("state"))
            return supported_states
        exceptions.check_exceptions(json_data["data"]["message"])
