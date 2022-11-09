# https://programmers.co.kr/learn/courses/30/lessons/12930

# 대/소문자 구별 기능
def spell(temp):
    result = ''

    for j in range(len(temp)):
        if j % 2 == 0:
            result += temp[j].upper()
        else:
            result += temp[j].lower()

    return result


# 단어만 추출하는 기능
def word(s):
    s = s + ' '
    voca = []
    temp = ''

    for i in range(len(s)):
        if s[i] == ' ':
            voca.append(temp)
            temp = ''
            continue

        temp += s[i]

    return voca


# 단어들을 한 문장으로 만들면서 대/소문자 구별
def solution(s):
    answer = ''

    for i in word(s):
        answer += spell(i) + ' '

    return answer[0:-1]


print(solution("try hello world"))  # "TrY HeLlO WoRlD"
