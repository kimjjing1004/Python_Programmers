# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3


def solution(arr):

    min_value = arr[0]

    for i in arr:
        if min_value > i:
            min_value = i

    # arr.remove(min_value)
    result = []
    for i in arr:
        if min_value != i:
            result.append(i)

    if not result:  # if arr is None:
        result.append(-1)

    return result


print(solution([4, 3, 2, 1]))  # [4, 3, 2]
print(solution([10]))  # [-1]
