from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class"""

    first_name: str
    is_alive: bool

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        if not isinstance(is_alive, bool):
            raise ValueError("Is alive must be a boolean")

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill the character"""
        self.is_alive = False


class Stark(Character):
    """Stark class"""
    def __init__(self, first_name, is_alive=True):
        """Stark constructor"""
        super().__init__(first_name, is_alive)
