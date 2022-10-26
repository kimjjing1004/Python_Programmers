# https://programmers.co.kr/learn/courses/30/lessons/12931

# str 쓰지 말고 풀기
def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10
        n = n // 10

    return answer


print(solution(123))  # 6
print(solution(987))  # 24
