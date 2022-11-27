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


def join(arr):
    result = ''
    for i in range(len(arr)):
        result += str(arr[i])

    return result


def calc_index(n):
    n -= 1

    return [n // 3, n % 3]


def get_line(arr):
    result = ''

    for n in arr:
        temp = calc_index(n)
        a = temp[0]
        b = temp[1]
        result += str(board[a][b])

    return result


for i in range(len(board)):
    print(board[i])
print()

count = 0
ox = ['O', 'X']
players = ['Player1: ', 'Player2: ']

while count < 9:
    temp = input(players[count % 2])

    if temp not in '0123456789':
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    temp = int(temp)

    a, b = calc_index(temp)
    if board[a][b] == 'O' or board[a][b] == 'X':
        print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
        continue

    if temp > 9 or temp < 1:
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    print()
    print('----------------------------------')
    print()

    board[a][b] = ox[count % 2]

    for i in range(len(board)):
        print(board[i])

    # 승리 조건(Player1 = 'O' / Player2 = 'X'), # 드로우 조건(count)
    game_set = False
    for i in range(len(end_case)):
        if get_line(end_case[i]) == 'OOO':
            print()
            print('Player1 *********WIN*********')
            print('Player2 LOSE.....')
            game_set = True
            break

        if get_line(end_case[i]) == 'XXX':
            print()
            print('Player2 *********WIN*********')
            print('Player1 LOSE.....')
            game_set = True
            break

    if game_set:
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
