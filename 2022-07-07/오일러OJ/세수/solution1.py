# https://euleroj.io/problemset/editor/1010

def solution(a, b, c):
    answer = 0

    if a > b:
        answer = a + b
    elif a < b:
        answer = b // c

    return answer


print(solution(5, 3, 8))  # 5 + 3 = 8
print(solution(5, 15, 3))  # 5 = 15 / 3
