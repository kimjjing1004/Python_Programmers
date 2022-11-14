# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    result = ''
    s = list(s)

    for i in range(len(s)):
        answer = ord(s[i])

        if answer == 32:
            result += s[i]
            continue

        # 소문자 처리기능
        if answer > 96 and answer < 123:
            answer = answer + n
            if answer > 122:
                answer = answer - 26

        # 대문자 처리기능
        if answer > 64 and answer < 91:
            answer = answer + n
            if answer > 90:
                answer = answer - 26

        result += chr(answer)

    return result


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
