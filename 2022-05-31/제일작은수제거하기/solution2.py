# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

# 가장 작은 수 찾기
def solution(arr):
    answer = 100
    for i in arr:
        if answer > i:
            answer = i

    return answer


print(solution([4, 3, 2, 1]))  # 1
print(solution([4, 3, 2, 5, 6, 7, 8]))  # 2
print(solution([4, 3]))  # 3
print(solution([10]))  # 10
