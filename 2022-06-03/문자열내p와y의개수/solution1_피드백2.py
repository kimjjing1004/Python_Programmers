# https://programmers.co.kr/learn/courses/30/lessons/12916

def counter(s, c):
    s = s.lower()
    r1 = 0
    for i in s:
        if i == c:
            r1 += 1

    return r1


def solution(s):
    r1 = counter(s, 'p')
    r2 = counter(s, 'y')

    if r1 == r2:
        answer = True
    else:
        answer = False

    return answer


print(solution("pPoooyY"))  # true
print(solution("Pyy"))  # false
print(solution("ooo"))  # true
