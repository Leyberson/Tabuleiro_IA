from Board import Board

board = Board(3)
target = Board(3)
board.shuffle( )

visited_board = []

visited_board.append(board)
previous = [-1]

for boards in visited_board:
    for i in range(1,5):
        next_board = boards.copy()
        next_board.move(i)
        if next_board not in visited_board:
            visited_board.append(next_board)
            previous.append(visited_board.index(boards))
    if target in visited_board:
        break

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
    print(visited_board[i])