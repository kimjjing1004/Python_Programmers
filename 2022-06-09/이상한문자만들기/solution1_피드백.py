# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    temp = ''

    for i in range(len(s)):
        if s[i] == ' ':
            print(temp)
            temp = ''
        else:
            temp += s[i]

    return answer


print(solution("try hello world "))  # "TrY HeLlO WoRlD"
