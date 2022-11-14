# https://programmers.co.kr/learn/courses/30/lessons/12926

def common(answer, n, a, b, c):
    if answer > a and answer < b:
        answer = answer + n
        if answer > c:
            answer = answer - 26

    return answer


def lower(answer, n):
    return common(answer, n, 96, 123, 122)


def upper(answer, n):
    return common(answer, n, 64, 91, 90)


def solution(s, n):
    result = ''

    for i in range(len(s)):
        answer = ord(s[i])
        answer = lower(answer, n)
        answer = upper(answer, n)

        result += chr(answer)

    return result


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
