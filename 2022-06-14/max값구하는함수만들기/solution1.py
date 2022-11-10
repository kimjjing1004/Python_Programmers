# 맥스값 구하는 함수 만들기

def max(arr):
    answer = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                answer = arr[i]

    return answer


print(max([1, 3, 2, 5, 4]))  # 5
