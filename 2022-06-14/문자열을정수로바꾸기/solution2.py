# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    temp = s[0]
    if temp.isdigit():  # 부호 없이 숫자만 있을때 int로 변환
        return int(s)
    else:               # 부호가 있다면 (+, -) 일 것이다.
        if temp == "+":
            return int(s[1:])  # 양수는 +1234 == 1234
        else:
            return -1 * int(s[1:])  # 음수는 -1 * 1234 == -1234


print(solution("1234"))  # 1234
print(solution("-1234"))  # -1234
