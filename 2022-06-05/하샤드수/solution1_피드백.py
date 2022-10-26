# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = 0
    x = str(x)
    for i in x:
        answer += int(i)

    return int(x) % answer == 0


print(solution(10))  # true
print(solution(12))  # true
print(solution(11))  # false
print(solution(13))  # false
