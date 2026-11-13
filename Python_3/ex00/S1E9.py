from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract class for a character'''

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Constructor for Character class'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Makes the character ded function'''
        self.is_alive = False


class Stark(Character):
    '''Stark, a Character subclass'''

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
