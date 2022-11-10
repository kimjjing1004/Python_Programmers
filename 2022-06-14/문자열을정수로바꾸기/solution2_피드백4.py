# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    result = 0
    neg = False

    if s[0] == '-':
        neg = True
        s = s[1:]

    for i in range(len(s)):
        result += int(s[i]) * (10 ** (len(s) - (i + 1)))

    if neg:
        # result = result * -1
        result *= -1

    return result


print(solution("1234"))  # 1234
# 1000 + 200 + 30 + 4

print(solution("-1234"))  # -1234
