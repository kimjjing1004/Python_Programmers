# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    x = '0123456789'

    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] not in x:
                return False

    return answer


print(solution("a234"))  # false
print(solution("1234"))  # True
print(solution("123a"))  # False
print(solution("12@4"))  # False
print(solution("123 4"))  # False
print(solution("12345"))  # False
print(solution("123456"))  # True
