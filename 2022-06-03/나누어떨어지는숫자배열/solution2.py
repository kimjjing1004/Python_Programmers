# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        answer.append(-1)

    min_value = answer[0]
    for i in answer:
        if min_value > i:
            min_value = i
    # print(min_value)
    return answer
# 정렬 해야함


# print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]
# print(solution([3, 2, 6], 10))  # [-1]
