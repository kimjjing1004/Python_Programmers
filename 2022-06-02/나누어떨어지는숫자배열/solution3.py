# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

def solution(arr, divisor):
    answer = []
    swap = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        elif not answer:
            answer.append(-1)

    for i in range(len(answer)):
        min_value = i
        for j in range(i + 1, len(answer)):
            if answer[min_value] > answer[j]:
                min_value = j
        swap = answer[i]
        answer[i] = answer[min_value]
        answer[min_value] = swap
        # answer[i], answer[min_value] = answer[min_value], answer[i]
    return answer
# 정렬 해야함


print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]
print(solution([3, 2, 6], 10))  # [-1]
