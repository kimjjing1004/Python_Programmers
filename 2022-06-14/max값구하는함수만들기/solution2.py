# 맥스값 구하는 함수 만들기

def max(arr):
    answer = 0

    for i in range(len(arr)):
        if answer < arr[i]:
            answer = arr[i]

    return answer


print(max([1, 3, 2, 5, 4]))  # 5
