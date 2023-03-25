import random

board = list('ABCDEFGH' * 2)

ran = []
boardboard = []

random.shuffle(board)
count = 0

for i in range(len(board)):
    ran.append(board[i])
    count += 1
    if count == 4:
        boardboard.append(ran)
        count = 0
        ran = []

print(boardboard)
