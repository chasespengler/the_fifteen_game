from re import L
import numpy as np

class gameBoard():
    def __init__(self, pattern):

        if pattern == 1:
            self.board = np.array([
                ['1', '2', '3', '4'],
                ['5', '6', '7', '8'],
                ['9', '10', '11', '12'],
                ['13', '14', '15', '--']
            ])

            self.blank_loc = (3, 3)
            self.adjs = ['15', '12']

    #Updates adjacent numbers to blank location
    def update_adjs(self):
        self.adjs = []
        for i in [-1, 1]:
            adjx = (self.blank_loc[0] + i, self.blank_loc[1])
            adjy = (self.blank_loc[0], self.blank_loc[1] + i)
            if 0 <= adjx[0] <= 3 and 0 <= adjx[1] <= 3:
                self.adjs.append(self.board[adjx[0]][adjx[1]])
            if 0 <= adjy[0] <= 3 and 0 <= adjy[1] <= 3:
                self.adjs.append(self.board[adjy[0]][adjy[1]])
        
    #Returns valid moves
    def valid_moves(self):
        moves = []
        move_loc_end = self.blank_loc
        if 0 < move_loc_end[0]:
            moves.append(move(move_loc_end, (move_loc_end[0] - 1, move_loc_end[1]), self.board))
        if 3 > move_loc_end[0]:
            moves.append(move(move_loc_end, (move_loc_end[0] + 1, move_loc_end[1]), self.board))
        if 0 < move_loc_end[1]:
            moves.append(move(move_loc_end, (move_loc_end[0], move_loc_end[1] - 1), self.board))
        if 3 > move_loc_end[1]:
            moves.append(move(move_loc_end, (move_loc_end[0], move_loc_end[1] + 1), self.board))
        return moves

    #Makes move
    def make_move(self, move):
        piece_moved = self.board[move.empty_loc_end[0]][move.empty_loc_end[1]]
        self.board[move.empty_loc_end[0]][move.empty_loc_end[1]] = "--"
        self.board[move.empty_loc_start[0]][move.empty_loc_start[1]] = piece_moved
        self.blank_loc = (move.empty_loc_end[0], move.empty_loc_end[1])
        self.update_adjs()

    #Shuffles the board
    def shuffle(self):
        for x in range(50):
            moves = self.valid_moves()
            rand_move_id = np.random.randint(0, len(moves))
            rand_move = moves[rand_move_id]
            self.make_move(rand_move)

class move():
    def __init__(self, empty_loc_start, empty_loc_end, board):
        self.empty_loc_start = empty_loc_start
        self.empty_loc_end = empty_loc_end
        self.move_id = empty_loc_end[0] * 1000 + empty_loc_end[1] * 100 + empty_loc_start[0] * 10 + empty_loc_start[1]

    #To enable comparison between objects (like checking for valid moves)
    def __eq__(self, other):
        if isinstance(other, move):
            return self.move_id == other.move_id
