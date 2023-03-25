import random

board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]

ranBoard = []

for i in range(len(board)):
    for j in range(len(board[i])):
        ranBoard.append(board[i][j])

random.shuffle(ranBoard)

ran = []
count = 0
boardboard = []

for i in range(len(ranBoard)):
    ran.append(ranBoard[i])
    count += 1
    if count == 4:
        boardboard.append(ran)
        count = 0
        ran = []

selected = []
correct = []


def display():
    count = 1
    for i in range(len(boardboard)):
        for j in range(len(boardboard[i])):
            if boardboard[i][j] in correct:
                print(' ' + boardboard[i][j], end=' ')
            elif count in selected:
                is_correct = False
                if len(selected) == 2:
                    a, b = calc_index(selected[0])
                    c, d = calc_index(selected[1])
                    if boardboard[a][b] == boardboard[c][d]:
                        correct.append(boardboard[a][b])
                        is_correct = True
                if is_correct:
                    print(' ' + boardboard[i][j], end=' ')
                else:
                    print(' ' + boardboard[i][j], end=' ')
            elif count < 10:
                print(' ' + str(count), end=' ')
            else:
                print(count, end=' ')
            count += 1
        print()


def calc_index(n):
    n -= 1

    return [n // 4, n % 4]


display()
temp = ''
score = 0
while True:
    print()
    temp = input('숫자 입력: ')
    print()

    if temp not in '0123456789101112' or temp in ' ':
        display()
        print()
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    temp = int(temp)

    if temp > 12 or temp < 1:
        display()
        print()
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    if temp in selected:
        display()
        print()
        print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
        continue

    selected.append(temp)
    display()
    score += 1
    print()
    print('\t\t사용 횟수: {0}'.format(score))

    if len(selected) >= 2:
        selected = []

    if len(correct) == 6:
        print()
        print('게임 끝!')
        print('\t\t총 사용 횟수: {0}'.format(score))
        break

    print()
    print('----------------------------------')

# 판 섞기(랜덤)
# 처음 숫자 선택시 선택한 위치에 알파벳 보여 주기
# 두번째 선택시 알파벳 보여주고 첫번째와 같은 문자가 아니면 다시 리셋
# 일치하면 계속 보여주면서 다음 선택지 선택 여부
# 초,중,고급 플레이어로 난이도 조절(판수 + 문자수)
# 몇번 만에 해결 or 타임어택!
# 여러가지 문자 넣기(!@#$%^&*, 이모지 포함)
