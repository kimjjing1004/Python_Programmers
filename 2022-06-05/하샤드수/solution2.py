# https://programmers.co.kr/learn/courses/30/lessons/12947

# str 쓰지 말고 풀기
def solution(x):
    answer = 0
    n = x

    while n > 0:
        answer += n % 10
        n = n // 10

    return x % answer == 0


print(solution(10))  # true
print(solution(12))  # true
print(solution(11))  # false
print(solution(13))  # false
