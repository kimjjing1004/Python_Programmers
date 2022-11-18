board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

end_case = [
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],

    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],

    [board[0][0], board[1][1], board[2][2]],
    [board[0][2], board[1][1], board[2][0]],
]

for i in range(len(board)):
    print(board[i])
print()

count = 0
o = -1
x = -1
while count < 9:
    temp = -1
    if count % 2 == 0:
        o = input('Player1: ')
        temp = o
    else:
        x = input('Player2: ')
        temp = x

    if temp not in '0123456789':
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    temp = int(temp)
    o = int(o)
    x = int(x)

    # if 'O' in board or 'X' in board:
    #     print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
    #     continue

    if temp > 9 or temp < 1:
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         if board[i][j] == 'O' or board[i][j] == 'X':
    #             print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
    #             continue

    print()
    print('----------------------------------')
    print()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == o:
                board[i][j] = 'O'
            elif board[i][j] == x:
                board[i][j] = 'X'

    for i in range(len(board)):
        print(board[i])

    # 승리 조건(Player1 = 'O' / Player2 = 'X'), # 드로우 조건(count)
    if end_case[0] == 'O' or end_case[1] == 'O' or end_case[2] == 'O' or \
            end_case[3] == 'O' or end_case[4] == 'O' or end_case[5] == 'O' or \
            end_case[6] == 'O' or end_case[7] == 'O':
        print()
        print('Player1 *********WIN*********')
        print('Player2 LOSE.....')
        break
    elif end_case[0] == 'X' or end_case[1] == 'X' or end_case[2] == 'X' or \
            end_case[3] == 'X' or end_case[4] == 'X' or end_case[5] == 'X' or \
            end_case[6] == 'X' or end_case[7] == 'X':
        print()
        print('Player2 *********WIN*********')
        print('Player1 LOSE.....')
        break
    elif count == 8:
        print()
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
