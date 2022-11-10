# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            answer += 1

    return answer


print(solution(10))  # 4 [2, 3, 5, 7]
print(solution(5))  # 3 [2, 3, 5]
