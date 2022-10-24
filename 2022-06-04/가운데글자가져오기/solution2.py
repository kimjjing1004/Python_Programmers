# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = len(s) // 2
    if len(s) % 2 == 1:
        return s[answer]
    else:
        return s[answer - 1] + s[answer]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"
