# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i][n] == strings[j][n]:
                if strings[i] > strings[j]:
                    strings[i], strings[j] = strings[j], strings[i]

            if strings[i][n] > strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]

    return strings


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]
print(solution(["aea", "ba", "ce", "aee"], 1))  # ['ba', 'aea', 'aee', 'ce']
