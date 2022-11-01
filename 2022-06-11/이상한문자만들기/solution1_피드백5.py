# https://programmers.co.kr/learn/courses/30/lessons/12930

def sub(temp):
    result = ''

    for j in range(len(temp)):
        if j % 2 == 0:
            result += temp[j].upper()
        else:
            result += temp[j].lower()

    return result


def sub2(s):
    s = s + ' '
    answer = []
    temp = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer.append(temp)
            temp = ''
            continue

        temp += s[i]

    return answer

# print(sub2("try hello world"))  # ['try', 'hello', 'world']


def solution(s):
    answer = ''

    for i in sub2(s):
        answer += sub(i) + ' '

    return answer[0:-1]


print(solution("try hello world"))  # "TrY HeLlO WoRlD"
