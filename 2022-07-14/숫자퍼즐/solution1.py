# http://sample.codeonlab.com/slidingpuzzle/level1/index.html

board = []

for i in range(1, 16):
    board.append(str(i))
board.append(' @')


def display():
    count = 0
    for i in range(len(board)):
        count += 1
        if count % 4 == 0 and count < 9:
            print(' ' + board[i], end=' ')
            print()
        elif count > 9:
            if count == 12:
                print(board[i], end=' ')
                print()
                count += 1
                continue
            print(board[i], end=' ')
        else:
            print(' ' + board[i], end=' ')
    print()


def used(value, arr):

    if value in arr:
        display()
        print()
        print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
        return True

    return False


def is_blank(temp):
    if temp in ['\n', ' ', '']:
        display()
        print()
        print('공백 불가!')
        return True

    return False


def is_length(temp):
    if len(temp) > 2 or temp[0] == '0':
        display()
        print()
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        return True

    return False


def is_number(temp):
    for i in temp:
        if i not in '0123456789':
            display()
            print()
            print('올바른 범위 안에 숫자만 입력해 주세요!')
            return True

    return False


def is_range(temp):
    temp = int(temp)

    if temp > 15 or temp < 1:
        display()
        print()
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        return True

    return False


def is_check():
    space_index = -1
    for i in range(len(board)):
        if board[i] == '@':
            space_index = i
            break

    left = space_index - 1
    right = space_index + 1
    up = space_index - 4
    down = space_index + 4
    if right >= len(board):
        print('right', right)
    if down >= len(board):
        print('down', down)
    if up <= len(board):
        print('up', up)
    if left <= len(board):
        print('left', left)


display()
while True:
    print()
    temp = input('숫자 입력: ')
    print()

    flag = False
    for i in [is_blank, is_length, is_number, is_range]:
        if i(temp):
            flag = True
            break
    if flag:
        continue

    is_check()

    temp = int(temp)
    display()

    print()
    print('----------------------------------')
