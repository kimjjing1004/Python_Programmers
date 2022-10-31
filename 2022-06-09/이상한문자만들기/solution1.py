# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    z = 0
    # x = 'abcdefghijklmnopqrstuvwxyz '
    # for i in range(len(s)):
    #     if s[i] == ' ':
    #         for j in range(len(s) - i)
    #         for j in range(i):
    #             print(j)
    #             answer += s[j]

    # for i in range(len(s)):
    #     if s[i] == ' ':
    #         z = len(s) - i
    #         for j in range(i):
    #             answer += s[j]

    while len(s) - z > 0:
        for i in range(len(s)):
            answer += s[i]
            if s[i] == ' ':
                z = len(s) - i
        print(z)

    return answer


print(solution("try hello world"))  # "TrY HeLlO WoRlD"
