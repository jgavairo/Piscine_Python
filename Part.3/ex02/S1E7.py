from S1E9 import Character


class Baratheon(Character):
    """Baratheon class"""

    def __init__(self, first_name, is_alive=True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """String representation"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Repr representation"""
        return self.__str__()


class Lannister(Character):
    """Lannister class"""

    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """String representation"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Repr representation"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister"""
        return cls(first_name, is_alive)
