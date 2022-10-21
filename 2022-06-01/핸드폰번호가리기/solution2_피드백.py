# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

def solution(pn):
    answer = ''
    for i in range(len(pn)):
        print(i, pn[i], len(pn) - 4)

        if i >= len(pn) - 4:
            answer += pn[i]
        else:
            answer += '*'

    return answer


# 11 - 4 = 7
#               012345678910
print(solution("01033334444"))  # "*******4444"
# 9 - 4 = 5
#                 012345678
# print(solution("027778888"))  # "*****8888"
