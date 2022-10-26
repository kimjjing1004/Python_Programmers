# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer


print(solution(
    [[1, 2], [2, 3]],   # arr1 arr1[0][0]
    [[3, 4], [5, 6]]))  # arr2 arr2[0][0]
  # [[4, 6], [7, 9]]

print(solution(
    [[1], [2]],   # arr1 arr1[0][0]
    [[3], [4]]))  # arr2 arr2[0][0]
  # [[4], [6]]
