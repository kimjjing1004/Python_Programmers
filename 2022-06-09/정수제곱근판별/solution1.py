# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    x = 0

    for i in range(1, n + 1):
        if n // i == i:
            x = (i + 1) ** 2
        elif x == 0:
            x = -1

    return x

# 테스트 중 절반은 시간 초과로 실패.....


print(solution(121))  # 144
print(solution(3))  # -1
