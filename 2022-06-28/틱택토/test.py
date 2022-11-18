board = [
    ['O', 1, 'O'],
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


def join(arr):
    result = ''
    for i in range(len(arr)):
        result += str(arr[i])

    return result


# print(end_case[0])
# print(end_case[0] == 'O')


print(join(end_case[0]))
# print(''.join(end_case[0]))

