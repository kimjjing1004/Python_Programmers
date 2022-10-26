# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    # answer = list(n) 정수에서 리스트 변환 왜 안 되는지 물어보기
    answer = list(str(n))
    print(answer)

    # answer = [int(i) for i in answer]
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    print('answer', answer)

    for i in range(len(answer)):
        for j in range(i + 1, len(answer)):
            if answer[i] < answer[j]:
                answer[i], answer[j] = answer[j], answer[i]
    print(answer)

    result = ''
    for i in range(len(answer)):
        result += str(answer[i])

    return int(result)


print(solution(118372))  # 873211
