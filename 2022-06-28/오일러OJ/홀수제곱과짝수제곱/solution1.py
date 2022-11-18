# https://euleroj.io/problemset/editor/1004

def solution(n):
    answer = 0
    result = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i ** 2

        if i % 2 == 1:
            result += i ** 2

    print(result - answer)


solution(10)  # -55
