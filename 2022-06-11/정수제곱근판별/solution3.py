# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    x = -1

    for i in range(1, n + 1):
        if i ** 2 == n:
            x = (i + 1) ** 2
            break

    return x

# if n // i == i 으로 하면 5를 넣었을 때 안됨


print(solution(121))  # 144
print(solution(3))  # -1
