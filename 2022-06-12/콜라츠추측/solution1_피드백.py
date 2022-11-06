# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 1

    if num == 1:
        answer = 0
        return answer

    while answer <= 500:
        if num % 2 == 0:
            num = num / 2
            if num == 1:
                return answer
        else:
            num = (num * 3) + 1

        answer += 1

    answer = -1

    return answer


print(solution(6))  # 8
print(solution(16))  # 4
print(solution(626331))  # -1
print(solution(1))  # 0
