# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        print(i)
        phone_number = phone_number.replace("0103333", "*******")

    return phone_number


print(solution("01033334444"))  # "*******4444"
# print(solution("027778888"))  # "*****8888"
