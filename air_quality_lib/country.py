from abc import ABC, abstractmethod

class Country(ABC):
    def __init__(self, country):
        self.country = country

    @abstractmethod
    def get_country_name(self):
        pass
    
    @abstractmethod
    def get_supported_countries(self, asJson = False):
        pass