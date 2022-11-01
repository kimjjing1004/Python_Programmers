# https://programmers.co.kr/learn/courses/30/lessons/12930

def sub(temp):
    result = ''

    for j in range(len(temp)):
        if j % 2 == 0:
            result += temp[j].upper()
        else:
            result += temp[j].lower()

    return result


def solution(s):
    s = s + ' '
    answer = ''
    temp = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += sub(temp) + ' '
            temp = ''
            continue

        temp += s[i]

    return answer[0:-1]


print(solution("try hello world"))  # "TrY HeLlO WoRlD"
