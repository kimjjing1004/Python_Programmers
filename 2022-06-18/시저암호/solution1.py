# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = 0
    result = ''
    s = list(s)

    for i in range(len(s)):
        answer = ord(s[i]) + n
        if answer > 122:
            answer = answer - 26

        result += chr(answer)

    return result


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
