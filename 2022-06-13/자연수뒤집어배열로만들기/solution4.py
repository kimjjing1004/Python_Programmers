# https://programmers.co.kr/learn/courses/30/lessons/12932

# 리스트 요소 순서를 뒤집는 기능(reverse)
def sub(arr):
    result = []

    for i in range(len(arr)):
        x = len(arr) - i - 1
        result.append(arr[x])

    return result


# 문자를 정수로 변환하는 기능(str -> int)
def num(s):

    for i in range(len(s)):
        s[i] = int(s[i])

    return s


def solution(n):
    return num(sub(list(str(n))))


print(solution(12345))  # [5, 4, 3, 2, 1]
print(solution(23154))  # [4, 5, 1, 3, 2]
print(solution(247513))  # [3, 1, 5, 7, 4, 2]
