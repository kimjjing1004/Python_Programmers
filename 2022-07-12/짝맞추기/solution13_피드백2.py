import random
from time import time

start = time()

board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]

# for i in range(len(board)):
#     for j in range(len(board[i])):
#         a = random.randrange(0, len(board))
#         b = random.randrange(0, len(board[i]))
#         c = random.randrange(0, len(board))
#         d = random.randrange(0, len(board[i]))
#
#         board[a][b], board[c][d] = board[c][d], board[a][b]

selected = []
correct = ['B', 'C', 'D', 'E', 'F']


def is_correct(arr):
    if len(arr) == 2:
        a, b = calc_index(arr[0])
        c, d = calc_index(arr[1])
        if board[a][b] == board[c][d]:
            correct.append(board[a][b])
            return True
    return False


def display():
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            count += 1

            if board[i][j] in correct:
                print(' ' + board[i][j], end=' ')
                continue

            if count in selected:
                print(' ' + board[i][j], end=' ')
                continue

            if count < 10:
                print(' ' + str(count), end=' ')
            else:
                print(count, end=' ')

        print()


def calc_index(n):
    n -= 1

    return [n // 4, n % 4]


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

    if temp > 12 or temp < 1:
        display()
        print()
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        return True

    return False


display()
temp = ''
total_count = 0
score = 50
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

    temp = int(temp)
    x, y = calc_index(temp)
    if used(board[x][y], correct):
        continue

    if used(temp, selected):
        continue

    selected.append(temp)

    if len(selected) >= 2:
        total_count += 1
        if is_correct(selected):
            score += 10
        else:
            score += -10
        selected = []

    display()

    print()
    print('\t\t사용 횟수: {0}'.format(total_count))
    print('실시간 점수: {0}점!'.format(score))

    if len(correct) == 6:
        print()
        print('----------------------------------')
        print('\t\t\t게임 끝!')
        print('\t\t총 사용 횟수: {0}'.format(total_count))
        print('\t\t총 점수: {0}점!'.format(score))
        break

    print()
    print('----------------------------------')

end = time()
sec = int(end - start)

m = sec // 60
sec = sec % 60

h = m // 60
m = m % 60

message = '총 걸린 시간: '

if h > 0:
    message += '{}시간 '.format(h)
if m > 0:
    message += '{}분 '.format(m)
if sec > 0:
    message += '{}초 '.format(sec)
print(message)


# 판 섞기(랜덤)
# 처음 숫자 선택시 선택한 위치에 알파벳 보여 주기
# 두번째 선택시 알파벳 보여주고 첫번째와 같은 문자가 아니면 다시 리셋
# 일치하면 계속 보여주면서 다음 선택지 선택 여부
# 초,중,고급 플레이어로 난이도 조절(판수 + 문자수)
# 몇번 만에 해결 or 타임어택!
# 여러가지 문자 넣기(!@#$%^&*, 이모지 포함)
