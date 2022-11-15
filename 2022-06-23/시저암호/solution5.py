# https://programmers.co.kr/learn/courses/30/lessons/12926

def spell(i, n, spelling):
    spelling = 'abcdefghijklmnopqrstuvwxyz'
    spelling = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []

    if i in spelling:
        special = spelling.find(i) + n
        result.append(spelling[special % 26])

    return result


def lower(i, n):
    return spell(i, n, i)


def upper(i, n):
    return spell(i, n, i)


# ASCII 코드 말고 문자로 풀기
def solution(s, n):
    answer = ''
    result = []

    for i in s:
        # 공백 처리
        if i == ' ':
            result.append(' ')

        result = lower(i, n)
        result = upper(i, n)

    for i in range(len(result)):
        answer += result[i]

    return answer


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
