# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution_p(s):
    r1 = 0
    s.lower()
    for i in s:
        if i == "p":
            r1 += 1

    return r1


def solution_y(s):
    r1 = 0
    s.lower()
    for i in s:
        if i == "y":
            r1 += 1

    return r1


def solution(s):
    r1 = solution_p(s)
    r2 = solution_y(s)

    if r1 == r2:
        answer = True
    else:
        answer = False

    return answer


print(solution("pPoooyY"))  # true
print(solution("Pyy"))  # false
print(solution("ooo"))  # true
