# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    answer = False
    result = 0

    if s[0] == '-':
        answer = True
        s = s[1:]
    elif s[0] == '+':
        answer = False
        s = s[1:]

    for i in range(len(s)):
        result += int(s[i]) * (10 ** (len(s) - (i + 1)))

    if answer:
        result *= -1

    return result


print(solution("1234"))  # 1234
print(solution("-1234"))  # -1234
print(solution("+1234"))  # 1234
