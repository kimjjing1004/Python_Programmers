# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    arr = list(s)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr)):
        answer += arr[i]

    return answer


print(solution("Zbcdefg"))  # "gfedcbZ"
