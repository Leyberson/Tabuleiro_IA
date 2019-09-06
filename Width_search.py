from Board import Board
from os import system
from time import sleep

board = Board(3)
target = Board(3)
board.shuffle(number_of_moviments=56)
print("Wait a moment I'm thinking")
sleep(1)

visited_board = []

visited_board.append(board)
previous = [-1]

for boards in visited_board:
    for i in range(1,5):
        next_board = boards.copy()
        next_board.move(i)
        if next_board not in visited_board:
            print(next_board)
            visited_board.append(next_board)
            previous.append(visited_board.index(boards))
    if target in visited_board:
        break

sleep(1)

index = visited_board.index(target)

way = [0]

while index not in way:
    i = index
    j = 0
    while i not in way:
        j = i
        i = previous[i]
    way.append(j)

for i in way:
    system("clear")
    print("Board")
    print(board)
    print('==================')
    print("Solving")
    print(visited_board[i])
    sleep(1)

print(len(way) - 1)