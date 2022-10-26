# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer


print(solution(123))  # 6
print(solution(987))  # 24
