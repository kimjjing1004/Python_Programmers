# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3

def solution(n):
    answer = ''

    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'

    return answer


print(solution(3))  # 수박수
# print(solution(4))  # 수박수박
