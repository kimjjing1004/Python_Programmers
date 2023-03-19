# https://euleroj.io/problemset/editor/1006

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        answer += i * i
    return answer


print(solution(10))  # 385
