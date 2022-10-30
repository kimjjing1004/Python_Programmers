# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    x = list(s)

    for i in range(len(x)):
        x[i] = int(x[i])  # 예외 처리 밖에 생각이 안남

    return answer


print(solution("a234"))  # false
print(solution("1234"))  # true
