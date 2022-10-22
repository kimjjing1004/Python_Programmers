# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    r1 = 0
    r2 = 0

    for i in s:
        if i == "p" or i == "P":
            r1 += 1

    for i in s:
        if i == "y" or i == "Y":
            r2 += 1

    if r1 == r2:
        answer = True
    else:
        answer = False
    return answer


# print(solution("pPoooyY"))  # true
# print(solution("Pyy"))  # false
print(solution("ooo"))  # true
