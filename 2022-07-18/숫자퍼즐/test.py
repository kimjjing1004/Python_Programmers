board = []
board2 = []
board3 = []

for i in range(1, 17):
    if i == 13:
        board.append(' @')
    else:
        board.append(str(i))

count = 0
for i in range(len(board)):
    count += 1
    board2.append(board[i])
    if count == 4:
        board3.append(board2)
        count = 0
        board2 = []

for i in range(len(board3)):
    for j in range(len(board3[i])):
        if board3[i][j] == ' @':
            a = i
            b = j

print(a, b)

# if a < 0 or a > 3:
Flag = False
if b >= 0 and b <= 3:
    left = board3[a][b - 1]
    Flag = True
else:
    Flag = False

# left = board3[a][b - 1]
#
# right = board3[a][b + 1]
# up = board3[a - 1][b]
# down = board3[a + 1][b]

