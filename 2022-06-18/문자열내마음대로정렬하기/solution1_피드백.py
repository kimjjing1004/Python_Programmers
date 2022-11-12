# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []

    for i in range(len(strings)):
        for j in range(len(strings)):
            print(strings[i], strings[j], strings[i][n], strings[j][n])

    return answer


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
# print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]

s = 'hi hello'
s[0] = 'p'
print(s)
