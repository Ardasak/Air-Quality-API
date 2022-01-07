import json
import air_quality_lib

api_key = "4732196d-a1af-40a0-af2e-023f6b6a225d"
country_obj = air_quality_lib.Country(api_key)
city_obj = air_quality_lib.City(api_key)
state_obj = air_quality_lib.State(api_key)

def test_app():
    # City Object Test

    print(city_obj.get_supported_cities("USA", "Alaska", asJson=True))
    print(city_obj.get_supported_cities("USA", "Alaska"))

    # State Object Test

    print(state_obj.get_supported_states("USA", asJson=True))
    print(state_obj.get_supported_states("USA"))

    # Country Object Test

    print(country_obj.get_supported_countries(asJson=True))
    print(country_obj.get_supported_countries())

test_app()