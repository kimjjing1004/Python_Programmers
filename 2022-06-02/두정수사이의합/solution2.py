# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    r1 = 0
    r2 = 0

    # 아래 코드를 중복제거 하시오.
    if a > b:
        for i in range(a + 1):
            r1 += i

        for i in range(b):
            r2 += i
    else:
        for i in range(a):
            r1 += i

        for i in range(b + 1):
            r2 += i

    # print(r1, r2)

    if r1 > r2:
        return r1 - r2

    return r2 - r1


print(solution(3, 5))  # 12
print(solution(3, 3))  # 3
print(solution(5, 3))  # 12
