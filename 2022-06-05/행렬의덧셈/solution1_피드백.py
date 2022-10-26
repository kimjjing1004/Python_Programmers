# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        # print(i, arr1[i])
        temp = []
        for j in range(len(arr1[i])):
            # print(i, j, arr1[i], arr1[i][j])
            # print(i, j, arr2[i], arr2[i][j])
            # print(arr1[i][j] + arr2[i][j])
            temp.append(arr1[i][j] + arr2[i][j])
        # print('temp', temp)
        answer.append(temp)

    return answer


print(solution(
    [[1, 2], [2, 3]],   # arr1 arr1[0][0]
    [[3, 4], [5, 6]]))  # arr2 arr2[0][0]
  # [[4, 6], [7, 9]]
print(solution(
    [[1], [2]],
    [[3], [4]]))
  # [[4], [6]]


# arr = [[1, 2]]
# print(arr[0])  # [1, 2]
# print(arr[0][0])  # 1
# print(arr[0][1])  # 2
