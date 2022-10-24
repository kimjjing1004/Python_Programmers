# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 1:
        return s[middle]
    else:
        return s[middle - 1] + s[middle]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"
