import numpy as np
from random import randint

class Board:
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = []
        aux_board = []
        for row in range(0, dimension):
            for column in range(0, dimension):
                aux_board.append((row*dimension) + column + 1)
            self.board.append(aux_board)
            aux_board = []
        del(aux_board)
        self.board[dimension - 1][dimension - 1] = 0
        self.board = np.array(self.board)
        self.zero_position = [self.dimension - 1, self.dimension - 1]
    
    def __str__(self):
        return str(self.board)

    def __eq__(self, obj):
        if self.dimension != obj.dimension:
            return False
        for row in range(0, self.dimension):
            for column in range(0, self.dimension):
                if self.board[row][column] != obj.board[row][column]:
                    return False
        return True

    def move_down(self):
        if self.zero_position[0] > 0:
            self.board[self.zero_position[0]][self.zero_position[1]] = self.board[self.zero_position[0] - 1][self.zero_position[1]]
            self.board[self.zero_position[0] - 1][self.zero_position[1]] = 0
            self.zero_position[0] -= 1

    def move_up(self):
        if self.zero_position[0] < self.dimension - 1:
            self.board[self.zero_position[0]][self.zero_position[1]] = self.board[self.zero_position[0] + 1][self.zero_position[1]]
            self.board[self.zero_position[0] + 1][self.zero_position[1]] = 0
            self.zero_position[0] += 1

    def move_left(self):
        if self.zero_position[1] < self.dimension - 1:
            self.board[self.zero_position[0]][self.zero_position[1]] = self.board[self.zero_position[0]][self.zero_position[1] + 1]
            self.board[self.zero_position[0]][self.zero_position[1] + 1] = 0
            self.zero_position[1] += 1

    def move_right(self):
        if self.zero_position[1] > 0:
            self.board[self.zero_position[0]][self.zero_position[1]] = self.board[self.zero_position[0]][self.zero_position[1] - 1]
            self.board[self.zero_position[0]][self.zero_position[1] - 1] = 0
            self.zero_position[1] -= 1
    
    def move(self, next_moviment):
        if next_moviment == 1:
            self.move_down()
        elif next_moviment == 2:
            self.move_up()
        elif next_moviment == 3:
            self.move_left()
        elif next_moviment == 4:
            self.move_right()

    def manhatan_distance_target(self):
        distance = 0
        for row in range(0, self.dimension):
            for column in range(0, self.dimension):
                if self.board[row][column] != 0:
                    aux = self.board[row][column] - 1
                    target_position = [aux // self.dimension , aux % self.dimension]
                    distance += (abs(target_position[0] - row) + abs(target_position[1] - column))
        return distance

    def shuffle(self, number_of_moviments = randint(1000,2000)):
        for i in range(0, number_of_moviments):
            self.move(randint(1,4))
    
    def copy(self):
        board = Board(self.dimension)
        board.zero_position[0] = self.zero_position[0]
        board.zero_position[1] = self.zero_position[1]
        board.board = self.board.copy()
        return board


        

target = Board(3)
board = Board(3)
print(target)
print(board)
print(target == board)
print(target.manhatan_distance_target())
target.shuffle()
print(target)
print(target.manhatan_distance_target())

lista = [target, board]
# target.move_down()
print(target in lista)
board = target.copy()
print(board)
board.move_down()
print(target)
print(board)
target.move_down()
print(target)
print(target == board)