from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, state):
        self.state = state
        
    @abstractmethod
    def get_state_name(self):
        pass