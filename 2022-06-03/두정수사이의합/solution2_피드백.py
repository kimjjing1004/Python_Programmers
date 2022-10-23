# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    r1 = 0
    r2 = 0

    if a > b:
        # temp = a
        # a = b
        # b = temp
        a, b = b, a
    
    for i in range(a):
        r1 += i

    for i in range(b + 1):
        r2 += i

    # print(r1, r2)

    return r2 - r1


print(solution(3, 5))  # 12
print(solution(3, 3))  # 3
print(solution(5, 3))  # 12
