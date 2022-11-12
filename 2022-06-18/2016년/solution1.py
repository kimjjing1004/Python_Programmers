# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    for i in range(1, 13):
        for j in range(1, 32):
            answer = '{}'.format(i, j)
            print(i, j, week)
    return answer


# print(solution(5, 24))  # "TUE"
print(solution(1, 1))  # "FRI"
