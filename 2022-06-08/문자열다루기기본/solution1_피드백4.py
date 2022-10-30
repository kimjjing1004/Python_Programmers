# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    z = '0123456789'

    for i in range(len(s)):
        if s[i] in z:
            answer = True
        else:
            answer = False

    return answer


print(solution("a234"))  # false
print(solution("1234"))  # true
print(solution("123a"))  # False
print(solution("12@4"))  # False
print(solution("123 4"))  # False