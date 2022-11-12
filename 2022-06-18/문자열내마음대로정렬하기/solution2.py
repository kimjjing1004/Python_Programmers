# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    for i in range(len(strings)):
        for j in range(len(strings)):
            # print(strings[i], strings[j], strings[i][n], strings[j][n])
            if strings[i][n] < strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]
            elif strings[i][n] == strings[j][n]:
                for k in range(len(strings) - 1):
                    for l in range(len(strings) - 1):
                        if strings[i][n+1] < strings[j][n+1]:
                            strings[k], strings[l] = strings[l], strings[k]

    return strings


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]
