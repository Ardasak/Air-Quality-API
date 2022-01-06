import json
import air_quality_lib
from air_quality_lib import city

api_key = "4732196d-a1af-40a0-af2e-023f6b6a225d"
country_obj = air_quality_lib.Country(api_key)
city_obj = air_quality_lib.City(api_key)
state_obj = air_quality_lib.State(api_key)

def test_app():
    for func in dir(city_obj):
        if func.startswith("get_"):
            print(getattr(city_obj, func)())

    for func in dir(air_quality_lib.Country):
        if func.startswith("get_"):
            print(getattr(country_obj, func)())

    for func in dir(state_obj):
        if func.startswith("get_"):
            print(getattr(state_obj, func)())

test_app()