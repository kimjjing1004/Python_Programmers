board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i in range(len(board)):
    print(board[i])
print()

count = 0
while count < 9:
# for count in range(9):
    if count % 2 == 0:
        o = int(input('Player1: '))
        print()
        print('--------------------------------')
        print()

        if o > 9 or o < 1:
            print('올바른 범위 안에 숫자만 입력해 주세요!')
            continue

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == o:
                    board[i][j] = 'O'
                # elif 'O' or 'X' in board:
                #     print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
                #     continue

    else:
        x = int(input('Player2: '))
        print()
        print('--------------------------------')
        print()

        if x > 9 or x < 1:
            print('올바른 범위 안에 숫자만 입력해 주세요!')
            continue

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == x:
                    board[i][j] = 'X'
                # elif 'O' or 'X' in board:
                #     print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
                #     continue

    for i in range(len(board)):
        print(board[i])

    # 승리 조건(Player1)
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2]) or \
            (board[1][0] == board[1][1] and board[1][0] == board[1][2]) or \
            (board[2][0] == board[2][1] and board[2][0] == board[2][2]) or \
            (board[0][0] == board[1][0] and board[0][0] == board[2][0]) or \
            (board[0][1] == board[1][1] and board[0][1] == board[2][1]) or \
            (board[0][2] == board[1][2] and board[0][2] == board[2][2]) or \
            (board[0][2] == board[1][1] and board[0][2] == board[2][0]) or \
            (board[0][0] == board[1][1] and board[0][0] == board[2][2]) == 'O':
        print('Player1 *********WIN*********')
        print('Player2 LOSE.....')
        break
    # 승리 조건(Player2)
    elif (board[0][0] == board[0][1] and board[0][0] == board[0][2]) or \
            (board[1][0] == board[1][1] and board[1][0] == board[1][2]) or \
            (board[2][0] == board[2][1] and board[2][0] == board[2][2]) or \
            (board[0][0] == board[1][0] and board[0][0] == board[2][0]) or \
            (board[0][1] == board[1][1] and board[0][1] == board[2][1]) or \
            (board[0][2] == board[1][2] and board[0][2] == board[2][2]) or \
            (board[0][2] == board[1][1] and board[0][2] == board[2][0]) or \
            (board[0][0] == board[1][1] and board[0][0] == board[2][2]) == 'X':
        print('Player2 *********WIN*********')
        print('Player1 LOSE.....')
        break
    # 드로우 조건
    elif count == 8:
        print('Player1 ******DRAW****** Player2')
        break

    print()
    count += 1


# 1 player O
# 2 player X

# 게임판 보여 주기

# 입력 하는 기능
# 게임판 다시 보여 주기

# 턴제
# 이미 입력된 칸은 입력 제한

# 게임이 끝나는 8가지 조건
# 누가 이겼냐?
# 비겼냐?
