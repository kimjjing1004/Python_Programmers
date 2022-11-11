# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = ''

    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            # answer = '김서방은 %d에 있다' % i
            answer = '김서방은 {}에 있다'.format(i)

    return answer


print(solution(["Jane", "Kim"]))  # "김서방은 1에 있다"
