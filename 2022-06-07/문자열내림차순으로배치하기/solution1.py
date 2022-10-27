# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    x = list(s)
    x.sort()
    x.reverse()

    for i in x:
        answer += i

    return answer


print(solution("Zbcdefg"))  # "gfedcbZ"
