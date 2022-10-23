# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    r2 = 0

    if a > b:
        a, b = b, a

    for i in range(a, b + 1):
        r2 += i

    return r2


print(solution(3, 5))  # 12
print(solution(3, 3))  # 3
print(solution(5, 3))  # 12
