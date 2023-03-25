import random

board = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']

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