from .country import Country
from .state import State
from .city import City
import requests

class air_quality_lib:
    def __init__(self, key):
        self.key = key

    class City(City):
        def __init__(self, city):
            super().__init__(city)

        def get_city_name(self):
            return self.city

    class Country(Country):
        def __init__(self, country):
            super().__init__(country)

        def get_country_name(self):
            return self.country

        def get_supported_countries(self, asJson = False):
            resp = requests.get(url="http://api.airvisual.com/v2/countries?key=4732196d-a1af-40a0-af2e-023f6b6a225d")
            json_data = resp.json()
            if json_data["status"] == "success":
                if(asJson):
                    return json_data
                supported_countries = []
                for data in json_data["data"]:
                    supported_countries.append(data.get("country"))
                return supported_countries
            raise Exception(f"Error: {resp.json()['data']['message']}")
            
    class State(State):
        def __init__(self, state):
            super().__init__(state)

        def get_state_name(self):
            return self.state