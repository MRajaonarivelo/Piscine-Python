from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family'''

    def __init__(self, first_name, is_alive=True):
        '''Constructor for Baratheon class'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __str__(self):
        '''Gives readable output of the class for printing'''
        return repr(self)


class Lannister(Character):
    '''Representing the Lannister family'''

    def __init__(self, first_name, is_alive=True):
        '''Constructor for Lannister class'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        '''gives unambiguous representation of the class'''
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __str__(self):
        '''Gives readable output of the class for printing'''
        return repr(self)

    @classmethod
    def create_lannister(cls, name, alive):
        '''class method to create a new Lannister'''
        return cls(name, alive)
