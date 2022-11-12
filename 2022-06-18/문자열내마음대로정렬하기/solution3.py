# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    for i in range(len(strings)):
        for j in range(len(strings)):
            # print(strings[i], strings[j], strings[i][n], strings[j][n])
            if strings[i][n] < strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]

    for i in range(len(strings)):
        idx = i
        for j in range(i, len(strings)):
            if strings[idx][n] > strings[j][n]:
                idx = j
        strings[idx], strings[i] = strings[i], strings[idx]

    return strings


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]
