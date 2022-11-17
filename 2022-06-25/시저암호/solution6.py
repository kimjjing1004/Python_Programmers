# https://programmers.co.kr/learn/courses/30/lessons/12926

def spell(s, n, alphabet):
    answer = ''

    if s in alphabet:
        for i in range(len(alphabet)):
            if alphabet[i] == s:
                answer = alphabet[(i + n) % 26]

    return answer


def lower(s, n):
    return spell(s, n, 'abcdefghijklmnopqrstuvwxyz')


def upper(s, n):
    return spell(s, n, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def space(s):
    answer = ''

    for i in s:
        if i == ' ':
            answer = ' '

    return answer


def solution(s, n):
    answer = ''
    result = []

    for i in s:
        result.append(space(i))
        result.append(lower(i, n))
        result.append(upper(i, n))

    for i in range(len(result)):
        answer += result[i]

    return answer


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
