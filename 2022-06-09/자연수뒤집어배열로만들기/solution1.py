# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    n = str(n)

    for i in range(len(n)):
        answer.append(int(n[i]))
    answer.reverse()  # reverse() 말고는 방법이 없는지 질문!

    return answer


print(solution(12345))  # [5, 4, 3, 2, 1]
