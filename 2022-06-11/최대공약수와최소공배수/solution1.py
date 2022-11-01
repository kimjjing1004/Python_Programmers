# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    r1 = []
    r2 = []
    r3 = []

    for i in range(1, n + 1):
        if n % i == 0:
            r1.append(i)
    print(r1)

    for i in range(1, m + 1):
        if m % i == 0:
            r2.append(i)
    print(r2)

    for i in r1:
        if i in r2:
            r3.append(i)
    print(r3)

    r3 = r3[len(r3) - 1]
    print(r3)

    r4 = n // r3
    r5 = m // r3
    r6 = r3 * r4 * r5
    print(r6)

    answer.append(r3)
    answer.append(r6)

    return answer


print(solution(3, 12))  # [3, 12]
print(solution(2, 5))  # [1, 10]
# print(solution(9, 12))  # [3, 36]
