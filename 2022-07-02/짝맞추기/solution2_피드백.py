import random

board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]

# random.shuffle(board[0])
# print(board[0])

for i in range(len(board)):
    random.shuffle(board[i])
for i in range(len(board)):
    random.shuffle(board[i])

print(board)
