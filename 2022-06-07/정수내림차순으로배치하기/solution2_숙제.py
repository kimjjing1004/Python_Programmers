# https://programmers.co.kr/learn/courses/30/lessons/12933

# 함수로 분리하는 연습 하세요!

# 정수를 리스트에 넣는 함수
def int_list(n):
    answer = list(str(n))

    for i in range(len(answer)):
        answer[i] = int(answer[i])

    return answer


# 리스트 안에서 정렬하는 함수
def sort_list(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# 누적 시키는 함수
def str_sum(arr):
    result = ''

    for i in range(len(arr)):
        result += str(arr[i])

    return int(result)


def solution(n):
    return str_sum(sort_list(int_list(n)))


print(solution(118372))  # 873211
