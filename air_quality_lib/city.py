from abc import ABC, abstractmethod
class City(ABC):
    def __init__(self, city):
        self.city = city

    @abstractmethod
    def get_city_name(self):
        pass