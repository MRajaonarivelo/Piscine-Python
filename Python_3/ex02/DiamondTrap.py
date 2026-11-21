from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Representing Westeros'''

    def __init__(self, first_name, is_alive=True):
        '''Constructor fit for a King'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        '''Sets a King's eyes to color'''
        self.eyes = color
    
    def set_hairs(self, color):
        '''Sets a King's hairs to color'''
        self.hairs = color
    
    def get_eyes(self) -> str:
        '''Returns a King's eye color'''
        return self.eyes

    def get_hairs(self) -> str:
        '''Returns a King's hair color'''
        return self.hairs