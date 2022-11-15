# https://programmers.co.kr/learn/courses/30/lessons/12926

# ASCII 코드 말고 문자로 풀기
def solution(s, n):
    answer = ''
    result = []
    lower_list = 'abcdefghijklmnopqrstuvwxyz'
    upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in s:
        # 공백 처리
        if i == ' ':
            result.append(' ')

        # 소문자 처리
        if i in lower_list:
            special = lower_list.find(i) + n
            result.append(lower_list[special % 26])

        # 대문자 처리
        if i in upper_list:
            special = upper_list.find(i) + n
            result.append(upper_list[special % 26])

    for i in range(len(result)):
        answer += result[i]

    return answer


print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"
