# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

# 가장 작은 수 찾기
def solution(arr):
    answer = 100
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]

    if answer > a:
        answer = a

    if answer > b:
        answer = b

    if answer > c:
        answer = c

    if answer > d:
        answer = d

    return answer


# print(solution([4, 3, 2, 1]))  # 1
print(solution([4, 3, 2, 5, 6, 7, 8]))  # 2
# print(solution([4, 3]))  # 3
# print(solution([10]))  # [-1]
