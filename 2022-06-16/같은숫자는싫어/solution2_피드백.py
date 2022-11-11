# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    temp = -1
    answer = []

    for i in range(len(arr)):
        if temp != arr[i]:
            answer.append(arr[i])
            temp = arr[i]

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))  # [4, 3]
