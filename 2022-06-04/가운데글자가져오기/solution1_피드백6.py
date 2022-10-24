# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    middle = len(s) // 2
    if len(s) % 2 == 1:
        return s[middle]
    else:
        return s[middle - 1] + s[middle]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"
