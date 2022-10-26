# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    # answer = [[]]
    total = arr1 + arr2
    print(total)
    print(total[0], total[1], total[2], total[3])
    print(len(total))

    r1 = []
    r2 = []
    for i in range(len(total)):
        if i % 2 == 0:
            r1 += total[i]
        else:
            r2 += total[i]
    print(r1)
    print(r2)

    r3 = 0
    r4 = 0
    for i in range(len(r1)):
        if i % 2 == 0:
            r3 += r1[i]
        else:
            r4 += r1[i]
    print(r3)
    print(r4)

    r5 = 0
    r6 = 0
    for i in range(len(r2)):
        if i % 2 == 0:
            r5 += r2[i]
        else:
            r6 += r2[i]
    print(r5)
    print(r6)

    special1 = list(str(r3)) + list(str(r5))
    special1 = [int(i) for i in special1]

    special2 = list(str(r4)) + list(str(r6))
    special2 = [int(i) for i in special2]

    print(special1)
    print(special2)

    answer = [[i, j] for i, j in zip(special1, special2)]

    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))  # [[4, 6], [7, 9]]
print(solution([[1], [2]], [[3], [4]]))  # [[4], [6]]
