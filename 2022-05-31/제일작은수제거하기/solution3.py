# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3


def solution(arr):

    min_value = 100

    for i in arr:
        if min_value > i:
            min_value = i

    arr.remove(min_value)

    if arr == []:
        arr.append(-1)
    return arr


print(solution([4, 3, 2, 1]))  # [4, 3, 2]
print(solution([10]))  # [-1]
