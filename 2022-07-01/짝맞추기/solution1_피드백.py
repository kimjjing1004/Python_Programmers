board = [
    ['A', 'A', 'B', 'B'],
    ['C', 'C', 'D', 'D'],
    ['E', 'E', 'F', 'F'],
]


def display():
    count = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if count < 10:
                print(' ' + str(count), end=' ')
            else:
                print(count, end=' ')
            count += 1
        print()


while True:
    display()

    break
