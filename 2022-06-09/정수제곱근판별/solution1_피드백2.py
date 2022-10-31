# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    x = -1

    for i in range(1, n + 1):
        # print(n // i == i, n, i, n // i)
        if n // i == i:
            x = (i + 1) ** 2
            break

    return x

# 테스트 중 절반은 시간 초과로 실패.....


# print(solution(121))  # 144
# print(solution(3))  # -1


def sub(n):
    for i in range(1, n + 1):
        if i * i == n:
            return (i + 1) ** 2
    return -1


for i in range(1, 50000000000000):
    x = solution(i)
    y = sub(i)
    if x <= 0 or y <= 0:
        continue

    if x == y:
        print(True, i, x, y)

