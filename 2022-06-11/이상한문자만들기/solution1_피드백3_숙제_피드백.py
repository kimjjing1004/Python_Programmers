# https://programmers.co.kr/learn/courses/30/lessons/12930

def typing(s):
    s = s + ' '
    answer = ''
    temp = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += spell(temp)
            answer += ' '
            temp = ''
            continue

        temp += s[i]

    return answer


def spell(temp):
    answer = ''

    for j in range(len(temp)):
        if j % 2 == 0:
            answer += temp[j].upper()
        else:
            answer += temp[j].lower()

    return answer


def solution(s):
    return typing(s)


print(solution("try hello world"))  # "TrY HeLlO WoRlD"
