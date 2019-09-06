from Board import Board
from os import system
from time import sleep

board = Board(3)
target = Board(3)
board.shuffle(number_of_moviments=25)
print("Wait a moment I'm thinking")

visted_board = []