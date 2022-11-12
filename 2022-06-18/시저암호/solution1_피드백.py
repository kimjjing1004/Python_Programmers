# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    result = ''
    s = list(s)

    # 공백 처리 기능
    for i in range(len(s)):
        if 32 == ord(s[i]):
            answer += s[i]
        else:
            answer += s[i]

    return answer


# print(solution("AB", 1))  # "BC"
# print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
