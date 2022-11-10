# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    result = 0

    for i in range(len(s)):
        if s[0] == "-":
            for j in range(len(s) - 1):
                result += int(s[j + 1]) * (10 ** (len(s) - (j + 2)))
            result = -1 * result

            return result

        elif s[0] == "+":
            for j in range(len(s) - 1):
                result += int(s[j + 1]) * (10 ** (len(s) - (j + 2)))

            return result

        result += int(s[i]) * (10 ** (len(s) - (i + 1)))

    return result


print(solution("1234"))  # 1234
# 1000 + 200 + 30 + 4

print(solution("-1234"))  # -1234
