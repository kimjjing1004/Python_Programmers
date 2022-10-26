# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    n = 0
    x = str(x)
    for i in x:
        n += int(i)

    if int(x) % n == 0:
        answer = True
    else:
        answer = False

    return answer


print(solution(10))  # true
print(solution(12))  # true
print(solution(11))  # false
print(solution(13))  # false
