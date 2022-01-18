import air_quality_lib

# Here is an example community api key
api_key = "4732196d-a1af-40a0-af2e-023f6b6a225d"

country_obj = air_quality_lib.Country(api_key)
city_obj = air_quality_lib.City(api_key)
state_obj = air_quality_lib.State(api_key)
station_obj = air_quality_lib.Station(api_key)

def test_app():
    print(city_obj.get_supported_cities("USA", "Alaska", asJson=True))
    print(city_obj.get_supported_cities("USA", "Alaska"))

    print(state_obj.get_supported_states("USA", asJson=True))
    print(state_obj.get_supported_states("USA"))

    print(country_obj.get_supported_countries(asJson=True))
    print(country_obj.get_supported_countries())

test_app()