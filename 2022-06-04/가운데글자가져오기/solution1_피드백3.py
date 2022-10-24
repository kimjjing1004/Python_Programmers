# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    length = len(s)
    if length % 2 == 1:
        r1 = (length // 2)

        return s[r1]
    else:
        r1 = (length // 2) - 1
        r2 = r1 + 1

        return s[r1] + s[r2]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"
