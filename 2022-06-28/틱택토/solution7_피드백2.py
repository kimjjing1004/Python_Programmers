board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

end_case = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],

    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],

    [1, 5, 9],
    [3, 5, 7],
]


def calc_index(n):
    n -= 1
    return [n // 3, n % 3]


def get_line(arr):
    result = ''
    for i in arr:
        temp = calc_index(i)
        a = temp[0]
        b = temp[1]
        # print('=========', i, a, b)
        result += str(board[a][b])

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

    a, b = calc_index(temp)
    if 'O' == board[a][b] or 'X' == board[a][b]:
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

    is_win = False
    for i in range(len(end_case)):
        if get_line(end_case[i]) == 'OOO':
            print()
            print('Player1 *********WIN*********')
            print('Player2 LOSE.....')
            is_win = True
            break

        if get_line(end_case[i]) == 'XXX':
            print()
            print('Player2 *********WIN*********')
            print('Player1 LOSE.....')
            is_win = True
            break

    if is_win:
        break

    count += 1

    if count == 9:
        print()
        print('Player1 ******DRAW****** Player2')
        break

    print()

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
