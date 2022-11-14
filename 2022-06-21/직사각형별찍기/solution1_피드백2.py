# https://programmers.co.kr/learn/courses/30/lessons/12969

def solution(n, m):
    answer = []

    for i in range(m):
        temp = ''
        for j in range(n):
            temp += '*'
        answer.append(temp)

    result = ''
    for i in answer:
        result += i + '\n'

    result2 = ''
    for i in range(len(result) - 1):
        result2 += result[i]

    return result2

# 도데체 왜 자꾸 Output size differs 이게 나오는지 1도 모르겠음
# 아무리 봐도 내 코드와 결과 값은 문제 없는 거 같음
# 하지만, 내 예상은 입력 값이 '5', '3'이게 아니라 '5 3'이거 여야만 해서?


print(solution(5, 3))
# *****
# *****
# *****


# s = 'abc'
# len 3
# 0, 1, 2
