# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3

def solution(x, n):
    answer = []
    for i in range(n):
        # print((i + 1) * x)
        answer.append((i + 1) * x)
    return answer


print(solution(2, 5))  # [2, 4, 6, 8, 10]
print(solution(4, 3))  # [4, 8, 12]
print(solution(-4, 2))  # [-4, -8]
