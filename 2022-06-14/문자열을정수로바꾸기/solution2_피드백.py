# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    result = 0

    for i in range(len(s)):  # 양수인 문자 열을 정수로 반환
        result += int(s[i]) * (10 ** (len(s) - (i + 1)))

    return result


print(solution("1234"))  # 1234
# 1000 + 200 + 30 + 4

# print(solution("-1234"))  # -1234
