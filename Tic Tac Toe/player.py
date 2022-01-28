import math
from multiprocessing.sharedctypes import Value
import random

class Player:
    def __init__(self, letter):
        # letter x or o
        self.letter = letter
    
    #pas trop compris
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + '''\'s turn. Input move (0-8)
>>> ''')
            #On va verfier que la valeur est bonne en essayant de la
            #transformer en un entier, et si ce n'en est pas un, alors ça va être invalide
            #si cet endroit est aussi indisponible sur le plateau, alors ça va aussi être invalide
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # si c'est bon
            except ValueError:
                print('Invalid square. Try again')
        
        return val