# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    x = 'abcdefghijklmnopqrstuvwxyz'
    y = '`~!@#$%^&*()-_=+ '

    for i in range(len(s)):
        if s[i] in x:
            # print(s[i])
            return False
        elif s[i] in y:
            return False

    return answer


print(solution("a234"))  # false
print(solution("1234"))  # true

print(solution("12@34"))  # False
print(solution("123 4"))  # False
