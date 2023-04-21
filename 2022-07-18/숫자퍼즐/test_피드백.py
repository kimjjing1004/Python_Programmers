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

left = False
if b - 1 >= 0 and b - 1 <= 3:
    left = True
print(left)

right = False
if b + 1 >= 0 and b + 1 <= 3:
    right = True
print(right)

