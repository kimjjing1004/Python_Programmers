# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    n = str(n)

    for i in range(len(n)):
        answer.append(int(n[i]))

    result = []

    for i in range(len(answer)):
        x = len(answer) - i - 1
        result.append(answer[x])

    return result


print(solution(12345))  # [5, 4, 3, 2, 1]
print(solution(23154))  # [4, 5, 1, 3, 2]
print(solution(247513))  # [3, 1, 5, 7, 4, 2]
