# https://euleroj.io/problemset/editor/1009

def solution(a, b):
    answer = 0

    for i in range(a, b + 1):
        if i % 2 == 1:
            answer += i

    return answer


print(solution(3, 9))  # 24
