import Board

board = Board(3)
target = Board(3)
board.shuffle()

visited_board = []

visited_board.append((board, -1))

for i in range(0, len(visited_board)):
    pass    