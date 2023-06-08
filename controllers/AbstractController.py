from abc import ABC, abstractmethod

class AbstractController(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self, id):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def update(self, id):
        pass

