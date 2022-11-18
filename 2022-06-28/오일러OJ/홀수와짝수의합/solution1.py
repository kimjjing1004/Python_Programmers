# https://euleroj.io/problemset/editor/1003

def solution(n):
    answer = 0
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i

        if i % 2 == 1:
            result += i
    print(answer)
    print(result)


solution(10)
# 30
# 25
