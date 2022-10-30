# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    x = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(s)):
        if s[i] in x:
            # print(s[i])
            return False

    return answer


print(solution("a234"))  # false
print(solution("1234"))  # true
print(solution("1234a"))  # Flase

print(solution("12@34"))  # False
print(solution("123 4"))  # False

print(solution("123ㄱ4"))  # False
print(solution("123가4"))  # False

