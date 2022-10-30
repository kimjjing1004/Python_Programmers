# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    z = '0123456789'

    for i in range(len(s)):
        if s[i] not in z:
            return False

    return answer


print(solution("a234"))  # False
print(solution("1234"))  # True
print(solution("123a"))  # False
print(solution("12@4"))  # False
print(solution("123 4"))  # False
