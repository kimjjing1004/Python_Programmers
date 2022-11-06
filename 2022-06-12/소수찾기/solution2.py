# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = []
    x = []

    for i in range(2, n + 1):  # 2 ~ n 이하의 자연수
        answer.append(i)
        for j in range(2, n + 1):
            x.append(2 * i)  # 2의 배수 포함
            if j % 2 == 1:  # j가 홀수 일때
                x.append(j * i)  # j 자신을 제외한 j의 배수

    result = []

    for i in range(len(answer)):
        if answer[i] not in x:
            result.append(answer[i])

    return len(result)

# 절반이 시간 초과로 실패.....


print(solution(10))  # 4 [2, 3, 5, 7]
print(solution(5))  # 3 [2, 3, 5]
