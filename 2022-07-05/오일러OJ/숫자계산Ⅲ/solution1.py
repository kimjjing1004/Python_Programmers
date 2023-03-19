# https://euleroj.io/problemset/editor/1007

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        answer += i * (n - (i - 1))
    return answer


print(solution(10))  # 220
