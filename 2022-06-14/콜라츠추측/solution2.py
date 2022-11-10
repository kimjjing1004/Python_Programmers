# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0

    for i in range(1, 501):
        if num == 1:
            return answer

        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1

        answer += 1

    return -1


print(solution(6))  # 8
print(solution(16))  # 4
print(solution(626331))  # -1
print(solution(1))  # 0
