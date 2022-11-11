# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    arr.append(-1)
    answer = []

    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))  # [4, 3]
