# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(s, n):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            # print(i, j, s[i], s[j])
            if s[i][n] > s[j][n]:
                s[i], s[j] = s[j], s[i]
            elif s[i][n] == s[j][n]:
                if s[i] > s[j]:
                    s[i], s[j] = s[j], s[i]

    return s


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]
print(solution(["aea", "ba", "ce", "aee"], 1))  # ['ba', 'aea', 'aee', 'ce']
