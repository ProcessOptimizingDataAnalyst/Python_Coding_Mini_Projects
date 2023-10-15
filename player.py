import math
import random

class Player:
    def __init__(self, letter): # we'll initialize the class with the letter the player is going to represent
        # letter is x or o
        self.letter = letter

    #We want all player to get their next move
    def get_move(self, game):
        pass # we're passing now because this is our base player class

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
    
