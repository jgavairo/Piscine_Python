from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King Class"""

    def __init__(self, first_name, is_alive=True):
        """King constructor"""
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        """Get eyes color property"""
        return self.__dict__['eyes']

    @eyes.setter
    def eyes(self, eyes):
        """Set eyes color property"""
        self.__dict__['eyes'] = eyes

    @property
    def hairs(self):
        """Get hairs color property"""
        return self.__dict__['hairs']

    @hairs.setter
    def hairs(self, hairs):
        """Set hairs color property"""
        self.__dict__['hairs'] = hairs

    def get_eyes(self):
        """Get eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get hairs color"""
        return self.hairs

    def set_eyes(self, eyes):
        """Set eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set hairs color"""
        self.hairs = hairs
