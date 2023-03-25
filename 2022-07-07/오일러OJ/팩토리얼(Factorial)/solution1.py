# https://euleroj.io/problemset/editor/1008

def solution(n):
    answer = 1

    for i in range(n):
        answer *= n - i

    return answer


print(solution(5))  # 5! = (1 * 2 * 3 * 4 * 5) = 120
