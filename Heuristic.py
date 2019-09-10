from Board import Board
from os import system
from time import sleep

board = Board(5)
target = Board(5)
board.shuffle(number_of_moviments=1000)
print("Wait a moment I'm thinking")

visited_board = [board]
heuristic_visited_board = [(0, board.manhatan_distance_target(), board.manhatan_distance_target(), -1)]

candidate_list = []
heuristic_candidate = []

for previous_board in visited_board:
    for move in range(0,5):
        candidate = previous_board.copy()
        candidate.move(move)
        print(candidate)
        if candidate not in visited_board:
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                heuristic = candidate.manhatan_distance_target()
                previous_index = visited_board.index(previous_board)
                moved = heuristic_visited_board[previous_index][0]
                heuristic_candidate.append((moved+1, heuristic, heuristic+moved+1, previous_index))
            else:
                heuristic = candidate.manhatan_distance_target()
                previous_index = visited_board.index(previous_board)
                moved = heuristic_visited_board[previous_index][0]
                my_index = candidate_list.index(candidate)
                if ((heuristic+moved+1) < heuristic_candidate[my_index][2]):
                    heuristic_candidate[my_index] = (moved+1, heuristic, heuristic+moved+1, previous_index)
    min_distance = (board.dimension ** 2) * (2 * board.dimension)
    min_position = 0
    for i in range(0, len(candidate_list)):
        if heuristic_candidate[i][2] < min_distance:
            min_distance = heuristic_candidate[i][2]
            min_position = i
    visited_board.append(candidate_list[min_position])
    heuristic_visited_board.append(heuristic_candidate[min_position])
    del(candidate_list[min_position])
    del(heuristic_candidate[min_position])
    if target in visited_board:
        break

print("success")

sleep(1)

index = visited_board.index(target)

way = [0]

while index not in way:
    i = index
    j = 0
    while i not in way:
        j = i
        i = heuristic_visited_board[i][3]
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