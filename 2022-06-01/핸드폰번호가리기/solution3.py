# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            answer += '*'
        else:
            answer += phone_number[i]
    return answer


# 11 - 4 = 7
#               012345678910
print(solution("01033334444"))  # "*******4444"

# 9 - 4 = 5
#                 012345678
# print(solution("027778888"))  # "*****8888"
