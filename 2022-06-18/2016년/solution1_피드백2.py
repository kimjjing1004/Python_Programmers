# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = b
    for i in range(0, a - 1):
        day += month[i]

    answer = week[day % 7 - 1]

    return answer


print(solution(5, 24))  # "TUE"
print(solution(1, 1))  # "FRI"
