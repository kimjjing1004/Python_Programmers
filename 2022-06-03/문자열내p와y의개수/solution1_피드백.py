# https://programmers.co.kr/learn/courses/30/lessons/12916

def counter_p(s):
    s = s.lower()
    r1 = 0
    for i in s:
        if i == 'p':
            r1 += 1

    return r1


def counter_y(s):
    s = s.lower()
    r1 = 0
    for i in s:
        if i == 'y':
            r1 += 1

    return r1


def solution(s):
    r1 = counter_p(s)
    r2 = counter_y(s)

    if r1 == r2:
        answer = True
    else:
        answer = False

    return answer


print(solution("pPoooyY"))  # true
print(solution("Pyy"))  # false
print(solution("ooo"))  # true
