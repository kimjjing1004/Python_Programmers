# https://programmers.co.kr/learn/courses/30/lessons/12937?language=python3

def solution(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(solution(3))  # Odd
print(solution(4))  # Even