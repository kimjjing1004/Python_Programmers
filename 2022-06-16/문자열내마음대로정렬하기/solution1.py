# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []

    for i in range(len(strings)):
        for j in range(len(strings[i])):
            print(j, strings[i])

    return answer


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
# print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]
