import json
from air_quality_lib import air_quality_lib

obj = air_quality_lib("4732196d-a1af-40a0-af2e-023f6b6a225d")

def test_app():
    for func in dir(obj.City):
        if func.startswith("get_"):
            print(getattr(obj.City("London"), func)())
    for func in dir(obj.Country):
        if func.startswith("get_"):
            print(getattr(obj.Country("Turkey"), func)())
    for func in dir(obj.State):
        if func.startswith("get_"):
            print(getattr(obj.State("Los Angeles"), func)())

test_app