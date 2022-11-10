# https://programmers.co.jr/learn/courses/30/lessons/12921

def solution(n):
    answer = []

    for i in range(n + 1):
        result = True
        if i < 2:
            result = False

        for j in range(2, i):
            if i % j == 0:
                result = False

        if result:
            answer.append(i)

    return len(answer)

# 에리토스테네스의 정리 없이 구현한 코드 (뭔 소린지 1도 모름)
# 테스트 3가지가 시간 초과로 실패.....
# 효용성 테스트 전부 실패...
# https://inten.tistory.com/entry/Python-3x-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0

print(solution(10))  # 4 [2, 3, 5, 7]
print(solution(5))  # 3 [2, 3, 5]
