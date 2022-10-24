# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    length = len(s)
    if length % 2 == 1:
        return s[length // 2]
    else:
        return s[(length // 2) - 1] + s[(length // 2)]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"
