from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family'''

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"



class Lannister(Character):
    '''Lannister class, inherited from Character'''

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    @classmethod
    def create_lannister(cls, name, alive):
        res = Lannister(name, alive)
        return res
