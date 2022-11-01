# https://programmers.co.kr/learn/courses/30/lessons/12932

def reverse(arr):
    result = []

    for i in range(len(arr)):
        x = len(arr) - i - 1
        result.append(arr[x])

    return result


def integer(arr):

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr


def solution(n):
    return integer(reverse(list(str(n))))


print(solution(12345))  # [5, 4, 3, 2, 1]
print(solution(23154))  # [4, 5, 1, 3, 2]
print(solution(247513))  # [3, 1, 5, 7, 4, 2]
