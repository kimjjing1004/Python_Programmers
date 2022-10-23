# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    result1 = 0
    result2 = 0

    for i in range(b + 1):
        for j in range(a):
            result1 += i
            result2 += j
            answer = result1 - result2
    return answer


print(solution(3, 5))  # 12
# print(solution(3, 3))  # 3
# print(solution(5, 3))  # 12
