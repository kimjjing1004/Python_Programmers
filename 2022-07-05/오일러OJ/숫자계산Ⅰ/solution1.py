# https://euleroj.io/problemset/editor/1005

def solution(n):
    answer = 0
    for i in range(1, 101):
        answer += n * i
    return answer


print(solution(2))  # 10100
