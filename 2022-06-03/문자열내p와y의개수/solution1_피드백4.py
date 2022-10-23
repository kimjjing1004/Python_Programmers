# https://programmers.co.kr/learn/courses/30/lessons/12916

def counter(s, c):
    s = s.lower()
    r1 = 0
    for i in s:
        if i == c:
            r1 += 1

    return r1


def counter_p(s):
    return counter(s, 'p')


def counter_y(s):
    return counter(s, 'y')


def solution(s):
    r1 = counter_p(s)
    r2 = counter_y(s)

    return r1 == r2


print(solution("pPoooyY"))  # true
print(solution("Pyy"))  # false
print(solution("ooo"))  # true
