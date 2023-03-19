import random

board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]

# for i in range(len(board)):
#     random.shuffle(board[i])
#
# random.shuffle(board)


selected = []
correct = []


def display():
    count = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if count in selected:
                print(' ' + board[i][j], end=' ')
                if count == temp:
                    correct.append(board[i][j])
            elif count < 10:
                is_correct = False
                for k in range(len(correct)):
                    if board[i][j] == correct[k]:
                        is_correct = True
                        break
                if is_correct:
                    print(' *', end=' ')
                else:
                    print(' ' + str(count), end=' ')
            else:
                print(count, end=' ')
            count += 1
        print()

# def calc_index(n):
#     n -= 1
#
#     return [n // 4, n % 4]


display()
temp = ''
while True:
    print()
    temp = input('숫자 입력: ')
    print()

    if temp not in '0123456789101112':
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    temp = int(temp)

    if temp > 12 or temp < 1:
        print('올바른 범위 안에 숫자만 입력해 주세요!')
        continue

    selected.append(temp)
    display()

    if len(selected) >= 2:
        selected = []

    if len(correct) >= 2:
        correct = []

    # a, b = calc_index(temp)
    # if board[a][b] == 'O':
    #     print('이미 선택된 곳 입니다! 다시 입력해 주세요!')
    #     continue

    print()
    print('----------------------------------')

    # board = board[a][b]

    # display(temp)


# 판 섞기(랜덤)
# 처음 숫자 선택시 선택한 위치에 알파벳 보여 주기
# 두번째 선택시 알파벳 보여주고 첫번째와 같은 문자가 아니면 다시 리셋
# 일치하면 계속 보여주면서 다음 선택지 선택 여부
