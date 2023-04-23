basic_board = []
pre_board = []
board = []

for i in range(1, 17):
    if i == 13:
        basic_board.append(' @')
    else:
        basic_board.append(str(i))

for i in range(len(basic_board)):
    pre_board.append(basic_board[i])

    if i % 4 == 3:
        board.append(pre_board)
        pre_board = []

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == ' @':
            a, b = i, j

flag = False
if 0 <= b - 1 <= 3:
    left = board[a][b - 1]
    flag = True

if 0 <= b + 1 <= 3:
    right = board[a][b + 1]
    flag = True

if 0 <= a - 1 <= 3:
    up = board[a - 1][b]
    flag = True

if 0 <= a + 1 <= 3:
    down = board[a + 1][b]
    flag = True
