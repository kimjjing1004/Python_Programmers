board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i in range(len(board)):
    print(board[i])

for k in range(9):
    o = int(input())

    for i in range(len(board)):
        for j in range(len(board[i])):
            if o == board[i][j]:
                board[i][j] = 'O'

    for i in range(len(board)):
        print(board[i])

    x = int(input())

    for i in range(len(board)):
        for j in range(len(board[i])):
            if x == board[i][j]:
                board[i][j] = 'X'

    for i in range(len(board)):
        print(board[i])


# 1 player O
# 2 player X

# 게임판 보여주기

# 입력하는 기능
# 게임판 다시 보여주기

# 턴제
# 이미 입력된 칸은 입력 제한

# 게임이 끝나는 8가지 조건
# 누가 이겼냐?
# 비겼냐?
