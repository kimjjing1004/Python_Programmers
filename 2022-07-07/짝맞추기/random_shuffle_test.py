import random

board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]

ranBoard = []
ran = []
boardboard = []

for i in range(len(board)):
    for j in range(len(board[i])):
        ranBoard.append(board[i][j])

random.shuffle(ranBoard)
count = 0

for i in range(len(ranBoard)):
    ran.append(ranBoard[i])
    count += 1
    if count == 4:
        boardboard.append(ran)
        count = 0
        ran = []
