import random

board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]

for i in range(len(board)):
    for j in range(len(board[i])):
        a = random.randrange(0, len(board))
        b = random.randrange(0, len(board[i]))
        c = random.randrange(0, len(board))
        d = random.randrange(0, len(board[i]))
        # print(a, b, c, d)

        temp = board[a][b]
        board[a][b] = board[c][d]
        board[c][d] = temp

print(board)
