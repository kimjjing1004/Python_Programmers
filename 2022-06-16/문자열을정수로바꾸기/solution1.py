# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    answer = ''
    s = list(s)

    if s[0] == '-':
        answer = '-'
        for i in range(1, len(s)):
            answer += s[i]
    else:
        for i in range(len(s)):
            answer += s[i]

    return int(answer)


print(solution("1234"))  # 1234
print(solution("-1234"))  # -1234
