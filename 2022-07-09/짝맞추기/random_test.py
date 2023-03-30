import random

board_str = list(('abcdef' * 2).upper())
random.shuffle(board_str)

count = 0
ran = []
board = []

for i in range(len(board_str)):
    ran.append(board_str[i])
    count += 1
    if count == 4:
        board.append(ran)
        ran = []
        count = 0

print(board)
