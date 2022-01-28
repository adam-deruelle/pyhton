import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # list 3x3
        self.current_winner = None # Le vainqueur
        
    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (quel nombre corrspond a quelle case)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        
    def available_moves(self) :
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # Si le mouvement est valide, alors on execute le mvmt (assigner le carré a la lettre)
        # puis on return True. If c'est pas valide, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Gagnant si 3 dans n'importe qu'lle ligne... on a besoin de tout verfier!
        
        # Premierment verifions les lignes
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Verifie les colonnes
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
    
        # Verifions les diagonales
        # mais seulement si le carré est un nombre pair (0, 2, 4, 6, 8)
        # se sont les seuls mouvement possible pour gagner sur une diagonale
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # diagoanle de gauche a droite
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # diagonale de droite a gauche
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # si tout échoue
        return False
            
def play(game, x_player, o_player, print_game = True):
    # retourne le gagnant du jeu (la lettre)! or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # Lettre qui commence
    # Itére pendant que le jeu a encore des cases vides
    # (on a pas besoin de se soucier du gagnant car on renverra ce qui casse la boucle)
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter)  :
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')# Juste une ligne vide
        
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter
        
        # Aprés avoir fait le mouvement, on alterne les lettres
        letter = 'O' if letter == 'X' else 'X' # Change de joueur
        
        time.sleep(0.8)
        
    if print_game:
        print('It\'s a tie!')
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)
            
            
        
            
        
        