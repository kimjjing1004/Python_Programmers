# https://programmers.co.kr/learn/courses/30/lessons/12928

# 약수 구하는 함수
def sub(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)

    return answer


# 누적 시키는 함수
def total(arr):
    answer = 0
    for i in arr:
        answer += i

    return answer


def solution(n):
    return total(sub(n))


print(solution(12))  # 28
print(solution(5))  # 6
