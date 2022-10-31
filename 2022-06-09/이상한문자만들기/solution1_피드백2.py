# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s = s + ' '
    answer = ''
    temp = ''

    for i in range(len(s)):
        if s[i] == ' ':

            for j in range(len(temp)):
                # print('j', j, temp[j])
                if j % 2 == 0:
                    answer += temp[j].upper()
                else:
                    answer += temp[j].lower()

            answer += ' '
            temp = ''
            continue

        temp += s[i]

    return answer[0:-1]


print(solution("try hello world"))  # "TrY HeLlO WoRlD"
