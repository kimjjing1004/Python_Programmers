# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    result = []

    # 최대 공약수
    for i in range(1, max(n, m) + 1):
        if n % i == 0 and m % i == 0:
            result.append(i)
    answer.append(result[len(result) - 1])

    # 최소 공배수
    for i in range(1, n * m + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer


print(solution(3, 12))  # [3, 12]
print(solution(2, 5))  # [1, 10]
print(solution(9, 12))  # [3, 36]
