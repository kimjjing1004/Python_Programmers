board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def join(arr):
    result = ''
    for i in range(len(arr)):
        result += str(arr[i])

    return result


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

    # 7
    # 2, 0
    # temp // 3
    # temp % 3 - 1

    # 5
    # 1, 1
    # temp // 3
    # temp % 3 - 1

    # print('temp', temp, board[temp // 3][temp % 3 - 1])

    if 'O' == board[temp // 3][temp % 3 - 1] or 'X' == board[temp // 3][temp % 3 - 1]:
        print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
        continue

    if temp > 9 or temp < 1:
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

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

    print('=====================')
    print(join(end_case[0]))
    print(join(end_case[1]))
    print(join(end_case[2]))
    print(join(end_case[3]))
    print(join(end_case[4]))
    print(join(end_case[5]))
    print(join(end_case[6]))
    print(join(end_case[7]))
    print('=====================')

    # 승리 조건(Player1 = 'O' / Player2 = 'X'), # 드로우 조건(count)
    if join(end_case[0]) == 'OOO' \
            or join(end_case[1]) == 'OOO' \
            or join(end_case[2]) == 'OOO' \
            or join(end_case[3]) == 'OOO' \
            or join(end_case[4]) == 'OOO' \
            or join(end_case[5]) == 'OOO' \
            or join(end_case[6]) == 'OOO' \
            or join(end_case[7]) == 'OOO':
        print()
        print('Player1 *********WIN*********')
        print('Player2 LOSE.....')
        break
    elif join(end_case[0]) == 'XXX' \
            or join(end_case[1]) == 'XXX' \
            or join(end_case[2]) == 'XXX' \
            or join(end_case[3]) == 'XXX' \
            or join(end_case[4]) == 'XXX' \
            or join(end_case[5]) == 'XXX' \
            or join(end_case[6]) == 'XXX' \
            or join(end_case[7]) == 'XXX':
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
