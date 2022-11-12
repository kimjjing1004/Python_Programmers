# https://programmers.co.kr/learn/courses/30/lessons/12926

# a - z / A - Z 까지 계속 돌리는 기능
def spell(s, n):
    answer = 0
    result = ''

    for i in range(len(s)):
        answer = ord(s[i])

        if answer > 96 and answer < 123:
            answer = answer + n
            if answer > 122:
                answer = answer - 26

        if answer > 64 and answer < 91:
            answer = answer + n
            if answer > 90:
                answer = answer - 26

        result += chr(answer)

    return result


def space(s, n):
    answer = 0
    total = spell(s, n)
    s = list(s)

    for i in range(len(s)):
        answer = ord(s[i])

        if answer == 32:
            total += s[i]
            continue

    return total


def solution(s, n):
    return space(s, n)


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
