from air_quality_lib import exceptions
import requests
import json

class Station():
    def __init__(self, key):
        self.key = key

    def get_supported_stations(self, city, state, country, asJson = False, beautify = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/stations?city={city}&state={state}&country={country}&key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if asJson:
                if beautify:
                    return json.dumps(json_data, indent=4)
                return json_data
            supported_stations = []
            for data in json_data["data"]:
                supported_stations.append(data.get("station"))
            return supported_stations
        exceptions.check_exceptions(json_data["data"]["message"])

    def get_nearest_station_data_ip(self, beautify = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/nearest_station?key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if beautify:
                return json.dumps(json_data, indent=4)
            return json_data
        exceptions.check_exceptions(json_data["data"]["message"])

    def get_nearest_station_data_gps(self, latitude, longitude, beautify = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/nearest_station?lat={latitude}&lon={longitude}&key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if beautify:
                return json.dumps(json_data, indent=4)
            return json_data
        exceptions.check_exceptions(json_data["data"]["message"])

    def get_specified_station_data(self, station, city, state, country, beautify = False):
        resp = requests.get(url=f"http://api.airvisual.com/v2/station?station={station}&city={city}&state={state}&country={country}&key={self.key}")
        json_data = resp.json()
        if json_data["status"] == "success":
            if beautify:
                return json.dumps(json_data, indent=4)
            return json_data
        exceptions.check_exceptions(json_data["data"]["message"])
