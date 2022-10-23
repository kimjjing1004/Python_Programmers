# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = 0
    for i in arr:
        answer += i

    answer = answer / len(arr)
    return answer


print(solution([1, 2, 3, 4]))  # 2.5
print(solution([5, 5]))  # 5
