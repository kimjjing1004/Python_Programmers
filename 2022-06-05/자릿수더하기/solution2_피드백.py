# https://programmers.co.kr/learn/courses/30/lessons/12931

# str 쓰지 말고 풀기
def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10
        n = n // 10

    print(n, answer)
    return answer


print(solution(123))  # 6
print(solution(987))  # 24


# print(123 % 10)  # 3
# print(12 % 10)  # 2
# print(1 % 10)  # 1

# print(123 // 10)  # 12
# print(12 // 10)  # 1
# print(1 // 10)  # 0


# print(123 % 10)  # 3
# print(123 // 10)  # 12

# print(12 % 10)  # 2
# print(12 // 10)  # 1

# print(1 % 10)  # 1
# print(1 // 10)  # 0

